#!/usr/bin/env python3
"""ZeroGPT AI-text detector for the SEO harness.

Standalone tool: run directly (`python3 tools/zerogpt.py ...`) or via the harness
subcommand (`seo_audit_harness.py zerogpt-check`, which delegates here).

Records the result as one `detector_note` on an authenticity log. A detector score
is a WEAK editorial signal, not proof of authorship. When ZeroGPT is unreachable,
it falls back to the local AI-pattern risk score, tagged `source: local_fallback`
so a fallback is never mistaken for a real ZeroGPT result.
"""
import argparse
import json
import os
import sys
from pathlib import Path
from urllib import error, request

# Reuse the harness's shared helpers rather than duplicating them.
from seo_audit_harness import (
    ai_text_risk_report,
    load_local_env,
    now_iso,
    read_json,
    write_json,
)

ZEROGPT_API_URL_ENV = "ZEROGPT_API_URL"
ZEROGPT_API_KEY_ENV = "ZEROGPT_API_KEY"
ZEROGPT_DEFAULT_URL = "https://api.zerogpt.com/api/detect/detectText"


def zerogpt_detect(text, open_url=None):
    """Call the free ZeroGPT detect API and return its AI/"fake" percentage (0-100).

    Reads an optional ZEROGPT_API_KEY (sent as the ApiKey header) and an optional
    ZEROGPT_API_URL override from the environment. Raises RuntimeError on any
    transport or contract failure so the caller can decide how to degrade.
    """
    load_local_env()
    api_url = os.environ.get(ZEROGPT_API_URL_ENV, "").strip() or ZEROGPT_DEFAULT_URL
    headers = {"Content-Type": "application/json"}
    api_key = os.environ.get(ZEROGPT_API_KEY_ENV, "").strip()
    if api_key:
        headers["ApiKey"] = api_key
    body = json.dumps({"input_text": text}).encode("utf-8")
    detect_request = request.Request(api_url, data=body, headers=headers, method="POST")
    opener = open_url or request.urlopen
    try:
        with opener(detect_request, timeout=30) as response:
            parsed = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = exc.read().decode("utf-8", "replace")[:500]
        raise RuntimeError("ZeroGPT failed with HTTP {}: {}".format(exc.code, message)) from exc
    except (error.URLError, ValueError, OSError) as exc:
        raise RuntimeError("ZeroGPT request failed: {}".format(exc)) from exc
    data = parsed.get("data") if isinstance(parsed, dict) else None
    if not isinstance(data, dict):
        raise RuntimeError("ZeroGPT returned an unexpected payload: {}".format(parsed))
    percent = None
    for key in ("fakePercentage", "fake_percentage", "ai_percentage", "isHumanPercentage"):
        if key in data and data[key] is not None:
            percent = data[key]
            if key == "isHumanPercentage":
                percent = 100.0 - float(percent)
            break
    if percent is None:
        raise RuntimeError("ZeroGPT payload had no AI percentage: {}".format(data))
    return {
        "score": round(float(percent), 2),
        "feedback": str(data.get("feedback", ""))[:300],
        "raw": data,
    }


def zerogpt_check(text, max_ai_detector_score=20.0, open_url=None):
    """ZeroGPT detector note with a transparent local fallback.

    Returns a detector-note dict (tool 'zerogpt') carrying the AI percentage as
    `score`, its `status` against the gate, and a `source` of either
    'zerogpt_api' or 'local_fallback'.
    """
    try:
        detected = zerogpt_detect(text, open_url=open_url)
        score = detected["score"]
        source = "zerogpt_api"
        note = "ZeroGPT AI-text percentage. Weak editorial signal, not proof of authorship."
        fallback_error = None
        feedback = detected.get("feedback", "")
    except RuntimeError as exc:
        local = ai_text_risk_report(text)
        score = float(local["score"])
        source = "local_fallback"
        note = (
            "ZeroGPT unreachable ({}). Fell back to the local AI-pattern risk score; "
            "this was NOT checked against ZeroGPT.".format(exc)
        )
        fallback_error = str(exc)
        feedback = ""
    status = "fail" if score >= max_ai_detector_score else "pass"
    result = {
        "tool": "zerogpt",
        "source": source,
        "score": score,
        "max_score": float(max_ai_detector_score),
        "status": status,
        "checked_at": now_iso(),
        "note": note,
    }
    if feedback:
        result["feedback"] = feedback
    if fallback_error:
        result["fallback_error"] = fallback_error
    return result


def run(args):
    if bool(args.content_file) == bool(args.text):
        write_json({"ok": False, "errors": ["provide exactly one of --content-file or --text"]}, args.output)
        return 2
    text = Path(args.content_file).read_text(encoding="utf-8") if args.content_file else args.text
    report = zerogpt_check(text, max_ai_detector_score=args.max_ai_detector_score)
    recorded = False
    if args.authenticity:
        log = read_json(args.authenticity)
        notes = log.setdefault("detector_notes", [])
        if isinstance(notes, list):
            notes.append(report)
            write_json(log, args.authenticity)
            recorded = True
    result = {
        "ok": report["status"] != "fail",
        "detector_note": report,
        "recorded_to_authenticity": recorded,
    }
    write_json(result, args.output)
    return 0 if result["ok"] else 1


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--content-file", help="File whose text to check")
    source.add_argument("--text", help="Inline text to check")
    parser.add_argument(
        "--authenticity",
        help="Authenticity log JSON to append the ZeroGPT detector note to (in place).",
    )
    parser.add_argument(
        "--max-ai-detector-score",
        type=float,
        default=20.0,
        help="AI percentage at or above which the check fails (default 20).",
    )
    parser.add_argument("--output", help="Output result JSON path")
    return parser


def main(argv=None):
    return run(build_parser().parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
