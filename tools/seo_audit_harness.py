#!/usr/bin/env python3
"""Compile and verify Strique SEO audit checklist matrices."""

import argparse
import csv
import hashlib
import json
import os
import re
import socket
import ssl
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib import error, request
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse


FIRECRAWL_API_KEY_ENV = "FIRECRAWL_API_KEY"
FIRECRAWL_SCRAPE_URL = "https://api.firecrawl.dev/v2/scrape"
DEFAULT_FIRECRAWL_FORMATS = ["markdown", "html", "rawHtml", "links", "images"]
STATUSES = {"pass", "fail", "not_applicable", "not_checked_blocked"}
CONNECTED_EVIDENCE_SOURCES = {
    "firecrawl",
    "public_http",
    "playwright",
    "lighthouse",
    "pagespeed",
    "crux",
    "gsc",
    "keyword_planner",
    "ga4",
    "posthog",
}
GOOGLE_VISIBLE_SCOPE = "google-visible"
GOOGLE_VISIBLE_REQUIRED_SOURCES = {
    "firecrawl",
    "playwright",
    "lighthouse",
    "pagespeed",
    "crux",
    "gsc",
    "keyword_planner",
}
GOOGLE_VISIBLE_OPTIONAL_SOURCE_PREFIXES = (
    "manual:cms-code",
    "manual:human-context",
    "manual:crm",
    "manual:crm-sales",
    "manual:logs-cdn-waf",
    "manual:off-page",
)
EVIDENCE_SOURCE_ALIASES = {
    "firecrawl": "firecrawl",
    "public_http": "public_http",
    "public http": "public_http",
    "playwright": "playwright",
    "lh": "lighthouse",
    "lighthouse": "lighthouse",
    "crux": "crux",
    "pagespeed": "pagespeed",
    "page speed": "pagespeed",
    "psi": "pagespeed",
    "gsc": "gsc",
    "google search console": "gsc",
    "gkp": "keyword_planner",
    "keyword planner": "keyword_planner",
    "google ads keyword planner": "keyword_planner",
    "ga4": "ga4",
    "google analytics": "ga4",
    "posthog": "posthog",
}
LOGICAL_SOURCE_ALIASES = {
    "firecrawl": "public_crawl",
    "public_http": "public_crawl",
    "public http": "public_crawl",
    "public crawl": "public_crawl",
    "playwright": "rendered_browser",
    "rendered browser": "rendered_browser",
    "browser": "rendered_browser",
    "lh": "performance_lab",
    "lighthouse": "performance_lab",
    "pagespeed": "performance_lab",
    "page speed": "performance_lab",
    "psi": "performance_lab",
    "crux": "performance_field",
    "field performance": "performance_field",
    "gsc": "search_console",
    "google search console": "search_console",
    "search console": "search_console",
    "gkp": "keyword_demand",
    "keyword planner": "keyword_demand",
    "google ads keyword planner": "keyword_demand",
    "keyword demand": "keyword_demand",
    "ga4": "analytics",
    "google analytics": "analytics",
    "posthog": "analytics",
    "analytics": "analytics",
}
DEFAULT_PROVIDER_CONNECTIONS = {
    "public_crawl": ["firecrawl"],
    "rendered_browser": ["playwright"],
    "search_console": ["gsc"],
    "keyword_demand": ["keyword_planner"],
    "performance_lab": ["lighthouse", "pagespeed"],
    "performance_field": ["crux"],
}
GOOGLE_VISIBLE_REQUIRED_LOGICAL_SOURCES = {
    "public_crawl",
    "rendered_browser",
    "search_console",
    "keyword_demand",
    "performance_lab",
    "performance_field",
}
AUDIT_ROW_FIELDS = {
    "checklist_id",
    "section_id",
    "item_id",
    "item_text",
    "status",
    "evidence_source",
    "artifact_ref",
    "result",
    "blocker",
    "next_action",
}
CONCRETE_SOURCE_TYPES = {
    "product_page",
    "brand_dna",
    "gsc",
    "ga4",
    "shopify",
    "merchant_center",
    "review",
    "customer_note",
    "merchandiser_note",
    "serp",
    "competitor_page",
    "human_context",
}
CONTEXT_SOURCE_PRIORITY = [
    "run_context",
    "brand_dna",
    "brand_answers",
    "connector",
    "crawl",
    "prompt_capture",
    "safe_inference",
    "hitl",
]
CONTEXT_FIELD_REQUIRED_KEYS = {
    "field_id",
    "label",
    "scope",
    "data_type",
    "durability",
    "allowed_sources",
    "safe_to_infer",
    "used_by",
    "sensitive",
}
QUESTION_REQUIRED_KEYS = {
    "question_id",
    "field_ids",
    "question",
    "recommended_option",
    "options",
    "allow_custom",
    "store_scope",
    "blocking_level",
    "used_by",
}
HIGH_RISK_CONTEXT_FIELDS = {
    "approved_claims",
    "restricted_claims",
    "compliance_rules",
    "legal_review_required",
    "off_page_risk_posture",
    "past_link_work",
    "ai_crawler_policy",
    "primary_business_goal",
    "lead_quality_definition",
}
LOCAL_CONTEXT_FIELDS = {"locations", "local_service_area", "primary_local_conversion"}
ECOMMERCE_CONTEXT_FIELDS = {
    "ecommerce_platform",
    "priority_product_groups",
    "catalog_source_of_truth",
}
OFF_PAGE_CONTEXT_FIELDS = {"off_page_goal", "off_page_risk_posture", "past_link_work"}
CONTEXT_FIELD_HINTS = [
    (("business goal", "primary goal", "goal is clear", "revenue goal"), ("primary_business_goal",)),
    (("business model", "business type", "site type", "store type"), ("business_model", "site_type")),
    (("target audience", "audience", "persona", "buyer stage", "who it is for"), ("target_audience", "buyer_stage")),
    (("priority query", "query set", "target query", "keyword", "search intent", "intent is classified"), ("priority_queries", "search_intent")),
    (("competitor", "cited or recommended", "market link intelligence"), ("competitors",)),
    (("ymyl", "legal", "compliance", "restricted", "regulated", "unsafe", "policy risk"), ("ymyl_exposure", "compliance_rules")),
    (("approved claim", "forbidden claim", "unsupported promise", "claim"), ("approved_claims", "restricted_claims")),
    (("conversion", "lead", "signup", "purchase", "demo", "trial", "revenue", "sales", "calls", "bookings", "directions"), ("primary_conversion",)),
    (("priority page", "important pages", "strategic importance", "page type"), ("priority_pages", "page_type")),
    (("location", "local", "service area", "geography", "nap", "gbp", "maps", "directions", "near me"), ("locations", "local_service_area", "primary_local_conversion")),
    (("shopify", "merchant center", "gmc", "catalog", "product group", "feed", "availability", "price", "shipping", "returns", "variant"), ("ecommerce_platform", "catalog_source_of_truth", "priority_product_groups")),
    (("ai overview", "ai mode", "chatgpt", "perplexity", "claude", "gemini", "copilot", "prompt", "ai visibility", "citation", "crawler policy"), ("ai_target_platforms", "ai_prompt_set", "ai_visibility_goal")),
    (("off-page", "link", "backlink", "digital pr", "public relations", "partnership", "affiliate", "sponsorship", "review program", "disavow"), ("off_page_goal", "off_page_risk_posture", "past_link_work")),
    (("cms", "engineering", "legacy url", "url pattern", "taxonomy", "navigation", "architecture", "migration"), ("platform_constraints", "current_pain")),
    (("brand voice", "editorial voice", "tone", "customer language"), ("brand_voice",)),
    (("country", "language", "locale", "international", "market"), ("target_countries", "target_languages")),
]
CONTENT_AUTHENTICITY_SKILL = "content-seo-authenticity"
CONTENT_AUTHENTICITY_SKILL_REF = ".agents/skills/content-seo-authenticity/SKILL.md"
AI_TEXT_RISK_SKILL = "ai-text-risk-gate"
AI_TEXT_RISK_SKILL_REF = ".agents/skills/ai-text-risk-gate/SKILL.md"
AI_DETECTOR_TOOL_TOKENS = (
    "ai detector",
    "ai-pattern",
    "ai pattern",
    "zerogpt",
    "gptzero",
    "originality",
    "copyleaks",
    "checkapp",
    "writer.com",
)
AI_TEXT_GENERIC_PHRASES = (
    "in today's digital landscape",
    "unlock your potential",
    "at its core",
    "it is worth noting",
    "when it comes to",
    "game changer",
    "ever-evolving",
    "seamlessly",
    "robust solution",
    "cutting-edge",
    "delve into",
    "comprehensive guide",
)
AI_TEXT_FORMULAIC_TRANSITIONS = (
    "additionally",
    "furthermore",
    "moreover",
    "in conclusion",
    "ultimately",
    "overall",
    "in summary",
    "as a result",
)
AI_TEXT_CONTRASTIVE_REFRAME_PATTERNS = (
    r"\b(?:it.?s|it is|this is|that is)?\s*not\s+(?:just|only|about)\b[^\n]{0,160}\b(?:but|it.?s|it is|rather)\b",
    r"\bisn.?t\s+(?:just|only|about)\b[^\n]{0,160}\b(?:but|it.?s|it is|rather)\b",
    r"\bno\b[^.!?\n]{1,60},\s*no\b[^.!?\n]{1,60},\s*(?:just|only)\b",
)
AI_TEXT_ABSTRACT_TERMS = (
    "optimize",
    "streamline",
    "leverage",
    "innovative",
    "transform",
    "unlock",
    "enhance",
    "empower",
    "seamless",
    "robust",
    "solution",
    "efficiency",
    "effective",
    "comprehensive",
    "dynamic",
    "strategic",
    "valuable",
)
KEYWORD_ROW_FIELDS = [
    "keyword",
    "intent",
    "page_type",
    "target_url",
    "volume",
    "difficulty",
    "priority",
    "source",
    "status",
    "notes",
]
KEYWORD_UNIVERSE_FIELDS = [
    "keyword",
    "normalized_keyword",
    "intent",
    "page_type",
    "target_url",
    "volume",
    "difficulty",
    "priority",
    "sources",
    "gsc_clicks",
    "gsc_impressions",
    "gsc_ctr",
    "gsc_position",
    "gsc_page",
    "gsc_country",
    "status",
    "notes",
]
URL_INVENTORY_FIELDS = [
    "url",
    "normalized_url",
    "status",
    "status_code",
    "content_type",
    "indexable",
    "canonical",
    "title",
    "meta_description",
    "h1_count",
    "word_count",
    "internal_link_count",
    "external_link_count",
    "image_count",
    "images_missing_alt_count",
    "schema_types",
    "depth",
    "parent_url",
    "source",
    "in_sitemap",
    "artifact_dir",
    "blocker",
    "last_seen",
]
SITE_CHECK_FIELDS = [
    "check_id",
    "url",
    "severity",
    "status",
    "source",
    "artifact_ref",
    "result",
    "next_action",
]
STATIC_ASSET_EXTENSIONS = {
    ".avif",
    ".css",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".svg",
    ".webm",
    ".webp",
    ".woff",
    ".woff2",
    ".xml",
    ".zip",
}
PRIVATE_PATH_PARTS = (
    "/admin",
    "/account",
    "/cart",
    "/checkout",
    "/login",
    "/sign-in",
    "/signin",
)
TRACKING_QUERY_PREFIXES = ("utm_",)
TEXT_QUALITY_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
    "your",
}
TRACKING_QUERY_KEYS = {
    "_hsenc",
    "_hsmi",
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "msclkid",
}
GSC_LIST_SITES_TOOL = "GOOGLE_SEARCH_CONSOLE_LIST_SITES"
GSC_GET_SITE_TOOL = "GOOGLE_SEARCH_CONSOLE_GET_SITE"
GSC_LIST_SITEMAPS_TOOL = "GOOGLE_SEARCH_CONSOLE_LIST_SITEMAPS"
GSC_GET_SITEMAP_TOOL = "GOOGLE_SEARCH_CONSOLE_GET_SITEMAP"
GSC_INSPECT_URL_TOOL = "GOOGLE_SEARCH_CONSOLE_INSPECT_URL"
GSC_SEARCH_ANALYTICS_TOOL = "GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY"
GSC_DIMENSION_SETS = {
    "query_page_country": ["query", "page", "country"],
    "query_page_date": ["query", "page", "date"],
    "page_date": ["page", "date"],
    "search_appearance_page": ["searchAppearance", "page"],
}
GOOGLE_ADS_KEYWORD_IDEA_URL = (
    "https://googleads.googleapis.com/v23/customers/{}:generateKeywordIdeas"
)
DEFAULT_LANGUAGE_CONSTANT = "languageConstants/1000"
DEFAULT_CHROME_PATH = (
    "/Users/poojan/Library/Caches/ms-playwright/chromium-1217/chrome-mac-arm64/"
    "Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
)
DEFAULT_PLAYWRIGHT_MODULE = "/Users/poojan/.codex/browser-qa/node_modules/playwright/index.mjs"
LIGHTHOUSE_DIAGNOSTIC_AUDITS = (
    "largest-contentful-paint",
    "interaction-to-next-paint",
    "cumulative-layout-shift",
    "speed-index",
    "total-blocking-time",
    "render-blocking-resources",
    "unused-css-rules",
    "font-display",
    "uses-rel-preload",
    "bootup-time",
    "third-party-summary",
    "third-party-facades",
)
GOOGLE_RICH_RESULT_REQUIRED_PROPERTIES = {
    "Article": ("headline",),
    "BlogPosting": ("headline",),
    "BreadcrumbList": ("itemListElement",),
    "FAQPage": ("mainEntity",),
    "HowTo": ("name", "step"),
    "JobPosting": ("title", "description", "datePosted", "hiringOrganization", "jobLocation"),
    "LocalBusiness": ("name", "address"),
    "Organization": ("name",),
    "Product": ("name",),
    "Recipe": ("name", "recipeIngredient", "recipeInstructions"),
    "Review": ("itemReviewed", "reviewRating", "author"),
    "SoftwareApplication": ("name", "applicationCategory"),
    "VideoObject": ("name", "description", "thumbnailUrl", "uploadDate"),
}
COUNTRY_ALIASES = {
    "usa": "United States",
    "us": "United States",
    "u.s.": "United States",
    "united states": "United States",
    "united states of america": "United States",
    "ind": "India",
    "in": "India",
    "india": "India",
    "gbr": "United Kingdom",
    "gb": "United Kingdom",
    "uk": "United Kingdom",
    "u.k.": "United Kingdom",
    "united kingdom": "United Kingdom",
    "can": "Canada",
    "ca": "Canada",
    "canada": "Canada",
    "aus": "Australia",
    "au": "Australia",
    "australia": "Australia",
    "sgp": "Singapore",
    "sg": "Singapore",
    "singapore": "Singapore",
    "are": "United Arab Emirates",
    "ae": "United Arab Emirates",
    "uae": "United Arab Emirates",
    "united arab emirates": "United Arab Emirates",
    "deu": "Germany",
    "de": "Germany",
    "germany": "Germany",
    "fra": "France",
    "fr": "France",
    "france": "France",
    "nld": "Netherlands",
    "nl": "Netherlands",
    "netherlands": "Netherlands",
    "esp": "Spain",
    "es": "Spain",
    "spain": "Spain",
    "ita": "Italy",
    "it": "Italy",
    "italy": "Italy",
    "bra": "Brazil",
    "br": "Brazil",
    "brazil": "Brazil",
}
GOOGLE_ADS_GEO_TARGETS = {
    "United States": "geoTargetConstants/2840",
    "India": "geoTargetConstants/2356",
    "United Kingdom": "geoTargetConstants/2826",
    "Canada": "geoTargetConstants/2124",
    "Australia": "geoTargetConstants/2036",
    "Singapore": "geoTargetConstants/2702",
    "United Arab Emirates": "geoTargetConstants/2784",
    "Germany": "geoTargetConstants/2276",
    "France": "geoTargetConstants/2250",
    "Netherlands": "geoTargetConstants/2528",
    "Spain": "geoTargetConstants/2724",
    "Italy": "geoTargetConstants/2380",
    "Brazil": "geoTargetConstants/2076",
}


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def item_hash(text):
    normalized = " ".join(text.strip().split()).lower()
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:8]


def read_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(data, path):
    if not path:
        print(json.dumps(data, indent=2, sort_keys=True))
        return
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def write_text_file(path, text):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def load_local_env(paths=(".env.local", ".env")):
    for path in paths:
        env_path = Path(path)
        if not env_path.exists():
            continue
        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def get_firecrawl_api_key():
    load_local_env()
    api_key = os.environ.get(FIRECRAWL_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError("{} is required".format(FIRECRAWL_API_KEY_ENV))
    return api_key


def normalize_firecrawl_scrape(response):
    data = response.get("data", {})
    metadata = data.get("metadata", {})
    return {
        "status": metadata.get("statusCode"),
        "headers": metadata.get("headers", {}),
        "raw_html": data.get("rawHtml", ""),
        "rendered_html": data.get("html", ""),
        "rendered_text": data.get("markdown", ""),
        "links": data.get("links", []),
        "images": data.get("images", []),
        "screenshot": data.get("screenshot", ""),
        "metadata": metadata,
    }


def firecrawl_scrape(
    url,
    formats=None,
    only_main_content=True,
    wait_for=0,
    mobile=False,
    timeout=60000,
    open_url=None,
):
    payload = {
        "url": url,
        "formats": formats or DEFAULT_FIRECRAWL_FORMATS,
        "onlyMainContent": only_main_content,
        "waitFor": wait_for,
        "mobile": mobile,
        "timeout": timeout,
    }
    body = json.dumps(payload).encode("utf-8")
    scrape_request = request.Request(
        FIRECRAWL_SCRAPE_URL,
        data=body,
        headers={
            "Authorization": "Bearer {}".format(get_firecrawl_api_key()),
            "Content-Type": "application/json",
        },
        method="POST",
    )
    opener = open_url or request.urlopen
    try:
        with opener(scrape_request, timeout=(timeout / 1000) + 5) as response:
            parsed = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = exc.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(
            "Firecrawl scrape failed with HTTP {}: {}".format(exc.code, message)
        ) from exc
    if not parsed.get("success"):
        raise RuntimeError("Firecrawl scrape failed: {}".format(parsed))
    return normalize_firecrawl_scrape(parsed)


def canonical_evidence_source(value):
    raw = str(value or "").strip().strip("`").strip(".")
    if not raw:
        return ""
    normalized = re.sub(r"\s+", " ", raw.replace("_", " ").lower())
    normalized = normalized.replace("&", "and")
    alias = EVIDENCE_SOURCE_ALIASES.get(normalized)
    if alias:
        return alias
    contains_aliases = [
        ("firecrawl", "firecrawl"),
        ("public http", "public_http"),
        ("playwright", "playwright"),
        ("lighthouse", "lighthouse"),
        ("pagespeed", "pagespeed"),
        ("page speed", "pagespeed"),
        ("crux", "crux"),
        ("search console", "gsc"),
        ("keyword planner", "keyword_planner"),
        ("ga4", "ga4"),
        ("posthog", "posthog"),
        ("google analytics", "ga4"),
    ]
    for needle, source in contains_aliases:
        if needle in normalized:
            return source
    return "manual:{}".format(slugify(normalized))


def parse_evidence_sources(value):
    tokens = re.findall(r"`([^`]+)`", str(value or ""))
    if not tokens and value:
        tokens = [part.strip() for part in str(value).split(",")]
    sources = []
    seen = set()
    for token in tokens:
        source = canonical_evidence_source(token)
        if source and source not in seen:
            seen.add(source)
            sources.append(source)
    return sources


def canonical_logical_source(value):
    raw = str(value or "").strip().strip("`").strip(".")
    if not raw:
        return ""
    if raw.startswith("manual:"):
        return raw
    normalized = re.sub(r"\s+", " ", raw.replace("_", " ").lower())
    normalized = normalized.replace("&", "and")
    alias = LOGICAL_SOURCE_ALIASES.get(normalized)
    if alias:
        return alias
    contains_aliases = [
        ("firecrawl", "public_crawl"),
        ("public http", "public_crawl"),
        ("playwright", "rendered_browser"),
        ("lighthouse", "performance_lab"),
        ("pagespeed", "performance_lab"),
        ("page speed", "performance_lab"),
        ("crux", "performance_field"),
        ("search console", "search_console"),
        ("keyword planner", "keyword_demand"),
        ("ga4", "analytics"),
        ("google analytics", "analytics"),
        ("posthog", "analytics"),
    ]
    for needle, source in contains_aliases:
        if needle in normalized:
            return source
    return "manual:{}".format(slugify(normalized))


def parse_logical_evidence_sources(value):
    tokens = re.findall(r"`([^`]+)`", str(value or ""))
    if not tokens and value:
        tokens = [part.strip() for part in str(value).split(",")]
    sources = []
    seen = set()
    for token in tokens:
        source = canonical_logical_source(token)
        if source and source not in seen:
            seen.add(source)
            sources.append(source)
    return sources


def provider_connections_path(brand_dir):
    return Path(brand_dir) / "references" / "provider-connections.json"


def normalize_provider_connections(data):
    raw_providers = data.get("providers", data) if isinstance(data, dict) else {}
    providers = {key: list(value) for key, value in DEFAULT_PROVIDER_CONNECTIONS.items()}
    for raw_logical, raw_value in raw_providers.items():
        logical = canonical_logical_source(raw_logical)
        if not logical:
            continue
        values = raw_value if isinstance(raw_value, list) else [raw_value]
        normalized = [
            canonical_evidence_source(value)
            for value in values
            if canonical_evidence_source(value)
        ]
        providers[logical] = normalized
    return providers


def load_provider_connections(brand_dir=""):
    if brand_dir:
        path = provider_connections_path(brand_dir)
        if path.exists():
            return normalize_provider_connections(read_json(path))
    return normalize_provider_connections({})


def resolve_logical_sources(logical_sources, provider_connections):
    providers = []
    plan = []
    blockers = []
    for logical in logical_sources:
        if str(logical).startswith("manual:"):
            resolved = [logical]
            blockers.append(
                {
                    "logical_source": logical,
                    "blocker": "No connected provider for {}.".format(logical),
                    "next_action": "Record a manual artifact or configure this provider.",
                }
            )
        else:
            resolved = provider_connections.get(logical, [])
            if not resolved:
                blockers.append(
                    {
                        "logical_source": logical,
                        "blocker": "No connected provider for {}.".format(logical),
                        "next_action": "Add {} to provider-connections.json.".format(logical),
                    }
                )
        for provider in resolved:
            if provider not in providers:
                providers.append(provider)
        plan.append(
            {
                "logical_source": logical,
                "providers": resolved,
                "required": True,
                "status": "connected" if resolved and not str(logical).startswith("manual:") else "blocked",
            }
        )
    return providers, plan, blockers


def is_google_visible_optional_source(source):
    return source in {"analytics", "posthog", "ga4"} or any(
        str(source).startswith(prefix)
        for prefix in GOOGLE_VISIBLE_OPTIONAL_SOURCE_PREFIXES
    )


def google_visible_public_hint(text):
    return re.search(
        r"\b(title|meta|description|h1|heading|canonical|robots|sitemap|schema|"
        r"structured data|crawl|index|noindex|render|mobile|image|images|video|videos|"
        r"screenshot|screenshots|table|tables|chart|charts|calculator|calculators|alt|link|"
        r"performance|core web vitals|lighthouse|pagespeed|crux|status code|"
        r"hreflang|redirect|content|copy|url|media|docs|documentation|support|"
        r"interactive controls|snippet|preview)\b",
        text,
    )


def google_visible_process_only_item(item_text):
    text = str(item_text or "").lower()
    if google_visible_scope_not_applicable_item(text):
        return True
    if google_visible_public_hint(text):
        return False
    return bool(
        re.search(
            r"\b(owner|ownership|review cadence|editorial|governance|cms|code|"
            r"template|conversion|conversions|revenue|sales|crm|session|sessions|"
            r"funnel|engagement|traffic quality|business value|deployment date|"
            r"business goal|expected impact|annotation|human review|ai-assisted|drafting)\b",
            text,
        )
    )


def google_visible_scope_not_applicable_item(item_text):
    text = str(item_text or "").lower()
    return bool(
        re.search(
            r"\b(cdn|firewall|waf|bot protection|rate limits?|geo rules?|"
            r"reverse dns|official google ip|uptime|error-rate monitoring|"
            r"manual actions?|security issues?|deploy regressions?|"
            r"observed google title|google rewrites? the title|observed google snippet|"
            r"bing webmaster tools?|content is still accurate|time-sensitive data|"
            r"old content is updated|dates shown to users|updated content includes real improvements|"
            r"separate worse content.*for ai|llms\.txt.*required.*google|"
            r"google-extended.*opt-out|blocking all ai/search crawlers|"
            r"review themes are analyzed|community participation|spammy forum|"
            r"private blog networks?|large-scale link exchanges?|review gating|"
            r"fake awards?|fake certifications?|fake customers?|fake testimonials?|"
            r"spammy directory blasts?|comment/forum/profile spam|"
            r"recommendation poisoning|third-party site reputation abuse)\b",
            text,
        )
    )


def filter_google_visible_sources(candidate_sources):
    return [
        source
        for source in candidate_sources
        if source in GOOGLE_VISIBLE_REQUIRED_LOGICAL_SOURCES
        and not is_google_visible_optional_source(source)
    ]


def infer_logical_required_sources(item_text, candidate_sources, scope="page"):
    text = str(item_text or "").lower()
    if scope == GOOGLE_VISIBLE_SCOPE and google_visible_process_only_item(text):
        return []
    rules = [
        (
            r"\b(tls|certificate|hsts|x-robots-tag|non-html|pdfs?|documents?|feeds?|moved permanently|permanent redirect|redirects?|staging|preview|non-production)\b",
            ["public_crawl"],
        ),
        (
            r"\b(crawl stats|wasted crawl|soft 404|5xx|429|low-value parameter)\b",
            ["public_crawl", "search_console"],
        ),
        (
            r"\b(search appearance|url inspection|query drift|decaying pages|lost impressions|lost clicks|ctr|rankings|serp expectations?)\b",
            ["search_console"],
        ),
        (
            r"\b(rich result|required and recommended properties)\b",
            ["rendered_browser"],
        ),
        (
            r"\b(critical css|font loading|render-blocking|lab tests?|root causes?)\b",
            ["performance_lab"],
        ),
        (
            r"\b(third-party scripts?|third party scripts?)\b",
            ["performance_lab", "rendered_browser"],
        ),
        (
            r"\b(primary search intent|search intent|page purpose|page type|business goal|target audience|cannibaliz|clear next step)\b",
            ["public_crawl", "search_console", "keyword_demand"],
        ),
        (
            r"\b(core web vitals|lcp|inp|cls|performance|page speed|pagespeed|lighthouse)\b",
            ["performance_lab", "performance_field"],
        ),
        (
            r"\b(rendered|javascript|mobile|visual|accessibility|screenshot|viewport)\b",
            ["rendered_browser"],
        ),
        (
            r"\b(queries|query|clicks|impressions|indexing|indexed|sitemap submission|search console)\b",
            ["search_console"],
        ),
        (
            r"\b(keyword|keywords|volume|competition|search demand|query mapping)\b",
            ["keyword_demand"],
        ),
        (
            r"\b(behavior|conversion|conversions|funnel|traffic quality|engagement|analytics)\b",
            ["analytics"],
        ),
        (
            r"\b(crawl|crawlability|indexability|canonical|canonicals|robots|sitemap|links|images|schema|structured data|hreflang)\b",
            ["public_crawl"],
        ),
        (
            r"\b(title|meta description|description|h1|heading)\b",
            ["public_crawl"],
        ),
    ]
    for pattern, sources in rules:
        if re.search(pattern, text):
            if scope == GOOGLE_VISIBLE_SCOPE:
                return filter_google_visible_sources(sources)
            return sources

    if scope == GOOGLE_VISIBLE_SCOPE:
        google_visible_sources = filter_google_visible_sources(candidate_sources)
        if google_visible_sources:
            return google_visible_sources[:1]
        return []

    for source in candidate_sources:
        if source in DEFAULT_PROVIDER_CONNECTIONS:
            return [source]
    for source in candidate_sources:
        if source.startswith("manual:"):
            return [source]
    return candidate_sources[:1]


def route_evidence_for_item(item_text, candidate_sources, scope="page", provider_connections=None):
    logical_candidates = []
    for source in candidate_sources:
        logical = canonical_logical_source(source)
        if logical and logical not in logical_candidates:
            logical_candidates.append(logical)
    logical_required = infer_logical_required_sources(
        item_text,
        logical_candidates,
        scope=scope,
    )
    resolved, evidence_plan, provider_blockers = resolve_logical_sources(
        logical_required,
        provider_connections or load_provider_connections(""),
    )
    return {
        "candidate_sources": logical_candidates,
        "logical_required_sources": logical_required,
        "resolved_required_sources": resolved,
        "required_sources": resolved,
        "evidence_plan": evidence_plan,
        "provider_blockers": provider_blockers,
    }


def infer_required_sources(item_text, candidate_sources, scope="page", provider_connections=None):
    return route_evidence_for_item(
        item_text,
        candidate_sources,
        scope=scope,
        provider_connections=provider_connections,
    )["required_sources"]


def artifact_ref_exists(artifact_ref, base_dir=None):
    ref = str(artifact_ref or "").strip()
    if not ref:
        return False
    if re.match(r"^https?://", ref):
        return True
    path = Path(ref)
    if path.is_absolute() and path.exists():
        return True
    if path.exists():
        return True
    if base_dir and (Path(base_dir) / path).exists():
        return True
    return False


def row_evidence_sources(value):
    return parse_evidence_sources(str(value or "").replace("+", ",").replace(";", ","))


def evidence_run_id():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def evidence_dir(brand_dir, run_id):
    return Path(brand_dir) / "references" / "evidence" / run_id


def crawl_dir(brand_dir, run_id):
    return Path(brand_dir) / "references" / "crawls" / run_id


def crawl_manifest_path(brand_dir, run_id):
    return crawl_dir(brand_dir, run_id) / "manifest.json"


def url_inventory_path(brand_dir):
    return Path(brand_dir) / "exports" / "url-inventory.csv"


def site_checks_path(brand_dir):
    return Path(brand_dir) / "exports" / "site-checks.csv"


def site_checks_json_path(brand_dir, run_id):
    return evidence_dir(brand_dir, run_id) / "site-checks.json"


def write_evidence_artifact(target_dir, name, data):
    path = Path(target_dir) / name
    write_json(data, path)
    return str(path)


def url_hash(url):
    normalized = " ".join(str(url or "").strip().lower().split())
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:12]


