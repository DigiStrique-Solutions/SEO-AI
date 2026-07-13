#!/usr/bin/env python3
"""Google PageSpeed / Lighthouse / CrUX collector for the SEO harness.

Standalone tool: run directly (`python3 tools/google_pagespeed.py ...`) or import
its functions from the harness. These three services all authenticate with a
single Google Cloud API key (`GOOGLE_API_KEY`), unlike GSC/GA4 which use OAuth
brokered by Composio:

- **PageSpeed Insights API** (`pagespeedonline/v5/runPagespeed`) — Lighthouse LAB
  result (category scores + lab Core Web Vitals) plus embedded FIELD CrUX data
  under `loadingExperience`.
- **Chrome UX Report API** (`chromeuxreport.googleapis.com`) — standalone FIELD
  Core Web Vitals (real-user p75) for a URL or an origin.

Field (CrUX) numbers are real-user measurements; lab (Lighthouse) numbers are a
single synthetic run. Keep them labelled separately — a lab pass is not proof of
a good field experience. When the key or an API is missing, each function raises
RuntimeError so the caller can mark the audit row `not_checked_blocked` rather
than silently passing it.
"""
import argparse
import os
import sys
from pathlib import Path
from urllib.parse import urlencode

# Reuse the harness's shared helpers rather than duplicating them.
from seo_audit_harness import (
    fetch_google_api_json,
    load_local_env,
    now_iso,
    write_json,
)

GOOGLE_API_KEY_ENV = "GOOGLE_API_KEY"
PAGESPEED_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
CRUX_ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"

# Lighthouse audits carrying the lab Core Web Vitals and their supporting metrics.
LAB_CWV_AUDITS = (
    "largest-contentful-paint",
    "cumulative-layout-shift",
    "total-blocking-time",
    "first-contentful-paint",
    "speed-index",
    "interactive",
    "max-potential-fid",
)


def _require_api_key():
    """Return the Google Cloud API key or raise so the caller can degrade cleanly.

    Loads `.env` from both the current directory and the repo root (parent of
    this file's `tools/`), so the key resolves regardless of the caller's cwd.
    """
    repo_root = Path(__file__).resolve().parent.parent
    load_local_env(paths=(".env.local", ".env", repo_root / ".env.local", repo_root / ".env"))
    api_key = os.environ.get(GOOGLE_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is required for PageSpeed/CrUX. Add it to .env "
            "(enable the PageSpeed Insights API and Chrome UX Report API on the key)."
        )
    return api_key


def pagespeed_report(url, strategy="mobile", categories=None, open_url=None):
    """Run PageSpeed Insights (v5) and return a compact lab+field summary.

    Pulls the Lighthouse category scores (0-100), the lab Core Web Vitals, and the
    embedded CrUX field snapshot under `loadingExperience`. Raises RuntimeError on
    a missing key or any API/transport failure.
    """
    api_key = _require_api_key()
    params = [("url", url), ("strategy", strategy), ("key", api_key)]
    for category in categories or ("performance", "accessibility", "best-practices", "seo"):
        params.append(("category", category))
    data = fetch_google_api_json(
        "{}?{}".format(PAGESPEED_ENDPOINT, urlencode(params)),
        open_url=open_url,
    )
    lighthouse = data.get("lighthouseResult", {})
    audits = lighthouse.get("audits", {})
    return {
        "service": "pagespeed",
        "url": url,
        "strategy": strategy,
        "checked_at": now_iso(),
        "final_url": lighthouse.get("finalUrl") or lighthouse.get("finalDisplayedUrl"),
        "category_scores": {
            key: (round(value.get("score") * 100) if isinstance(value.get("score"), (int, float)) else None)
            for key, value in lighthouse.get("categories", {}).items()
            if isinstance(value, dict)
        },
        "lab_core_web_vitals": {
            key: {
                "numeric_value": audits[key].get("numericValue"),
                "display_value": audits[key].get("displayValue"),
                "score": audits[key].get("score"),
            }
            for key in LAB_CWV_AUDITS
            if isinstance(audits.get(key), dict)
        },
        "field_loading_experience": _field_metrics(data.get("loadingExperience", {})),
        "origin_loading_experience": _field_metrics(data.get("originLoadingExperience", {})),
    }


