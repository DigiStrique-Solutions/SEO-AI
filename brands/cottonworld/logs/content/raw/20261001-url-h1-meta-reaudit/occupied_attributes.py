"""Summarize attribute differences for occupied proposed handles."""
import gzip
import html
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parent
sheet = json.load(gzip.open(root/"source-sheet.json.gz","rt",encoding="utf-8"))["values"]
catalog = {p["handle"]: p for p in json.load(gzip.open(root/"catalog.json.gz","rt",encoding="utf-8"))["products"]}
rows = [x["row"] for x in json.loads((root/"parallel-live-products.json").read_text(encoding="utf-8"))]
def attrs(p):
    output = {}
    for item in re.findall(r"<li\b[^>]*>(.*?)</li>", p.get("body_html") or "", re.I|re.S):
        item = html.unescape(re.sub(r"<[^>]*>","",item)).strip()
        if ":" in item:
            k,v=item.split(":",1)
            output[k.strip().upper()]=v.strip()
    return output
out=[]
for row in rows:
    cells=sheet[row-1]
    a=catalog[cells[0].split("/products/")[-1]]
    b=catalog[cells[1].split("/products/")[-1]]
    x,y=attrs(a),attrs(b)
    keys=["PRINT","FABRIC","FABRIC COMPOSITION","FIT TYPE","COLOR","NECKCOLLAR","SLEEVE","OPENING","HEMLINE","POCKET"]
    out.append({"row":row,"source_title":a["title"],"proposed_title":b["title"],"source":{k:x.get(k) for k in keys},"occupied":{k:y.get(k) for k in keys},"source_tags":a.get("tags"),"occupied_tags":b.get("tags"),"source_image":a.get("images",[{}])[0].get("src"),"occupied_image":b.get("images",[{}])[0].get("src")})
(root/"occupied-handle-attributes.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps([{k:v for k,v in r.items() if k not in ["source_tags","occupied_tags","source_image","occupied_image"]} for r in out],ensure_ascii=False))