def root_url(url):
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return url.rstrip("/")
    return "{}://{}".format(parsed.scheme, parsed.netloc).rstrip("/")


def normalized_host(url):
    return site_host(url).removeprefix("www.")


def same_site_url(left, right):
    return normalized_host(left) == normalized_host(right)


def is_tracking_query_key(key):
    normalized = str(key or "").lower()
    return normalized in TRACKING_QUERY_KEYS or normalized.startswith(
        TRACKING_QUERY_PREFIXES
    )


def normalize_public_url(raw_url, base_url=""):
    joined = urljoin(base_url, str(raw_url or "").strip())
    parsed = urlparse(joined)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return ""
    query = urlencode(
        [
            (key, value)
            for key, value in parse_qsl(parsed.query, keep_blank_values=True)
            if not is_tracking_query_key(key)
        ]
    )
    path = parsed.path or "/"
    return urlunparse(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            path,
            "",
            query,
            "",
        )
    )


def normalize_crawl_url(raw_url, base_url=""):
    normalized = normalize_public_url(raw_url, base_url=base_url)
    if not normalized:
        return ""
    parsed = urlparse(normalized)
    path = parsed.path.lower()
    if any(part in path for part in PRIVATE_PATH_PARTS):
        return ""
    if Path(path).suffix in STATIC_ASSET_EXTENSIONS:
        return ""
    return normalized


def crawl_url_key(url):
    normalized = normalize_public_url(url)
    parsed = urlparse(normalized)
    host = parsed.netloc.lower().removeprefix("www.")
    return urlunparse((parsed.scheme.lower(), host, parsed.path or "/", "", parsed.query, "")).lower()


def fetch_text_url(url, open_url=None, timeout=30):
    fetch_request = request.Request(
        url,
        headers={"User-Agent": "StriqueSEOAuditHarness/1.0"},
    )
    opener = open_url or request.urlopen
    with opener(fetch_request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def parse_robots_sitemaps(text):
    sitemaps = []
    for raw_line in str(text or "").splitlines():
        line = raw_line.strip()
        if line.lower().startswith("sitemap:"):
            sitemap = line.split(":", 1)[1].strip()
            if sitemap:
                sitemaps.append(sitemap)
    return sitemaps


def parse_sitemap_xml(text):
    root = ET.fromstring(text)
    locs = [
        (element.text or "").strip()
        for element in root.iter()
        if element.tag.lower().endswith("loc") and (element.text or "").strip()
    ]
    if root.tag.lower().endswith("sitemapindex"):
        return {"sitemaps": locs, "urls": []}
    return {"sitemaps": [], "urls": locs}


def discover_sitemap_pages(base_url, open_url=None):
    base = root_url(base_url)
    sitemaps = []
    blockers = []
    try:
        robots_text = fetch_text_url(urljoin(base + "/", "robots.txt"), open_url=open_url)
        sitemaps.extend(parse_robots_sitemaps(robots_text))
    except Exception as exc:
        blockers.append("robots.txt not fetched: {}".format(exc))
    sitemaps.append(urljoin(base + "/", "sitemap.xml"))

    pages = []
    seen_sitemaps = set()
    queue = [
        normalize_public_url(sitemap, base_url=base)
        for sitemap in sitemaps
        if normalize_public_url(sitemap, base_url=base)
    ]
    while queue:
        sitemap_url = queue.pop(0)
        key = sitemap_url.lower()
        if key in seen_sitemaps:
            continue
        seen_sitemaps.add(key)
        try:
            parsed = parse_sitemap_xml(fetch_text_url(sitemap_url, open_url=open_url))
        except Exception as exc:
            blockers.append("sitemap not fetched: {}: {}".format(sitemap_url, exc))
            continue
        for nested in parsed["sitemaps"]:
            nested_url = normalize_public_url(nested, base_url=sitemap_url)
            if nested_url and nested_url.lower() not in seen_sitemaps:
                queue.append(nested_url)
        for page in parsed["urls"]:
            normalized = normalize_crawl_url(page, base_url=sitemap_url)
            if normalized and same_site_url(base, normalized):
                pages.append(normalized)
    return {"pages": pages, "sitemaps": sorted(seen_sitemaps), "blockers": blockers}


class SEOHTMLExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_chunks = []
        self.text_chunks = []
        self.links = []
        self.images = []
        self.h1_count = 0
        self.meta_description = ""
        self.robots = ""
        self.canonical = ""
        self.json_ld = []
        self._in_title = False
        self._in_json_ld = False
        self._script_chunks = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attributes = {key.lower(): value or "" for key, value in attrs}
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = attributes.get("name", "").lower()
            if name == "description" and not self.meta_description:
                self.meta_description = attributes.get("content", "").strip()
            elif name == "robots" and not self.robots:
                self.robots = attributes.get("content", "").strip()
        elif tag == "link":
            rel = attributes.get("rel", "").lower()
            if "canonical" in rel and not self.canonical:
                self.canonical = attributes.get("href", "").strip()
        elif tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"].strip())
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.images.append(
                {
                    "src": attributes.get("src", "").strip(),
                    "alt": attributes.get("alt", "").strip(),
                }
            )
        elif tag == "script" and "application/ld+json" in attributes.get("type", "").lower():
            self._in_json_ld = True
            self._script_chunks = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._script_chunks).strip())
            self._script_chunks = []
            self._in_json_ld = False

    def handle_data(self, data):
        if self._in_json_ld:
            self._script_chunks.append(data)
            return
        if self._in_title:
            self.title_chunks.append(data)
        if data.strip():
            self.text_chunks.append(data)


def collect_schema_types(value, output):
    if isinstance(value, dict):
        schema_type = value.get("@type")
        if isinstance(schema_type, str):
            output.add(schema_type)
        elif isinstance(schema_type, list):
            for item in schema_type:
                if isinstance(item, str):
                    output.add(item)
        for nested in value.values():
            collect_schema_types(nested, output)
    elif isinstance(value, list):
        for item in value:
            collect_schema_types(item, output)


def schema_types_from_json_ld(scripts):
    schema_types = set()
    for script in scripts:
        try:
            collect_schema_types(json.loads(script), schema_types)
        except json.JSONDecodeError:
            continue
    return sorted(schema_types)


def extract_html_features(html):
    parser = SEOHTMLExtractor()
    parser.feed(html or "")
    return {
        "title": " ".join("".join(parser.title_chunks).split()),
        "meta_description": " ".join(parser.meta_description.split()),
        "canonical": parser.canonical,
        "robots": parser.robots,
        "h1_count": parser.h1_count,
        "links": parser.links,
        "image_count": len(parser.images),
        "images_missing_alt_count": len([image for image in parser.images if not image["alt"]]),
        "schema_types": schema_types_from_json_ld(parser.json_ld),
        "word_count": len(re.findall(r"\w+", " ".join(parser.text_chunks))),
    }


def header_value(headers, name):
    for key, value in (headers or {}).items():
        if str(key).lower() == name.lower():
            return value
    return ""


def page_inventory_from_scrape(url, data, depth, parent_url, source, in_sitemap, artifact_dir):
    html = "\n".join(
        part for part in (data.get("raw_html", ""), data.get("rendered_html", "")) if part
    )
    features = extract_html_features(html)
    links = []
    for link in list(data.get("links") or []) + features["links"]:
        normalized = normalize_public_url(link, base_url=url)
        if normalized:
            links.append(normalized)
    unique_links = sorted(set(links))
    internal_links = [link for link in unique_links if same_site_url(url, link)]
    external_links = [link for link in unique_links if not same_site_url(url, link)]
    status_code = int(coerce_float(data.get("status")))
    headers = data.get("headers") or data.get("metadata", {}).get("headers", {})
    robots = features["robots"].lower()
    indexable = status_code < 400 and "noindex" not in robots
    text_word_count = len(re.findall(r"\w+", data.get("rendered_text", "")))
    word_count = max(features["word_count"], text_word_count)
    canonical = normalize_public_url(features["canonical"], base_url=url) if features["canonical"] else ""
    return {
        "url": url,
        "normalized_url": crawl_url_key(url),
        "status": "success",
        "status_code": str(status_code) if status_code else "",
        "content_type": header_value(headers, "content-type"),
        "indexable": "yes" if indexable else "no",
        "canonical": canonical,
        "title": features["title"],
        "meta_description": features["meta_description"],
        "h1_count": str(features["h1_count"]),
        "word_count": str(word_count),
        "internal_link_count": str(len(internal_links)),
        "external_link_count": str(len(external_links)),
        "image_count": str(features["image_count"] or len(data.get("images") or [])),
        "images_missing_alt_count": str(features["images_missing_alt_count"]),
        "schema_types": ", ".join(features["schema_types"]),
        "depth": str(depth),
        "parent_url": parent_url,
        "source": source,
        "in_sitemap": "yes" if in_sitemap else "no",
        "artifact_dir": str(artifact_dir),
        "blocker": "",
        "last_seen": now_iso(),
    }, internal_links


def parse_checklist(path):
    checklist_path = Path(path)
    checklist_id = slugify(checklist_path.stem.replace("-checklist", ""))
    title = checklist_path.stem
    section_id = "unsectioned"
    section_title = "Unsectioned"
    section_evidence = ""
    items = []
    sections = []
    seen_sections = set()
    heading_pattern = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
    item_pattern = re.compile(r"^\s*-\s+\[\s*\]\s+(.+?)\s*$")

    with open(checklist_path, "r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.rstrip("\n")
            heading = heading_pattern.match(line)
            if heading:
                level = len(heading.group(1))
                heading_text = heading.group(2).strip()
                if level == 1:
                    title = heading_text
                elif level == 2:
                    section_title = heading_text
                    section_id = slugify(heading_text)
                    section_evidence = ""
                    if section_id not in seen_sections:
                        seen_sections.add(section_id)
                        sections.append(
                            {
                                "section_id": section_id,
                                "section_title": section_title,
                                "source_line": line_number,
                            }
                        )
                continue

            if line.startswith("Evidence sources:"):
                section_evidence = line.split(":", 1)[1].strip()
                continue

            item = item_pattern.match(line)
            if not item:
                continue

            item_text = " ".join(item.group(1).strip().split())
            items.append(
                {
                    "checklist_id": checklist_id,
                    "checklist_title": title,
                    "section_id": section_id,
                    "section_title": section_title,
                    "item_id": "{}.{}.{}".format(
                        checklist_id, section_id, item_hash(item_text)
                    ),
                    "item_text": item_text,
                    "required_evidence": section_evidence,
                    "source_path": str(checklist_path),
                    "source_line": line_number,
                }
            )

    return {
        "checklist_id": checklist_id,
        "title": title,
        "path": str(checklist_path),
        "sections": sections,
        "items": items,
    }


def compile_checklists(paths):
    checklists = [parse_checklist(path) for path in sorted(paths)]
    items = []
    for checklist in checklists:
        items.extend(checklist["items"])
    return {
        "generated_at": now_iso(),
        "checklists": checklists,
        "items": items,
    }


def default_checklist_paths():
    return sorted(str(path) for path in Path("docs/checklists").glob("*.md"))


def repo_root():
    return Path(__file__).resolve().parents[1]


def default_registry_dir():
    return repo_root() / "registry"


def context_fields_path(registry_dir=None):
    return Path(registry_dir or default_registry_dir()) / "context-fields.json"


def question_registry_path(registry_dir=None):
    return Path(registry_dir or default_registry_dir()) / "question-registry.json"


def checklist_context_map_path(registry_dir=None):
    return Path(registry_dir or default_registry_dir()) / "checklist-context-map.json"


def brand_context_dir(brand_dir):
    return Path(brand_dir) / "context"


def brand_context_path(brand_dir):
    return brand_context_dir(brand_dir) / "brand-dna.json"


def brand_answers_path(brand_dir):
    return brand_context_dir(brand_dir) / "answers.json"


def brand_open_questions_path(brand_dir):
    return brand_context_dir(brand_dir) / "open-questions.json"


def run_context_dir(brand_dir, run_id):
    return Path(brand_dir) / "runs" / run_id


def run_context_path(brand_dir, run_id):
    return run_context_dir(brand_dir, run_id) / "run-context.json"


def hitl_questions_path(brand_dir, run_id):
    return run_context_dir(brand_dir, run_id) / "hitl-questions.json"


def context_answer(field_id, value, source_type, source_ref, confidence, scope="brand", reason=""):
    answer = {
        "field_id": field_id,
        "value": value,
        "source_type": source_type,
        "source_ref": source_ref,
        "confidence": confidence,
        "scope": scope,
        "updated_at": now_iso(),
    }
    if reason:
        answer["reason"] = reason
    return answer


def load_context_fields(registry_dir=None):
    data = read_json(context_fields_path(registry_dir))
    fields = data.get("fields", [])
    errors = []
    seen = set()
    for field in fields:
        missing = sorted(CONTEXT_FIELD_REQUIRED_KEYS.difference(field))
        if missing:
            errors.append("context field missing keys: {} {}".format(field.get("field_id", "<unknown>"), ", ".join(missing)))
        field_id = field.get("field_id", "")
        if not field_id:
            continue
        if field_id in seen:
            errors.append("duplicate context field: {}".format(field_id))
        seen.add(field_id)
    if errors:
        raise RuntimeError("; ".join(errors))
    return data


def load_question_registry(registry_dir=None):
    data = read_json(question_registry_path(registry_dir))
    questions = data.get("questions", [])
    fields = {field["field_id"] for field in load_context_fields(registry_dir).get("fields", [])}
    errors = []
    seen = set()
    for question in questions:
        missing = sorted(QUESTION_REQUIRED_KEYS.difference(question))
        if missing:
            errors.append("question missing keys: {} {}".format(question.get("question_id", "<unknown>"), ", ".join(missing)))
        question_id = question.get("question_id", "")
        if question_id in seen:
            errors.append("duplicate question: {}".format(question_id))
        seen.add(question_id)
        if len(question.get("options", [])) != 3:
            errors.append("question must have exactly 3 options: {}".format(question_id))
        for field_id in question.get("field_ids", []):
            if field_id not in fields:
                errors.append("question {} references unknown field {}".format(question_id, field_id))
    if errors:
        raise RuntimeError("; ".join(errors))
    return data


def context_field_index(registry_dir=None):
    return {
        field["field_id"]: field
        for field in load_context_fields(registry_dir).get("fields", [])
    }


def question_index_by_field(registry_dir=None):
    index = {}
    for question in load_question_registry(registry_dir).get("questions", []):
        for field_id in question.get("field_ids", []):
            index.setdefault(field_id, question)
    return index


def evidence_source_labels(value):
    tokens = re.findall(r"`([^`]+)`", str(value or ""))
    if not tokens and value:
        tokens = [part.strip() for part in str(value).split(",")]
    sources = []
    seen = set()
    for token in tokens:
        source = canonical_evidence_source(token)
        if source and source not in seen:
            seen.add(source)
            sources.append(source)
    return sources


def infer_context_fields_for_item(item, fields):
    text = " ".join(
        [
            item.get("checklist_id", ""),
            item.get("section_title", ""),
            item.get("item_text", ""),
            item.get("required_evidence", ""),
        ]
    ).lower()
    required = []
    seen = set()
    for needles, field_ids in CONTEXT_FIELD_HINTS:
        if any(needle in text for needle in needles):
            for field_id in field_ids:
                if field_id in fields and field_id not in seen:
                    seen.add(field_id)
                    required.append(field_id)
    checklist_id = item.get("checklist_id", "")
    if checklist_id == "ecommerce-seo":
        for field_id in ("ecommerce_platform", "priority_product_groups"):
            if field_id in fields and field_id not in seen:
                seen.add(field_id)
                required.append(field_id)
    if checklist_id == "local-seo":
        for field_id in ("locations", "primary_local_conversion"):
            if field_id in fields and field_id not in seen:
                seen.add(field_id)
                required.append(field_id)
    if checklist_id == "ai-seo-aeo-geo":
        for field_id in ("ai_target_platforms", "ai_prompt_set"):
            if field_id in fields and field_id not in seen:
                seen.add(field_id)
                required.append(field_id)
    return required


def checklist_ids_from_args(values):
    if not values:
        return set()
    return {slugify(value.replace("_", "-")) for value in values}


def build_checklist_context_map(checklist_paths=None, registry_dir=None):
    checklist_paths = checklist_paths or default_checklist_paths()
    compiled = compile_checklists(checklist_paths)
    fields = context_field_index(registry_dir)
    questions_by_field = question_index_by_field(registry_dir)
    entries = []
    for item in compiled.get("items", []):
        requires = infer_context_fields_for_item(item, fields)
        question_ids = []
        for field_id in requires:
            question = questions_by_field.get(field_id)
            if question and question["question_id"] not in question_ids:
                question_ids.append(question["question_id"])
        can_infer = bool(requires) and all(
            fields[field_id].get("safe_to_infer") and field_id not in HIGH_RISK_CONTEXT_FIELDS
            for field_id in requires
        )
        evidence_sources = evidence_source_labels(item.get("required_evidence", ""))
        entries.append(
            {
                "checklist_id": item["checklist_id"],
                "checklist_title": item["checklist_title"],
                "section_id": item["section_id"],
                "section_title": item["section_title"],
                "item_id": item["item_id"],
                "item_text": item["item_text"],
                "requires": requires,
                "question_ids": question_ids,
                "evidence_sources": evidence_sources,
                "preferred_source_order": list(CONTEXT_SOURCE_PRIORITY),
                "can_infer": can_infer,
                "on_missing": "ask" if requires else "evidence",
                "blocked_status": "not_checked_blocked",
                "used_for": ["audit", "strategy", "content", "media_plan", "analysis", "reporting"],
            }
        )
    return {
        "generated_at": now_iso(),
        "source": "docs/checklists",
        "item_count": len(entries),
        "entries": entries,
    }


def validate_checklist_context_map(data, registry_dir=None, checklist_paths=None):
    fields = set(context_field_index(registry_dir))
    questions = {
        question["question_id"]
        for question in load_question_registry(registry_dir).get("questions", [])
    }
    errors = []
    seen = set()
    for entry in data.get("entries", []):
        item_id = entry.get("item_id", "")
        if not item_id:
            errors.append("map entry missing item_id")
            continue
        if item_id in seen:
            errors.append("duplicate map item_id: {}".format(item_id))
        seen.add(item_id)
        for field_id in entry.get("requires", []):
            if field_id not in fields:
                errors.append("map item {} references unknown field {}".format(item_id, field_id))
        for question_id in entry.get("question_ids", []):
            if question_id not in questions:
                errors.append("map item {} references unknown question {}".format(item_id, question_id))
        if entry.get("blocked_status") not in ("not_checked_blocked", ""):
            errors.append("map item {} has invalid blocked_status".format(item_id))
    if checklist_paths:
        compiled_ids = {
            item["item_id"]
            for item in compile_checklists(checklist_paths).get("items", [])
        }
        mapped_ids = {entry.get("item_id", "") for entry in data.get("entries", [])}
        missing = sorted(compiled_ids.difference(mapped_ids))
        extra = sorted(mapped_ids.difference(compiled_ids))
        if missing:
            errors.append("context map missing {} checklist items".format(len(missing)))
        if extra:
            errors.append("context map has {} stale items".format(len(extra)))
    return errors


def validate_context_system(registry_dir=None, checklist_paths=None):
    registry_dir = registry_dir or default_registry_dir()
    errors = []
    try:
        load_context_fields(registry_dir)
        load_question_registry(registry_dir)
    except RuntimeError as exc:
        errors.append(str(exc))
    map_path = checklist_context_map_path(registry_dir)
    if map_path.exists():
        errors.extend(
            validate_checklist_context_map(
                read_json(map_path),
                registry_dir=registry_dir,
                checklist_paths=checklist_paths or default_checklist_paths(),
            )
        )
    else:
        errors.append("missing checklist context map: {}".format(map_path))
    return {"ok": not errors, "errors": errors}


def section_list_value(markdown_text, heading):
    pattern = r"## {}\s*\n+(.*?)(?=\n## |\Z)".format(re.escape(heading))
    match = re.search(pattern, markdown_text, re.IGNORECASE | re.DOTALL)
    if not match:
        return []
    values = []
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            values.append(stripped[2:].strip())
    return values


def brand_context_from_markdown(brand_dir):
    brand_dir = Path(brand_dir)
    markdown_path = brand_dir / "brand-dna.md"
    fields = {}
    if not markdown_path.exists():
        return {
            "brand_id": brand_dir.name,
            "generated_at": now_iso(),
            "source_ref": str(markdown_path),
            "fields": fields,
        }
    text = markdown_path.read_text(encoding="utf-8")
    source_ref = str(markdown_path)
    mappings = {
        "brand_name": extract_brand_name(text),
        "website_url": extract_brand_website(text),
        "business_description": extract_section_value(text, "Business Description"),
        "brand_voice": extract_section_value(text, "Tone of Voice"),
        "target_audience": extract_section_value(text, "Target Audience"),
    }
    for field_id, value in mappings.items():
        if value and value.upper() != "TBD":
            fields[field_id] = context_answer(
                field_id,
                value,
                "brand_dna_markdown",
                source_ref,
                "medium",
            )
    competitors = section_list_value(text, "Competitors")
    if competitors and competitors != ["TBD"]:
        fields["competitors"] = context_answer(
            "competitors",
            competitors,
            "brand_dna_markdown",
            source_ref,
            "medium",
        )
    open_questions = section_list_value(text, "Open Questions")
    return {
        "brand_id": brand_dir.name,
        "generated_at": now_iso(),
        "source_ref": source_ref,
        "fields": fields,
        "open_questions": open_questions,
    }


def load_brand_context(brand_dir):
    path = brand_context_path(brand_dir)
    if path.exists():
        return read_json(path)
    return brand_context_from_markdown(brand_dir)


def load_brand_answers(brand_dir):
    path = brand_answers_path(brand_dir)
    if not path.exists():
        return {"brand_id": Path(brand_dir).name, "answers": {}}
    return read_json(path)


def load_run_context(brand_dir, run_id):
    if not run_id:
        return {"answers": {}}
    path = run_context_path(brand_dir, run_id)
    if not path.exists():
        return {"run_id": run_id, "answers": {}}
    return read_json(path)


def answer_value(record):
    if isinstance(record, dict):
        return record.get("value")
    return record


def values_text(values):
    if isinstance(values, dict):
        return values_text(values.values())
    if isinstance(values, (list, tuple, set)):
        return " ".join(values_text(value) for value in values)
    return str(values or "")


def brand_model_text(brand_context):
    fields = brand_context.get("fields", {})
    values = [
        answer_value(fields.get("business_model")),
        answer_value(fields.get("site_type")),
        answer_value(fields.get("business_description")),
    ]
    return values_text(values).lower()


def context_field_relevant(field_id, brand_context, selected_checklists):
    selected = set(selected_checklists or [])
    if not selected:
        return True
    text = brand_model_text(brand_context)
    if field_id in LOCAL_CONTEXT_FIELDS:
        return "local-seo" in selected or any(
            token in text
            for token in ("local", "restaurant", "clinic", "location", "service area", "multi-location")
        )
    if field_id in ECOMMERCE_CONTEXT_FIELDS:
        return "ecommerce-seo" in selected or any(
            token in text
            for token in ("ecommerce", "e-commerce", "dtc store", "shopify", "retail catalog", "marketplace")
        )
    if field_id in OFF_PAGE_CONTEXT_FIELDS:
        return "off-page-seo" in selected
    return True


def infer_context_value(field_id, brand_context):
    if field_id in HIGH_RISK_CONTEXT_FIELDS:
        return None
    text = " ".join(
        str(answer_value(value) or "")
        for value in brand_context.get("fields", {}).values()
    ).lower()
    if field_id == "business_model":
        if "ecommerce" in text or "dtc" in text:
            return context_answer(field_id, ["ecommerce"], "system_inferred", "brand_context", "medium", reason="Brand context mentions ecommerce or DTC.")
        if "saas" in text or "software" in text or "platform" in text:
            return context_answer(field_id, ["saas"], "system_inferred", "brand_context", "medium", reason="Brand context mentions SaaS, software, or platform.")
        if "clinic" in text or "restaurant" in text or "local" in text:
            return context_answer(field_id, ["local"], "system_inferred", "brand_context", "medium", reason="Brand context mentions local business signals.")
    if field_id == "site_type":
        model = infer_context_value("business_model", brand_context)
        if model:
            return context_answer(field_id, answer_value(model), "system_inferred", "brand_context", "medium", reason="Site type inferred from business model.")
    if field_id == "ymyl_exposure":
        if any(token in text for token in ("health", "clinic", "medical", "finance", "legal", "safety")):
            return context_answer(field_id, True, "system_inferred", "brand_context", "medium", reason="Brand context includes YMYL category terms.")
    return None


def resolve_context_fields(brand_dir, required_fields, registry_dir=None, run_id="", target_urls=None):
    fields = context_field_index(registry_dir)
    questions_by_field = question_index_by_field(registry_dir)
    brand_context = load_brand_context(brand_dir)
    brand_answers = load_brand_answers(brand_dir)
    run_context = load_run_context(brand_dir, run_id)
    resolved = {}
    assumptions = {}
    blocked = {}
    questions = {}
    for field_id in sorted(required_fields):
        run_answer = run_context.get("answers", {}).get(field_id)
        if run_answer:
            resolved[field_id] = run_answer
            continue
        brand_answer = brand_context.get("fields", {}).get(field_id)
        if brand_answer:
            resolved[field_id] = brand_answer
            continue
        prior_answer = brand_answers.get("answers", {}).get(field_id)
        if prior_answer:
            resolved[field_id] = prior_answer
            continue
        field = fields.get(field_id, {})
        inferred = None
        if field.get("safe_to_infer"):
            inferred = infer_context_value(field_id, brand_context)
        if inferred:
            inferred["scope"] = field.get("scope", "brand")
            resolved[field_id] = inferred
            assumptions[field_id] = inferred
            continue
        question = questions_by_field.get(field_id)
        if question:
            questions[question["question_id"]] = dict(question)
            continue
        blocked[field_id] = {
            "field_id": field_id,
            "status": "not_checked_blocked",
            "blocker": "{} is missing.".format(field.get("label", field_id)),
            "next_action": "Add {} to Brand DNA or run context.".format(field_id),
        }
    return {
        "brand_id": Path(brand_dir).name,
        "run_id": run_id,
        "target_urls": target_urls or [],
        "resolved": resolved,
        "assumptions": assumptions,
        "questions": list(questions.values()),
        "blocked": list(blocked.values()),
    }


def resolve_context_for_work(brand_dir, checklist_ids=None, run_id="", work_type="", target_urls=None, registry_dir=None, write_run=False):
    registry_dir = registry_dir or default_registry_dir()
    map_data = read_json(checklist_context_map_path(registry_dir))
    selected = checklist_ids_from_args(checklist_ids)
    entries = [
        entry for entry in map_data.get("entries", [])
        if not selected or entry.get("checklist_id") in selected
    ]
    brand_context = load_brand_context(brand_dir)
    required_fields = set()
    for entry in entries:
        for field_id in entry.get("requires", []):
            if context_field_relevant(field_id, brand_context, selected):
                required_fields.add(field_id)
    result = resolve_context_fields(
        brand_dir,
        required_fields,
        registry_dir=registry_dir,
        run_id=run_id,
        target_urls=target_urls or [],
    )
    result.update(
        {
            "ok": True,
            "work_type": work_type,
            "checklist_ids": sorted(selected) if selected else sorted({entry.get("checklist_id") for entry in entries}),
            "required_field_count": len(required_fields),
            "resolved_count": len(result["resolved"]),
            "question_count": len(result["questions"]),
            "blocked_count": len(result["blocked"]),
            "context_map_entries": len(entries),
            "generated_at": now_iso(),
        }
    )
    if write_run and run_id:
        run_context = {
            "run_id": run_id,
            "brand_id": Path(brand_dir).name,
            "work_type": work_type,
            "checklist_ids": result["checklist_ids"],
            "target_urls": target_urls or [],
            "required_fields": sorted(required_fields),
            "resolved": result["resolved"],
            "assumptions": result["assumptions"],
            "blocked": result["blocked"],
            "generated_at": result["generated_at"],
        }
        write_json(run_context, run_context_path(brand_dir, run_id))
        write_json({"questions": result["questions"]}, hitl_questions_path(brand_dir, run_id))
        write_json({"questions": result["questions"], "blocked": result["blocked"]}, brand_open_questions_path(brand_dir))
    return result


def init_brand_context(brand_dir):
    brand_dir = Path(brand_dir)
    brand_context = brand_context_from_markdown(brand_dir)
    brand_context_dir(brand_dir).mkdir(parents=True, exist_ok=True)
    write_json(brand_context, brand_context_path(brand_dir))
    if not brand_answers_path(brand_dir).exists():
        write_json({"brand_id": brand_dir.name, "answers": {}}, brand_answers_path(brand_dir))
    if not brand_open_questions_path(brand_dir).exists():
        write_json({"questions": [], "blocked": []}, brand_open_questions_path(brand_dir))
    return {"ok": True, "brand_context_path": str(brand_context_path(brand_dir)), "field_count": len(brand_context.get("fields", {}))}


def record_context_answer(brand_dir, field_id, value, question_id="", run_id="", scope="brand", confidence="high"):
    brand_dir = Path(brand_dir)
    parsed_value = [part.strip() for part in value.split(",") if part.strip()] if "," in value else value.strip()
    answer = context_answer(
        field_id,
        parsed_value,
        "client_confirmed",
        "question:{}".format(question_id or field_id),
        confidence,
        scope=scope,
    )
    if scope == "run":
        if not run_id:
            raise RuntimeError("run_id is required for run-scoped answers")
        run_context = load_run_context(brand_dir, run_id)
        run_context.setdefault("run_id", run_id)
        run_context.setdefault("answers", {})[field_id] = answer
        write_json(run_context, run_context_path(brand_dir, run_id))
        return {"ok": True, "scope": "run", "path": str(run_context_path(brand_dir, run_id)), "answer": answer}
    brand_context = load_brand_context(brand_dir)
    brand_context.setdefault("brand_id", brand_dir.name)
    brand_context.setdefault("fields", {})[field_id] = answer
    write_json(brand_context, brand_context_path(brand_dir))
    answers = load_brand_answers(brand_dir)
    answers.setdefault("brand_id", brand_dir.name)
    answers.setdefault("answers", {})[field_id] = answer
    write_json(answers, brand_answers_path(brand_dir))
    return {"ok": True, "scope": "brand", "path": str(brand_context_path(brand_dir)), "answer": answer}


def init_audit(
    compiled,
    target_url,
    audit_type,
    strict_evidence=False,
    scope="page",
    evidence_run_id_value="",
    brand_dir="",
):
    rows = []
    provider_connections = load_provider_connections(brand_dir)
    for item in compiled["items"]:
        row = {
            "checklist_id": item["checklist_id"],
            "section_id": item["section_id"],
            "item_id": item["item_id"],
            "item_text": item["item_text"],
            "status": "not_checked_blocked",
            "evidence_source": "",
            "artifact_ref": "",
            "result": "",
            "blocker": "Evidence not collected yet.",
            "next_action": "Collect evidence and set pass, fail, or not_applicable.",
        }
        if strict_evidence:
            route = route_evidence_for_item(
                item["item_text"],
                parse_logical_evidence_sources(item.get("required_evidence", "")),
                scope=scope,
                provider_connections=provider_connections,
            )
            row.update(route)
            row["evidence_run_id"] = evidence_run_id_value
            row["evidence_artifacts"] = []
            if route["provider_blockers"]:
                row["blocker"] = "; ".join(
                    blocker["blocker"] for blocker in route["provider_blockers"]
                )
                row["next_action"] = "; ".join(
                    blocker["next_action"] for blocker in route["provider_blockers"]
                )
        rows.append(row)
    metadata = {
        "created_at": now_iso(),
        "target_url": target_url,
        "audit_type": audit_type,
        "checklist_count": len(compiled["checklists"]),
        "item_count": len(compiled["items"]),
        "strict_evidence": bool(strict_evidence),
        "scope": scope,
    }
    if evidence_run_id_value:
        metadata["evidence_run_id"] = evidence_run_id_value
    if scope in {"site", GOOGLE_VISIBLE_SCOPE} and brand_dir and evidence_run_id_value:
        metadata.update(
            {
                "url_inventory_path": str(url_inventory_path(brand_dir)),
                "site_checks_path": str(site_checks_path(brand_dir)),
                "evidence_manifest_path": str(
                    evidence_dir(brand_dir, evidence_run_id_value) / "manifest.json"
                ),
            }
        )
    return {"metadata": metadata, "rows": rows}


def coverage_counts(rows):
    counts = {status: 0 for status in sorted(STATUSES)}
    for row in rows:
        status = row.get("status")
        if status in counts:
            counts[status] += 1
    return counts


def compiled_item_ids(compiled):
    return {item["item_id"] for item in compiled.get("items", [])}


def validate_audit(compiled, audit, strict_evidence=False, base_dir=None):
    errors = []
    expected_ids = compiled_item_ids(compiled)
    rows = audit.get("rows")
    if not isinstance(rows, list):
        return ["audit.rows must be a list"]

    seen_ids = set()
    for index, row in enumerate(rows, 1):
        missing = sorted(AUDIT_ROW_FIELDS - set(row))
        if missing:
            errors.append("row {} missing fields: {}".format(index, ", ".join(missing)))
            continue

        item_id = row.get("item_id")
        if item_id not in expected_ids:
            errors.append("row {} has unknown item_id: {}".format(index, item_id))
        if item_id in seen_ids:
            errors.append("row {} duplicates item_id: {}".format(index, item_id))
        seen_ids.add(item_id)

        status = row.get("status")
        if status not in STATUSES:
            errors.append("row {} has invalid status: {}".format(index, status))
            continue

        if status in {"pass", "fail"}:
            for field in ("evidence_source", "artifact_ref", "result"):
                if not str(row.get(field, "")).strip():
                    errors.append(
                        "row {} status {} needs nonempty {}".format(index, status, field)
                    )
            if strict_evidence:
                required_sources = (
                    row.get("resolved_required_sources")
                    or row.get("required_sources")
                    or []
                )
                evidence_sources = row_evidence_sources(row.get("evidence_source", ""))
                if row.get("provider_blockers"):
                    errors.append(
                        "row {} has unresolved provider blockers".format(index)
                    )
                if required_sources and not source_satisfies_required(
                    row.get("evidence_source", ""), required_sources
                ):
                    errors.append(
                        "row {} evidence_source must include one of: {}".format(
                            index, ", ".join(required_sources)
                        )
                    )
                if not artifact_ref_exists(row.get("artifact_ref", ""), base_dir=base_dir):
                    errors.append(
                        "row {} artifact_ref does not exist: {}".format(
                            index, row.get("artifact_ref", "")
                        )
                    )
                if any(str(source).startswith("manual:") for source in required_sources):
                    if not set(required_sources).intersection(evidence_sources):
                        errors.append(
                            "row {} manual source needs recorded evidence or blocker".format(
                                index
                            )
                        )
            if status == "fail" and not str(row.get("next_action", "")).strip():
                errors.append("row {} status fail needs nonempty next_action".format(index))
        elif status == "not_checked_blocked":
            for field in ("blocker", "next_action"):
                if not str(row.get(field, "")).strip():
                    errors.append("row {} blocked needs nonempty {}".format(index, field))
        elif status == "not_applicable":
            if not str(row.get("result", "")).strip():
                errors.append("row {} not_applicable needs a result reason".format(index))

    missing_ids = sorted(expected_ids - seen_ids)
    extra_ids = sorted(seen_ids - expected_ids)
    if missing_ids:
        errors.append("matrix missing {} checklist items".format(len(missing_ids)))
    if extra_ids:
        errors.append("matrix has {} unknown checklist items".format(len(extra_ids)))
    if len(rows) != len(expected_ids):
        errors.append(
            "row count {} does not match checklist item count {}".format(
                len(rows), len(expected_ids)
            )
        )

    metadata = audit.get("metadata", {})
    audit_type = metadata.get("audit_type", "partial")
    if (
        strict_evidence
        and metadata.get("scope") in {"site", GOOGLE_VISIBLE_SCOPE}
        and audit_type == "full"
    ):
        for field in (
            "url_inventory_path",
            "site_checks_path",
            "evidence_manifest_path",
        ):
            if not artifact_ref_exists(metadata.get(field, ""), base_dir=base_dir):
                errors.append("site audit metadata missing existing {}".format(field))
    counts = coverage_counts(rows)
    if audit_type == "full" and counts["not_checked_blocked"]:
        errors.append(
            "full audit has {} not_checked_blocked rows".format(
                counts["not_checked_blocked"]
            )
        )
    return errors


def init_authenticity(target):
    return {
        "metadata": {
            "created_at": now_iso(),
            "target": target,
            "status": "draft",
            "required_skill": CONTENT_AUTHENTICITY_SKILL,
            "required_skill_ref": CONTENT_AUTHENTICITY_SKILL_REF,
            "required_ai_text_risk_skill": AI_TEXT_RISK_SKILL,
            "required_ai_text_risk_skill_ref": AI_TEXT_RISK_SKILL_REF,
        },
        "sources": [],
        "claims": [],
        "detector_notes": [],
    }


def parse_detector_score_percent(value):
    if isinstance(value, (int, float)):
        if 0 < float(value) <= 1:
            return float(value) * 100
        return float(value)
    text = str(value or "")
    match = re.search(r"(\d+(?:\.\d+)?)", text)
    if not match:
        return None
    score = float(match.group(1))
    if "%" not in text and 0 < score <= 1:
        return score * 100
    return score


def is_ai_detector_note(note):
    haystack = "{} {}".format(note.get("tool", ""), note.get("note", "")).lower()
    return any(token in haystack for token in AI_DETECTOR_TOOL_TOKENS)


def strip_markdown_for_ai_text_risk(text):
    text = re.sub(r"(?s)\A---\s*.*?\s*---", " ", text or "")
    text = re.sub(r"(?s)```.*?```", " ", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r" \1 ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r" \1 ", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s+", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = re.sub(r"(?m)^\s*\d+[.]\s+", "", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text):
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text)
        if sentence.strip()
    ]