def _field_metrics(loading_experience):
    """Normalize a PageSpeed `loadingExperience` block into per-metric p75 + category."""
    if not isinstance(loading_experience, dict):
        return {}
    metrics = loading_experience.get("metrics", {})
    normalized = {
        key: {
            "percentile": value.get("percentile"),
            "category": value.get("category"),
        }
        for key, value in metrics.items()
        if isinstance(value, dict)
    }
    result = {"metrics": normalized}
    if "overall_category" in loading_experience:
        result["overall_category"] = loading_experience.get("overall_category")
    return result


def crux_report(url, form_factor=None, origin=False, open_url=None):
    """Query the Chrome UX Report API for real-user field Core Web Vitals.

    Pass `origin=True` to query origin-level data (aggregated across the whole
    site) instead of a single URL. `form_factor` may be PHONE, DESKTOP, or TABLET
    to narrow to one device class; omit it for the combined record. Raises
    RuntimeError on a missing key or any API/transport failure (including the
    404 CrUX returns when a URL has no field data).
    """
    api_key = _require_api_key()
    payload = {"origin": url} if origin else {"url": url}
    if form_factor:
        payload["formFactor"] = form_factor
    data = fetch_google_api_json(
        "{}?{}".format(CRUX_ENDPOINT, urlencode({"key": api_key})),
        payload=payload,
        open_url=open_url,
    )
    record = data.get("record", {})
    metrics = record.get("metrics", {})
    return {
        "service": "crux",
        "scope": "origin" if origin else "url",
        "queried": url,
        "form_factor": form_factor or "ALL_FORM_FACTORS",
        "checked_at": now_iso(),
        "key": record.get("key", {}),
        "metrics": {
            name: {
                "p75": metric.get("percentiles", {}).get("p75"),
                "histogram": metric.get("histogram", []),
            }
            for name, metric in metrics.items()
            if isinstance(metric, dict) and "percentiles" in metric
        },
        "collection_period": record.get("collectionPeriod", {}),
    }


def run(args):
    if args.command == "pagespeed":
        report = pagespeed_report(args.url, strategy=args.strategy)
    elif args.command == "crux":
        report = crux_report(args.url, form_factor=args.form_factor, origin=args.origin)
    elif args.command == "cwv":
        # Lab + field in one call: PageSpeed (lab + embedded field) plus the
        # standalone CrUX record, so a blocked/absent CrUX record is explicit.
        report = {"service": "core_web_vitals", "url": args.url, "checked_at": now_iso()}
        report["pagespeed"] = pagespeed_report(args.url, strategy=args.strategy)
        try:
            report["crux"] = crux_report(args.url, form_factor=args.form_factor)
        except RuntimeError as exc:
            report["crux"] = {"status": "not_checked_blocked", "blocker": str(exc)}
    else:  # pragma: no cover - argparse enforces the choices
        raise ValueError("unknown command: {}".format(args.command))
    write_json({"ok": True, "report": report}, args.output)
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    ps = sub.add_parser("pagespeed", help="Run PageSpeed Insights (lab + embedded field).")
    ps.add_argument("--url", required=True, help="Page URL to analyze.")
    ps.add_argument("--strategy", choices=("mobile", "desktop"), default="mobile")
    ps.add_argument("--output", help="Output result JSON path.")

    cr = sub.add_parser("crux", help="Query the Chrome UX Report field data.")
    cr.add_argument("--url", required=True, help="URL, or origin when --origin is set.")
    cr.add_argument("--origin", action="store_true", help="Query origin-level field data.")
    cr.add_argument("--form-factor", dest="form_factor", choices=("PHONE", "DESKTOP", "TABLET"))
    cr.add_argument("--output", help="Output result JSON path.")

    cw = sub.add_parser("cwv", help="Lab + field Core Web Vitals for a URL in one call.")
    cw.add_argument("--url", required=True, help="Page URL to analyze.")
    cw.add_argument("--strategy", choices=("mobile", "desktop"), default="mobile")
    cw.add_argument("--form-factor", dest="form_factor", choices=("PHONE", "DESKTOP", "TABLET"))
    cw.add_argument("--output", help="Output result JSON path.")
    return parser


def main(argv=None):
    return run(build_parser().parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
