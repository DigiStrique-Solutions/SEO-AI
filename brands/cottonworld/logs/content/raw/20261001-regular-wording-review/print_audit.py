"""Cross-check print wording in proposed product names against merchant print fields."""
import gzip, html, json, re
from pathlib import Path
root=Path(__file__).resolve().parent
rows=json.load(gzip.open(root/"final-sheet.json.gz","rt",encoding="utf-8"))["values"]
catalog={p["handle"]:p for p in json.load(gzip.open(root.parent/"20261001-url-h1-meta-reaudit"/"catalog.json.gz","rt",encoding="utf-8"))["products"]}
terms=re.compile(r"\b(stripe|stripes|striped|pinstripe|check|checked|plaid|graphic|print|printed|solid|plain|floral|abstract|cartoon|cassette|astronaut|vinyl|landscape|grid|textured|pattern|melange|colourblock|colorblock)\b",re.I)
records=[]
for rownum,cells in enumerate(rows[1:],2):
    h1=cells[2]
    match=terms.findall(h1)
    if not match: continue
    product=catalog.get(cells[0].split("/products/")[-1])
    attrs={}
    if product:
        for item in re.findall(r"<li\b[^>]*>(.*?)</li>",product.get("body_html") or "",re.I|re.S):
            item=html.unescape(re.sub(r"<[^>]+>","",item)).strip()
            if ":" in item:
                k,v=item.split(":",1);attrs[k.strip().upper()]=v.strip()
    actual=(attrs.get("PRINT") or "").upper()
    tags=[str(x).upper() for x in product.get("tags",[])] if product else []
    groups=set()
    for term in match:
        t=term.lower()
        if t in {"stripe","stripes","striped","pinstripe","grid"}:groups.add("STRIPE")
        elif t in {"check","checked","plaid"}:groups.add("CHECK")
        elif t in {"solid","plain"}:groups.add("SOLID")
        elif t in {"graphic","print","printed","floral","abstract","cartoon","cassette","astronaut","vinyl","landscape"}:groups.add("PRINT")
    flags=[]
    for group in groups:
        if group=="STRIPE" and not (actual=="STRIPE" or "STRIPE" in tags):flags.append("stripe_not_in_merchant_print")
        if group=="CHECK" and not (actual=="CHECK" or "CHECK" in tags):flags.append("check_not_in_merchant_print")
        if group=="SOLID" and not (actual in {"SOLID","PLAIN"} or "SOLID" in tags):flags.append("solid_not_in_merchant_print")
        if group=="PRINT" and not (actual in {"PRINT","GRAPHIC"} or "PRINT" in tags or "GRAPHIC TEES" in tags):flags.append("graphic_not_in_merchant_print")
    records.append({"row":rownum,"h1":h1,"meta_description":cells[4],"name_terms":match,"merchant_print":actual,"tags":tags,"catalog_found":bool(product),"flags":flags,"image":product.get("images",[{}])[0].get("src") if product else None})
(root/"print-audit.json").write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"print_named_rows":len(records),"flagged":[{"row":r["row"],"h1":r["h1"],"merchant_print":r["merchant_print"],"flags":r["flags"]} for r in records if r["flags"]]},ensure_ascii=False))