def split_paragraphs(text):
    text = re.sub(r"(?s)\A---\s*.*?\s*---", "", text or "").strip()
    return [
        strip_markdown_for_ai_text_risk(paragraph)
        for paragraph in re.split(r"\n\s*\n", text)
        if strip_markdown_for_ai_text_risk(paragraph)
    ]


def top_ratio(values):
    if not values:
        return 0.0
    counts = Counter(values)
    return max(counts.values()) / len(values)


def ai_text_risk_report(text):
    clean_text = strip_markdown_for_ai_text_risk(text)
    words = re.findall(r"[A-Za-z][A-Za-z']*", clean_text)
    word_count = len(words)
    lower_text = clean_text.lower()
    features = []
    score = 0.0

    def add_feature(name, points, evidence):
        nonlocal score
        points = round(float(points), 2)
        if points <= 0:
            return
        score += points
        features.append({"name": name, "points": points, "evidence": evidence})

    phrase_hits = [
        phrase for phrase in AI_TEXT_GENERIC_PHRASES if phrase in lower_text
    ]
    add_feature(
        "generic_phrases",
        min(24, len(phrase_hits) * 8),
        phrase_hits[:5],
    )

    transition_hits = []
    for sentence in split_sentences(clean_text):
        start = sentence.lower().strip(" ,:")
        if any(start.startswith(transition) for transition in AI_TEXT_FORMULAIC_TRANSITIONS):
            transition_hits.append(sentence[:80])
    if word_count:
        transition_rate = len(transition_hits) / max(1, word_count / 1000)
        add_feature(
            "formulaic_transitions",
            min(14, max(0, transition_rate - 3) * 2),
            transition_hits[:5],
        )

    sentences = split_sentences(clean_text)
    contrastive_hits = []
    for pattern in AI_TEXT_CONTRASTIVE_REFRAME_PATTERNS:
        for match in re.finditer(pattern, clean_text, re.IGNORECASE):
            contrastive_hits.append(re.sub(r"\s+", " ", match.group(0)).strip()[:120])
    contrastive_hits = list(dict.fromkeys(contrastive_hits))
    if len(contrastive_hits) >= 2:
        add_feature(
            "contrastive_reframe",
            min(10, len(contrastive_hits) * 3),
            contrastive_hits[:5],
        )

    sentence_lengths = [
        len(re.findall(r"[A-Za-z][A-Za-z']*", sentence)) for sentence in sentences
    ]
    if len(sentence_lengths) >= 8:
        average_length = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((length - average_length) ** 2 for length in sentence_lengths) / len(sentence_lengths)
        variation = (variance ** 0.5) / average_length if average_length else 0
        if 11 <= average_length <= 26 and variation < 0.38:
            add_feature(
                "uniform_sentence_rhythm",
                min(14, (0.38 - variation) * 36),
                {"average_words": round(average_length, 2), "variation": round(variation, 2)},
            )

    starts = []
    for sentence in sentences:
        match = re.match(r"([A-Za-z][A-Za-z']*)", sentence)
        if match:
            starts.append(match.group(1).lower())
    repeated_start_ratio = top_ratio(starts)
    if len(starts) >= 10 and repeated_start_ratio >= 0.22:
        add_feature(
            "repeated_sentence_starts",
            min(12, (repeated_start_ratio - 0.18) * 50),
            {"ratio": round(repeated_start_ratio, 2)},
        )

    paragraphs = split_paragraphs(text)
    paragraph_starts = []
    paragraph_lengths = []
    for paragraph in paragraphs:
        match = re.match(r"([A-Za-z][A-Za-z']*)", paragraph)
        if match:
            paragraph_starts.append(match.group(1).lower())
        paragraph_lengths.append(len(re.findall(r"[A-Za-z][A-Za-z']*", paragraph)))
    paragraph_start_ratio = top_ratio(paragraph_starts)
    if len(paragraph_starts) >= 6 and paragraph_start_ratio >= 0.28:
        add_feature(
            "repeated_paragraph_starts",
            min(10, (paragraph_start_ratio - 0.22) * 36),
            {"ratio": round(paragraph_start_ratio, 2)},
        )
    if len(paragraph_lengths) >= 6:
        paragraph_average = sum(paragraph_lengths) / len(paragraph_lengths)
        paragraph_variance = sum((length - paragraph_average) ** 2 for length in paragraph_lengths) / len(paragraph_lengths)
        paragraph_variation = (paragraph_variance ** 0.5) / paragraph_average if paragraph_average else 0
        if 35 <= paragraph_average <= 95 and paragraph_variation < 0.45:
            add_feature(
                "uniform_paragraph_blocks",
                min(10, (0.45 - paragraph_variation) * 22),
                {"average_words": round(paragraph_average, 2), "variation": round(paragraph_variation, 2)},
            )

    abstract_hits = [
        word for word in words if word.lower() in AI_TEXT_ABSTRACT_TERMS
    ]
    if word_count:
        abstract_rate = len(abstract_hits) / word_count * 100
        add_feature(
            "abstract_marketing_language",
            min(16, max(0, abstract_rate - 3) * 4),
            {"per_100_words": round(abstract_rate, 2), "examples": sorted(set(abstract_hits[:8]))},
        )

    digit_count = len(re.findall(r"\d", clean_text))
    proper_noun_count = len(
        re.findall(r"\b[A-Z][a-z]{2,}\b", re.sub(r"(?m)^#+.*$", "", text or ""))
    )
    if word_count >= 500 and digit_count < 3 and proper_noun_count < 8:
        add_feature(
            "low_specificity",
            12,
            {"digits": digit_count, "proper_nouns": proper_noun_count},
        )

    generic_endings = (
        "in conclusion",
        "final thoughts",
        "to sum up",
        "in summary",
    )
    headings = [
        line.strip("# ").lower()
        for line in (text or "").splitlines()
        if line.lstrip().startswith("#")
    ]
    ending_hits = [heading for heading in headings if heading in generic_endings]
    add_feature("generic_conclusion_heading", 6, ending_hits)

    score = round(min(100, score), 2)
    status = "not_checked_blocked" if word_count < 120 else "pass"
    if word_count >= 120 and score >= 20:
        status = "fail"
    return {
        "tool": "Strique local AI text risk gate",
        "score": score,
        "max_score": 20.0,
        "status": status,
        "word_count": word_count,
        "features": features,
        "note": (
            "Local AI-pattern risk score. This is an editorial signal, not proof of authorship."
        ),
    }


def content_authenticity_skill_errors(log):
    metadata = log.get("metadata", {})
    errors = []
    if metadata.get("required_skill") != CONTENT_AUTHENTICITY_SKILL:
        errors.append("content write missing required_skill {}".format(CONTENT_AUTHENTICITY_SKILL))
    if metadata.get("required_skill_ref") != CONTENT_AUTHENTICITY_SKILL_REF:
        errors.append(
            "content write missing required_skill_ref {}".format(
                CONTENT_AUTHENTICITY_SKILL_REF
            )
        )
    if not (Path(__file__).resolve().parents[1] / CONTENT_AUTHENTICITY_SKILL_REF).exists():
        errors.append("content authenticity skill file is missing")
    return errors


def ai_text_risk_skill_errors():
    if not (Path(__file__).resolve().parents[1] / AI_TEXT_RISK_SKILL_REF).exists():
        return ["AI text risk skill file is missing"]
    return []


def validate_authenticity(
    log,
    rewrite_text="",
    max_ai_detector_score=20.0,
    require_content_skill=False,
):
    errors = []
    if require_content_skill:
        errors.extend(content_authenticity_skill_errors(log))

    sources = log.get("sources")
    if not isinstance(sources, list):
        return ["sources must be a list"]

    concrete_sources = []
    source_ids = set()
    for index, source in enumerate(sources, 1):
        source_id = str(source.get("source_id", "")).strip()
        source_type = str(source.get("source_type", "")).strip()
        if not source_id:
            errors.append("source {} missing source_id".format(index))
        else:
            source_ids.add(source_id)
        for field in ("source_type", "source_ref", "extracted_facts"):
            if not str(source.get(field, "")).strip():
                errors.append("source {} missing {}".format(index, field))
        if source_type in CONCRETE_SOURCE_TYPES:
            concrete_sources.append(source)

    if not concrete_sources:
        errors.append("no concrete source found for publish-ready content")

    claims = log.get("claims", [])
    if not isinstance(claims, list):
        errors.append("claims must be a list")
        claims = []

    best_top_claims = []
    for index, claim in enumerate(claims, 1):
        claim_type = str(claim.get("claim_type", "")).strip()
        if claim_type == "best_top":
            best_top_claims.append(claim)
            refs = claim.get("source_ids", [])
            if not refs:
                errors.append("claim {} best_top needs source_ids".format(index))
            for source_id in refs:
                if source_id not in source_ids:
                    errors.append(
                        "claim {} references unknown source_id {}".format(index, source_id)
                    )

    if rewrite_text and re.search(r"\b(best|top)\b", rewrite_text, re.IGNORECASE):
        if not best_top_claims:
            errors.append("rewrite uses best/top language without best_top claim support")

    if rewrite_text:
        errors.extend(ai_text_risk_skill_errors())
        local_report = ai_text_risk_report(rewrite_text)
        if local_report["score"] >= max_ai_detector_score:
            errors.append(
                "local AI text risk score {} meets or exceeds max AI detector score {}".format(
                    local_report["score"], max_ai_detector_score
                )
            )

    detector_notes = log.get("detector_notes", [])
    if not isinstance(detector_notes, list):
        errors.append("detector_notes must be a list")
        detector_notes = []
    for index, note in enumerate(detector_notes, 1):
        if not isinstance(note, dict):
            errors.append("detector note {} must be an object".format(index))
            continue
        has_score = str(note.get("score", "")).strip() != ""
        if not is_ai_detector_note(note) and not has_score:
            continue
        score = parse_detector_score_percent(note.get("score", ""))
        tool = str(note.get("tool", "AI detector")).strip() or "AI detector"
        if score is None:
            errors.append(
                "detector note {} {} missing parseable AI detector score".format(
                    index, tool
                )
            )
        elif score >= max_ai_detector_score:
            errors.append(
                "detector note {} {} score {} meets or exceeds max AI detector score {}".format(
                    index, tool, score, max_ai_detector_score
                )
            )

    return errors


def write_content_with_authenticity(
    draft_file,
    content_output,
    authenticity_file,
    max_ai_detector_score=20.0,
):
    draft_text = Path(draft_file).read_text(encoding="utf-8")
    log = read_json(authenticity_file)
    ai_text_risk = ai_text_risk_report(draft_text)
    errors = validate_authenticity(
        log,
        draft_text,
        max_ai_detector_score=max_ai_detector_score,
        require_content_skill=True,
    )
    if errors:
        return {
            "ok": False,
            "errors": errors,
            "written": False,
            "required_skill": CONTENT_AUTHENTICITY_SKILL,
            "ai_text_risk": ai_text_risk,
        }
    write_text_file(content_output, draft_text)
    return {
        "ok": True,
        "errors": [],
        "written": True,
        "output": str(content_output),
        "required_skill": CONTENT_AUTHENTICITY_SKILL,
        "ai_text_risk": ai_text_risk,
    }


def parse_json_output(stdout):
    text = stdout.strip()
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        starts = [index for index in (text.find("{"), text.find("[")) if index >= 0]
        start = min(starts) if starts else -1
        end = max(text.rfind("}"), text.rfind("]"))
        if start < 0 or end < start:
            raise
        return json.loads(text[start : end + 1])


