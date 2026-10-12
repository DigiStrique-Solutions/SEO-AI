import concurrent.futures
import gzip
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from lxml import html

HERE = Path(__file__).resolve().parent
TARGETS = json.loads((HERE / "targets.json").read_text(encoding="utf-8"))["links"]
RAW = HERE / "html"
RAW.mkdir(exist_ok=True)
USER_AGENT = "Mozilla/5.0 (compatible; StriqueSEOAudit/1.0; +https://cottonworld.net/)"


def text_of(node):
    return re.sub(r"\s+", " ", node.text_content()).strip()


def check(item):
    url = item["href"]
    key = hashlib.sha256(url.encode()).hexdigest()[:12]
    path = urlsplit(url).path.rstrip("/").split("/")[-1] or "collection"
    filename = f"{path}-{key}.html.gz"
    result = {
        "label": item["text"],
        "url": url,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "raw_html": f"html/{filename}",
    }
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read()
                result["http_status"] = response.status
                result["final_url"] = response.url
            break
        except urllib.error.HTTPError as exc:
            result["http_status"] = exc.code
            result["error"] = str(exc)
            if exc.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            return result
        except Exception as exc:
            result["error"] = str(exc)
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            return result
    with gzip.open(RAW / filename, "wb") as file:
        file.write(body)
    result["bytes"] = len(body)
    doc = html.fromstring(body)
    title = doc.xpath("//title")
    result["title"] = text_of(title[0]) if title else ""
    canonical = doc.xpath("//link[translate(@rel,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='canonical']/@href")
    result["canonical"] = canonical[0] if canonical else None
    sections = doc.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' cw-collection-read-more-section ')]")
    result["read_more_section_count"] = len(sections)
    bodies = doc.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' cw-collection-read-more__body ')]")
    snippets = [text_of(x) for x in bodies]
    content = " ".join(x for x in snippets if x)
    result["body_chars"] = len(content)
    result["body_words"] = len(content.split())
    result["body_excerpt"] = content[:240]
    result["body_headings"] = [text_of(h)[:120] for b in bodies for h in b.xpath(".//h1|.//h2|.//h3")][:8]
    result["details_open_by_default"] = any(bool(x.get("open")) for s in sections for x in s.xpath(".//details"))
    result["footer_content_status"] = "present" if result["body_words"] >= 30 else "absent"
    return result


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    records = list(pool.map(check, TARGETS))

summary = {
    "run_id": "cottonworld-men-collection-footer-20261012",
    "source_url": "https://cottonworld.net/pages/landing-page-men",
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "definition": "Dedicated collection-specific text inside the below-grid cw-collection-read-more__body; shared site footer excluded.",
    "records": records,
}
(HERE / "results.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "total": len(records),
    "present": sum(r.get("footer_content_status") == "present" for r in records),
    "absent": sum(r.get("footer_content_status") == "absent" for r in records),
    "blocked": sum("footer_content_status" not in r for r in records),
    "results": [{k: r.get(k) for k in ("label", "url", "http_status", "body_words", "footer_content_status", "error")} for r in records],
}, ensure_ascii=False))
