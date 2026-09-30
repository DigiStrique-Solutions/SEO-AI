"""Compare final sheet product attributes against merchant catalog fields."""
import gzip
import html
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
sheet = json.load(gzip.open(root / "source-sheet.json.gz", "rt", encoding="utf-8"))["values"]
products = {p["handle"]: p for p in json.load(gzip.open(root / "catalog.json.gz", "rt", encoding="utf-8"))["products"]}
changes = {x["row"]: x["after"] for x in json.loads((root / "change-plan.json").read_text(encoding="utf-8"))["changes"]}

def attributes(product):
    found = {}
    for item in re.findall(r"<li\b[^>]*>(.*?)</li>", product.get("body_html") or "", flags=re.I | re.S):
        value = html.unescape(re.sub(r"<[^>]*>", "", item)).strip()
        if ":" in value:
            key, content = value.split(":", 1)
            found[key.strip().upper()] = content.strip()
    return found

def normalize(text):
    text = text.lower().replace("’", "").replace("'", "")
    text = re.sub(r"\bdk\b", "dark", text)
    text = text.replace("offwhite", "off white").replace("darkgreen", "dark green")
    text = text.replace("melan", "melange")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()

issues = []
for row, cells in enumerate(sheet[1:], 2):
    source_url = cells[0]
    product = products.get(source_url.split("/products/")[-1])
    if not product:
        continue
    current = changes.get(row, {})
    h1 = current.get("h1", cells[2])
    description = current.get("metaDescription", cells[4])
    values = attributes(product)
    color = values.get("COLOR")
    fit = values.get("FIT TYPE")
    fabric = values.get("FABRIC")
    result = {"row": row, "source_url": source_url, "h1": h1, "merchant_title": product["title"], "merchant_color": color, "merchant_fit": fit, "merchant_fabric": fabric}
    flags = []
    if color and normalize(color) not in normalize(h1):
        flags.append("merchant_color_not_in_h1")
    if fit and normalize(fit) not in normalize(h1):
        flags.append("merchant_fit_not_in_h1")
    if fabric and "ORGANIC" in fabric.upper() and "organic" not in h1.lower():
        flags.append("merchant_organic_not_in_h1")
    if fabric and "ORGANIC" not in fabric.upper() and "organic" in h1.lower():
        flags.append("h1_organic_not_in_merchant_fabric")
    if flags:
        result["flags"] = flags
        result["description"] = description
        issues.append(result)
report = {"source_products_matched": len(sheet)-1-sum(c[0].split("/products/")[-1] not in products for c in sheet[1:]), "issue_count": len(issues), "issues": issues}
(root / "merchant-attribute-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
