#!/usr/bin/env python3
"""A read-only stdio MCP server for Google Ads Keyword Planner.

Only `google_ads_generate_keyword_ideas` is exposed.  It deliberately has no
campaign, account-management, GAQL, or write operations.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


TOOL_NAME = "google_ads_generate_keyword_ideas"
REQUIRED_ENV = (
    "GOOGLE_ADS_PLATFORM_ID",
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_CUSTOMER_ID",
)


def load_local_env() -> None:
    """Load simple KEY=VALUE entries from the repository .env without logging them."""
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    try:
        with open(env_path, encoding="utf-8") as env_file:
            for raw_line in env_file:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key, value = key.strip(), value.strip()
                if key and key not in os.environ:
                    os.environ[key] = value.strip('"').strip("'")
    except FileNotFoundError:
        pass


def fail(message: str) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": message}], "isError": True}


def post_json(url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Google Ads API returned HTTP {error.code}: {body}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Could not reach Google Ads API: {error.reason}") from error


def access_token() -> str:
    """Return a temporary supplied token or refresh one from OAuth credentials."""
    direct_token = os.environ.get("GOOGLE_ADS_ACCESS_TOKEN")
    if direct_token:
        return direct_token
    if not os.environ.get("GOOGLE_ADS_REFRESH_TOKEN"):
        raise RuntimeError("Set GOOGLE_ADS_REFRESH_TOKEN or a temporary GOOGLE_ADS_ACCESS_TOKEN.")
    data = urllib.parse.urlencode(
        {
            "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            "grant_type": "refresh_token",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"OAuth token refresh failed (HTTP {error.code}).") from error
    token = result.get("access_token")
    if not token:
        raise RuntimeError("OAuth token refresh returned no access token.")
    return token


def generate_ideas(args: dict[str, Any]) -> dict[str, Any]:
    missing = [name for name in REQUIRED_ENV if not os.environ.get(name)]
    if missing:
        return fail("Missing required environment variables: " + ", ".join(missing))

    platform_id = str(args.get("platform_id", "")).replace("-", "")
    configured_platform = os.environ["GOOGLE_ADS_PLATFORM_ID"].replace("-", "")
    if platform_id != configured_platform:
        return fail("platform_id must match the configured GOOGLE_ADS_PLATFORM_ID.")

    keywords = args.get("seed_keywords") or []
    url = args.get("seed_url")
    if not keywords and not url:
        return fail("Provide at least one seed_keyword or a seed_url.")
    if not isinstance(keywords, list) or not all(isinstance(item, str) and item.strip() for item in keywords):
        return fail("seed_keywords must be a list of non-empty strings.")
    if len(keywords) > 20:
        return fail("At most 20 seed_keywords are allowed per request.")

    language_id = str(args.get("language_id", "1000"))
    geo_ids = args.get("geo_target_ids", [2356])  # India
    if not isinstance(geo_ids, list) or not geo_ids:
        return fail("geo_target_ids must be a non-empty list of Google geo target IDs.")
    page_size = args.get("page_size", 100)
    if not isinstance(page_size, int) or not 1 <= page_size <= 10000:
        return fail("page_size must be an integer between 1 and 10000.")

    date_range = args.get("year_month_range")
    if date_range is not None:
        if not isinstance(date_range, dict):
            return fail("year_month_range must contain start and end year/month objects.")
        start, end = date_range.get("start"), date_range.get("end")
        if not all(isinstance(value, dict) for value in (start, end)):
            return fail("year_month_range must contain start and end year/month objects.")
        for boundary in (start, end):
            if not isinstance(boundary.get("year"), int) or not isinstance(boundary.get("month"), str):
                return fail("Each year_month_range boundary requires an integer year and month name.")

    payload: dict[str, Any] = {
        "language": f"languageConstants/{language_id}",
        "geoTargetConstants": [f"geoTargetConstants/{str(item)}" for item in geo_ids],
        "keywordPlanNetwork": args.get("network", "GOOGLE_SEARCH"),
        "includeAdultKeywords": bool(args.get("include_adult_keywords", False)),
        "pageSize": page_size,
    }
    if date_range is not None:
        payload["historicalMetricsOptions"] = {"yearMonthRange": date_range}
    if keywords and url:
        payload["keywordAndUrlSeed"] = {"keywords": keywords, "url": url}
    elif keywords:
        payload["keywordSeed"] = {"keywords": keywords}
    else:
        payload["urlSeed"] = {"url": url}

    api_version = os.environ.get("GOOGLE_ADS_API_VERSION", "v25")
    customer_id = os.environ["GOOGLE_ADS_CUSTOMER_ID"].replace("-", "")
    headers = {
        "Authorization": f"Bearer {access_token()}",
        "developer-token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
    }
    login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").replace("-", "")
    if login_customer_id:
        headers["login-customer-id"] = login_customer_id
    try:
        result = post_json(
            f"https://googleads.googleapis.com/{api_version}/customers/{customer_id}:generateKeywordIdeas",
            payload,
            headers,
        )
    except RuntimeError as error:
        return fail(str(error))

    output = {
        "source": "Google Ads KeywordPlanIdeaService.GenerateKeywordIdeas",
        "retrieved_at_unix": int(time.time()),
        "targeting": {
            "language_id": language_id,
            "geo_target_ids": geo_ids,
            "network": payload["keywordPlanNetwork"],
        },
        "ideas": result.get("results", []),
        "next_page_token": result.get("nextPageToken"),
    }
    return {"content": [{"type": "text", "text": json.dumps(output, indent=2)}]}


TOOL = {
    "name": TOOL_NAME,
    "description": "Read-only Google Ads Keyword Planner ideas and historical metrics. No campaign or account changes.",
    "inputSchema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["platform_id"],
        "properties": {
            "platform_id": {"type": "string", "description": "Must be the configured Google Ads platform ID."},
            "seed_keywords": {"type": "array", "items": {"type": "string"}, "maxItems": 20},
            "seed_url": {"type": "string", "format": "uri"},
            "language_id": {"type": "string", "default": "1000", "description": "Google Ads language criterion ID; 1000 is English."},
            "geo_target_ids": {"type": "array", "items": {"type": ["string", "integer"]}, "default": [2356], "description": "Google Ads geo criterion IDs; 2356 is India."},
            "network": {"type": "string", "enum": ["GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"], "default": "GOOGLE_SEARCH"},
            "include_adult_keywords": {"type": "boolean", "default": False},
            "page_size": {"type": "integer", "minimum": 1, "maximum": 10000, "default": 100},
            "year_month_range": {
                "type": "object",
                "description": "Optional historical metrics window, such as Apr–Aug 2025.",
                "required": ["start", "end"],
                "properties": {
                    "start": {"type": "object", "required": ["year", "month"], "properties": {"year": {"type": "integer"}, "month": {"type": "string", "enum": ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]}}},
                    "end": {"type": "object", "required": ["year", "month"], "properties": {"year": {"type": "integer"}, "month": {"type": "string", "enum": ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]}}},
                },
            },
        },
    },
}


def respond(message: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(message, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def main() -> None:
    load_local_env()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            method = request.get("method")
            request_id = request.get("id")
            if method == "notifications/initialized":
                continue
            if method == "initialize":
                result = {"protocolVersion": request.get("params", {}).get("protocolVersion", "2025-03-26"), "capabilities": {"tools": {}}, "serverInfo": {"name": "google-ads-keyword-planner", "version": "1.0.0"}}
            elif method == "tools/list":
                result = {"tools": [TOOL]}
            elif method == "tools/call":
                params = request.get("params", {})
                if params.get("name") != TOOL_NAME:
                    result = fail("This server exposes only google_ads_generate_keyword_ideas.")
                else:
                    result = generate_ideas(params.get("arguments", {}))
            else:
                if request_id is not None:
                    respond({"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "Method not found"}})
                continue
            if request_id is not None:
                respond({"jsonrpc": "2.0", "id": request_id, "result": result})
        except Exception as error:  # Never print secrets or tracebacks to the MCP client.
            if request_id is not None:
                respond({"jsonrpc": "2.0", "id": request_id, "error": {"code": -32603, "message": f"Internal error: {error}"}})


if __name__ == "__main__":
    main()
