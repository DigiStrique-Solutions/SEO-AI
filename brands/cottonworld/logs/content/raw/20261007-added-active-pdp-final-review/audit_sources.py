"""Independently compare PDP copy with merchant title, URL and body attributes."""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
OLD = ROOT.parent / "20261006-added-active-pdp"
EDIT = ROOT.parent / "20261006-added-active-pdp-copyedit"
records = {r["row"]: r for r in json.loads((OLD / "records.json").read_text(encoding="utf-8"))}
copy = json.loads((EDIT / "revised.json").read_text(encoding="utf-8"))

def norm(value):
    value = html.unescape(value or "").lower()
    value = value.replace("offwhite", "off white").replace("multicolour", "multi")
    value = value.replace("dark", "dk").replace("melange", "melan")
    value = value.replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def body_fields(product):
    raw = product.get("Body (HTML)") or ""
    out = {}
    for key, value in re.findall(r"<li>\s*([^:<]+):\s*(.*?)\s*</li>", raw, re.I | re.S):
        out[key.strip().upper()] = html.unescape(re.sub(r"<[^>]+>", "", value)).strip()
    return out

flags = []
for item in copy:
    row = item["row"]
    record = records[row]
    product = record["product"]
    if not product:
        continue
    fields = body_fields(product)
    title = product["Title"]
    slug = record["updated_url"].rsplit("/", 1)[-1]
    facts = item["facts"]
    body = item["after"].split("\n\nProduct ID:")[0]
    colour = fields.get("COLOR") or fields.get("COLOUR") or product.get("Colour (product.metafields.custom.colour)", "")
    if colour and norm(colour) not in norm(title) and norm(colour) not in norm(slug):
        flags.append({"row": row, "kind": "merchant colour conflicts with title and URL", "merchant": colour, "title": title, "url": slug, "description": body[:180]})
    fit = fields.get("FIT TYPE") or product.get("Fit Type (product.metafields.custom.fit_type)", "")
    if fit and "fit" in norm(title):
        f = norm(fit).replace("relaxed fit", "relax fit")
        if f not in norm(title).replace("relaxed fit", "relax fit"):
            flags.append({"row": row, "kind": "merchant fit conflicts with title", "merchant": fit, "title": title})
    typ = fields.get("TYPE") or product.get("Product Type (product.metafields.custom.product_type)", "")
    canonical_type = {"blouses": "blouse", "dresses": "dress", "kdresses": "kdress"}.get(norm(typ), norm(typ))
    if canonical_type and canonical_type not in norm(item["code"]):
        flags.append({"row": row, "kind": "merchant type conflicts with product ID", "merchant": typ, "code": item["code"]})
    if fields.get("PRINT") == "SOLID" and any(t in norm(slug).split() for t in ["printed", "check", "checked", "stripe", "striped"]):
        flags.append({"row": row, "kind": "merchant solid conflicts with URL pattern", "url": slug})
    if fields.get("FABRIC COMPOSITION") and not all(x.lower() in body.lower() for x in re.findall(r"\d+%\s*[A-Za-z]+", facts["fabric"])):
        flags.append({"row": row, "kind": "fabric composition absent from copy", "merchant": fields["FABRIC COMPOSITION"], "description": body[:180]})

(ROOT / "source-flags.json").write_text(json.dumps(flags, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"source_rows": sum(bool(r["product"]) for r in records.values()), "flags": len(flags), "sample": flags[:60]}, ensure_ascii=False, indent=2))
