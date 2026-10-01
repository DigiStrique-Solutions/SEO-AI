"""Audit live Boltworks rows against current Cottonworld product data."""
import gzip
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
sheet = json.load(gzip.open(root / "source-sheet.json.gz", "rt", encoding="utf-8"))["values"]
catalog = {p["handle"]: p for p in json.load(gzip.open(root / "catalog.json.gz", "rt", encoding="utf-8"))["products"]}

def attrs(product):
    found = {}
    for item in re.findall(r"<li\b[^>]*>(.*?)</li>", product.get("body_html") or "", flags=re.I | re.S):
        item = html.unescape(re.sub(r"<[^>]+>", "", item)).strip()
        if ":" in item:
            key, value = item.split(":", 1)
            found[key.strip().upper()] = value.strip()
    return found

def normalize(value):
    value = str(value).lower().replace("’", "").replace("'", "")
    value = re.sub(r"\bdk\b", "dark", value)
    value = value.replace("offwhite", "off white").replace("darkgreen", "dark green")
    value = re.sub(r"(?<![a-z])t-shirt", "tshirt", value)
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def slug(value):
    return normalize(value).replace(" ", "-")

records = []
for rownum, row in enumerate(sheet[1:], 2):
    original, proposed, h1, title, description, dup_feedback, discrepancy_feedback, _, status = row
    handle = original.split("/products/")[-1]
    proposed_handle = proposed.split("/products/")[-1]
    product = catalog.get(handle)
    facts = attrs(product) if product else {}
    color = facts.get("COLOR", "")
    fit = facts.get("FIT TYPE", "")
    fabric = facts.get("FABRIC", "")
    title_color = color or ""
    issues = []
    if normalize(proposed_handle) != normalize(h1):
        issues.append("url_h1_mismatch")
    if title != h1 + " | Cottonworld":
        issues.append("h1_meta_title_mismatch")
    if not re.fullmatch(r"https://cottonworld\.net/products/[a-z0-9]+(?:-[a-z0-9]+)*", proposed):
        issues.append("malformed_proposed_url")
    if re.search(r"\bbuy\b|\b\d{4,}\b", title, re.I):
        issues.append("meta_title_product_code_or_buy")
    if re.search(r"\b\d{4,}\b", description):
        issues.append("meta_description_product_code")
    if len(description) > 160:
        issues.append("meta_description_over_160")
    if color and not slug(proposed_handle).endswith(slug(color)):
        issues.append("merchant_colour_not_last_in_url")
    if color and normalize(color) not in normalize(h1):
        issues.append("merchant_colour_not_in_h1")
    if fit and normalize(fit) not in normalize(h1):
        issues.append("merchant_fit_not_in_h1")
    if fabric and "ORGANIC" in fabric.upper() and "organic" not in h1.lower():
        issues.append("merchant_organic_not_in_h1")
    if fabric and "ORGANIC" not in fabric.upper() and "organic" in h1.lower():
        issues.append("h1_organic_not_in_merchant_fabric")
    records.append({"row": rownum, "original": original, "proposed": proposed, "h1": h1, "title": title, "description": description, "feedback_duplicate": dup_feedback, "feedback_discrepancy": discrepancy_feedback, "status": status, "source_in_catalog": bool(product), "proposed_in_catalog": proposed_handle in catalog, "merchant_title": product.get("title") if product else None, "merchant_color": title_color, "merchant_fit": fit, "merchant_fabric": fabric, "issues": issues})

duplicates = {}
for name, key in [("original", "original"), ("proposed", "proposed"), ("h1", "h1"), ("title", "title"), ("description", "description")]:
    groups = defaultdict(list)
    for record in records:
        groups[record[key]].append(record["row"])
    duplicates[name] = [{"value": value, "rows": nums} for value, nums in groups.items() if len(nums) > 1]

summary = {
    "rows": len(records),
    "catalog_products": len(catalog),
    "source_in_catalog": sum(r["source_in_catalog"] for r in records),
    "proposed_in_catalog": sum(r["proposed_in_catalog"] for r in records),
    "duplicates": duplicates,
    "issue_counts": dict(Counter(issue for r in records for issue in r["issues"])),
    "issue_rows": [{key: r[key] for key in ["row", "original", "proposed", "h1", "merchant_title", "merchant_color", "merchant_fit", "merchant_fabric", "status", "issues"]} for r in records if r["issues"]],
    "status_missing": [r["row"] for r in records if not r["status"]],
    "feedback_duplicate_rows": [r["row"] for r in records if r["feedback_duplicate"]],
    "feedback_discrepancy_rows": [r["row"] for r in records if r["feedback_discrepancy"]],
}
(root / "audit.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({key: value for key, value in summary.items() if key not in ["issue_rows", "status_missing", "feedback_duplicate_rows", "feedback_discrepancy_rows"]}, ensure_ascii=False))
print(json.dumps(summary["issue_rows"], ensure_ascii=False))
