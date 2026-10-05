"""Reconstruct the 5 October sheet and compare names to merchant variant facts."""

import gzip
import html
import json
import re
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
prior = root.parent / "20261001-regular-wording-review" / "final-sheet.json.gz"
catalog_path = root.parent / "20261001-url-h1-meta-reaudit" / "catalog.json.gz"
values = json.load(gzip.open(prior, "rt", encoding="utf-8"))["values"]
for change in json.loads((root / "live-diff.json").read_text(encoding="utf-8")):
    cell = values[change["row"] - 1][change["col"] - 1]
    assert cell == change["old"], change
    values[change["row"] - 1][change["col"] - 1] = change["value"]
with gzip.open(root / "source-sheet.json.gz", "wt", encoding="utf-8") as output:
    json.dump({"spreadsheetId": "1IlMiV6ccSfYyngMLuWyrEd3HD94wP4hbwcWQhOPnqcw", "sheet": "Boltworks sheet", "values": values}, output, ensure_ascii=False)

catalog = {
    item["handle"]: item
    for item in json.load(gzip.open(catalog_path, "rt", encoding="utf-8"))["products"]
}
groups = defaultdict(list)
for row_number, cells in enumerate(values[1:], 2):
    handle = cells[0].split("/products/")[-1]
    match = re.fullmatch(r"(.*?-\d+-\d+)-(.+)", handle)
    if not match:
        continue
    group_key, color = match.groups()
    product = catalog.get(handle)
    attributes = {}
    if product:
        for element in re.findall(r"<li\b[^>]*>(.*?)</li>", product.get("body_html") or "", re.I | re.S):
            text = html.unescape(re.sub(r"<[^>]+>", "", element)).strip()
            if ":" in text:
                key, value = text.split(":", 1)
                attributes[key.strip().upper()] = value.strip()
    groups[group_key].append({
        "row": row_number,
        "original_handle": handle,
        "original_color": color,
        "proposed_url": cells[1],
        "h1": cells[2],
        "title": cells[3],
        "description": cells[4],
        "merchant_title": product.get("title") if product else None,
        "merchant_attributes": {key: attributes.get(key) for key in ["PRINT", "FABRIC", "FIT TYPE", "NECKCOLLAR", "SLEEVE", "POCKET", "OPENING", "HEMLINE", "LENGTH"]},
        "merchant_tags": product.get("tags", []) if product else [],
        "image": product.get("images", [{}])[0].get("src") if product else None,
        "catalog_found": bool(product),
    })

records = [{"group": key, "variants": group} for key, group in groups.items() if len(group) > 1]
(root / "variant-groups.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"variant_groups": len(records), "variant_rows": sum(len(x["variants"]) for x in records), "missing_in_catalog": [(x["group"], v["row"]) for x in records for v in x["variants"] if not v["catalog_found"]]}, ensure_ascii=True))