def run_composio(args, runner=None):
    command = ["composio"] + args
    subprocess_runner = runner or subprocess.run
    process = subprocess_runner(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0:
        detail = (process.stderr or process.stdout or "").strip()[:1000]
        raise RuntimeError("Composio command failed: {}".format(detail))
    parsed = parse_json_output(process.stdout or "{}")
    if isinstance(parsed, dict) and parsed.get("successful") is False:
        detail = parsed.get("error") or parsed.get("message") or parsed
        raise RuntimeError("Composio command failed: {}".format(detail))
    if isinstance(parsed, dict) and parsed.get("storedInFile") and parsed.get("outputFilePath"):
        try:
            stored_text = Path(parsed["outputFilePath"]).read_text(encoding="utf-8")
            parsed = parse_json_output(stored_text)
        except OSError as exc:
            raise RuntimeError("Composio output file could not be read: {}".format(exc))
        if isinstance(parsed, dict) and parsed.get("successful") is False:
            detail = parsed.get("error") or parsed.get("message") or parsed
            raise RuntimeError("Composio command failed: {}".format(detail))
    return parsed


def composio_execute(tool_slug, payload=None, runner=None):
    return run_composio(
        ["execute", tool_slug, "-d", json.dumps(payload or {})],
        runner=runner,
    )


def composio_proxy(url, payload, runner=None):
    return run_composio(
        [
            "proxy",
            url,
            "--toolkit",
            "googleads",
            "-X",
            "POST",
            "-H",
            "content-type: application/json",
            "-d",
            json.dumps(payload),
        ],
        runner=runner,
    )


def unwrap_composio_data(payload):
    data = payload.get("data", payload) if isinstance(payload, dict) else payload
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return data
    if isinstance(data, dict):
        body = data.get("body")
        if isinstance(body, str):
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                return data
        if isinstance(body, dict):
            return body
    return data


def keyword_csv_path(brand_dir):
    return Path(brand_dir) / "keywords" / "keywords.csv"


def keyword_universe_path(brand_dir):
    return Path(brand_dir) / "exports" / "keyword-universe.csv"


def keyword_summary_path(brand_dir):
    return Path(brand_dir) / "references" / "keyword-research-summary.json"


def read_csv_dict_rows(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        rows = list(reader)
        return reader.fieldnames or [], rows


def write_csv_dict_rows(path, fields, rows):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def normalize_keyword(value):
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def coerce_float(value):
    if value in (None, ""):
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def format_metric(value):
    number = coerce_float(value)
    if not number:
        return ""
    if number.is_integer():
        return str(int(number))
    return "{:.2f}".format(number).rstrip("0").rstrip(".")


def canonical_country(value):
    raw = str(value or "").strip()
    if not raw:
        return ""
    normalized = re.sub(r"\s+", " ", raw.lower().replace("_", " "))
    return COUNTRY_ALIASES.get(normalized, raw.title())


def infer_country_from_brand_dna(brand_dna_text):
    text = brand_dna_text or ""
    countries = sorted(GOOGLE_ADS_GEO_TARGETS.keys(), key=len, reverse=True)
    for country in countries:
        if re.search(r"\b{}\b".format(re.escape(country)), text, re.IGNORECASE):
            return country
    abbreviation_patterns = [
        (r"\bUSA\b|\bU\.S\.\b|\bUS\b(?=\s+(market|audience|traffic|customers|users))", "United States"),
        (r"\bUK\b|\bU\.K\.\b", "United Kingdom"),
        (r"\bUAE\b", "United Arab Emirates"),
    ]
    for pattern, country in abbreviation_patterns:
        if re.search(pattern, text):
            return country
    return ""


def infer_target_country(gsc_rows, brand_dna_text, explicit_country=""):
    if explicit_country:
        return canonical_country(explicit_country), "cli"

    totals = {}
    for row in gsc_rows or []:
        country = canonical_country(row.get("country") or row.get("gsc_country"))
        if not country:
            continue
        stats = totals.setdefault(country, {"clicks": 0.0, "impressions": 0.0})
        stats["clicks"] += coerce_float(row.get("clicks") or row.get("gsc_clicks"))
        stats["impressions"] += coerce_float(
            row.get("impressions") or row.get("gsc_impressions")
        )
    if totals:
        selected = max(
            totals.items(),
            key=lambda item: (item[1]["clicks"], item[1]["impressions"]),
        )[0]
        return selected, "gsc"

    country = infer_country_from_brand_dna(brand_dna_text)
    if country:
        return country, "brand_dna"
    return "", ""


def google_ads_geo_target(country):
    canonical = canonical_country(country)
    return GOOGLE_ADS_GEO_TARGETS.get(canonical, "")


def extract_section_value(markdown_text, heading):
    pattern = r"### {}\s*\n+\s*([^\n#]+)".format(re.escape(heading))
    match = re.search(pattern, markdown_text, re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_brand_website(brand_dna_text):
    explicit = extract_section_value(brand_dna_text, "Website URL")
    if explicit:
        return explicit.rstrip(".,)")
    match = re.search(r"https?://[^\s)]+", brand_dna_text)
    return match.group(0).rstrip(".,)") if match else ""


def extract_brand_name(brand_dna_text):
    return extract_section_value(brand_dna_text, "Name") or "brand"


def base_website_url(website_url):
    parsed = urlparse(website_url)
    if not parsed.scheme or not parsed.netloc:
        return website_url.rstrip("/")
    return "{}://{}".format(parsed.scheme, parsed.netloc).rstrip("/")


def normalize_site_url(value):
    raw = str(value or "").strip().lower().rstrip("/")
    if raw.startswith("sc-domain:"):
        return raw
    parsed = urlparse(raw)
    if not parsed.scheme or not parsed.netloc:
        return raw
    return "{}://{}{}".format(parsed.scheme, parsed.netloc, parsed.path.rstrip("/"))


def site_host(value):
    raw = str(value or "").strip().lower().rstrip("/")
    if raw.startswith("sc-domain:"):
        return raw.split(":", 1)[1].lstrip(".")
    parsed = urlparse(raw)
    return (parsed.netloc or raw).split("@")[-1].split(":")[0].lstrip(".")


def domains_match(left, right):
    left_host = site_host(left).removeprefix("www.")
    right_host = site_host(right).removeprefix("www.")
    return (
        left_host == right_host
        or left_host.endswith("." + right_host)
        or right_host.endswith("." + left_host)
    )


def list_gsc_sites(runner=None):
    response = composio_execute(GSC_LIST_SITES_TOOL, {}, runner=runner)
    data = unwrap_composio_data(response)
    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict):
        entries = (
            data.get("siteEntry")
            or data.get("site_entry")
            or data.get("sites")
            or data.get("entries")
            or []
        )
    else:
        entries = []

    sites = []
    for entry in entries:
        if isinstance(entry, str):
            sites.append({"siteUrl": entry})
        elif isinstance(entry, dict):
            site_url = entry.get("siteUrl") or entry.get("site_url") or entry.get("url")
            if site_url:
                normalized = dict(entry)
                normalized["siteUrl"] = site_url
                sites.append(normalized)
    return sites


def select_gsc_site(sites, website_url):
    expected = normalize_site_url(website_url)
    for site in sites:
        if normalize_site_url(site.get("siteUrl")) == expected:
            return site
    for site in sites:
        if domains_match(site.get("siteUrl"), website_url):
            return site
    return None


def matching_gsc_sites(sites, website_url):
    matches = [
        site
        for site in sites
        if normalize_site_url(site.get("siteUrl")) == normalize_site_url(website_url)
        or domains_match(site.get("siteUrl"), website_url)
    ]
    matches.sort(
        key=lambda site: (
            0 if str(site.get("siteUrl", "")).startswith("sc-domain:") else 1,
            str(site.get("siteUrl", "")),
        )
    )
    return matches


def first_rows_list(payload):
    data = unwrap_composio_data(payload)
    if isinstance(data, dict):
        rows = data.get("rows")
        if isinstance(rows, list):
            return rows
        for value in data.values():
            if isinstance(value, dict) and isinstance(value.get("rows"), list):
                return value.get("rows")
    return []


def parse_gsc_dimension_rows(payload, dimensions=None):
    dimensions = dimensions or ["query"]
    parsed_rows = []
    for row in first_rows_list(payload):
        if not isinstance(row, dict):
            continue
        keys = row.get("keys") or row.get("dimensions") or []
        parsed = {
            "dimensions": list(dimensions),
            "clicks": coerce_float(row.get("clicks")),
            "impressions": coerce_float(row.get("impressions")),
            "ctr": coerce_float(row.get("ctr")),
            "position": coerce_float(row.get("position")),
            "source": "gsc",
        }
        for index, dimension in enumerate(dimensions):
            parsed[dimension] = str(keys[index]).strip() if index < len(keys) else ""
        parsed_rows.append(parsed)
    return parsed_rows


def parse_gsc_rows(payload, dimensions=None):
    dimensions = dimensions or ["query", "page", "country"]
    parsed_rows = []
    for row in first_rows_list(payload):
        if not isinstance(row, dict):
            continue
        keys = row.get("keys") or row.get("dimensions") or []
        values = {}
        for index, dimension in enumerate(dimensions):
            if index < len(keys):
                values[dimension] = keys[index]
        query = row.get("query") or values.get("query") or ""
        if not str(query).strip():
            continue
        parsed_rows.append(
            {
                "keyword": str(query).strip(),
                "page": str(row.get("page") or values.get("page") or "").strip(),
                "country": str(row.get("country") or values.get("country") or "").strip(),
                "clicks": coerce_float(row.get("clicks")),
                "impressions": coerce_float(row.get("impressions")),
                "ctr": coerce_float(row.get("ctr")),
                "position": coerce_float(row.get("position")),
                "source": "gsc",
            }
        )
    return parsed_rows


def keyword_research_date_range(today=None):
    end_date = (today or date.today()) - timedelta(days=3)
    start_date = end_date - timedelta(days=480)
    return start_date.isoformat(), end_date.isoformat()


def fetch_gsc_keyword_rows(site_url, start_date, end_date, runner=None, row_limit=5000):
    rows = []
    start_row = 0
    while True:
        payload = {
            "site_url": site_url,
            "start_date": start_date,
            "end_date": end_date,
            "dimensions": ["query", "page", "country"],
            "row_limit": row_limit,
            "start_row": start_row,
            "data_state": "final",
            "search_type": "web",
        }
        response = composio_execute(GSC_SEARCH_ANALYTICS_TOOL, payload, runner=runner)
        batch = parse_gsc_rows(response, dimensions=payload["dimensions"])
        rows.extend(batch)
        if len(batch) < row_limit:
            break
        start_row += row_limit
    return rows


def fetch_gsc_dimension_rows(
    site_url,
    start_date,
    end_date,
    dimensions,
    runner=None,
    row_limit=5000,
    max_rows=None,
):
    rows = []
    start_row = 0
    while True:
        payload = {
            "site_url": site_url,
            "start_date": start_date,
            "end_date": end_date,
            "dimensions": dimensions,
            "row_limit": row_limit,
            "start_row": start_row,
            "data_state": "final",
            "search_type": "web",
        }
        response = composio_execute(GSC_SEARCH_ANALYTICS_TOOL, payload, runner=runner)
        batch = parse_gsc_dimension_rows(response, dimensions=dimensions)
        rows.extend(batch)
        if max_rows and len(rows) >= max_rows:
            return rows[:max_rows]
        if len(batch) < row_limit:
            break
        start_row += row_limit
    return rows


def get_gsc_site(site_url, runner=None):
    return unwrap_composio_data(
        composio_execute(GSC_GET_SITE_TOOL, {"site_url": site_url}, runner=runner)
    )


def list_gsc_sitemaps(site_url, runner=None):
    data = unwrap_composio_data(
        composio_execute(GSC_LIST_SITEMAPS_TOOL, {"site_url": site_url}, runner=runner)
    )
    if isinstance(data, dict):
        return data.get("sitemap") or data.get("sitemaps") or []
    return data if isinstance(data, list) else []


def get_gsc_sitemap(site_url, feedpath, runner=None):
    return unwrap_composio_data(
        composio_execute(
            GSC_GET_SITEMAP_TOOL,
            {"site_url": site_url, "feedpath": feedpath},
            runner=runner,
        )
    )


def inspect_gsc_url(site_url, inspection_url, runner=None):
    return unwrap_composio_data(
        composio_execute(
            GSC_INSPECT_URL_TOOL,
            {"site_url": site_url, "inspection_url": inspection_url},
            runner=runner,
        )
    )


def select_gsc_inspection_urls(inventory_rows, fallback_url="", limit=10):
    urls = []
    if fallback_url:
        urls.append(normalize_crawl_url(fallback_url, base_url=fallback_url) or fallback_url)
    sorted_rows = sorted(
        inventory_rows or [],
        key=lambda row: (
            0 if row.get("in_sitemap") == "yes" else 1,
            int(coerce_float(row.get("depth"))),
            row.get("url", ""),
        ),
    )
    for row in sorted_rows:
        url = row.get("url", "")
        if url and "?" not in url and url not in urls:
            urls.append(url)
        if len(urls) >= limit:
            break
    return urls[:limit]


def parse_keyword_planner_response(payload):
    data = unwrap_composio_data(payload)
    if isinstance(data, dict):
        results = (
            data.get("results")
            or data.get("keywordIdeas")
            or data.get("keyword_ideas")
            or []
        )
    elif isinstance(data, list):
        results = data
    else:
        results = []

    ideas = []
    for result in results:
        if not isinstance(result, dict):
            continue
        keyword = (
            result.get("text")
            or result.get("keyword")
            or result.get("keywordText")
            or result.get("keyword_text")
            or ""
        )
        keyword = str(keyword).strip()
        if not keyword:
            continue
        metrics = (
            result.get("keywordIdeaMetrics")
            or result.get("keyword_idea_metrics")
            or {}
        )
        avg_monthly_searches = metrics.get("avgMonthlySearches")
        if avg_monthly_searches is None:
            avg_monthly_searches = metrics.get("avg_monthly_searches")
        competition = metrics.get("competition") or ""
        competition_index = metrics.get("competitionIndex")
        if competition_index is None:
            competition_index = metrics.get("competition_index")
        ideas.append(
            {
                "keyword": keyword,
                "volume": format_metric(avg_monthly_searches),
                "competition": str(competition or "").upper(),
                "competition_index": format_metric(competition_index),
                "source": "keyword_planner",
            }
        )
    return ideas


def keyword_planner_payload(seed_keywords, website_url, geo_target, language):
    payload = {
        "language": language,
        "geoTargetConstants": [geo_target],
        "includeAdultKeywords": False,
        "keywordPlanNetwork": "GOOGLE_SEARCH",
    }
    seed_keywords = [keyword for keyword in seed_keywords if keyword]
    if website_url and seed_keywords:
        payload["keywordAndUrlSeed"] = {
            "url": website_url,
            "keywords": seed_keywords,
        }
    elif seed_keywords:
        payload["keywordSeed"] = {"keywords": seed_keywords}
    else:
        payload["urlSeed"] = {"url": website_url}
    return payload


def chunked(values, size):
    for index in range(0, len(values), size):
        yield values[index : index + size]


def generate_keyword_planner_ideas(
    customer_id,
    country,
    seed_keywords,
    website_url,
    language=DEFAULT_LANGUAGE_CONSTANT,
    runner=None,
    raw_limit=500,
):
    geo_target = google_ads_geo_target(country)
    if not geo_target:
        raise RuntimeError(
            "No Google Ads geo target mapping for target country: {}".format(country)
        )

    normalized_customer_id = re.sub(r"\D+", "", str(customer_id))
    if not normalized_customer_id:
        raise RuntimeError("google ads customer id is required")

    ideas = []
    seen = set()
    endpoint = GOOGLE_ADS_KEYWORD_IDEA_URL.format(normalized_customer_id)
    batches = list(chunked(seed_keywords, 20)) or [[]]
    for batch in batches:
        payload = keyword_planner_payload(batch, website_url, geo_target, language)
        response = composio_proxy(endpoint, payload, runner=runner)
        for idea in parse_keyword_planner_response(response):
            key = normalize_keyword(idea["keyword"])
            if key in seen:
                continue
            seen.add(key)
            ideas.append(idea)
            if len(ideas) >= raw_limit:
                return ideas
    return ideas


def extract_brand_seed_keywords(brand_dna_text):
    lower_text = brand_dna_text.lower()
    phrase_bank = [
        "agentic ai marketing platform",
        "ai marketing os",
        "ai marketing platform",
        "ai marketing agent",
        "marketing automation ai",
        "ai marketing automation",
        "paid media automation",
        "seo automation",
        "content automation",
        "lifecycle marketing automation",
        "marketing reporting automation",
        "ai content generation",
        "ai ad generator",
        "ai ad creator",
        "google ads automation",
        "meta ads automation",
        "shopify marketing automation",
        "ecommerce marketing automation",
        "dtc marketing automation",
        "ai marketing analytics",
        "marketing agency ai",
        "jasper alternatives",
        "adroll alternatives",
        "growth marketing automation",
        "ai campaign optimization",
        "ai seo automation",
        "marketing agent platform",
    ]
    seeds = []
    for phrase in phrase_bank:
        tokens = [token for token in phrase.split() if len(token) > 2]
        if phrase in lower_text or all(token in lower_text for token in tokens):
            seeds.append(phrase)
    return seeds


def keyword_is_relevant(keyword, brand_name=""):
    normalized = normalize_keyword(keyword)
    if not normalized:
        return False
    words = normalized.split()
    brand = normalize_keyword(brand_name)
    if brand and brand != "brand" and brand in normalized:
        return True
    if len(words) == 1 and normalized not in {"seo", "aso"}:
        return False
    context_pattern = (
        r"\b(marketing|advertising|advertisement|ad|ads|seo|aso|content|copywriting|"
        r"email|lifecycle|automation|analytics|growth|campaign|creative|ecommerce|"
        r"e-commerce|dtc|d2c|shopify|meta|facebook|instagram|google ads|hubspot|"
        r"posthog|platform|software|jasper|adroll)\b"
    )
    if re.search(r"\b(ai|artificial intelligence|agentic|agent)\b", normalized):
        return bool(re.search(context_pattern, normalized))
    return bool(re.search(context_pattern, normalized))


def build_seed_keywords(existing_rows, gsc_rows, brand_dna_text, brand_name="", limit=100):
    seeds = []
    for row in existing_rows:
        seeds.append(row.get("keyword", ""))
    sorted_gsc_rows = sorted(
        gsc_rows,
        key=lambda row: (coerce_float(row.get("clicks")), coerce_float(row.get("impressions"))),
        reverse=True,
    )
    for row in sorted_gsc_rows[:80]:
        seeds.append(row.get("keyword", ""))
    seeds.extend(extract_brand_seed_keywords(brand_dna_text))

    unique = []
    seen = set()
    for seed in seeds:
        key = normalize_keyword(seed)
        if not key or key in seen or not keyword_is_relevant(key, brand_name):
            continue
        seen.add(key)
        unique.append(key)
        if len(unique) >= limit:
            break
    return unique


def existing_keyword_candidates(existing_rows):
    candidates = []
    for row in existing_rows:
        keyword = row.get("keyword", "").strip()
        if not keyword:
            continue
        difficulty = row.get("difficulty", "")
        competition = difficulty.split(" ", 1)[0] if difficulty else ""
        competition_index = difficulty.split(" ", 1)[1] if " " in difficulty else ""
        candidates.append(
            {
                "keyword": keyword,
                "volume": row.get("volume", ""),
                "competition": competition,
                "competition_index": competition_index,
                "target_url": row.get("target_url", ""),
                "intent": row.get("intent", ""),
                "page_type": row.get("page_type", ""),
                "source": "existing",
            }
        )
    return candidates


def deduplicate_keyword_candidates(candidates):
    merged = {}
    order = []
    for candidate in candidates:
        key = normalize_keyword(candidate.get("keyword"))
        if not key:
            continue
        if key not in merged:
            merged[key] = {
                "keyword": key,
                "normalized_keyword": key,
                "sources": set(),
                "gsc_clicks": 0.0,
                "gsc_impressions": 0.0,
            }
            order.append(key)
        existing = merged[key]
        source = candidate.get("source")
        if source:
            existing["sources"].add(source)
        for field in ("competition", "competition_index", "target_url", "intent", "page_type"):
            if candidate.get(field) and not existing.get(field):
                existing[field] = candidate.get(field)

        current_volume = coerce_float(existing.get("volume"))
        candidate_volume = coerce_float(candidate.get("volume"))
        if candidate_volume > current_volume or (candidate.get("volume") and not existing.get("volume")):
            existing["volume"] = candidate.get("volume")

        clicks = coerce_float(candidate.get("clicks") or candidate.get("gsc_clicks"))
        impressions = coerce_float(
            candidate.get("impressions") or candidate.get("gsc_impressions")
        )
        existing["gsc_clicks"] += clicks
        existing["gsc_impressions"] += impressions
        if candidate.get("ctr") and not existing.get("gsc_ctr"):
            existing["gsc_ctr"] = format_metric(candidate.get("ctr"))
        if candidate.get("position") and not existing.get("gsc_position"):
            existing["gsc_position"] = format_metric(candidate.get("position"))
        if candidate.get("page") and not existing.get("gsc_page"):
            existing["gsc_page"] = candidate.get("page")
        if candidate.get("country") and not existing.get("gsc_country"):
            existing["gsc_country"] = canonical_country(candidate.get("country"))

    result = []
    for key in order:
        row = merged[key]
        row["sources"] = sorted(row["sources"])
        row["gsc_clicks"] = format_metric(row.get("gsc_clicks"))
        row["gsc_impressions"] = format_metric(row.get("gsc_impressions"))
        result.append(row)
    return result


def classify_keyword(candidate, website_url, brand_name):
    keyword = normalize_keyword(candidate.get("keyword"))
    base_url = base_website_url(website_url)
    brand = normalize_keyword(brand_name)

    if brand and brand != "brand" and brand in keyword:
        return {
            "intent": "navigational",
            "page_type": "homepage",
            "target_url": base_url,
        }
    if re.search(r"\b(best|top|vs|versus|alternative|alternatives|compare|comparison)\b", keyword):
        return {
            "intent": "commercial",
            "page_type": "comparison",
            "target_url": "{}/vs".format(base_url),
        }
    if re.search(r"\b(what|how|examples|guide|tutorial|ideas)\b", keyword):
        return {
            "intent": "informational",
            "page_type": "blog",
            "target_url": "{}/blog/what-is-an-ai-marketing-agent".format(base_url),
        }
    if re.search(r"\b(ecommerce|e-commerce|dtc|d2c|shopify)\b", keyword):
        return {
            "intent": "commercial",
            "page_type": "solutions",
            "target_url": "{}/solutions/ecommerce".format(base_url),
        }
    if re.search(r"\b(b2b|saas)\b", keyword):
        return {
            "intent": "commercial",
            "page_type": "solutions",
            "target_url": "{}/solutions/b2b-saas".format(base_url),
        }
    if re.search(r"\b(agency|agencies|freelancer|freelancers)\b", keyword):
        return {
            "intent": "commercial",
            "page_type": "solutions",
            "target_url": "{}/solutions/agencies".format(base_url),
        }
    if re.search(r"\b(meta|facebook|instagram)\b", keyword):
        return {
            "intent": "commercial",
            "page_type": "integration",
            "target_url": "{}/integrations/meta-ads".format(base_url),
        }
    if "google ads" in keyword or "adwords" in keyword:
        return {
            "intent": "commercial",
            "page_type": "integration",
            "target_url": "{}/integrations/google-ads".format(base_url),
        }
    if "hubspot" in keyword:
        return {
            "intent": "commercial",
            "page_type": "integration",
            "target_url": "{}/integrations/hubspot".format(base_url),
        }
    if "posthog" in keyword:
        return {
            "intent": "commercial",
            "page_type": "integration",
            "target_url": "{}/integrations/posthog".format(base_url),
        }
    if re.search(
        r"\b(ai|agent|agentic|marketing|automation|analytics|content|seo|email|ad|ads|campaign)\b",
        keyword,
    ):
        return {
            "intent": "commercial",
            "page_type": "product",
            "target_url": "{}/product".format(base_url),
        }
    return {
        "intent": candidate.get("intent") or "informational",
        "page_type": candidate.get("page_type") or "blog",
        "target_url": candidate.get("target_url") or "{}/blog".format(base_url),
    }


def keyword_priority(candidate, classification, brand_name):
    keyword = normalize_keyword(candidate.get("keyword"))
    brand = normalize_keyword(brand_name)
    volume = coerce_float(candidate.get("volume"))
    impressions = coerce_float(candidate.get("gsc_impressions"))
    clicks = coerce_float(candidate.get("gsc_clicks"))
    core_terms = re.search(
        r"\b(ai marketing|marketing automation|marketing agent|agentic ai|ai ad|ai ads|ecommerce marketing)\b",
        keyword,
    )
    if brand and brand != "brand" and brand in keyword:
        return "high"
    if clicks > 0 or impressions >= 100:
        return "high"
    if core_terms and classification.get("page_type") != "blog":
        return "high"
    if volume >= 500 and classification.get("target_url"):
        return "high"
    if volume >= 20 or classification.get("page_type") in {"solutions", "integration", "comparison"}:
        return "medium"
    return "low"


def keyword_difficulty(candidate):
    competition = str(candidate.get("competition") or "").strip()
    competition_index = str(candidate.get("competition_index") or "").strip()
    return " ".join(part for part in (competition, competition_index) if part)


def keyword_notes(candidate):
    notes = []
    if candidate.get("volume"):
        notes.append("GKP volume {}".format(candidate.get("volume")))
    difficulty = keyword_difficulty(candidate)
    if difficulty:
        notes.append("competition {}".format(difficulty))
    if candidate.get("gsc_clicks") or candidate.get("gsc_impressions"):
        notes.append(
            "GSC {} clicks and {} impressions".format(
                candidate.get("gsc_clicks") or "0",
                candidate.get("gsc_impressions") or "0",
            )
        )
    if candidate.get("gsc_page"):
        notes.append("observed page {}".format(candidate.get("gsc_page")))
    if not notes:
        notes.append("Seeded from normalized keyword research evidence")
    return "; ".join(notes)


def keyword_source_label(candidate):
    labels = []
    sources = set(candidate.get("sources") or [])
    if "gsc" in sources:
        labels.append("Google Search Console via Composio")
    if "keyword_planner" in sources:
        labels.append("Google Ads Keyword Planner via Composio")
    if "existing" in sources and not labels:
        labels.append("existing keywords.csv")
    return " + ".join(labels) or "keyword research harness"


def enrich_keyword_candidate(candidate, website_url, brand_name):
    classification = classify_keyword(candidate, website_url, brand_name)
    intent = candidate.get("intent") or classification["intent"]
    page_type = candidate.get("page_type") or classification["page_type"]
    target_url = candidate.get("target_url") or classification["target_url"]
    priority = keyword_priority(
        candidate,
        {"intent": intent, "page_type": page_type, "target_url": target_url},
        brand_name,
    )
    enriched = dict(candidate)
    enriched.update(
        {
            "keyword": candidate.get("keyword") or candidate.get("normalized_keyword"),
            "intent": intent,
            "page_type": page_type,
            "target_url": target_url,
            "difficulty": keyword_difficulty(candidate),
            "priority": priority,
            "source": keyword_source_label(candidate),
            "status": "new",
            "notes": keyword_notes(candidate),
        }
    )
    return enriched


def priority_sort_key(row):
    priority_order = {"high": 0, "medium": 1, "low": 2}
    return (
        priority_order.get(row.get("priority"), 9),
        -coerce_float(row.get("volume")),
        -coerce_float(row.get("gsc_impressions")),
        row.get("keyword", ""),
    )


def build_keyword_rows(existing_rows, gsc_rows, keyword_planner_rows, website_url, brand_name):
    candidates = (
        existing_keyword_candidates(existing_rows)
        + list(gsc_rows)
        + list(keyword_planner_rows)
    )
    candidates = [
        candidate
        for candidate in candidates
        if keyword_is_relevant(candidate.get("keyword", ""), brand_name)
    ]
    deduped = deduplicate_keyword_candidates(candidates)
    enriched = [
        enrich_keyword_candidate(candidate, website_url, brand_name)
        for candidate in deduped
    ]
    return sorted(enriched, key=priority_sort_key)


def keyword_universe_rows(enriched_rows):
    rows = []
    for row in enriched_rows:
        rows.append(
            {
                "keyword": row.get("keyword", ""),
                "normalized_keyword": normalize_keyword(row.get("keyword")),
                "intent": row.get("intent", ""),
                "page_type": row.get("page_type", ""),
                "target_url": row.get("target_url", ""),
                "volume": row.get("volume", ""),
                "difficulty": row.get("difficulty", ""),
                "priority": row.get("priority", ""),
                "sources": "; ".join(row.get("sources", [])),
                "gsc_clicks": row.get("gsc_clicks", ""),
                "gsc_impressions": row.get("gsc_impressions", ""),
                "gsc_ctr": row.get("gsc_ctr", ""),
                "gsc_position": row.get("gsc_position", ""),
                "gsc_page": row.get("gsc_page", ""),
                "gsc_country": row.get("gsc_country", ""),
                "status": row.get("status", ""),
                "notes": row.get("notes", ""),
            }
        )
    return rows


def keyword_tracker_rows(enriched_rows, max_rows=150):
    return [
        {field: row.get(field, "") for field in KEYWORD_ROW_FIELDS}
        for row in enriched_rows[:max_rows]
    ]


def generate_keyword_research(
    brand_dir,
    google_ads_customer_id,
    country="",
    language=DEFAULT_LANGUAGE_CONSTANT,
    max_prioritized=150,
    raw_limit=500,
    runner=None,
):
    brand_dir = Path(brand_dir)
    brand_dna_path = brand_dir / "brand-dna.md"
    if not brand_dna_path.exists():
        raise RuntimeError("Brand DNA not found: {}".format(brand_dna_path))
    brand_dna_text = brand_dna_path.read_text(encoding="utf-8")
    website_url = extract_brand_website(brand_dna_text)
    if not website_url:
        raise RuntimeError("Website URL not found in Brand DNA")
    brand_name = extract_brand_name(brand_dna_text)

    existing_rows = []
    keywords_path = keyword_csv_path(brand_dir)
    if keywords_path.exists():
        _, existing_rows = read_csv_dict_rows(keywords_path)

    blockers = []
    start_date, end_date = keyword_research_date_range()
    gsc_site = None
    gsc_rows = []
    available_sites = []
    try:
        available_sites = list_gsc_sites(runner=runner)
        gsc_site = select_gsc_site(available_sites, website_url)
        if not gsc_site:
            available = [site.get("siteUrl", "") for site in available_sites]
            raise RuntimeError(
                "No matching GSC property for {}. Available properties: {}".format(
                    website_url,
                    ", ".join(available) or "none",
                )
            )
        gsc_rows = fetch_gsc_keyword_rows(
            gsc_site.get("siteUrl"), start_date, end_date, runner=runner
        )
    except RuntimeError as exc:
        if available_sites and not gsc_site:
            raise
        blockers.append({"source": "gsc", "message": str(exc)})

    target_country, target_country_source = infer_target_country(
        gsc_rows,
        brand_dna_text,
        explicit_country=country,
    )
    if not target_country:
        raise RuntimeError(
            "Target country could not be inferred. Add target country to Brand DNA "
            "or pass --country."
        )

    seed_keywords = build_seed_keywords(existing_rows, gsc_rows, brand_dna_text, brand_name)
    keyword_planner_rows = []
    try:
        keyword_planner_rows = generate_keyword_planner_ideas(
            google_ads_customer_id,
            target_country,
            seed_keywords,
            website_url,
            language=language,
            runner=runner,
            raw_limit=raw_limit,
        )
    except RuntimeError as exc:
        blockers.append({"source": "keyword_planner", "message": str(exc)})

    enriched_rows = build_keyword_rows(
        existing_rows,
        gsc_rows,
        keyword_planner_rows,
        website_url,
        brand_name,
    )
    universe_rows = keyword_universe_rows(enriched_rows)
    prioritized_rows = keyword_tracker_rows(enriched_rows, max_rows=max_prioritized)

    write_csv_dict_rows(keyword_universe_path(brand_dir), KEYWORD_UNIVERSE_FIELDS, universe_rows)
    write_csv_dict_rows(keyword_csv_path(brand_dir), KEYWORD_ROW_FIELDS, prioritized_rows)

    summary = {
        "generated_at": now_iso(),
        "brand_dir": str(brand_dir),
        "website_url": website_url,
        "brand_name": brand_name,
        "target_country": target_country,
        "target_country_source": target_country_source,
        "language": language,
        "gsc_property": gsc_site.get("siteUrl") if gsc_site else "",
        "gsc_available_properties": [
            site.get("siteUrl", "") for site in available_sites
        ],
        "date_range": {"start_date": start_date, "end_date": end_date},
        "sources": {
            "gsc": {
                "tool": GSC_SEARCH_ANALYTICS_TOOL,
                "row_count": len(gsc_rows),
            },
            "keyword_planner": {
                "endpoint": GOOGLE_ADS_KEYWORD_IDEA_URL.format(
                    re.sub(r"\D+", "", str(google_ads_customer_id))
                ),
                "row_count": len(keyword_planner_rows),
            },
        },
        "counts": {
            "existing_keywords": len(existing_rows),
            "gsc_rows": len(gsc_rows),
            "keyword_planner_rows": len(keyword_planner_rows),
            "deduped_universe_rows": len(universe_rows),
            "prioritized_rows": len(prioritized_rows),
        },
        "blockers": blockers,
    }
    write_json(summary, keyword_summary_path(brand_dir))
    return {
        "ok": True,
        "summary_path": str(keyword_summary_path(brand_dir)),
        "keywords_path": str(keyword_csv_path(brand_dir)),
        "universe_path": str(keyword_universe_path(brand_dir)),
        "summary": summary,
    }


def summary_has_source_blocker(summary):
    for blocker in summary.get("blockers", []):
        text = json.dumps(blocker).lower()
        if (
            "gsc" in text
            or "search console" in text
            or "keyword_planner" in text
            or "keyword planner" in text
        ):
            return True
    return False


def validate_keyword_outputs(
    brand_dir,
    min_prioritized=50,
    max_prioritized=150,
    min_universe=200,
    allow_large=False,
):
    brand_dir = Path(brand_dir)
    errors = []
    counts = {
        "prioritized_rows": 0,
        "universe_rows": 0,
        "high_priority_rows": 0,
    }

    try:
        fields, rows = read_csv_dict_rows(keyword_csv_path(brand_dir))
    except (OSError, csv.Error) as exc:
        return {
            "errors": ["keywords.csv does not parse as CSV: {}".format(exc)],
            "counts": counts,
        }

    missing = [field for field in KEYWORD_ROW_FIELDS if field not in fields]
    if missing:
        errors.append("keywords.csv missing required columns: {}".format(", ".join(missing)))

    prioritized_rows = [
        row
        for row in rows
        if row.get("keyword", "").strip()
        and row.get("priority", "").strip().lower() in {"high", "medium", "low"}
    ]
    counts["prioritized_rows"] = len(prioritized_rows)
    counts["high_priority_rows"] = len(
        [row for row in prioritized_rows if row.get("priority", "").lower() == "high"]
    )

    seen = {}
    for index, row in enumerate(rows, 2):
        key = normalize_keyword(row.get("keyword"))
        if not key:
            continue
        if key in seen:
            errors.append(
                "duplicate keyword at row {} also appears at row {}: {}".format(
                    index,
                    seen[key],
                    row.get("keyword", ""),
                )
            )
        else:
            seen[key] = index

    if len(prioritized_rows) < min_prioritized:
        errors.append(
            "keywords.csv has {} prioritized rows, expected at least {}".format(
                len(prioritized_rows),
                min_prioritized,
            )
        )
    if not allow_large and len(prioritized_rows) > max_prioritized:
        errors.append(
            "keywords.csv has {} prioritized rows, expected at most {}".format(
                len(prioritized_rows),
                max_prioritized,
            )
        )

    for index, row in enumerate(rows, 2):
        if row.get("priority", "").strip().lower() != "high":
            continue
        for field in ("target_url", "source", "intent", "notes"):
            if not row.get(field, "").strip():
                errors.append("high-priority row {} missing {}".format(index, field))

    try:
        summary = read_json(keyword_summary_path(brand_dir))
    except (OSError, json.JSONDecodeError) as exc:
        summary = {}
        errors.append(
            "keyword research summary missing or invalid: {}".format(exc)
        )
    if not (summary.get("target_country") or summary.get("market")):
        errors.append("keyword research summary has no target country or market")

    try:
        universe_fields, universe_rows = read_csv_dict_rows(keyword_universe_path(brand_dir))
        counts["universe_rows"] = len(universe_rows)
    except (OSError, csv.Error) as exc:
        universe_fields = []
        universe_rows = []
        errors.append("keyword universe missing or invalid: {}".format(exc))

    if universe_rows and "keyword" not in universe_fields:
        errors.append("keyword universe missing keyword column")
    if len(universe_rows) < min_universe and not summary_has_source_blocker(summary):
        errors.append(
            "keyword universe has {} rows, expected at least {} without a GSC or "
            "Keyword Planner blocker".format(len(universe_rows), min_universe)
        )

    return {"errors": errors, "counts": counts}


def source_result(source, status, artifact="", blocker="", next_action="", summary=""):
    return {
        "source": source,
        "status": status,
        "artifact": artifact,
        "blocker": blocker,
        "next_action": next_action,
        "summary": summary,
    }


def fetch_google_api_json(url, payload=None, open_url=None):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    api_request = request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST" if payload is not None else "GET",
    )
    opener = open_url or request.urlopen
    try:
        with opener(api_request, timeout=65) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = exc.read().decode("utf-8", "replace")[:500]
        raise RuntimeError(
            "Google API request failed with HTTP {}: {}".format(exc.code, message)
        ) from exc
    except error.URLError as exc:
        raise RuntimeError("Google API request failed: {}".format(exc.reason)) from exc


def pagespeed_api_response(url, open_url=None):
    load_local_env()
    api_key = os.environ.get("GOOGLE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is required for PageSpeed Insights")
    query = urlencode({"url": url, "strategy": "mobile", "key": api_key})
    return fetch_google_api_json(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?{}".format(query),
        open_url=open_url,
    )


def lighthouse_summary(raw):
    audits = raw.get("audits", {})
    return {
        "finalUrl": raw.get("finalUrl") or raw.get("finalDisplayedUrl"),
        "categories": {
            key: value.get("score")
            for key, value in raw.get("categories", {}).items()
            if isinstance(value, dict)
        },
        "audits": {
            key: audits.get(key, {})
            for key in LIGHTHOUSE_DIAGNOSTIC_AUDITS
            if key in audits
        },
    }


def collect_firecrawl_source(context):
    data = firecrawl_scrape(context["url"], open_url=context.get("open_url"))
    artifact = write_evidence_artifact(context["target_dir"], "firecrawl.json", data)
    return source_result("firecrawl", "success", artifact, summary="Firecrawl scrape saved.")


def collect_playwright_source(context):
    script = r"""
const url = process.argv[1];
const desktopShot = process.argv[2];
const mobileShot = process.argv[3];
const playwrightModule = process.env.PLAYWRIGHT_MODULE || "playwright";
const { chromium } = await import(playwrightModule);
const browser = await chromium.launch({ headless: true });

function assertion(status, result, nextAction = "", viewport = "both", samples = []) {
  return { status, result, next_action: status === "fail" ? nextAction : "", viewport, samples };
}

function mergeAssertions(id, desktop, mobile) {
  const items = [desktop, mobile].filter(Boolean);
  const failed = items.filter((item) => item.status === "fail");
  if (failed.length) {
    return assertion(
      "fail",
      failed.map((item) => item.result).join(" "),
      failed[0].next_action || "Fix the failing Playwright assertion.",
      "both",
      failed.flatMap((item) => item.samples || []).slice(0, 12)
    );
  }
  if (items.length && items.every((item) => item.status === "not_applicable")) {
    return assertion(
      "not_applicable",
      items[0].result || `${id} is not applicable on sampled pages.`,
      "",
      "both",
      items.flatMap((item) => item.samples || []).slice(0, 12)
    );
  }
  return assertion(
    "pass",
    items.map((item) => item.result).filter(Boolean).join(" ") || `${id} passed.`,
    "",
    "both",
    items.flatMap((item) => item.samples || []).slice(0, 12)
  );
}

async function keyboardAssertion(page, viewportName) {
  const focusable = await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('a[href],button,input:not([type="hidden"]),select,textarea,[tabindex]:not([tabindex="-1"]),[role="button"]')];
    return nodes.filter((el) => {
      const style = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
    }).length;
  });
  if (!focusable) {
    return assertion("not_applicable", "No visible keyboard-focusable controls found.", "", viewportName);
  }
  const seen = [];
  for (let index = 0; index < Math.min(focusable + 3, 25); index += 1) {
    await page.keyboard.press("Tab");
    seen.push(await page.evaluate(() => {
      const el = document.activeElement;
      if (!el || el === document.body) return "";
      const label = el.getAttribute("aria-label") || el.innerText || el.value || el.tagName;
      return `${el.tagName.toLowerCase()} ${String(label).trim().slice(0, 60)}`;
    }));
  }
  const unique = [...new Set(seen.filter(Boolean))];
  if (unique.length >= Math.min(3, focusable)) {
    return assertion("pass", `Keyboard focus reached ${unique.length} visible controls.`, "", viewportName, unique.slice(0, 8));
  }
  return assertion(
    "fail",
    `Keyboard focus reached only ${unique.length} of ${focusable} visible controls.`,
    "Fix focus order, hidden focus traps, or controls that cannot receive keyboard focus.",
    viewportName,
    unique.slice(0, 8)
  );
}

async function layoutStressAssertion(page, viewportName, id, label, css, nextAction) {
  const before = await page.evaluate(() => ({
    textLength: document.body?.innerText?.trim().length || 0
  }));
  const handle = await page.addStyleTag({ content: css });
  const after = await page.evaluate(() => ({
    overflow: document.documentElement.scrollWidth > window.innerWidth + 2,
    textLength: document.body?.innerText?.trim().length || 0
  }));
  await handle.evaluate((node) => node.remove()).catch(() => {});
  if (after.overflow || after.textLength < before.textLength * 0.9) {
    return assertion("fail", `${label} caused overflow or content loss.`, nextAction, viewportName, [after]);
  }
  return assertion("pass", `${label} did not cause overflow or content loss.`, "", viewportName);
}

async function routeStatusAssertion() {
  const parsed = new URL(url);
  if (parsed.pathname.replace(/\/$/, "") !== "") {
    return assertion("not_applicable", "Route status handling is tested from the site root.", "", "desktop");
  }
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const testUrl = new URL(`/__seo-audit-missing-route-${Date.now()}`, url).href;
  try {
    const response = await page.goto(testUrl, { waitUntil: "networkidle", timeout: 30000 });
    const status = response ? response.status() : 0;
    const pageData = await page.evaluate(() => ({
      title: document.title,
      robots: document.querySelector('meta[name="robots"]')?.content || "",
      text: document.body?.innerText?.slice(0, 1000) || ""
    }));
    await page.close();
    const missingCopy = /404|not found|page not found|does not exist/i.test(`${pageData.title} ${pageData.text}`);
    const noindex = /noindex/i.test(pageData.robots);
    if (status >= 400 || missingCopy || noindex) {
      return assertion("pass", `Missing route returned status ${status || "unknown"} with missing-page signals.`, "", "desktop", [testUrl]);
    }
    return assertion(
      "fail",
      `Missing route returned status ${status || "unknown"} without clear 404 or noindex signals.`,
      "Return a real 404, noindex the fallback page, or render clear not-found content.",
      "desktop",
      [testUrl]
    );
  } catch (error) {
    await page.close().catch(() => {});
    return assertion("not_applicable", `Missing route status test could not complete: ${String(error).slice(0, 160)}`, "", "desktop", [testUrl]);
  }
}

async function collectAssertions(page, viewportName) {
  const dom = await page.evaluate((viewportName) => {
    function make(status, result, nextAction = "", samples = []) {
      return { status, result, next_action: status === "fail" ? nextAction : "", viewport: viewportName, samples };
    }
    function selector(el) {
      if (el.id) return `${el.tagName.toLowerCase()}#${el.id}`;
      const classes = [...el.classList].slice(0, 2).join(".");
      const text = (el.innerText || el.getAttribute("aria-label") || el.getAttribute("alt") || "").trim().replace(/\s+/g, " ").slice(0, 50);
      return `${el.tagName.toLowerCase()}${classes ? `.${classes}` : ""}${text ? ` ${text}` : ""}`;
    }
    function visible(el) {
      const style = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && Number(style.opacity || 1) > 0 && rect.width > 0 && rect.height > 0;
    }
    function accessName(el) {
      const id = el.getAttribute("aria-labelledby");
      const labelled = id ? id.split(/\s+/).map((part) => document.getElementById(part)?.innerText || "").join(" ") : "";
      const label = el.id ? document.querySelector(`label[for="${CSS.escape(el.id)}"]`)?.innerText || "" : "";
      const wrapped = el.closest("label")?.innerText || "";
      return (el.getAttribute("aria-label") || labelled || label || wrapped || el.getAttribute("alt") || el.getAttribute("title") || el.getAttribute("placeholder") || el.innerText || "").trim();
    }
    function rgb(value) {
      const match = String(value || "").match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([.\d]+))?\)/);
      if (!match || (match[4] && Number(match[4]) === 0)) return null;
      return { r: Number(match[1]), g: Number(match[2]), b: Number(match[3]) };
    }
    function background(el) {
      for (let node = el; node && node.nodeType === 1; node = node.parentElement) {
        const color = rgb(getComputedStyle(node).backgroundColor);
        if (color) return color;
      }
      return { r: 255, g: 255, b: 255 };
    }
    function luminance(color) {
      const values = [color.r, color.g, color.b].map((channel) => {
        const value = channel / 255;
        return value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
      });
      return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2];
    }
    function contrast(a, b) {
      const bright = Math.max(luminance(a), luminance(b));
      const dark = Math.min(luminance(a), luminance(b));
      return (bright + 0.05) / (dark + 0.05);
    }

    const checks = {};
    const textNodes = [...document.querySelectorAll("p,li,a,button,label,h1,h2,h3,span")].filter((el) => visible(el) && (el.innerText || "").trim().length > 1).slice(0, 120);
    const readabilityNodes = [...document.querySelectorAll("p,li,a,button,label")].filter((el) => visible(el) && (el.innerText || "").trim().length > 1).slice(0, 100);
    const bodyTextNodes = [...document.querySelectorAll("p,li")].filter((el) => visible(el) && (el.innerText || "").trim().length >= 80).slice(0, 80);
    const controls = [...document.querySelectorAll('a[href],button,input:not([type="hidden"]),select,textarea,[role="button"],[onclick]')].filter(visible).slice(0, 120);
    const fields = [...document.querySelectorAll('input:not([type="hidden"]):not([type="submit"]):not([type="button"]):not([type="reset"]),select,textarea')].filter(visible);
    const forms = [...document.querySelectorAll("form")].filter(visible);

    if (viewportName === "mobile") {
      const tooSmallText = readabilityNodes.filter((el) => {
        const style = getComputedStyle(el);
        const size = parseFloat(style.fontSize || "0");
        const lineHeight = parseFloat(style.lineHeight || "0") || size * 1.2;
        return size < 14 || lineHeight / Math.max(size, 1) < 1.15;
      }).slice(0, 10);
      checks.mobile_text_readability = tooSmallText.length
        ? make("fail", `${tooSmallText.length} sampled text elements are too small or tight on mobile.`, "Increase mobile font size or line height for readable body text.", tooSmallText.map(selector))
        : make(readabilityNodes.length ? "pass" : "not_applicable", readabilityNodes.length ? "Sampled mobile text is readable without zooming." : "No visible body text samples found on mobile.");

      const rects = controls.map((el) => ({ el, rect: el.getBoundingClientRect() })).filter((item) => item.rect.width > 0 && item.rect.height > 0);
      const small = rects.filter((item) => Math.min(item.rect.width, item.rect.height) < 40).slice(0, 10);
      const crowded = [];
      for (let index = 0; index < Math.min(rects.length, 80); index += 1) {
        for (let other = index + 1; other < Math.min(rects.length, 80); other += 1) {
          const a = rects[index].rect;
          const b = rects[other].rect;
          const close = Math.abs((a.left + a.right) / 2 - (b.left + b.right) / 2) < 44 && Math.abs((a.top + a.bottom) / 2 - (b.top + b.bottom) / 2) < 44;
          if (close) crowded.push(selector(rects[index].el));
        }
      }
      checks.tap_targets = small.length || crowded.length
        ? make("fail", `${small.length} small and ${crowded.length} crowded mobile tap targets found.`, "Increase tap target size or spacing to at least common mobile accessibility targets.", small.map((item) => selector(item.el)).concat(crowded).slice(0, 10))
        : make(controls.length ? "pass" : "not_applicable", controls.length ? "Mobile tap targets are large enough in sampled controls." : "No visible tap targets found.");
    }

    const overflow = document.documentElement.scrollWidth > window.innerWidth + 2;
    checks.horizontal_scroll = overflow
      ? make("fail", `Document width ${document.documentElement.scrollWidth}px exceeds viewport ${window.innerWidth}px.`, "Fix elements causing horizontal overflow.", [{ scrollWidth: document.documentElement.scrollWidth, viewportWidth: window.innerWidth }])
      : make("pass", "No horizontal overflow detected.");

    const overlayNodes = [...document.querySelectorAll('dialog[open],[role="dialog"],[aria-modal="true"],.modal,.popup,.interstitial,.cookie,[class*="modal"],[class*="popup"],[class*="overlay"]')]
      .concat([...document.querySelectorAll("body *")].filter((el) => ["fixed", "sticky"].includes(getComputedStyle(el).position)))
      .filter(visible)
      .filter((el) => {
        const rect = el.getBoundingClientRect();
        const area = rect.width * rect.height;
        return area > window.innerWidth * window.innerHeight * 0.25 && rect.top < window.innerHeight * 0.75;
      })
      .slice(0, 10);
    checks.blocking_popups_interstitials = overlayNodes.length
      ? make("fail", `${overlayNodes.length} large fixed, modal, or interstitial elements may block main content.`, "Remove or reduce blocking overlays on first render, especially on mobile.", overlayNodes.map(selector))
      : make("pass", "No blocking popup or interstitial overlay detected on first render.");

    const hashLinks = [...document.querySelectorAll("a[href*='#']")].filter((el) => {
      const href = new URL(el.href, location.href);
      return visible(el) && href.origin === location.origin && href.pathname === location.pathname && href.hash.length > 1;
    }).slice(0, 30);
    const missingHashTargets = hashLinks.filter((el) => {
      const id = decodeURIComponent(new URL(el.href).hash.slice(1));
      return !document.getElementById(id) && !document.querySelector(`[name="${CSS.escape(id)}"]`);
    }).slice(0, 10);
    checks.fragment_deep_links = missingHashTargets.length
      ? make("fail", `${missingHashTargets.length} same-page fragment links point to missing targets.`, "Add matching ids or remove broken fragment links.", missingHashTargets.map((el) => el.href))
      : make(hashLinks.length ? "pass" : "not_applicable", hashLinks.length ? "Same-page fragment links have matching targets." : "No same-page fragment links found.");

    const lazyImages = [...document.querySelectorAll('img[loading="lazy"],img[data-src],img[data-srcset],source[data-srcset]')].filter((el) => {
      const rect = el.getBoundingClientRect();
      return rect.top >= 0 && rect.top < window.innerHeight && rect.left < window.innerWidth;
    }).slice(0, 40);
    const unloadedLazy = lazyImages.filter((el) => el.tagName !== "IMG" || !el.naturalWidth).slice(0, 10);
    checks.lazy_loading_in_viewport = unloadedLazy.length
      ? make("fail", `${unloadedLazy.length} in-viewport lazy elements are not loaded after network idle.`, "Avoid lazy-loading critical in-viewport content.", unloadedLazy.map(selector))
      : make("pass", "No unloaded in-viewport lazy content detected.");

    const unlabeledFields = fields.filter((el) => !accessName(el)).slice(0, 10);
    checks.form_accessibility = fields.length
      ? (unlabeledFields.length
        ? make("fail", `${unlabeledFields.length} visible form fields lack labels or accessible names.`, "Add visible labels, aria-label, or aria-labelledby for form fields.", unlabeledFields.map(selector))
        : make("pass", "Visible form fields have accessible names."))
      : make("not_applicable", "No visible form fields found.");

    const badContrast = textNodes.filter((el) => {
      const style = getComputedStyle(el);
      const foreground = rgb(style.color);
      if (!foreground) return false;
      const ratio = contrast(foreground, background(el));
      const size = parseFloat(style.fontSize || "0");
      const threshold = size >= 24 ? 3 : 4.5;
      return ratio < threshold;
    }).slice(0, 10);
    checks.color_contrast = badContrast.length
      ? make("fail", `${badContrast.length} sampled text elements have low contrast.`, "Increase foreground/background contrast for readable text.", badContrast.map(selector))
      : make(textNodes.length ? "pass" : "not_applicable", textNodes.length ? "Sampled text meets contrast thresholds." : "No visible text samples found for contrast.");

    const unnamedControls = controls.filter((el) => !accessName(el)).slice(0, 10);
    checks.inaccessible_controls = unnamedControls.length
      ? make("fail", `${unnamedControls.length} visible controls lack accessible names.`, "Add text, aria-label, or labelledby values to interactive controls.", unnamedControls.map(selector))
      : make(controls.length ? "pass" : "not_applicable", controls.length ? "Visible controls have accessible names." : "No visible controls found.");

    const tables = [...document.querySelectorAll("table")].filter(visible);
    const weakTables = tables.filter((table) => !table.querySelector("th,caption,[scope]") && table.getAttribute("role") !== "presentation").slice(0, 10);
    checks.table_semantics = tables.length
      ? (weakTables.length
        ? make("fail", `${weakTables.length} visible tables lack semantic headers or captions.`, "Use table headers/captions for tabular data or avoid layout tables.", weakTables.map(selector))
        : make("pass", "Visible tables include semantic table structure."))
      : make("not_applicable", "No visible tables found.");

    const longLines = bodyTextNodes.filter((el) => {
      const style = getComputedStyle(el);
      const size = parseFloat(style.fontSize || "16");
      const approxCharacters = el.getBoundingClientRect().width / Math.max(size * 0.5, 1);
      return approxCharacters > (viewportName === "mobile" ? 80 : 105);
    }).slice(0, 10);
    checks.body_text_line_length = longLines.length
      ? make("fail", `${longLines.length} long-form text blocks have excessive line length.`, "Constrain text measure for readable desktop and mobile content.", longLines.map(selector))
      : make(bodyTextNodes.length ? "pass" : "not_applicable", bodyTextNodes.length ? "Sampled body text line length is readable." : "No long-form body text blocks found.");

    if (viewportName === "mobile") {
      const mobileIssues = [];
      if (unlabeledFields.length) mobileIssues.push("unlabeled fields");
      if (forms.length && !forms.some((form) => form.querySelector('button,input[type="submit"],[role="button"]'))) mobileIssues.push("missing visible submit control");
      if (fields.length > 12) mobileIssues.push("too many visible fields");
      if (overflow) mobileIssues.push("horizontal overflow");
      checks.mobile_form_usability = fields.length
        ? (mobileIssues.length
          ? make("fail", `Mobile form usability issues found: ${mobileIssues.join(", ")}.`, "Simplify mobile forms, label fields, and keep submit controls visible.", mobileIssues)
          : make("pass", "Mobile forms are short enough and usable in the viewport."))
        : make("not_applicable", "No visible mobile form fields found.");
    }

    const hasSpaMarker = Boolean(document.querySelector("#__next,#root,[data-reactroot]")) || [...document.scripts].some((script) => /_next|vite|webpack|react|vue|nuxt/i.test(script.src || ""));
    checks.client_route_metadata = hasSpaMarker
      ? make("not_applicable", "SPA markers were found, but route-change metadata was not triggered by this deterministic pass.")
      : make("not_applicable", "No client-side route-change evidence detected.");

    return checks;
  }, viewportName);
  dom.keyboard_navigation = await keyboardAssertion(page, viewportName);
  dom.zoom_readability = await layoutStressAssertion(
    page,
    viewportName,
    "zoom_readability",
    "Common zoom readability",
    "html { font-size: 200% !important; }",
    "Fix layouts that lose content or overflow when users zoom text."
  );
  dom.text_spacing = await layoutStressAssertion(
    page,
    viewportName,
    "text_spacing",
    "WCAG text spacing",
    "* { line-height: 1.5 !important; letter-spacing: 0.12em !important; word-spacing: 0.16em !important; } p { margin-bottom: 2em !important; }",
    "Fix layouts that lose content or overflow with increased text spacing."
  );
  return dom;
}

async function inspect(viewport, screenshotPath, viewportName) {
  const page = await browser.newPage({ viewport });
  await page.goto(url, { waitUntil: "networkidle", timeout: 45000 });
  await page.screenshot({ path: screenshotPath, fullPage: true });
  const data = await page.evaluate(() => ({
    url: location.href,
    title: document.title,
    metaDescription: document.querySelector('meta[name="description"]')?.content || "",
    canonical: document.querySelector('link[rel="canonical"]')?.href || "",
    robots: document.querySelector('meta[name="robots"]')?.content || "",
    headings: [...document.querySelectorAll("h1,h2,h3")].slice(0, 80).map((el) => ({ tag: el.tagName, text: el.innerText.trim() })),
    links: [...document.querySelectorAll("a[href]")].slice(0, 250).map((el) => ({ text: el.innerText.trim(), href: el.href })),
    scripts: [...document.scripts].slice(0, 250).map((el) => ({ src: el.src || "", type: el.type || "", async: el.async, defer: el.defer })),
    jsonLd: [...document.querySelectorAll('script[type="application/ld+json"]')].map((el) => el.textContent.trim()),
    visibleTextLength: document.body?.innerText?.trim().length || 0
  }));
  data.assertions = await collectAssertions(page, viewportName);
  await page.close();
  return data;
}
const desktop = await inspect({ width: 1440, height: 1100 }, desktopShot, "desktop");
const mobile = await inspect({ width: 390, height: 844, isMobile: true }, mobileShot, "mobile");
const routeStatus = await routeStatusAssertion();
const assertions = {
  fragment_deep_links: desktop.assertions.fragment_deep_links,
  mobile_text_readability: mobile.assertions.mobile_text_readability,
  tap_targets: mobile.assertions.tap_targets,
  horizontal_scroll: mergeAssertions("horizontal_scroll", desktop.assertions.horizontal_scroll, mobile.assertions.horizontal_scroll),
  blocking_popups_interstitials: mergeAssertions("blocking_popups_interstitials", desktop.assertions.blocking_popups_interstitials, mobile.assertions.blocking_popups_interstitials),
  route_status_handling: routeStatus,
  client_route_metadata: desktop.assertions.client_route_metadata,
  lazy_loading_in_viewport: mergeAssertions("lazy_loading_in_viewport", desktop.assertions.lazy_loading_in_viewport, mobile.assertions.lazy_loading_in_viewport),
  form_accessibility: mergeAssertions("form_accessibility", desktop.assertions.form_accessibility, mobile.assertions.form_accessibility),
  color_contrast: mergeAssertions("color_contrast", desktop.assertions.color_contrast, mobile.assertions.color_contrast),
  keyboard_navigation: mergeAssertions("keyboard_navigation", desktop.assertions.keyboard_navigation, mobile.assertions.keyboard_navigation),
  inaccessible_controls: mergeAssertions("inaccessible_controls", desktop.assertions.inaccessible_controls, mobile.assertions.inaccessible_controls),
  table_semantics: mergeAssertions("table_semantics", desktop.assertions.table_semantics, mobile.assertions.table_semantics),
  zoom_readability: mergeAssertions("zoom_readability", desktop.assertions.zoom_readability, mobile.assertions.zoom_readability),
  text_spacing: mergeAssertions("text_spacing", desktop.assertions.text_spacing, mobile.assertions.text_spacing),
  body_text_line_length: mergeAssertions("body_text_line_length", desktop.assertions.body_text_line_length, mobile.assertions.body_text_line_length),
  mobile_form_usability: mobile.assertions.mobile_form_usability
};
await browser.close();
console.log(JSON.stringify({ desktop, mobile, assertions, screenshots: { desktop: desktopShot, mobile: mobileShot } }));
"""
    target_dir = Path(context["target_dir"])
    desktop_shot = str(target_dir / "playwright-desktop.png")
    mobile_shot = str(target_dir / "playwright-mobile.png")
    runner = context.get("runner") or subprocess.run
    env = dict(os.environ)
    env.setdefault("PLAYWRIGHT_MODULE", DEFAULT_PLAYWRIGHT_MODULE)
    process = runner(
        ["node", "--input-type=module", "-e", script, context["url"], desktop_shot, mobile_shot],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    if process.returncode != 0:
        raise RuntimeError((process.stderr or process.stdout or "Playwright failed")[:1000])
    artifact = write_evidence_artifact(
        target_dir, "playwright.json", parse_json_output(process.stdout)
    )
    return source_result("playwright", "success", artifact, summary="Playwright render saved.")


def collect_lighthouse_source(context):
    env = dict(os.environ)
    env.setdefault("CHROME_PATH", DEFAULT_CHROME_PATH)
    runner = context.get("runner") or subprocess.run
    process = runner(
        [
            "lighthouse",
            context["url"],
            "--chrome-flags=--headless=new --no-sandbox",
            "--output=json",
            "--quiet",
        ],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    if process.returncode != 0:
        psi = pagespeed_api_response(context["url"], open_url=context.get("open_url"))
        summary = lighthouse_summary(psi.get("lighthouseResult", {}))
        summary["fallback"] = {
            "source": "pagespeed_lighthouse",
            "local_error": (process.stderr or process.stdout or "Lighthouse failed")[:1000],
        }
    else:
        summary = lighthouse_summary(parse_json_output(process.stdout))
    artifact = write_evidence_artifact(context["target_dir"], "lighthouse.json", summary)
    return source_result("lighthouse", "success", artifact, summary="Lighthouse summary saved.")


def collect_pagespeed_source(context):
    data = pagespeed_api_response(context["url"], open_url=context.get("open_url"))
    lighthouse = data.get("lighthouseResult", {})
    audits = lighthouse.get("audits", {})
    summary = {
        "id": data.get("id"),
        "loadingExperience": data.get("loadingExperience", {}),
        "originLoadingExperience": data.get("originLoadingExperience", {}),
        "categories": {
            key: value.get("score")
            for key, value in lighthouse.get("categories", {}).items()
            if isinstance(value, dict)
        },
        "audits": {
            key: audits.get(key, {})
            for key in LIGHTHOUSE_DIAGNOSTIC_AUDITS
            if key in audits
        },
    }
    artifact = write_evidence_artifact(context["target_dir"], "pagespeed.json", summary)
    return source_result("pagespeed", "success", artifact, summary="PageSpeed summary saved.")


def fetch_public_http_evidence(url, open_url=None):
    parsed = urlparse(url)
    request_url = urlunparse((parsed.scheme or "https", parsed.netloc, parsed.path or "/", "", "", ""))
    headers = {}
    status = 0
    final_url = request_url
    blocker = ""
    opener = open_url or request.urlopen
    request_headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Strique SEO Audit Harness; +https://www.strique.io)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    for method in ("HEAD", "GET"):
        try:
            public_request = request.Request(request_url, headers=request_headers, method=method)
            with opener(public_request, timeout=20) as response:
                status = getattr(response, "status", 0) or response.getcode()
                final_url = response.geturl()
                headers = {key.lower(): value for key, value in response.headers.items()}
                blocker = ""
                break
        except error.HTTPError as exc:
            status = exc.code
            final_url = exc.geturl()
            headers = {key.lower(): value for key, value in exc.headers.items()}
            blocker = str(exc)
            if method == "HEAD":
                continue
        except Exception as exc:
            blocker = str(exc)
            if method == "HEAD":
                continue

    tls = {}
    if (parsed.scheme or "https") == "https" and parsed.hostname:
        try:
            context = ssl.create_default_context()
            with socket.create_connection((parsed.hostname, parsed.port or 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=parsed.hostname) as secure_sock:
                    cert = secure_sock.getpeercert()
            not_after = cert.get("notAfter", "")
            expires_at = datetime.fromtimestamp(
                ssl.cert_time_to_seconds(not_after),
                timezone.utc,
            )
            days_remaining = (expires_at - datetime.now(timezone.utc)).days
            tls = {
                "host": parsed.hostname,
                "not_after": not_after,
                "expires_at": expires_at.isoformat(),
                "days_remaining": days_remaining,
                "valid": days_remaining >= 0,
                "subject_alt_names": [
                    value for key, value in cert.get("subjectAltName", []) if key == "DNS"
                ],
            }
        except Exception as exc:
            tls = {"host": parsed.hostname, "valid": False, "blocker": str(exc)}

    return {
        "url": request_url,
        "final_url": final_url,
        "status": status,
        "headers": headers,
        "tls": tls,
        "blocker": blocker,
    }


def collect_public_http_source(context):
    data = fetch_public_http_evidence(context["url"], open_url=context.get("open_url"))
    artifact = write_evidence_artifact(context["target_dir"], "public-http.json", data)
    return source_result("public_http", "success", artifact, summary="Public HTTP/TLS evidence saved.")


def collect_crux_source(context):
    load_local_env()
    api_key = os.environ.get("GOOGLE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is required for CrUX")
    data = fetch_google_api_json(
        "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key={}".format(api_key),
        payload={"url": context["url"]},
        open_url=context.get("open_url"),
    )
    artifact = write_evidence_artifact(context["target_dir"], "crux.json", data)
    return source_result("crux", "success", artifact, summary="CrUX record saved.")


def collect_gsc_source(context):
    start_date, end_date = keyword_research_date_range()
    dimension_row_cap = int(context.get("gsc_dimension_row_cap", 5000) or 0)
    dimension_row_limit = min(5000, dimension_row_cap) if dimension_row_cap else 5000
    sites = list_gsc_sites(runner=context.get("runner"))
    matching_sites = matching_gsc_sites(sites, context["url"])
    site = matching_sites[0] if matching_sites else select_gsc_site(sites, context["url"])
    if not site:
        raise RuntimeError(
            "No matching GSC property for {}".format(context["url"])
        )
    matching_sites = matching_sites or [site]
    rows = []
    properties = {}
    for matched_site in matching_sites:
        site_url = matched_site.get("siteUrl")
        property_data = {
            "site": site_url,
            "site_info": {},
            "dimension_sets": {},
        }
        try:
            property_data["site_info"] = get_gsc_site(
                site_url, runner=context.get("runner")
            )
        except Exception as exc:
            property_data["site_info_blocker"] = str(exc)
        for label, dimensions in GSC_DIMENSION_SETS.items():
            try:
                dimension_rows = fetch_gsc_dimension_rows(
                    site_url,
                    start_date,
                    end_date,
                    dimensions,
                    runner=context.get("runner"),
                    row_limit=dimension_row_limit,
                    max_rows=dimension_row_cap or None,
                )
            except Exception as exc:
                property_data["dimension_sets"][label] = {
                    "dimensions": dimensions,
                    "row_count": 0,
                    "rows": [],
                    "blocker": str(exc),
                }
                continue
            property_data["dimension_sets"][label] = {
                "dimensions": dimensions,
                "row_count": len(dimension_rows),
                "rows": dimension_rows,
            }
            if label == "query_page_country":
                rows.extend(
                    {
                        "keyword": row.get("query", ""),
                        "page": row.get("page", ""),
                        "country": row.get("country", ""),
                        "clicks": row.get("clicks", 0.0),
                        "impressions": row.get("impressions", 0.0),
                        "ctr": row.get("ctr", 0.0),
                        "position": row.get("position", 0.0),
                        "source": "gsc",
                        "site": site_url,
                    }
                    for row in dimension_rows
                    if row.get("query")
                )
        properties[site_url] = property_data

    sitemap_rows = []
    sitemap_details = []
    try:
        sitemap_rows = list_gsc_sitemaps(site.get("siteUrl"), runner=context.get("runner"))
        for sitemap in sitemap_rows:
            feedpath = (
                sitemap.get("path")
                or sitemap.get("feedpath")
                or sitemap.get("feedPath")
                if isinstance(sitemap, dict)
                else sitemap
            )
            if feedpath:
                try:
                    sitemap_details.append(
                        get_gsc_sitemap(
                            site.get("siteUrl"), feedpath, runner=context.get("runner")
                        )
                    )
                except Exception as exc:
                    sitemap_details.append({"feedpath": feedpath, "blocker": str(exc)})
    except Exception as exc:
        sitemap_details.append({"blocker": str(exc)})

    url_inspections = {}
    for inspection_url in select_gsc_inspection_urls(
        context.get("inventory_rows", []),
        fallback_url=context.get("url", ""),
        limit=int(context.get("gsc_inspection_limit", 10)),
    ):
        try:
            url_inspections[inspection_url] = inspect_gsc_url(
                site.get("siteUrl"), inspection_url, runner=context.get("runner")
            )
        except Exception as exc:
            url_inspections[inspection_url] = {"blocker": str(exc)}

    artifact = write_evidence_artifact(
        context["target_dir"],
        "gsc.json",
        {
            "site": site.get("siteUrl"),
            "matched_sites": [matched.get("siteUrl") for matched in matching_sites],
            "date_range": {"start_date": start_date, "end_date": end_date},
            "row_count": len(rows),
            "rows": rows,
            "properties": properties,
            "sitemaps": {
                "row_count": len(sitemap_rows),
                "rows": sitemap_rows,
                "details": sitemap_details,
            },
            "url_inspections": {
                "row_count": len(url_inspections),
                "rows": url_inspections,
            },
        },
    )
    return source_result("gsc", "success", artifact, summary="GSC evidence saved.")


def collect_keyword_planner_source(context):
    brand_dir = Path(context["brand_dir"])
    artifacts = []
    for path in (keyword_universe_path(brand_dir), keyword_summary_path(brand_dir)):
        if path.exists():
            artifacts.append(str(path))
    if not artifacts:
        raise RuntimeError("Keyword Planner artifacts are missing. Run generate-keywords.")
    artifact = write_evidence_artifact(
        context["target_dir"],
        "keyword_planner.json",
        {"artifacts": artifacts},
    )
    return source_result(
        "keyword_planner",
        "success",
        artifact,
        summary="Keyword Planner artifacts linked.",
    )


def collect_posthog_source(context):
    existing = Path(context["target_dir"]) / "posthog.json"
    if existing.exists():
        try:
            data = read_json(existing)
            if data.get("status") == "recorded":
                return source_result(
                    "posthog",
                    "recorded",
                    str(existing),
                    summary=data.get("summary", "PostHog artifact recorded."),
                )
        except (OSError, json.JSONDecodeError):
            pass
    artifact = write_evidence_artifact(
        context["target_dir"],
        "posthog.json",
        {
            "status": "blocked",
            "blocker": "PostHog evidence must be recorded from MCP output.",
            "next_action": "Call PostHog MCP and attach the normalized output with record-evidence.",
        },
    )
    return source_result(
        "posthog",
        "blocked",
        artifact,
        blocker="PostHog evidence must be recorded from MCP output.",
        next_action="Call PostHog MCP and attach the normalized output with record-evidence.",
    )


def collect_ga4_source(context):
    existing = Path(context["target_dir"]) / "ga4.json"
    if existing.exists():
        try:
            data = read_json(existing)
            if data.get("status") == "recorded":
                return source_result(
                    "ga4",
                    "recorded",
                    str(existing),
                    summary=data.get("summary", "GA4 evidence recorded."),
                )
        except (OSError, json.JSONDecodeError):
            pass
    artifact = write_evidence_artifact(
        context["target_dir"],
        "ga4.json",
        {
            "status": "blocked",
            "source": "ga4",
            "blocker": "GA4 evidence must be recorded from connector output.",
            "next_action": "Attach normalized GA4 output with record-source-evidence.",
        },
    )
    return source_result(
        "ga4",
        "blocked",
        artifact,
        blocker="GA4 evidence must be recorded from connector output.",
        next_action="Attach normalized GA4 output with record-source-evidence.",
    )


def load_resumable_crawl_rows(brand_dir, run_id):
    if not crawl_manifest_path(brand_dir, run_id).exists():
        return []
    path = url_inventory_path(brand_dir)
    if not path.exists():
        return []
    fields, rows = read_csv_dict_rows(path)
    return rows if set(URL_INVENTORY_FIELDS).issubset(set(fields)) else []


def refresh_crawl_row_from_artifact(row):
    artifact = Path(row.get("artifact_dir", "")) / "firecrawl.json"
    if row.get("status") != "success" or not artifact.exists():
        return row
    try:
        data = read_json(artifact)
        refreshed, _links = page_inventory_from_scrape(
            row.get("url", ""),
            data,
            int(coerce_float(row.get("depth"))),
            row.get("parent_url", ""),
            row.get("source", ""),
            row.get("in_sitemap") == "yes",
            row.get("artifact_dir", ""),
        )
        row.update(refreshed)
    except (OSError, json.JSONDecodeError):
        return row
    return row


def crawl_site(
    brand_dir,
    url,
    run_id=None,
    max_pages=0,
    scrape=None,
    open_url=None,
):
    run_id = run_id or evidence_run_id()
    brand_dir = Path(brand_dir)
    target_dir = crawl_dir(brand_dir, run_id)
    target_dir.mkdir(parents=True, exist_ok=True)
    inventory_path = url_inventory_path(brand_dir)
    base = root_url(url)
    max_pages = int(max_pages or 0)
    rows_by_key = {}
    queue = []
    resumed_rows = load_resumable_crawl_rows(brand_dir, run_id)

    def add_url(raw_url, source, depth=0, parent_url="", in_sitemap=False):
        normalized = normalize_crawl_url(raw_url, base_url=base)
        if not normalized or not same_site_url(base, normalized):
            return
        key = crawl_url_key(normalized)
        existing = rows_by_key.get(key)
        if existing:
            if in_sitemap:
                existing["in_sitemap"] = "yes"
            sources = [part for part in existing.get("source", "").split(";") if part]
            if source not in sources:
                sources.append(source)
                existing["source"] = ";".join(sources)
            return
        if max_pages and len(rows_by_key) >= max_pages:
            return
        row = {field: "" for field in URL_INVENTORY_FIELDS}
        row.update(
            {
                "url": normalized,
                "normalized_url": key,
                "status": "pending",
                "depth": str(depth),
                "parent_url": parent_url,
                "source": source,
                "in_sitemap": "yes" if in_sitemap else "no",
                "last_seen": now_iso(),
            }
        )
        rows_by_key[key] = row
        queue.append(normalized)

    for row in resumed_rows:
        if not row.get("url"):
            continue
        row = refresh_crawl_row_from_artifact(dict(row))
        key = crawl_url_key(row["url"])
        rows_by_key[key] = row
        if row.get("status") == "pending":
            queue.append(row["url"])

    add_url(url, "seed", depth=0)
    sitemap_result = discover_sitemap_pages(base, open_url=open_url)
    for sitemap_url in sitemap_result["pages"]:
        add_url(sitemap_url, "sitemap", depth=0, in_sitemap=True)

    scrape_fn = scrape or firecrawl_scrape
    processed = 0
    while queue:
        current = queue.pop(0)
        key = crawl_url_key(current)
        row = rows_by_key.get(key)
        if not row or row.get("status") in {"success", "blocked"}:
            continue
        page_dir = target_dir / "pages" / url_hash(current)
        page_dir.mkdir(parents=True, exist_ok=True)
        try:
            data = scrape_fn(current, open_url=open_url)
            write_json(data, page_dir / "firecrawl.json")
            next_row, internal_links = page_inventory_from_scrape(
                current,
                data,
                int(coerce_float(row.get("depth"))),
                row.get("parent_url", ""),
                row.get("source", ""),
                row.get("in_sitemap") == "yes",
                page_dir,
            )
            row.update(next_row)
            for link in internal_links:
                add_url(
                    link,
                    "internal_link",
                    depth=int(coerce_float(row.get("depth"))) + 1,
                    parent_url=current,
                )
        except Exception as exc:
            row.update(
                {
                    "status": "blocked",
                    "artifact_dir": str(page_dir),
                    "blocker": str(exc),
                    "last_seen": now_iso(),
                }
            )
        processed += 1

    rows = sorted(rows_by_key.values(), key=lambda item: item.get("url", ""))
    write_csv_dict_rows(inventory_path, URL_INVENTORY_FIELDS, rows)
    manifest = {
        "run_id": run_id,
        "generated_at": now_iso(),
        "target_url": url,
        "brand_dir": str(brand_dir),
        "inventory_path": str(inventory_path),
        "url_count": len(rows),
        "processed_this_run": processed,
        "resumed": bool(resumed_rows),
        "sitemaps": sitemap_result["sitemaps"],
        "blockers": sitemap_result["blockers"],
    }
    write_json(manifest, crawl_manifest_path(brand_dir, run_id))
    return {
        "ok": True,
        "run_id": run_id,
        "inventory_path": str(inventory_path),
        "manifest_path": str(crawl_manifest_path(brand_dir, run_id)),
        "url_count": len(rows),
    }


def default_page_collectors():
    return {
        "firecrawl": collect_firecrawl_source,
        "playwright": collect_playwright_source,
        "lighthouse": collect_lighthouse_source,
        "pagespeed": collect_pagespeed_source,
        "crux": collect_crux_source,
    }


def default_site_collectors(provider_connections=None):
    collectors = {
        "public_http": collect_public_http_source,
        "gsc": collect_gsc_source,
        "keyword_planner": collect_keyword_planner_source,
    }
    analytics_providers = (
        ["posthog"] if provider_connections is None else provider_connections.get("analytics", [])
    )
    for provider in analytics_providers:
        if provider == "posthog":
            collectors["posthog"] = collect_posthog_source
        elif provider == "ga4":
            collectors["ga4"] = collect_ga4_source
    return collectors


def provider_status(provider_connections, site_sources):
    statuses = {}
    page_sources = set(default_page_collectors())
    for logical_source, providers in provider_connections.items():
        statuses[logical_source] = []
        for provider in providers:
            if provider in site_sources:
                status = site_sources[provider].get("status", "")
            elif provider in page_sources:
                status = "page_collected"
            else:
                status = "configured"
            statuses[logical_source].append({"provider": provider, "status": status})
    return statuses


def collect_source_set(collectors, context):
    sources = {}
    for source, collector in collectors.items():
        try:
            sources[source] = collector(context)
        except Exception as exc:
            sources[source] = source_result(
                source,
                "blocked",
                blocker=str(exc),
                next_action="Fix access or record this source manually.",
            )
    return sources


def write_site_page_maps(target_dir, brand_dir, inventory_rows, site_sources):
    inventory_keys = {row.get("normalized_url") for row in inventory_rows}
    maps = {}
    gsc_artifact = site_sources.get("gsc", {}).get("artifact", "")
    if gsc_artifact and Path(gsc_artifact).exists():
        gsc_data = read_json(gsc_artifact)
        grouped = {}
        for row in gsc_data.get("rows", []):
            page = row.get("page", "")
            key = crawl_url_key(page)
            if key in inventory_keys:
                grouped.setdefault(key, []).append(row)
        maps["gsc"] = write_evidence_artifact(
            target_dir,
            "gsc-page-map.json",
            {"page_count": len(grouped), "pages": grouped},
        )
    keyword_path = keyword_universe_path(brand_dir)
    if keyword_path.exists():
        fields, keyword_rows = read_csv_dict_rows(keyword_path)
        grouped = {}
        for row in keyword_rows:
            page = row.get("target_url", "")
            key = crawl_url_key(page)
            if key in inventory_keys:
                grouped.setdefault(key, []).append(row)
        maps["keyword_planner"] = write_evidence_artifact(
            target_dir,
            "keyword-page-map.json",
            {"page_count": len(grouped), "pages": grouped},
        )
    return maps


def collect_site_evidence(
    brand_dir,
    url,
    google_ads_customer_id="",
    run_id=None,
    max_pages=0,
    page_collectors=None,
    site_collectors=None,
    runner=None,
    open_url=None,
    scrape=None,
):
    run_id = run_id or evidence_run_id()
    crawl_result = crawl_site(
        brand_dir,
        url,
        run_id=run_id,
        max_pages=max_pages,
        scrape=scrape,
        open_url=open_url,
    )
    brand_dir = Path(brand_dir)
    target_dir = evidence_dir(brand_dir, run_id)
    target_dir.mkdir(parents=True, exist_ok=True)
    fields, inventory_rows = read_csv_dict_rows(url_inventory_path(brand_dir))
    provider_connections = load_provider_connections(brand_dir)
    site_context = {
        "brand_dir": str(brand_dir),
        "url": url,
        "target_dir": str(target_dir),
        "google_ads_customer_id": google_ads_customer_id,
        "runner": runner,
        "open_url": open_url,
        "inventory_rows": inventory_rows,
        "provider_connections": provider_connections,
    }
    site_sources = collect_source_set(
        site_collectors or default_site_collectors(provider_connections),
        site_context,
    )
    page_maps = write_site_page_maps(target_dir, brand_dir, inventory_rows, site_sources)
    pages = {}
    for row in inventory_rows:
        page_url = row.get("url", "")
        if not page_url:
            continue
        page_dir = target_dir / "pages" / url_hash(page_url)
        page_dir.mkdir(parents=True, exist_ok=True)
        page_context = dict(site_context)
        page_context.update({"url": page_url, "target_dir": str(page_dir)})
        pages[page_url] = {
            "url": page_url,
            "artifact_dir": str(page_dir),
            "sources": collect_source_set(page_collectors or default_page_collectors(), page_context),
        }
    manifest = {
        "run_id": run_id,
        "mode": "site",
        "generated_at": now_iso(),
        "brand_dir": str(brand_dir),
        "target_url": url,
        "crawl_manifest_path": crawl_result["manifest_path"],
        "inventory_path": crawl_result["inventory_path"],
        "provider_connections": provider_connections,
        "provider_status": provider_status(provider_connections, site_sources),
        "sources": site_sources,
        "page_maps": page_maps,
        "pages": pages,
    }
    manifest_path = write_evidence_artifact(target_dir, "manifest.json", manifest)
    return {"ok": True, "run_id": run_id, "manifest_path": manifest_path, "manifest": manifest}


def load_page_artifact(manifest, url, source):
    page = manifest.get("pages", {}).get(url, {})
    source_data = page.get("sources", {}).get(source, {})
    artifact = source_data.get("artifact", "")
    if artifact and Path(artifact).exists():
        try:
            return read_json(artifact), artifact
        except (OSError, json.JSONDecodeError):
            return {}, artifact
    return {}, artifact


def load_site_artifact(manifest, source):
    source_data = manifest.get("sources", {}).get(source, {})
    artifact = source_data.get("artifact", "")
    if artifact and Path(artifact).exists():
        try:
            return read_json(artifact), artifact
        except (OSError, json.JSONDecodeError):
            return {}, artifact
    return {}, artifact


def site_source_artifact(manifest, source):
    source_data = manifest.get("sources", {}).get(source, {})
    artifact = source_data.get("artifact", "")
    if artifact and Path(artifact).exists():
        return artifact
    return ""


def page_source_artifacts(manifest, source):
    artifacts = []
    for page in (manifest.get("pages") or {}).values():
        source_data = (page.get("sources") or {}).get(source, {})
        artifact = source_data.get("artifact", "")
        if artifact and Path(artifact).exists():
            artifacts.append(artifact)
    return artifacts


def add_site_check(checks, check_id, url, passed, severity, source, artifact_ref, result, next_action):
    status = passed if isinstance(passed, str) else ("pass" if passed else "fail")
    checks.append(
        {
            "check_id": check_id,
            "url": url,
            "severity": severity,
            "status": status,
            "source": source,
            "artifact_ref": artifact_ref,
            "result": result,
            "next_action": next_action if status == "fail" else "",
        }
    )


def text_tokens(value):
    return re.findall(r"[a-z0-9]+", str(value or "").lower())


def keyword_stuffed_text(value):
    tokens = [
        token
        for token in text_tokens(value)
        if len(token) > 2 and token not in TEXT_QUALITY_STOPWORDS
    ]
    if len(tokens) < 6:
        return False
    counts = {token: tokens.count(token) for token in set(tokens)}
    max_count = max(counts.values()) if counts else 0
    separator_count = sum(str(value or "").count(char) for char in "|,/\\")
    return max_count >= 4 or (separator_count >= 5 and len(tokens) < 18)


def markdown_headings(rendered_text):
    headings = []
    for line in str(rendered_text or "").splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.append(match.group(1).strip())
    return headings


def harmful_preview_controls(*html_values):
    html = "\n".join(str(value or "").lower() for value in html_values)
    return bool(
        re.search(
            r"(name=[\"']robots[\"'][^>]+content=[\"'][^\"']*(nosnippet|max-snippet\s*:\s*0|max-image-preview\s*:\s*none|max-video-preview\s*:\s*0)"
            r"|data-nosnippet)",
            html,
        )
    )


def dirty_url_path(url):
    parsed = urlparse(str(url or ""))
    path = parsed.path.lower()
    query_keys = {key.lower() for key, _value in parse_qsl(parsed.query, keep_blank_values=True)}
    if query_keys - TRACKING_QUERY_KEYS and not all(key.startswith(TRACKING_QUERY_PREFIXES) for key in query_keys):
        return True
    return bool(
        re.search(
            r"(/20\d{2}/\d{1,2}/|/[0-9a-f]{16,}(?:/|$)|\b(session|sid|token|debug|preview|staging)\b)",
            path,
        )
    )


def content_type_classifiable(row, rendered_text):
    url = row.get("url", "")
    path = urlparse(url).path.lower()
    title = row.get("title", "").lower()
    text = str(rendered_text or "").lower()
    if path in ("", "/"):
        return True
    patterns = (
        "/blog",
        "/docs",
        "/support",
        "/help",
        "/customers",
        "/pricing",
        "/product",
        "/for",
        "/case-stud",
        "/comparison",
        "/alternatives",
    )
    if any(pattern in path for pattern in patterns):
        return True
    return bool(re.search(r"\b(pricing|customer|case study|guide|docs|support|product|template|tool|faq)\b", title + " " + text))


def add_keyword_intent_site_check(checks, manifest, brand_dir):
    keyword_ref = site_source_artifact(manifest, "keyword_planner")
    universe_path = keyword_universe_path(brand_dir)
    fields, rows = read_csv_dict_rows(universe_path) if universe_path.exists() else ([], [])
    intents = {row.get("intent", "").strip().lower() for row in rows if row.get("intent", "").strip()}
    page_types = {row.get("page_type", "").strip().lower() for row in rows if row.get("page_type", "").strip()}
    add_site_check(
        checks,
        "keyword_intent_grouping",
        manifest.get("target_url", ""),
        len(rows) >= 50 and len(intents) >= 2 and len(page_types) >= 2,
        "medium",
        "keyword_planner",
        keyword_ref or str(universe_path),
        "{} keyword rows grouped into {} intents and {} page types.".format(len(rows), len(intents), len(page_types)),
        "Build a larger keyword universe with intent and page-type grouping.",
    )


def add_public_content_quality_checks(checks, row, artifact_ref):
    try:
        data = read_json(artifact_ref)
    except (OSError, json.JSONDecodeError):
        data = {}
    rendered_text = data.get("rendered_text", "") if isinstance(data, dict) else ""
    raw_html = data.get("raw_html", "") if isinstance(data, dict) else ""
    rendered_html = data.get("rendered_html", "") if isinstance(data, dict) else ""
    headings = markdown_headings(rendered_text)
    word_count = int(coerce_float(row.get("word_count"))) or len(text_tokens(rendered_text))
    content_visible = word_count >= 40 and bool(str(rendered_text).strip())
    title = row.get("title", "")
    heading_stuffed = any(keyword_stuffed_text(heading) for heading in headings)
    docs_url = bool(re.search(r"/(docs?|support|help|api|changelog)(/|$)", urlparse(row.get("url", "")).path.lower()))

    add_site_check(
        checks,
        "content_visible",
        row.get("url", ""),
        content_visible,
        "high",
        "firecrawl",
        artifact_ref,
        "Rendered public text has {} words.".format(word_count),
        "Make important content visible in rendered HTML.",
    )
    add_site_check(
        checks,
        "content_type_classifiable",
        row.get("url", ""),
        content_type_classifiable(row, rendered_text),
        "medium",
        "firecrawl",
        artifact_ref,
        "Public URL, title, and rendered text were reviewed for a recognizable page type.",
        "Make the page type and job clear in the URL, title, headings, or visible copy.",
    )
    add_site_check(
        checks,
        "resource_rendering_not_blocked",
        row.get("url", ""),
        row.get("status") == "success" and content_visible,
        "high",
        "firecrawl",
        artifact_ref,
        "Critical page content rendered successfully." if content_visible else "Critical page content was not visible in rendered crawl output.",
        "Unblock CSS, JavaScript, images, or API resources needed for content discovery.",
    )
    add_site_check(
        checks,
        "title_not_keyword_stuffed",
        row.get("url", ""),
        bool(title.strip()) and not keyword_stuffed_text(title),
        "medium",
        "firecrawl",
        artifact_ref,
        "Title reviewed for repeated terms and separator stuffing: {}.".format(title),
        "Rewrite the title without repeated keywords or excessive separators.",
    )
    add_site_check(
        checks,
        "heading_not_keyword_stuffed",
        row.get("url", ""),
        bool(headings) and not heading_stuffed,
        "medium",
        "firecrawl",
        artifact_ref,
        "{} rendered headings reviewed for stuffing.".format(len(headings)),
        "Rewrite headings in natural task language.",
    )
    add_site_check(
        checks,
        "preview_controls_safe",
        row.get("url", ""),
        not harmful_preview_controls(raw_html, rendered_html),
        "medium",
        "firecrawl",
        artifact_ref,
        "No harmful snippet preview controls were detected.",
        "Remove harmful nosnippet or restrictive max-preview directives unless intentionally required.",
    )
    add_site_check(
        checks,
        "url_path_clean",
        row.get("url", ""),
        not dirty_url_path(row.get("url", "")),
        "medium",
        "firecrawl",
        artifact_ref,
        "URL path reviewed for IDs, dates, session keys, and implementation details.",
        "Use clean canonical URLs without implementation details.",
    )
    add_site_check(
        checks,
        "media_support_present",
        row.get("url", ""),
        int(coerce_float(row.get("image_count"))) > 0 or "video" in row.get("schema_types", "").lower(),
        "low",
        "firecrawl",
        artifact_ref,
        "{} images found on the page.".format(row.get("image_count", "0")),
        "Add useful images, video, screenshots, tables, or examples where they help the task.",
    )
    add_site_check(
        checks,
        "content_not_ai_slop",
        row.get("url", ""),
        not re.search(r"\b(want me to|let me know if you want|go deeper|in conclusion)\b", rendered_text, re.I),
        "low",
        "firecrawl",
        artifact_ref,
        "Rendered copy reviewed for common generic AI filler phrases.",
        "Remove generic engagement-menu or filler phrasing.",
    )
    add_site_check(
        checks,
        "thin_prompt_variant_pages",
        row.get("url", ""),
        word_count >= 120,
        "medium",
        "firecrawl",
        artifact_ref,
        "Rendered public text has {} words.".format(word_count),
        "Avoid thin prompt-variant pages; consolidate or expand with useful evidence.",
    )
    add_site_check(
        checks,
        "docs_content_extractable",
        row.get("url", ""),
        "not_applicable" if not docs_url else content_visible and bool(headings),
        "medium",
        "firecrawl",
        artifact_ref,
        "Docs/support URL detected and reviewed." if docs_url else "This is not a docs or support URL.",
        "Make docs/support pages direct, headed, and extractable.",
    )


def add_source_availability_site_checks(checks, rows, manifest, brand_dir):
    site_url = manifest.get("target_url") or (rows[0].get("url", "") if rows else "")
    inventory_ref = str(url_inventory_path(brand_dir))
    add_site_check(
        checks,
        "public_crawl_evidence_available",
        site_url,
        bool(rows),
        "low",
        "firecrawl",
        inventory_ref,
        "{} public URLs are available in the crawl inventory.".format(len(rows)),
        "Run crawl-site or collect-site-evidence for public crawl evidence.",
    )
    playwright_artifacts = page_source_artifacts(manifest, "playwright")
    add_site_check(
        checks,
        "rendered_browser_evidence_available",
        site_url,
        bool(playwright_artifacts),
        "low",
        "playwright",
        playwright_artifacts[0] if playwright_artifacts else "",
        "{} Playwright page artifacts are available.".format(len(playwright_artifacts)),
        "Collect rendered browser evidence with Playwright.",
    )
    performance_artifacts = []
    for source in ("lighthouse", "pagespeed", "crux"):
        performance_artifacts.extend(page_source_artifacts(manifest, source))
    add_site_check(
        checks,
        "performance_evidence_available",
        site_url,
        bool(performance_artifacts),
        "low",
        "lighthouse",
        performance_artifacts[0] if performance_artifacts else "",
        "{} lab or field performance artifacts are available.".format(len(performance_artifacts)),
        "Collect Lighthouse, PageSpeed, or CrUX evidence.",
    )
    keyword_ref = site_source_artifact(manifest, "keyword_planner")
    add_site_check(
        checks,
        "keyword_demand_evidence_available",
        site_url,
        bool(keyword_ref),
        "low",
        "keyword_planner",
        keyword_ref,
        "Keyword Planner evidence is {}.".format("available" if keyword_ref else "missing"),
        "Run generate-keywords or collect keyword planner evidence.",
    )
    add_keyword_intent_site_check(checks, manifest, brand_dir)
    for source in ("posthog", "ga4"):
        source_data = (manifest.get("sources") or {}).get(source, {})
        artifact = source_data.get("artifact", "")
        if not artifact:
            continue
        add_site_check(
            checks,
            "{}_evidence_available".format(source),
            site_url,
            source_data.get("status") in {"success", "recorded"},
            "low",
            source,
            artifact if Path(artifact).exists() else "",
            "{} evidence status is {}.".format(source, source_data.get("status", "missing")),
            "Record analytics evidence from the connected provider.",
        )


def add_playwright_assertion_checks(checks, url, manifest):
    data, artifact_ref = load_page_artifact(manifest, url, "playwright")
    assertions = data.get("assertions", {}) if isinstance(data, dict) else {}
    for check_id, assertion_data in sorted(assertions.items()):
        if not isinstance(assertion_data, dict):
            continue
        status = assertion_data.get("status", "")
        if status not in {"pass", "fail", "not_applicable"}:
            continue
        add_site_check(
            checks,
            check_id,
            url,
            status,
            "medium",
            "playwright",
            artifact_ref,
            assertion_data.get("result", ""),
            assertion_data.get("next_action", "Fix the failing Playwright assertion."),
        )


def lighthouse_audits(*artifacts):
    merged = {}
    for artifact in artifacts:
        if isinstance(artifact, dict):
            merged.update(artifact.get("audits", {}) or {})
    return merged


def audit_items(audit):
    details = audit.get("details", {}) if isinstance(audit, dict) else {}
    items = details.get("items", [])
    return items if isinstance(items, list) else []


def audit_is_failing(audit):
    if not isinstance(audit, dict):
        return False
    score = audit.get("score")
    if score is not None:
        return coerce_float(score) < 1
    return bool(audit_items(audit)) or coerce_float(audit.get("numericValue")) > 0


def audit_issue_summary(audit_id, audit):
    items = audit_items(audit)
    if items:
        sample = []
        for item in items[:3]:
            if isinstance(item, dict):
                sample.append(
                    item.get("url")
                    or item.get("source")
                    or item.get("entity")
                    or item.get("label")
                    or str(item)[:120]
                )
        return "{} has {} flagged items: {}".format(
            audit_id,
            len(items),
            ", ".join(str(value) for value in sample if value),
        )
    return "{} score is {}.".format(audit_id, audit.get("score", "unknown"))


def parse_jsonld_objects(raw_values):
    objects = []
    errors = []

    def collect(value):
        if isinstance(value, list):
            for item in value:
                collect(item)
        elif isinstance(value, dict):
            objects.append(value)
            collect(value.get("@graph", []))

    for raw in raw_values or []:
        try:
            collect(json.loads(raw))
        except (TypeError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
    return objects, errors


def schema_type_names(value):
    values = value if isinstance(value, list) else [value]
    names = []
    for raw in values:
        name = str(raw or "").rsplit("/", 1)[-1].strip()
        if name:
            names.append(name)
    return names


def validate_rich_result_properties(playwright_data):
    raw_jsonld = []
    if isinstance(playwright_data, dict):
        raw_jsonld.extend(playwright_data.get("desktop", {}).get("jsonLd") or [])
        raw_jsonld.extend(playwright_data.get("mobile", {}).get("jsonLd") or [])
    objects, errors = parse_jsonld_objects(raw_jsonld)
    if errors:
        return "fail", "JSON-LD could not be parsed: {}.".format(errors[0]), "Fix malformed JSON-LD before validating rich result properties."
    supported = []
    missing = []
    for obj in objects:
        for type_name in schema_type_names(obj.get("@type")):
            required = GOOGLE_RICH_RESULT_REQUIRED_PROPERTIES.get(type_name)
            if not required:
                continue
            supported.append(type_name)
            absent = [name for name in required if not obj.get(name)]
            if absent:
                missing.append("{} missing {}".format(type_name, ", ".join(absent)))
    if missing:
        return "fail", "{} supported rich result schemas are missing required properties. Example: {}.".format(len(missing), missing[0]), "Add required public schema properties for supported rich result types."
    if supported:
        return "pass", "Supported rich result schema properties are present for: {}.".format(", ".join(sorted(set(supported)))), ""
    return "not_applicable", "No Google-supported rich result schema types were found in rendered JSON-LD.", ""


def script_inventory(playwright_data):
    scripts = []
    if not isinstance(playwright_data, dict):
        return scripts
    for viewport in ("desktop", "mobile"):
        for script in playwright_data.get(viewport, {}).get("scripts") or []:
            if isinstance(script, dict) and script.get("src"):
                item = dict(script)
                item["viewport"] = viewport
                scripts.append(item)
    seen = set()
    unique = []
    for script in scripts:
        key = (script.get("src"), script.get("viewport"))
        if key not in seen:
            seen.add(key)
            unique.append(script)
    return unique


def external_script_domains(url, playwright_data):
    domains = set()
    scripts = []
    for script in script_inventory(playwright_data):
        src = script.get("src", "")
        if src and not same_site_url(url, src):
            parsed = urlparse(src)
            if parsed.netloc:
                domains.add(parsed.netloc.lower())
                scripts.append(script)
    return domains, scripts


def add_rich_result_property_check(checks, url, manifest):
    playwright_data, playwright_ref = load_page_artifact(manifest, url, "playwright")
    if not playwright_data:
        return
    status, result, next_action = validate_rich_result_properties(playwright_data)
    add_site_check(
        checks,
        "rich_result_properties",
        url,
        status,
        "medium",
        "playwright",
        playwright_ref,
        result,
        next_action,
    )


def add_lab_diagnostic_checks(checks, url, manifest, lighthouse_data, lighthouse_ref):
    pagespeed_data, pagespeed_ref = load_page_artifact(manifest, url, "pagespeed")
    playwright_data, playwright_ref = load_page_artifact(manifest, url, "playwright")
    audits = lighthouse_audits(lighthouse_data, pagespeed_data)
    artifact_ref = lighthouse_ref or pagespeed_ref
    source = "lighthouse" if lighthouse_ref else "pagespeed"

    relevant = {
        key: audits.get(key, {})
        for key in ("render-blocking-resources", "unused-css-rules", "font-display", "uses-rel-preload")
        if key in audits
    }
    failing = [audit_issue_summary(key, audit) for key, audit in relevant.items() if audit_is_failing(audit)]
    if relevant:
        add_site_check(
            checks,
            "critical_css_font_loading",
            url,
            "fail" if failing else "pass",
            "medium",
            source,
            artifact_ref,
            failing[0] if failing else "Critical CSS and font loading diagnostics passed.",
            "Fix render-blocking CSS, unused CSS, font-display, or preload diagnostics.",
        )
    elif artifact_ref:
        add_site_check(
            checks,
            "critical_css_font_loading",
            url,
            False,
            "medium",
            source,
            artifact_ref,
            "Stored lab artifact does not include critical CSS or font diagnostics.",
            "Recollect Lighthouse or PageSpeed evidence with CSS and font diagnostics.",
        )

    render_audit = audits.get("render-blocking-resources", {})
    render_items = [
        item for item in audit_items(render_audit)
        if ".js" in str(item.get("url") or item.get("source") or "").lower()
    ]
    scripts = script_inventory(playwright_data)
    blocking_scripts = [
        script for script in scripts
        if script.get("src")
        and not script.get("async")
        and not script.get("defer")
        and str(script.get("type", "")).lower() != "module"
    ]
    if render_audit:
        failed = audit_is_failing(render_audit) and (render_items or not audit_items(render_audit))
        add_site_check(
            checks,
            "render_blocking_scripts",
            url,
            not failed,
            "medium",
            source,
            artifact_ref,
            audit_issue_summary("render-blocking-resources", render_audit) if failed else "No render-blocking script diagnostics failed.",
            "Defer, async, module-load, or remove scripts that block first render.",
        )
    elif scripts:
        add_site_check(
            checks,
            "render_blocking_scripts",
            url,
            not blocking_scripts,
            "medium",
            "playwright",
            playwright_ref,
            "{} external or inline scripts lack async, defer, or module loading.".format(len(blocking_scripts)),
            "Defer, async, module-load, or remove scripts that block first render.",
        )
    elif artifact_ref or playwright_ref:
        add_site_check(
            checks,
            "render_blocking_scripts",
            url,
            False,
            "medium",
            source if artifact_ref else "playwright",
            artifact_ref or playwright_ref,
            "Stored artifacts do not include render-blocking script diagnostics.",
            "Recollect Lighthouse/PageSpeed diagnostics or Playwright script inventory.",
        )

    third_party_audit = audits.get("third-party-summary", {})
    third_party_items = audit_items(third_party_audit)
    heavy_items = []
    for item in third_party_items:
        if not isinstance(item, dict):
            continue
        transfer = coerce_float(item.get("transferSize"))
        blocking = coerce_float(item.get("blockingTime"))
        main_thread = coerce_float(item.get("mainThreadTime"))
        if transfer > 500000 or blocking > 250 or main_thread > 500:
            heavy_items.append(item)
    domains, external_scripts = external_script_domains(url, playwright_data)
    if third_party_audit:
        add_site_check(
            checks,
            "third_party_script_weight",
            url,
            not heavy_items,
            "medium",
            source,
            artifact_ref,
            "{} heavy third-party entities found.".format(len(heavy_items)) if heavy_items else "Third-party script weight is within thresholds.",
            "Reduce, defer, or replace heavy third-party scripts.",
        )
    elif scripts:
        too_many = len(domains) > 5 or len(external_scripts) > 10
        add_site_check(
            checks,
            "third_party_script_weight",
            url,
            not too_many,
            "medium",
            "playwright",
            playwright_ref,
            "{} third-party script domains and {} third-party script tags found.".format(len(domains), len(external_scripts)),
            "Reduce, defer, or replace heavy third-party scripts.",
        )
    elif artifact_ref or playwright_ref:
        add_site_check(
            checks,
            "third_party_script_weight",
            url,
            False,
            "medium",
            source if artifact_ref else "playwright",
            artifact_ref or playwright_ref,
            "Stored artifacts do not include third-party script weight diagnostics.",
            "Recollect Lighthouse/PageSpeed diagnostics or Playwright script inventory.",
        )

    diagnostic_keys = [key for key in LIGHTHOUSE_DIAGNOSTIC_AUDITS if key in audits]
    if lighthouse_data or pagespeed_data:
        add_site_check(
            checks,
            "lab_root_cause_diagnostics",
            url,
            bool(diagnostic_keys),
            "medium",
            source,
            artifact_ref,
            "Lab diagnostics available: {}.".format(", ".join(diagnostic_keys[:8])) if diagnostic_keys else "Lab artifact exists but contains no usable Lighthouse/PageSpeed diagnostics.",
            "Recollect Lighthouse or PageSpeed evidence with diagnostic audits.",
        )


def non_html_inventory_rows(rows):
    non_html = []
    for row in rows:
        url = row.get("url", "")
        content_type = row.get("content_type", "").lower()
        suffix = Path(urlparse(url).path).suffix.lower()
        if content_type and "html" not in content_type:
            non_html.append(row)
        elif suffix and suffix in STATIC_ASSET_EXTENSIONS:
            non_html.append(row)
    return non_html


def non_production_rows(rows):
    pattern = re.compile(r"\b(staging|preview|dev|test|sandbox|vercel|netlify)\b", re.I)
    return [row for row in rows if pattern.search(row.get("url", ""))]


def add_public_technical_site_checks(checks, rows, manifest, brand_dir):
    site_url = manifest.get("target_url") or (rows[0].get("url", "") if rows else "")
    inventory_ref = str(url_inventory_path(brand_dir))
    public_http, public_http_ref = load_site_artifact(manifest, "public_http")
    parameterized = [row for row in rows if urlparse(row.get("url", "")).query]
    error_rows = [
        row for row in rows
        if int(coerce_float(row.get("status_code"))) >= 400
        or row.get("status") == "blocked"
    ]
    if len(rows) < 500 and len(parameterized) < 10:
        add_site_check(
            checks,
            "crawl_waste_review",
            site_url,
            "not_applicable",
            "low",
            "firecrawl",
            inventory_ref,
            "Site inventory has {} URLs and {} parameterized URLs, so large-site crawl waste review is not applicable.".format(len(rows), len(parameterized)),
            "",
        )
    else:
        add_site_check(
            checks,
            "crawl_waste_review",
            site_url,
            not error_rows,
            "medium",
            "firecrawl",
            inventory_ref,
            "{} crawl error or blocked rows found in public inventory.".format(len(error_rows)),
            "Review crawl waste, redirects, low-value parameter URLs, and HTTP errors.",
        )

    redirect_rows = [row for row in rows if 300 <= int(coerce_float(row.get("status_code"))) < 400]
    add_site_check(
        checks,
        "redirect_chain_valid",
        site_url,
        "not_applicable" if not redirect_rows else False,
        "medium",
        "firecrawl",
        inventory_ref,
        "No moved URL or redirect inventory was provided." if not redirect_rows else "{} redirect rows need replacement-target validation.".format(len(redirect_rows)),
        "Add a moved URL inventory or fix redirect chains.",
    )

    non_html = non_html_inventory_rows(rows)
    add_site_check(
        checks,
        "non_html_asset_inventory",
        site_url,
        "not_applicable" if not non_html else True,
        "low",
        "firecrawl",
        inventory_ref,
        "No non-HTML public assets were included in the crawl inventory." if not non_html else "{} non-HTML assets are present in the inventory.".format(len(non_html)),
        "",
    )
    add_site_check(
        checks,
        "non_html_x_robots",
        site_url,
        "not_applicable" if not non_html else False,
        "low",
        "firecrawl",
        inventory_ref,
        "No non-HTML assets require X-Robots-Tag review." if not non_html else "Non-HTML asset headers were not captured for X-Robots-Tag validation.",
        "Collect response headers for non-HTML assets and set X-Robots-Tag where needed.",
    )

    if public_http:
        tls = public_http.get("tls", {})
        valid_tls = bool(tls.get("valid")) and int(coerce_float(tls.get("days_remaining"))) >= 7
        add_site_check(
            checks,
            "tls_certificate_valid",
            site_url,
            valid_tls,
            "high",
            "public_http",
            public_http_ref,
            "TLS certificate has {} days remaining.".format(tls.get("days_remaining", "unknown")),
            "Fix TLS certificate validity, hostname coverage, or expiry monitoring.",
        )
        headers = {str(key).lower(): value for key, value in (public_http.get("headers") or {}).items()}
        add_site_check(
            checks,
            "hsts_header_present",
            site_url,
            bool(headers.get("strict-transport-security")),
            "medium",
            "public_http",
            public_http_ref,
            "Strict-Transport-Security header is {}.".format("present" if headers.get("strict-transport-security") else "missing"),
            "Add HSTS if forced HTTPS is safe for the production domain.",
        )

    non_prod = non_production_rows(rows)
    canonical_issues = [
        row for row in non_prod
        if row.get("canonical") and same_site_url(row.get("url", ""), row.get("canonical", ""))
    ]
    indexable_non_prod = [row for row in non_prod if row.get("indexable") == "yes"]
    add_site_check(
        checks,
        "non_production_canonical",
        site_url,
        "not_applicable" if not non_prod else not canonical_issues,
        "medium",
        "firecrawl",
        inventory_ref,
        "No staging or preview URLs were discovered." if not non_prod else "{} non-production canonical issues found.".format(len(canonical_issues)),
        "Noindex non-production URLs and avoid canonicalizing production pages from preview environments.",
    )
    add_site_check(
        checks,
        "non_production_indexation",
        site_url,
        "not_applicable" if not non_prod else not indexable_non_prod,
        "medium",
        "firecrawl",
        inventory_ref,
        "No non-production URLs were discovered." if not non_prod else "{} non-production URLs are indexable.".format(len(indexable_non_prod)),
        "Block, noindex, or protect non-production URLs.",
    )


def full_gsc_artifact(gsc_data):
    if not isinstance(gsc_data, dict):
        return False
    return bool(gsc_data.get("properties")) and (
        "url_inspections" in gsc_data
        or "sitemaps" in gsc_data
    )


def gsc_dimension_rows(gsc_data, label):
    rows = []
    for property_data in (gsc_data.get("properties") or {}).values():
        dimension_set = (property_data.get("dimension_sets") or {}).get(label, {})
        rows.extend(dimension_set.get("rows") or [])
    return rows


def add_gsc_site_checks(checks, manifest):
    site_url = manifest.get("target_url", "")
    gsc_data, gsc_ref = load_site_artifact(manifest, "gsc")
    if not gsc_data or not full_gsc_artifact(gsc_data):
        return
    inspections = (gsc_data.get("url_inspections") or {}).get("rows") or {}
    if inspections:
        blocked = [
            url for url, row in inspections.items()
            if isinstance(row, dict) and row.get("blocker")
        ]
        not_indexed = []
        for inspection_url, row in inspections.items():
            index_result = (
                row.get("inspectionResult", {}).get("indexStatusResult", {})
                if isinstance(row, dict)
                else {}
            )
            coverage = str(index_result.get("coverageState", ""))
            verdict = str(index_result.get("verdict", ""))
            coverage_lower = coverage.lower().strip()
            negative_coverage = bool(
                re.search(
                    r"\b(not indexed|currently not indexed|blocked|excluded|duplicate|soft 404|alternate page)\b",
                    coverage_lower,
                )
            )
            positive_coverage = coverage_lower.startswith("indexed") or "submitted and indexed" in coverage_lower
            if negative_coverage or ((coverage or verdict) and not positive_coverage and verdict.lower() != "pass"):
                not_indexed.append("{}: {}".format(inspection_url, coverage or verdict))
        failed = blocked or not_indexed
        add_site_check(
            checks,
            "gsc_url_inspection_indexing",
            site_url,
            not failed,
            "high",
            "gsc",
            gsc_ref,
            "{} URL Inspection rows reviewed.".format(len(inspections)) if not failed else "URL Inspection issues found: {}".format((failed[0] if failed else "")),
            "Fix URL Inspection indexing blockers for priority URLs.",
        )

    search_appearance = gsc_dimension_rows(gsc_data, "search_appearance_page")
    add_site_check(
        checks,
        "gsc_search_appearance_review",
        site_url,
        True,
        "low",
        "gsc",
        gsc_ref,
        "GSC search appearance export reviewed with {} rows.".format(len(search_appearance)),
        "",
    )

    query_page_country = gsc_dimension_rows(gsc_data, "query_page_country")
    page_date = gsc_dimension_rows(gsc_data, "page_date")
    add_site_check(
        checks,
        "gsc_serp_expectation",
        site_url,
        bool(query_page_country),
        "medium",
        "gsc",
        gsc_ref,
        "{} query/page/country rows available for SERP expectation review.".format(len(query_page_country)),
        "Collect GSC query/page evidence for SERP expectation mapping.",
    )

    query_page_date = gsc_dimension_rows(gsc_data, "query_page_date")
    add_site_check(
        checks,
        "gsc_measurement_coverage",
        site_url,
        bool(query_page_country and page_date and "url_inspections" in gsc_data),
        "medium",
        "gsc",
        gsc_ref,
        "GSC artifact includes {} query/page/country rows, {} page/date rows, and {} URL Inspection rows.".format(
            len(query_page_country),
            len(page_date),
            (gsc_data.get("url_inspections") or {}).get("row_count", 0),
        ),
        "Collect GSC query, page, date, URL Inspection, and enhancement evidence.",
    )
    add_site_check(
        checks,
        "gsc_landing_page_performance",
        site_url,
        bool(query_page_country or page_date),
        "medium",
        "gsc",
        gsc_ref,
        "{} query/page/country rows and {} page/date rows available for organic landing-page review.".format(
            len(query_page_country),
            len(page_date),
        ),
        "Collect GSC query/page/device rows and analytics engagement or conversion artifacts where needed.",
    )
    add_site_check(
        checks,
        "gsc_query_drift",
        site_url,
        bool(query_page_date),
        "medium",
        "gsc",
        gsc_ref,
        "{} query/page/date rows available for query drift review.".format(len(query_page_date)),
        "Collect historical GSC query/page/date rows.",
    )

    decay_rows = page_date or query_page_date
    add_site_check(
        checks,
        "gsc_decay",
        site_url,
        bool(decay_rows),
        "medium",
        "gsc",
        gsc_ref,
        "{} dated GSC rows available for decay analysis.".format(len(decay_rows)),
        "Collect historical GSC page/date or query/page/date rows.",
    )


def run_site_checks(brand_dir, run_id):
    brand_dir = Path(brand_dir)
    fields, rows = read_csv_dict_rows(url_inventory_path(brand_dir))
    manifest_path = evidence_dir(brand_dir, run_id) / "manifest.json"
    manifest = read_json(manifest_path) if manifest_path.exists() else {"pages": {}}
    checks = []
    title_map = {}
    meta_map = {}
    canonical_map = {}
    status_by_key = {row.get("normalized_url"): row for row in rows}

    add_source_availability_site_checks(checks, rows, manifest, brand_dir)
    add_public_technical_site_checks(checks, rows, manifest, brand_dir)
    add_gsc_site_checks(checks, manifest)

    for row in rows:
        url = row.get("url", "")
        artifact_ref = str(Path(row.get("artifact_dir", "")) / "firecrawl.json")
        status_code = int(coerce_float(row.get("status_code")))
        add_site_check(
            checks,
            "crawl_status",
            url,
            row.get("status") == "success" and status_code < 400,
            "high",
            "firecrawl",
            artifact_ref,
            "URL crawled with status {}.".format(status_code or row.get("status")),
            "Resolve blocked crawl or HTTP error.",
        )
        add_site_check(
            checks,
            "indexable",
            url,
            row.get("indexable") == "yes",
            "high",
            "firecrawl",
            artifact_ref,
            "Indexability is {}.".format(row.get("indexable") or "unknown"),
            "Remove unintended noindex, robots block, or failing status.",
        )
        add_site_check(
            checks,
            "title_present",
            url,
            bool(row.get("title", "").strip()),
            "medium",
            "firecrawl",
            artifact_ref,
            "Title: {}".format(row.get("title", "")),
            "Add a descriptive title tag.",
        )
        add_site_check(
            checks,
            "meta_description_present",
            url,
            bool(row.get("meta_description", "").strip()),
            "medium",
            "firecrawl",
            artifact_ref,
            "Meta description: {}".format(row.get("meta_description", "")),
            "Add a concise meta description.",
        )
        h1_count = int(coerce_float(row.get("h1_count")))
        add_site_check(
            checks,
            "single_h1",
            url,
            h1_count == 1,
            "medium",
            "firecrawl",
            artifact_ref,
            "H1 count is {}.".format(h1_count),
            "Use one clear H1 on the page.",
        )
        canonical = row.get("canonical", "")
        canonical_ok = not canonical or crawl_url_key(canonical) == row.get("normalized_url")
        add_site_check(
            checks,
            "canonical_match",
            url,
            canonical_ok,
            "high",
            "firecrawl",
            artifact_ref,
            "Canonical: {}".format(canonical or "missing"),
            "Set canonical to the intended indexable URL.",
        )
        add_site_check(
            checks,
            "schema_present",
            url,
            bool(row.get("schema_types", "").strip()),
            "low",
            "firecrawl",
            artifact_ref,
            "Schema types: {}".format(row.get("schema_types", "")),
            "Add relevant JSON-LD schema when appropriate.",
        )
        missing_alt = int(coerce_float(row.get("images_missing_alt_count")))
        add_site_check(
            checks,
            "image_alt_text",
            url,
            missing_alt == 0,
            "low",
            "firecrawl",
            artifact_ref,
            "{} images are missing alt text.".format(missing_alt),
            "Add useful alt text for meaningful images.",
        )
        add_site_check(
            checks,
            "sitemap_inclusion",
            url,
            row.get("in_sitemap") == "yes",
            "low",
            "firecrawl",
            artifact_ref,
            "Sitemap inclusion is {}.".format(row.get("in_sitemap") or "unknown"),
            "Add canonical public URLs to the XML sitemap.",
        )
        add_public_content_quality_checks(checks, row, artifact_ref)
        page_lighthouse, lighthouse_ref = load_page_artifact(manifest, url, "lighthouse")
        performance_score = coerce_float(page_lighthouse.get("categories", {}).get("performance"))
        if page_lighthouse:
            add_site_check(
                checks,
                "performance_score",
                url,
                performance_score >= 0.9,
                "medium",
                "lighthouse",
                lighthouse_ref,
                "Performance score is {}.".format(format_metric(performance_score)),
                "Improve Core Web Vitals and Lighthouse performance bottlenecks.",
            )
        add_playwright_assertion_checks(checks, url, manifest)
        add_rich_result_property_check(checks, url, manifest)
        add_lab_diagnostic_checks(checks, url, manifest, page_lighthouse, lighthouse_ref)
        title = row.get("title", "").strip().lower()
        meta = row.get("meta_description", "").strip().lower()
        normalized_canonical = crawl_url_key(row.get("canonical", "")) if row.get("canonical") else ""
        if title:
            title_map.setdefault(title, []).append((url, artifact_ref))
        if meta:
            meta_map.setdefault(meta, []).append((url, artifact_ref))
        if normalized_canonical:
            canonical_map.setdefault(normalized_canonical, []).append((url, artifact_ref))

    for source_map, check_id, label in (
        (title_map, "duplicate_title", "title"),
        (meta_map, "duplicate_meta_description", "meta description"),
        (canonical_map, "duplicate_canonical", "canonical"),
    ):
        for value, entries in source_map.items():
            if len(entries) < 2:
                continue
            urls = ", ".join(entry[0] for entry in entries)
            for url, artifact_ref in entries:
                add_site_check(
                    checks,
                    check_id,
                    url,
                    False,
                    "medium",
                    "firecrawl",
                    artifact_ref,
                    "Duplicate {} shared by: {}".format(label, urls),
                    "Make this {} unique or consolidate duplicate URLs.".format(label),
                )

    for row in rows:
        artifact_path = Path(row.get("artifact_dir", "")) / "firecrawl.json"
        if not artifact_path.exists():
            continue
        try:
            data = read_json(artifact_path)
        except (OSError, json.JSONDecodeError):
            continue
        for link in sorted(set(data.get("links") or [])):
            normalized = normalize_crawl_url(link, base_url=row.get("url", ""))
            if not normalized or not same_site_url(row.get("url", ""), normalized):
                continue
            linked_row = status_by_key.get(crawl_url_key(normalized))
            if linked_row and int(coerce_float(linked_row.get("status_code"))) >= 400:
                add_site_check(
                    checks,
                    "broken_internal_link",
                    row.get("url", ""),
                    False,
                    "high",
                    "firecrawl",
                    str(artifact_path),
                    "Internal link returns {}: {}".format(
                        linked_row.get("status_code"), normalized
                    ),
                    "Update or remove the broken internal link.",
                )

    write_csv_dict_rows(site_checks_path(brand_dir), SITE_CHECK_FIELDS, checks)
    output = {
        "run_id": run_id,
        "generated_at": now_iso(),
        "inventory_path": str(url_inventory_path(brand_dir)),
        "check_count": len(checks),
        "fail_count": len([check for check in checks if check["status"] == "fail"]),
        "checks": checks,
    }
    write_json(output, site_checks_json_path(brand_dir, run_id))
    return {
        "ok": True,
        "site_checks_path": str(site_checks_path(brand_dir)),
        "site_checks_json_path": str(site_checks_json_path(brand_dir, run_id)),
        "check_count": len(checks),
        "fail_count": output["fail_count"],
    }


def google_visible_external_item(item_text):
    return bool(
        re.search(
            r"\b(serp|bing|bwt|ai overview|ai mode|chatgpt|perplexity|"
            r"manual ai|prompt set|off-page|backlink|reputation|citation|"
            r"third-party|review platform|logs?|cdn|waf|server)\b",
            str(item_text or "").lower(),
        )
    )


def google_visible_site_check_ids(item_text):
    text = str(item_text or "").lower()
    technical_third_party_script = "third-party script" in text or "third party script" in text
    gsc_serp_item = "search appearance" in text or "serp expectation" in text or "serp expectations" in text
    gsc_measurement_item = "search console tracks" in text or "organic landing-page performance" in text
    if google_visible_external_item(text) and not technical_third_party_script and not gsc_serp_item:
        return []
    checks = []
    non_html_item = bool(re.search(r"\b(non-html|pdfs?|documents?|feeds?)\b", text))
    if "crawl stats" in text or "crawl budget" in text or "wasted crawl" in text or "low-value parameter" in text:
        checks.append("crawl_waste_review")
    if "moved permanently" in text or "permanent redirect" in text:
        checks.append("redirect_chain_valid")
    if non_html_item and "x-robots-tag" not in text:
        checks.append("non_html_asset_inventory")
    if "x-robots-tag" in text:
        checks.append("non_html_x_robots")
    if "tls certificate" in text:
        checks.append("tls_certificate_valid")
    if "hsts" in text:
        checks.append("hsts_header_present")
    if "staging" in text or "preview" in text:
        checks.append("non_production_canonical")
    if "non-production" in text:
        checks.append("non_production_indexation")
    if "search appearance" in text:
        checks.append("gsc_search_appearance_review")
    if "serp expectations" in text or "serp expectation" in text:
        checks.append("gsc_serp_expectation")
    if "query drift" in text:
        checks.append("gsc_query_drift")
    if "decaying pages" in text or "lost impressions" in text or "lost clicks" in text:
        checks.append("gsc_decay")
    if "url inspection" in text or "indexing status" in text:
        checks.append("gsc_url_inspection_indexing")
    if "search console tracks" in text:
        checks.append("gsc_measurement_coverage")
    if "organic landing-page performance" in text:
        checks.append("gsc_landing_page_performance")
    if "query types are grouped" in text or "search behavior" in text:
        checks.append("keyword_intent_grouping")
    if "content type matches" in text or "page type" in text or "matches the job" in text:
        checks.append("content_type_classifiable")
    if "renders in html" in text or "content renders" in text or "visible without fragile" in text:
        checks.extend(["content_visible", "resource_rendering_not_blocked"])
    if "critical css" in text or "javascript" in text or "api resources" in text:
        checks.append("resource_rendering_not_blocked")
    if "required and recommended properties" in text or "rich result type" in text:
        checks.append("rich_result_properties")
    if "critical css" in text or "font loading" in text:
        checks.append("critical_css_font_loading")
    if "render-blocking script" in text or "render blocking script" in text:
        checks.append("render_blocking_scripts")
    if technical_third_party_script:
        checks.append("third_party_script_weight")
    if "lab tests" in text and "root cause" in text:
        checks.append("lab_root_cause_diagnostics")
    if "fragment" in text or "deep link" in text:
        checks.append("fragment_deep_links")
    if "text is readable without zooming" in text:
        checks.append("mobile_text_readability")
    if "tap target" in text:
        checks.append("tap_targets")
    if "interactive controls" in text and "accessible names" in text:
        checks.append("inaccessible_controls")
    if "horizontal scroll" in text or "horizontal scrolling" in text:
        checks.append("horizontal_scroll")
    if "popup" in text or "interstitial" in text or "app-install overlay" in text or "cookie banner" in text:
        checks.append("blocking_popups_interstitials")
    if "single-page app" in text or "route status" in text or "missing, private, and moved routes" in text:
        checks.append("route_status_handling")
    if "client-side route" in text or "route changes update metadata" in text:
        checks.append("client_route_metadata")
    if "lazy loading" in text or "lazy-loaded" in text:
        checks.append("lazy_loading_in_viewport")
    if "forms have labels" in text or "accessible instructions" in text or "error messages" in text:
        checks.append("form_accessibility")
    if "color contrast" in text:
        checks.append("color_contrast")
    if "keyboard" in text:
        checks.append("keyboard_navigation")
    if "inaccessible controls" in text or "trapped behind inaccessible" in text:
        checks.append("inaccessible_controls")
    if "tables are used" in text or "tabular data" in text:
        checks.append("table_semantics")
    if "common zoom" in text or "zoom levels" in text:
        checks.append("zoom_readability")
    if "text spacing" in text or "letter spacing" in text or "word spacing" in text:
        checks.append("text_spacing")
    if "line length" in text:
        checks.append("body_text_line_length")
    if "forms are short enough" in text or "work on mobile" in text:
        checks.append("mobile_form_usability")
    if "duplicate" in text and "title" in text:
        checks.append("duplicate_title")
    elif "title" in text and "google title" not in text:
        checks.append("title_present")
    if "title" in text and ("stuffed" in text or "stuffing" in text or "repeated keywords" in text):
        checks.append("title_not_keyword_stuffed")
    if "duplicate" in text and ("meta" in text or "description" in text):
        checks.append("duplicate_meta_description")
    elif "meta description" in text or ("description" in text and "snippet" not in text):
        checks.append("meta_description_present")
    if "h1" in text or "heading" in text:
        checks.append("single_h1")
    if "heading" in text and ("keyword" in text or "reader" in text or "human-readable" in text or "questions" in text):
        checks.append("heading_not_keyword_stuffed")
    if "duplicate" in text and "canonical" in text:
        checks.append("duplicate_canonical")
    elif "canonical" in text:
        checks.append("canonical_match")
    if "duplicate template variants" in text:
        checks.extend(["duplicate_canonical", "canonical_match"])
    if "sitemap" in text:
        checks.append("sitemap_inclusion")
    if ("image" in text or re.search(r"\balt\b", text)) and not non_html_item and not gsc_serp_item:
        checks.append("image_alt_text")
    if "snippet" in text or "nosnippet" in text or "max-snippet" in text or "max-image-preview" in text or "max-video-preview" in text:
        checks.append("preview_controls_safe")
    if "url path" in text or "url paths" in text or "session ids" in text or "tracking parameters" in text:
        checks.append("url_path_clean")
    if "template defaults" in text and ("duplicate titles" in text or "boilerplate copy" in text):
        checks.extend(["duplicate_title", "duplicate_meta_description"])
    if "taxonomy names" in text:
        checks.append("keyword_intent_grouping")
    if "media" in text or "screenshots" in text or "videos" in text or "charts" in text or "templates" in text or "calculators" in text or "code examples" in text:
        checks.append("media_support_present")
    if "generic engagement-menu" in text or "let me know if you want" in text or "go deeper" in text:
        checks.append("content_not_ai_slop")
    if "thin prompt-variant" in text:
        checks.append("thin_prompt_variant_pages")
    if "hiding the answer" in text or "gating all useful evidence" in text or "main task or question" in text:
        checks.append("content_visible")
    if "docs/support" in text or "documentation:" in text:
        checks.append("docs_content_extractable")
    if "schema" in text or "structured data" in text:
        checks.append("schema_present")
    if ("performance" in text or "core web vitals" in text or "lighthouse" in text) and not gsc_measurement_item:
        checks.append("performance_score")
    if "status code" in text or "returns 200" in text or "crawlability" in text:
        checks.append("crawl_status")
    if ("indexable" in text or "noindex" in text or "robots meta" in text) and not non_html_item:
        checks.append("indexable")
    return list(dict.fromkeys(checks))


def google_visible_source_check_ids(required_sources):
    sources = set(required_sources or [])
    checks = []
    if sources.intersection({"firecrawl", "public_http"}):
        checks.append("public_crawl_evidence_available")
    if "playwright" in sources:
        checks.append("rendered_browser_evidence_available")
    if sources.intersection({"lighthouse", "pagespeed", "crux"}):
        checks.append("performance_evidence_available")
    if "gsc" in sources:
        checks.append("gsc_measurement_coverage")
    if "keyword_planner" in sources:
        checks.append("keyword_demand_evidence_available")
    if "posthog" in sources:
        checks.append("posthog_evidence_available")
    if "ga4" in sources:
        checks.append("ga4_evidence_available")
    return checks


def google_visible_sources_for_site_checks(check_ids):
    source_by_check = {
        "crawl_waste_review": ["firecrawl"],
        "redirect_chain_valid": ["firecrawl"],
        "non_html_asset_inventory": ["firecrawl"],
        "non_html_x_robots": ["firecrawl"],
        "tls_certificate_valid": ["public_http"],
        "hsts_header_present": ["public_http"],
        "non_production_canonical": ["firecrawl"],
        "non_production_indexation": ["firecrawl"],
        "public_crawl_evidence_available": ["firecrawl"],
        "rendered_browser_evidence_available": ["playwright"],
        "performance_evidence_available": ["lighthouse", "pagespeed", "crux"],
        "keyword_demand_evidence_available": ["keyword_planner"],
        "keyword_intent_grouping": ["keyword_planner"],
        "posthog_evidence_available": ["posthog"],
        "ga4_evidence_available": ["ga4"],
        "crawl_status": ["firecrawl"],
        "indexable": ["firecrawl"],
        "title_present": ["firecrawl"],
        "content_visible": ["firecrawl"],
        "content_type_classifiable": ["firecrawl"],
        "resource_rendering_not_blocked": ["firecrawl"],
        "title_not_keyword_stuffed": ["firecrawl"],
        "heading_not_keyword_stuffed": ["firecrawl"],
        "preview_controls_safe": ["firecrawl"],
        "url_path_clean": ["firecrawl"],
        "media_support_present": ["firecrawl"],
        "content_not_ai_slop": ["firecrawl"],
        "thin_prompt_variant_pages": ["firecrawl"],
        "docs_content_extractable": ["firecrawl"],
        "meta_description_present": ["firecrawl"],
        "single_h1": ["firecrawl"],
        "canonical_match": ["firecrawl"],
        "schema_present": ["firecrawl"],
        "image_alt_text": ["firecrawl"],
        "sitemap_inclusion": ["firecrawl"],
        "duplicate_title": ["firecrawl"],
        "duplicate_meta_description": ["firecrawl"],
        "duplicate_canonical": ["firecrawl"],
        "broken_internal_link": ["firecrawl"],
        "rich_result_properties": ["playwright"],
        "critical_css_font_loading": ["lighthouse", "pagespeed"],
        "render_blocking_scripts": ["lighthouse", "pagespeed", "playwright"],
        "third_party_script_weight": ["lighthouse", "pagespeed", "playwright"],
        "lab_root_cause_diagnostics": ["lighthouse", "pagespeed"],
        "gsc_url_inspection_indexing": ["gsc"],
        "gsc_search_appearance_review": ["gsc"],
        "gsc_serp_expectation": ["gsc"],
        "gsc_query_drift": ["gsc"],
        "gsc_decay": ["gsc"],
        "gsc_measurement_coverage": ["gsc"],
        "gsc_landing_page_performance": ["gsc"],
    }
    playwright_checks = {
        "fragment_deep_links",
        "mobile_text_readability",
        "tap_targets",
        "horizontal_scroll",
        "blocking_popups_interstitials",
        "route_status_handling",
        "client_route_metadata",
        "lazy_loading_in_viewport",
        "form_accessibility",
        "color_contrast",
        "keyboard_navigation",
        "inaccessible_controls",
        "table_semantics",
        "zoom_readability",
        "text_spacing",
        "body_text_line_length",
        "mobile_form_usability",
    }
    sources = []
    for check_id in check_ids or []:
        mapped = source_by_check.get(check_id)
        if not mapped and check_id in playwright_checks:
            mapped = ["playwright"]
        for source in mapped or []:
            if source not in sources:
                sources.append(source)
    return sources


def summarize_site_check_resolution(site_checks, check_ids):
    if not check_ids:
        return None
    selected = [
        check for check in site_checks
        if check.get("check_id") in check_ids
    ]
    duplicate_ids = {"duplicate_title", "duplicate_meta_description", "duplicate_canonical"}
    if not selected and set(check_ids).issubset(duplicate_ids) and site_checks:
        return {
            "status": "pass",
            "source": "firecrawl",
            "result": "No duplicate metadata checks failed in site checks.",
            "next_action": "",
        }
    if not selected:
        return None
    failed = [check for check in selected if check.get("status") == "fail"]
    if failed:
        sample = failed[0]
        return {
            "status": "fail",
            "source": sample.get("source", "firecrawl"),
            "result": "{} of {} public site checks failed for {}. Example: {}".format(
                len(failed),
                len(selected),
                ", ".join(check_ids),
                sample.get("result", ""),
            ),
            "next_action": sample.get("next_action", "Fix the failing public site checks."),
        }
    applicable = [check for check in selected if check.get("status") != "not_applicable"]
    if not applicable:
        sample = selected[0]
        return {
            "status": "not_applicable",
            "source": sample.get("source", "firecrawl"),
            "result": "{} public site checks were not applicable for {}. Example: {}".format(
                len(selected),
                ", ".join(check_ids),
                sample.get("result", ""),
            ),
            "next_action": "",
        }
    return {
        "status": "pass",
        "source": applicable[0].get("source", "firecrawl"),
        "result": "{} public site checks passed for {}.".format(
            len(applicable),
            ", ".join(check_ids),
        ),
        "next_action": "",
    }


def source_satisfies_required(evidence_source, required_sources):
    if not required_sources:
        return True
    evidence_sources = set(row_evidence_sources(evidence_source))
    if set(required_sources).intersection(evidence_sources):
        return True
    rendered_sources = {"firecrawl", "playwright"}
    public_sources = {"firecrawl", "public_http"}
    performance_sources = {"lighthouse", "pagespeed", "crux"}
    if (
        evidence_sources.intersection(public_sources)
        and set(required_sources).intersection(public_sources)
    ):
        return True
    if (
        evidence_sources.intersection(performance_sources)
        and set(required_sources).intersection(performance_sources)
    ):
        return True
    return bool(
        evidence_sources.intersection(rendered_sources)
        and set(required_sources).intersection(rendered_sources)
    )


def google_visible_not_applicable_resolution(item_text):
    return {
        "status": "not_applicable",
        "source": "scope",
        "result": "Not applicable to google-visible scope or no deterministic public signal exists for this checklist wording.",
        "next_action": "",
    }


def resolve_google_visible_audit(brand_dir, run_id, audit_path, output_audit=None):
    brand_dir = Path(brand_dir)
    audit = read_json(audit_path)
    audit.setdefault("metadata", {})["scope"] = GOOGLE_VISIBLE_SCOPE
    provider_connections = load_provider_connections(brand_dir)
    checks_artifact = site_checks_json_path(brand_dir, run_id)
    checks_data = read_json(checks_artifact) if checks_artifact.exists() else {"checks": []}
    site_checks = checks_data.get("checks", [])
    resolved = 0
    for row in audit.get("rows", []):
        item_text = row.get("item_text", "")
        route = route_evidence_for_item(
            item_text,
            row.get("candidate_sources") or [],
            scope=GOOGLE_VISIBLE_SCOPE,
            provider_connections=provider_connections,
        )
        row.update(route)
        site_check_ids = google_visible_site_check_ids(item_text)
        if not site_check_ids:
            site_check_ids = google_visible_source_check_ids(row.get("required_sources", []))
        check_sources = google_visible_sources_for_site_checks(site_check_ids)
        if check_sources:
            row["required_sources"] = check_sources
            row["resolved_required_sources"] = check_sources
        refresh_from_site_checks = (
            row.get("status") in {"pass", "fail", "not_applicable"}
            and site_check_ids
            and (
                row.get("status") == "not_applicable"
                or row.get("artifact_ref") == str(checks_artifact)
            )
        )
        scope_not_applicable = google_visible_scope_not_applicable_item(item_text)
        if scope_not_applicable or (
            google_visible_process_only_item(item_text) and not google_visible_external_item(item_text)
        ):
            if row.get("status") == "not_applicable":
                continue
            row.update(
                {
                    "status": "not_applicable",
                    "evidence_source": "scope",
                    "artifact_ref": "",
                    "result": "Not applicable to google-visible scope; this requires business, backend, or process evidence rather than what Google can see.",
                    "blocker": "",
                    "next_action": "",
                }
            )
            resolved += 1
            continue
        invalidated_source = False
        if row.get("status") in {"pass", "fail"} and row.get("required_sources"):
            if not source_satisfies_required(row.get("evidence_source", ""), row["required_sources"]):
                row.update(
                    {
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Google-visible required evidence is missing: {}".format(
                            ", ".join(row["required_sources"])
                        ),
                        "next_action": "Collect the required public or GSC artifact, then rerun the resolver.",
                    }
                )
                resolved += 1
                invalidated_source = True
            if not refresh_from_site_checks and not invalidated_source:
                continue
        if row.get("status") != "not_checked_blocked" and not refresh_from_site_checks:
            continue
        resolution = summarize_site_check_resolution(
            site_checks,
            site_check_ids,
        )
        if not resolution:
            resolution = {
                "status": "not_checked_blocked",
                "source": "",
                "result": "",
                "blocker": "No deterministic google-visible evidence mapping found for this checklist row.",
                "next_action": "Add a site-check mapping or mark this wording as explicitly out of google-visible scope.",
            }
        if not source_satisfies_required(resolution["source"], row.get("required_sources", [])):
            resolution = {
                "status": "not_checked_blocked",
                "source": "",
                "result": "",
                "blocker": "Resolved evidence source does not satisfy required sources: {}".format(
                    ", ".join(row.get("required_sources", []))
                ),
                "next_action": "Fix evidence routing for this checklist row.",
            }
        row.update(
            {
                "status": resolution["status"],
                "evidence_source": resolution["source"],
                "artifact_ref": str(checks_artifact),
                "result": resolution["result"],
                "blocker": resolution.get("blocker", ""),
                "next_action": resolution["next_action"],
            }
        )
        resolved += 1
    target = output_audit or audit_path
    write_json(audit, target)
    return {
        "ok": True,
        "audit": str(target),
        "resolved_rows": resolved,
        "coverage_counts": coverage_counts(audit.get("rows", [])),
    }


def route_evidence_audit(brand_dir, audit_path, output_audit=None):
    brand_dir = Path(brand_dir)
    audit = read_json(audit_path)
    provider_connections = load_provider_connections(brand_dir)
    routed = 0
    blocked = 0
    for row in audit.get("rows", []):
        before = {
            "logical_required_sources": row.get("logical_required_sources"),
            "resolved_required_sources": row.get("resolved_required_sources"),
            "required_sources": row.get("required_sources"),
        }
        route = route_evidence_for_item(
            row.get("item_text", ""),
            row.get("candidate_sources") or [],
            scope=audit.get("metadata", {}).get("scope", "page"),
            provider_connections=provider_connections,
        )
        row.update(route)
        if before != {
            "logical_required_sources": row.get("logical_required_sources"),
            "resolved_required_sources": row.get("resolved_required_sources"),
            "required_sources": row.get("required_sources"),
        }:
            routed += 1
        if row.get("provider_blockers"):
            blocked += 1
            if row.get("status") == "not_checked_blocked" and not row.get("blocker"):
                row["blocker"] = "; ".join(
                    blocker["blocker"] for blocker in row["provider_blockers"]
                )
                row["next_action"] = "; ".join(
                    blocker["next_action"] for blocker in row["provider_blockers"]
                )
    target = output_audit or audit_path
    write_json(audit, target)
    return {
        "ok": True,
        "audit": str(target),
        "routed_rows": routed,
        "provider_blocked_rows": blocked,
        "coverage_counts": coverage_counts(audit.get("rows", [])),
    }


def record_source_evidence(brand_dir, run_id, source, input_path, summary):
    brand_dir = Path(brand_dir)
    target_dir = evidence_dir(brand_dir, run_id)
    target_dir.mkdir(parents=True, exist_ok=True)
    canonical_source = canonical_evidence_source(source)
    data = read_json(input_path)
    artifact = write_evidence_artifact(
        target_dir,
        "{}.json".format(canonical_source),
        {
            "status": "recorded",
            "source": canonical_source,
            "summary": summary,
            "recorded_at": now_iso(),
            "data": data,
        },
    )
    manifest_path = target_dir / "manifest.json"
    manifest = read_json(manifest_path) if manifest_path.exists() else {
        "run_id": run_id,
        "generated_at": now_iso(),
        "brand_dir": str(brand_dir),
        "sources": {},
    }
    manifest.setdefault("sources", {})[canonical_source] = source_result(
        canonical_source,
        "recorded",
        artifact,
        summary=summary,
    )
    write_json(manifest, manifest_path)
    return {"ok": True, "source": canonical_source, "artifact": artifact, "manifest_path": str(manifest_path)}


def collect_evidence(
    brand_dir,
    url,
    google_ads_customer_id="",
    run_id=None,
    collectors=None,
    runner=None,
    open_url=None,
):
    run_id = run_id or evidence_run_id()
    target_dir = evidence_dir(brand_dir, run_id)
    target_dir.mkdir(parents=True, exist_ok=True)
    context = {
        "brand_dir": str(brand_dir),
        "url": url,
        "target_dir": str(target_dir),
        "google_ads_customer_id": google_ads_customer_id,
        "runner": runner,
        "open_url": open_url,
    }
    collectors = collectors or {
        "firecrawl": collect_firecrawl_source,
        "playwright": collect_playwright_source,
        "lighthouse": collect_lighthouse_source,
        "pagespeed": collect_pagespeed_source,
        "crux": collect_crux_source,
        "gsc": collect_gsc_source,
        "keyword_planner": collect_keyword_planner_source,
        "posthog": collect_posthog_source,
    }
    sources = {}
    for source, collector in collectors.items():
        try:
            sources[source] = collector(context)
        except Exception as exc:
            sources[source] = source_result(
                source,
                "blocked",
                blocker=str(exc),
                next_action="Fix access or record this source manually.",
            )
    manifest = {
        "run_id": run_id,
        "generated_at": now_iso(),
        "brand_dir": str(brand_dir),
        "target_url": url,
        "sources": sources,
    }
    manifest_path = write_evidence_artifact(target_dir, "manifest.json", manifest)
    return {"ok": True, "manifest_path": manifest_path, "manifest": manifest}


def record_audit_evidence(
    audit_path,
    item_id,
    status,
    evidence_source,
    artifact_ref,
    result,
    next_action="",
    blocker="",
    evidence_run_id="",
    output=None,
):
    audit = read_json(audit_path)
    rows = audit.get("rows", [])
    matching = [row for row in rows if row.get("item_id") == item_id]
    if not matching:
        raise RuntimeError("item_id not found in audit: {}".format(item_id))
    row = matching[0]
    row.update(
        {
            "status": status,
            "evidence_source": canonical_evidence_source(evidence_source),
            "artifact_ref": artifact_ref,
            "result": result,
            "blocker": blocker,
            "next_action": next_action,
        }
    )
    if evidence_run_id:
        row["evidence_run_id"] = evidence_run_id
    artifacts = row.get("evidence_artifacts")
    if isinstance(artifacts, list):
        if artifact_ref and artifact_ref not in artifacts:
            artifacts.append(artifact_ref)
    else:
        row["evidence_artifacts"] = [artifact_ref] if artifact_ref else []
    target = output or audit_path
    write_json(audit, target)
    return {"ok": True, "audit_path": str(target), "item_id": item_id}


def command_compile(args):
    paths = args.checklist or default_checklist_paths()
    write_json(compile_checklists(paths), args.output)
    return 0


def command_init_audit(args):
    compiled = read_json(args.compiled)
    write_json(
        init_audit(
            compiled,
            args.url,
            args.audit_type,
            strict_evidence=args.strict_evidence,
            scope=args.scope,
            evidence_run_id_value=args.evidence_run_id,
            brand_dir=args.brand_dir,
        ),
        args.output,
    )
    return 0


def command_verify_audit(args):
    compiled = read_json(args.compiled)
    audit = read_json(args.audit)
    errors = validate_audit(
        compiled,
        audit,
        strict_evidence=args.strict_evidence,
        base_dir=Path(args.audit).parent,
    )
    counts = coverage_counts(audit.get("rows", []))
    result = {"ok": not errors, "coverage_counts": counts, "errors": errors}
    write_json(result, args.output)
    return 0 if not errors else 1


def command_summarize_audit(args):
    audit = read_json(args.audit)
    rows = audit.get("rows", [])
    result = {
        "target_url": audit.get("metadata", {}).get("target_url", ""),
        "audit_type": audit.get("metadata", {}).get("audit_type", "partial"),
        "item_count": len(rows),
        "coverage_counts": coverage_counts(rows),
    }
    write_json(result, args.output)
    return 0


def command_init_authenticity(args):
    write_json(init_authenticity(args.target), args.output)
    return 0


def command_verify_authenticity(args):
    log = read_json(args.authenticity)
    rewrite_text = ""
    if args.rewrite_file:
        rewrite_text = Path(args.rewrite_file).read_text(encoding="utf-8")
    errors = validate_authenticity(
        log,
        rewrite_text,
        max_ai_detector_score=args.max_ai_detector_score,
    )
    result = {"ok": not errors, "errors": errors}
    if rewrite_text:
        result["ai_text_risk"] = ai_text_risk_report(rewrite_text)
    write_json(result, args.output)
    return 0 if not errors else 1


def command_write_content(args):
    try:
        result = write_content_with_authenticity(
            args.draft_file,
            args.content_output,
            args.authenticity,
            max_ai_detector_score=args.max_ai_detector_score,
        )
    except (OSError, json.JSONDecodeError) as exc:
        result = {"ok": False, "errors": [str(exc)], "written": False}
    write_json(result, args.output)
    return 0 if result["ok"] else 1


def command_zerogpt_check(args):
    # Delegates to the standalone tools/zerogpt.py (lazy import avoids a cycle).
    from zerogpt import run as run_zerogpt_check

    return run_zerogpt_check(args)


def command_firecrawl_scrape(args):
    result = firecrawl_scrape(
        args.url,
        formats=args.format,
        only_main_content=not args.full_content,
        wait_for=args.wait_for,
        mobile=args.mobile,
        timeout=args.timeout,
    )
    write_json(result, args.output)
    return 0


def command_generate_keywords(args):
    try:
        result = generate_keyword_research(
            args.brand_dir,
            args.google_ads_customer_id,
            country=args.country,
            language=args.language,
            max_prioritized=args.max_prioritized,
            raw_limit=args.raw_limit,
        )
    except (RuntimeError, csv.Error) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def command_verify_keywords(args):
    result = validate_keyword_outputs(
        args.brand_dir,
        min_prioritized=args.min_prioritized,
        max_prioritized=args.max_prioritized,
        min_universe=args.min_universe,
        allow_large=args.allow_large,
    )
    output = {
        "ok": not result["errors"],
        "counts": result["counts"],
        "errors": result["errors"],
    }
    write_json(output, args.output)
    return 0 if output["ok"] else 1


def command_collect_evidence(args):
    result = collect_evidence(
        args.brand_dir,
        args.url,
        google_ads_customer_id=args.google_ads_customer_id,
        run_id=args.run_id,
    )
    write_json(result, args.output)
    return 0


def command_crawl_site(args):
    result = crawl_site(
        args.brand_dir,
        args.url,
        run_id=args.run_id,
        max_pages=args.max_pages,
    )
    write_json(result, args.output)
    return 0


def command_collect_site_evidence(args):
    result = collect_site_evidence(
        args.brand_dir,
        args.url,
        google_ads_customer_id=args.google_ads_customer_id,
        run_id=args.run_id,
        max_pages=args.max_pages,
    )
    write_json(result, args.output)
    return 0


def command_run_site_checks(args):
    result = run_site_checks(args.brand_dir, args.run_id)
    write_json(result, args.output)
    return 0


def command_resolve_google_visible_audit(args):
    result = resolve_google_visible_audit(
        args.brand_dir,
        args.run_id,
        args.audit,
        output_audit=args.output_audit,
    )
    write_json(result, args.output)
    return 0


def command_resolve_google_visible_audits(args):
    brand_dir = Path(args.brand_dir)
    audit_paths = [Path(path) for path in args.audit] if args.audit else sorted(
        (brand_dir / "audits").glob("*-google-visible-audit.json")
    )
    results = [
        resolve_google_visible_audit(brand_dir, args.run_id, audit_path)
        for audit_path in audit_paths
    ]
    write_json(
        {
            "ok": all(result.get("ok") for result in results),
            "audit_count": len(results),
            "results": results,
        },
        args.output,
    )
    return 0


def command_route_evidence(args):
    result = route_evidence_audit(
        args.brand_dir,
        args.audit,
        output_audit=args.output_audit,
    )
    write_json(result, args.output)
    return 0


def command_record_source_evidence(args):
    try:
        result = record_source_evidence(
            args.brand_dir,
            args.run_id,
            args.source,
            args.input,
            args.summary,
        )
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def command_record_evidence(args):
    try:
        result = record_audit_evidence(
            args.audit,
            args.item_id,
            args.status,
            args.evidence_source,
            args.artifact_ref,
            args.result,
            next_action=args.next_action,
            blocker=args.blocker,
            evidence_run_id=args.evidence_run_id,
            output=args.output_audit,
        )
    except RuntimeError as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def command_generate_context_map(args):
    try:
        result = build_checklist_context_map(
            checklist_paths=args.checklist or default_checklist_paths(),
            registry_dir=args.registry_dir,
        )
        if args.output:
            write_json(result, args.output)
        else:
            write_json(result, checklist_context_map_path(args.registry_dir))
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    return 0


def command_validate_context_system(args):
    result = validate_context_system(
        registry_dir=args.registry_dir,
        checklist_paths=args.checklist or default_checklist_paths(),
    )
    write_json(result, args.output)
    return 0 if result["ok"] else 1


def command_init_brand_context(args):
    try:
        result = init_brand_context(args.brand_dir)
    except (OSError, json.JSONDecodeError) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def command_resolve_context(args):
    try:
        result = resolve_context_for_work(
            args.brand_dir,
            checklist_ids=args.checklist_id,
            run_id=args.run_id or "",
            work_type=args.work_type or "",
            target_urls=args.target_url or [],
            registry_dir=args.registry_dir,
            write_run=args.write_run,
        )
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def command_record_context_answer(args):
    try:
        result = record_context_answer(
            args.brand_dir,
            args.field_id,
            args.value,
            question_id=args.question_id,
            run_id=args.run_id,
            scope=args.scope,
            confidence=args.confidence,
        )
    except (RuntimeError, OSError, json.JSONDecodeError) as exc:
        write_json({"ok": False, "errors": [str(exc)]}, args.output)
        return 1
    write_json(result, args.output)
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    compile_parser = subparsers.add_parser("compile-checklists")
    compile_parser.add_argument("--checklist", action="append", help="Checklist Markdown path")
    compile_parser.add_argument("--output", help="Output JSON path")
    compile_parser.set_defaults(func=command_compile)

    init_audit_parser = subparsers.add_parser("init-audit")
    init_audit_parser.add_argument("--compiled", required=True, help="Compiled checklist JSON")
    init_audit_parser.add_argument("--url", required=True, help="Audited URL")
    init_audit_parser.add_argument(
        "--audit-type", choices=("partial", "full"), default="partial"
    )
    init_audit_parser.add_argument(
        "--scope",
        choices=("page", "site", GOOGLE_VISIBLE_SCOPE),
        default="page",
    )
    init_audit_parser.add_argument("--evidence-run-id", default="")
    init_audit_parser.add_argument("--brand-dir", default="")
    init_audit_parser.add_argument("--strict-evidence", action="store_true")
    init_audit_parser.add_argument("--output", help="Output audit matrix JSON path")
    init_audit_parser.set_defaults(func=command_init_audit)

    verify_audit_parser = subparsers.add_parser("verify-audit")
    verify_audit_parser.add_argument("--compiled", required=True)
    verify_audit_parser.add_argument("--audit", required=True)
    verify_audit_parser.add_argument("--strict-evidence", action="store_true")
    verify_audit_parser.add_argument("--output", help="Output verification JSON path")
    verify_audit_parser.set_defaults(func=command_verify_audit)

    summarize_parser = subparsers.add_parser("summarize-audit")
    summarize_parser.add_argument("--audit", required=True)
    summarize_parser.add_argument("--output", help="Output summary JSON path")
    summarize_parser.set_defaults(func=command_summarize_audit)

    init_auth_parser = subparsers.add_parser("init-authenticity")
    init_auth_parser.add_argument("--target", required=True)
    init_auth_parser.add_argument("--output", help="Output authenticity JSON path")
    init_auth_parser.set_defaults(func=command_init_authenticity)

    verify_auth_parser = subparsers.add_parser("verify-authenticity")
    verify_auth_parser.add_argument("--authenticity", required=True)
    verify_auth_parser.add_argument("--rewrite-file")
    verify_auth_parser.add_argument(
        "--max-ai-detector-score",
        type=float,
        default=20.0,
        help="Maximum recorded detector or local AI-pattern risk score allowed before verification fails.",
    )
    verify_auth_parser.add_argument("--output", help="Output verification JSON path")
    verify_auth_parser.set_defaults(func=command_verify_authenticity)

    write_content_parser = subparsers.add_parser("write-content")
    write_content_parser.add_argument("--draft-file", required=True)
    write_content_parser.add_argument("--content-output", required=True)
    write_content_parser.add_argument("--authenticity", required=True)
    write_content_parser.add_argument(
        "--max-ai-detector-score",
        type=float,
        default=20.0,
        help="Maximum recorded detector or local AI-pattern risk score allowed before writing content.",
    )
    write_content_parser.add_argument("--output", help="Output write report JSON path")
    write_content_parser.set_defaults(func=command_write_content)

    zerogpt_parser = subparsers.add_parser(
        "zerogpt-check",
        help="Check text with the ZeroGPT AI detector and record it as a detector note (weak signal).",
    )
    zerogpt_source = zerogpt_parser.add_mutually_exclusive_group(required=True)
    zerogpt_source.add_argument("--content-file", help="File whose text to check")
    zerogpt_source.add_argument("--text", help="Inline text to check")
    zerogpt_parser.add_argument(
        "--authenticity",
        help="Authenticity log JSON to append the ZeroGPT detector note to (in place).",
    )
    zerogpt_parser.add_argument(
        "--max-ai-detector-score",
        type=float,
        default=20.0,
        help="AI percentage at or above which the check fails (default 20).",
    )
    zerogpt_parser.add_argument("--output", help="Output result JSON path")
    zerogpt_parser.set_defaults(func=command_zerogpt_check)

    firecrawl_parser = subparsers.add_parser("firecrawl-scrape")
    firecrawl_parser.add_argument("--url", required=True)
    firecrawl_parser.add_argument(
        "--format",
        action="append",
        help="Firecrawl output format. Repeat for multiple formats.",
    )
    firecrawl_parser.add_argument("--full-content", action="store_true")
    firecrawl_parser.add_argument("--wait-for", type=int, default=0)
    firecrawl_parser.add_argument("--mobile", action="store_true")
    firecrawl_parser.add_argument("--timeout", type=int, default=60000)
    firecrawl_parser.add_argument("--output", help="Output scrape JSON path")
    firecrawl_parser.set_defaults(func=command_firecrawl_scrape)

    generate_keywords_parser = subparsers.add_parser("generate-keywords")
    generate_keywords_parser.add_argument("--brand-dir", required=True)
    generate_keywords_parser.add_argument("--google-ads-customer-id", required=True)
    generate_keywords_parser.add_argument(
        "--country",
        default="",
        help="Target country override. If omitted, GSC and Brand DNA are used.",
    )
    generate_keywords_parser.add_argument(
        "--language",
        default=DEFAULT_LANGUAGE_CONSTANT,
        help="Google Ads language constant.",
    )
    generate_keywords_parser.add_argument("--max-prioritized", type=int, default=150)
    generate_keywords_parser.add_argument("--raw-limit", type=int, default=500)
    generate_keywords_parser.add_argument("--output", help="Output generation JSON path")
    generate_keywords_parser.set_defaults(func=command_generate_keywords)

    verify_keywords_parser = subparsers.add_parser("verify-keywords")
    verify_keywords_parser.add_argument("--brand-dir", required=True)
    verify_keywords_parser.add_argument("--min-prioritized", type=int, default=50)
    verify_keywords_parser.add_argument("--max-prioritized", type=int, default=150)
    verify_keywords_parser.add_argument("--min-universe", type=int, default=200)
    verify_keywords_parser.add_argument("--allow-large", action="store_true")
    verify_keywords_parser.add_argument("--output", help="Output verification JSON path")
    verify_keywords_parser.set_defaults(func=command_verify_keywords)

    collect_evidence_parser = subparsers.add_parser("collect-evidence")
    collect_evidence_parser.add_argument("--brand-dir", required=True)
    collect_evidence_parser.add_argument("--url", required=True)
    collect_evidence_parser.add_argument("--google-ads-customer-id", default="")
    collect_evidence_parser.add_argument("--run-id")
    collect_evidence_parser.add_argument("--output", help="Output collection JSON path")
    collect_evidence_parser.set_defaults(func=command_collect_evidence)

    crawl_site_parser = subparsers.add_parser("crawl-site")
    crawl_site_parser.add_argument("--brand-dir", required=True)
    crawl_site_parser.add_argument("--url", required=True)
    crawl_site_parser.add_argument("--run-id")
    crawl_site_parser.add_argument("--max-pages", type=int, default=0)
    crawl_site_parser.add_argument("--output", help="Output crawl JSON path")
    crawl_site_parser.set_defaults(func=command_crawl_site)

    collect_site_parser = subparsers.add_parser("collect-site-evidence")
    collect_site_parser.add_argument("--brand-dir", required=True)
    collect_site_parser.add_argument("--url", required=True)
    collect_site_parser.add_argument("--google-ads-customer-id", default="")
    collect_site_parser.add_argument("--run-id")
    collect_site_parser.add_argument("--max-pages", type=int, default=0)
    collect_site_parser.add_argument("--output", help="Output collection JSON path")
    collect_site_parser.set_defaults(func=command_collect_site_evidence)

    site_checks_parser = subparsers.add_parser("run-site-checks")
    site_checks_parser.add_argument("--brand-dir", required=True)
    site_checks_parser.add_argument("--run-id", required=True)
    site_checks_parser.add_argument("--output", help="Output site checks JSON path")
    site_checks_parser.set_defaults(func=command_run_site_checks)

    resolve_google_visible_parser = subparsers.add_parser("resolve-google-visible-audit")
    resolve_google_visible_parser.add_argument("--brand-dir", required=True)
    resolve_google_visible_parser.add_argument("--run-id", required=True)
    resolve_google_visible_parser.add_argument("--audit", required=True)
    resolve_google_visible_parser.add_argument("--output-audit")
    resolve_google_visible_parser.add_argument("--output", help="Output resolver JSON path")
    resolve_google_visible_parser.set_defaults(func=command_resolve_google_visible_audit)

    resolve_google_visible_batch_parser = subparsers.add_parser("resolve-google-visible-audits")
    resolve_google_visible_batch_parser.add_argument("--brand-dir", required=True)
    resolve_google_visible_batch_parser.add_argument("--run-id", required=True)
    resolve_google_visible_batch_parser.add_argument("--audit", action="append")
    resolve_google_visible_batch_parser.add_argument("--output", help="Output resolver JSON path")
    resolve_google_visible_batch_parser.set_defaults(func=command_resolve_google_visible_audits)

    route_evidence_parser = subparsers.add_parser("route-evidence")
    route_evidence_parser.add_argument("--brand-dir", required=True)
    route_evidence_parser.add_argument("--audit", required=True)
    route_evidence_parser.add_argument("--output-audit")
    route_evidence_parser.add_argument("--output", help="Output routing JSON path")
    route_evidence_parser.set_defaults(func=command_route_evidence)

    record_source_parser = subparsers.add_parser("record-source-evidence")
    record_source_parser.add_argument("--brand-dir", required=True)
    record_source_parser.add_argument("--run-id", required=True)
    record_source_parser.add_argument("--source", required=True)
    record_source_parser.add_argument("--input", required=True)
    record_source_parser.add_argument("--summary", required=True)
    record_source_parser.add_argument("--output", help="Output recording JSON path")
    record_source_parser.set_defaults(func=command_record_source_evidence)

    record_evidence_parser = subparsers.add_parser("record-evidence")
    record_evidence_parser.add_argument("--audit", required=True)
    record_evidence_parser.add_argument("--item-id", required=True)
    record_evidence_parser.add_argument(
        "--status", choices=sorted(STATUSES), required=True
    )
    record_evidence_parser.add_argument("--evidence-source", required=True)
    record_evidence_parser.add_argument("--artifact-ref", required=True)
    record_evidence_parser.add_argument("--result", required=True)
    record_evidence_parser.add_argument("--next-action", default="")
    record_evidence_parser.add_argument("--blocker", default="")
    record_evidence_parser.add_argument("--evidence-run-id", default="")
    record_evidence_parser.add_argument("--output-audit")
    record_evidence_parser.add_argument("--output", help="Output recording JSON path")
    record_evidence_parser.set_defaults(func=command_record_evidence)

    context_map_parser = subparsers.add_parser("generate-context-map")
    context_map_parser.add_argument("--registry-dir", default=str(default_registry_dir()))
    context_map_parser.add_argument("--checklist", action="append")
    context_map_parser.add_argument("--output", help="Output context map JSON path")
    context_map_parser.set_defaults(func=command_generate_context_map)

    validate_context_parser = subparsers.add_parser("validate-context-system")
    validate_context_parser.add_argument("--registry-dir", default=str(default_registry_dir()))
    validate_context_parser.add_argument("--checklist", action="append")
    validate_context_parser.add_argument("--output", help="Output validation JSON path")
    validate_context_parser.set_defaults(func=command_validate_context_system)

    init_brand_context_parser = subparsers.add_parser("init-brand-context")
    init_brand_context_parser.add_argument("--brand-dir", required=True)
    init_brand_context_parser.add_argument("--output", help="Output init report JSON path")
    init_brand_context_parser.set_defaults(func=command_init_brand_context)

    resolve_context_parser = subparsers.add_parser("resolve-context")
    resolve_context_parser.add_argument("--brand-dir", required=True)
    resolve_context_parser.add_argument("--registry-dir", default=str(default_registry_dir()))
    resolve_context_parser.add_argument("--checklist-id", action="append")
    resolve_context_parser.add_argument("--run-id", default="")
    resolve_context_parser.add_argument("--work-type", default="")
    resolve_context_parser.add_argument("--target-url", action="append")
    resolve_context_parser.add_argument("--write-run", action="store_true")
    resolve_context_parser.add_argument("--output", help="Output resolution JSON path")
    resolve_context_parser.set_defaults(func=command_resolve_context)

    record_context_parser = subparsers.add_parser("record-context-answer")
    record_context_parser.add_argument("--brand-dir", required=True)
    record_context_parser.add_argument("--field-id", required=True)
    record_context_parser.add_argument("--value", required=True)
    record_context_parser.add_argument("--question-id", default="")
    record_context_parser.add_argument("--run-id", default="")
    record_context_parser.add_argument("--scope", choices=("brand", "run"), default="brand")
    record_context_parser.add_argument("--confidence", default="high")
    record_context_parser.add_argument("--output", help="Output recording JSON path")
    record_context_parser.set_defaults(func=command_record_context_answer)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
