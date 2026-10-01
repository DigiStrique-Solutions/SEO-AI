"""Read merchant attributes for the user-edited product rows."""
import gzip
import html
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
rows = json.load(gzip.open(root/"source-sheet.json.gz","rt",encoding="utf-8"))["values"]
prior = root.parent/"20261001-url-h1-meta-reaudit"/"catalog.json.gz"
catalog = {p["handle"]: p for p in json.load(gzip.open(prior,"rt",encoding="utf-8"))["products"]}
selected = [132,142,146,148,149,260,262,272,280,291,292,302,303,310,318,353]
out = []
for row in selected:
    cells = rows[row-1]
    product = catalog.get(cells[0].split("/products/")[-1])
    facts = {}
    if product:
        for item in re.findall(r"<li\b[^>]*>(.*?)</li>",product.get("body_html") or "",re.I|re.S):
            item=html.unescape(re.sub(r"<[^>]+>","",item)).strip()
            if ":" in item:
                key,value=item.split(":",1)
                facts[key.strip().upper()]=value.strip()
    out.append({"row":row,"source_url":cells[0],"proposed_url":cells[1],"h1":cells[2],"meta_title":cells[3],"meta_description":cells[4],"catalog_found":bool(product),"merchant_title":product.get("title") if product else None,"attributes":facts,"tags":product.get("tags") if product else []})
(root/"source-attributes.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps([{k:r[k] for k in ["row","catalog_found","merchant_title","attributes"]} for r in out],ensure_ascii=False))
