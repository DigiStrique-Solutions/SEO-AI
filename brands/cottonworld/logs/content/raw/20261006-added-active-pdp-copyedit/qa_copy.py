"""Check copyedit integrity, repetition and product identity before sheet updates."""

import collections
import json
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).parent
rows = json.loads((ROOT / "revised.json").read_text(encoding="utf-8"))
prior = json.loads((ROOT.parent / "20261006-added-active-pdp" / "proposals.json").read_text(encoding="utf-8"))
original = {x["row"]: x for x in prior}
stop = set("a an and are as at be by for from has have in into is it of on or the their there these this to with you your when where that then them its".split())

errors, warnings = [], []
body_map = collections.defaultdict(list)
codes = collections.Counter(x["code"] for x in rows)
urls = collections.Counter(x["url"] for x in rows)

for r in rows:
    row, code = r["row"], r["code"]
    text = r["after"]
    body = text.split("\n\nProduct ID:")[0]
    parts = text.split("\n\n")
    facts = r["facts"]
    p = original[row]
    problems = []
    if len(parts) != 4:
        problems.append("paragraph count")
    if parts[-1] != "Product ID: " + code:
        problems.append("product ID")
    if code != p["code"] or r["url"] != p["url"]:
        problems.append("product identity changed")
    if facts["fabric"].lower() not in body.lower():
        problems.append("fabric missing")
    if f"{facts['gender']}'s" not in body:
        problems.append("gender missing")
    if len(re.findall(r"\b" + re.escape(facts["colour"]) + r"\b", body, re.I)) != 1:
        problems.append("colour missing or repeated")
    if r["row"] not in {93, 370} and facts != p["facts"]:
        problems.append("source facts changed")
    if r["row"] == 370 and facts["colour"] != "olive":
        problems.append("incorrect colour")
    if re.search(r"\b(\w+)\s+\1\b", body, re.I):
        problems.append("adjacent duplicate word")
    if re.search(r"  +|,,|;;|\.\.|\s[.,;]", body):
        problems.append("spacing or punctuation")
    for term in ["The surface detailing brings a point of interest", "the rest of your wardrobe", "regular collar", "regular placket", "The design has"]:
        if term in body:
            problems.append("old repetitive phrase: " + term)
    if facts["noun"] == "shirt" and "An unbuttoned shirt or light jacket" in body:
        problems.append("shirt layered over shirt")
    if re.search(r"\boffer a barrel leg\b", body):
        problems.append("awkward barrel-leg phrase")
    count = len(body.split())
    if not 80 <= count <= 145:
        problems.append("body length")

    words = re.findall(r"[a-z]+(?:'[a-z]+)?", body.lower())
    freq = collections.Counter(w for w in words if w not in stop and len(w) > 3)
    high = {w: n for w, n in freq.items() if n >= 3}
    if high:
        warnings.append({"row": row, "type": "word repeated 3+", "detail": high})
    seen = {}
    grams = []
    for i in range(len(words) - 2):
        chunk = words[i:i+3]
        if all(w in stop for w in chunk):
            continue
        key = " ".join(chunk)
        if key in seen and i - seen[key] >= 3:
            grams.append(key)
        else:
            seen[key] = i
    if grams:
        warnings.append({"row": row, "type": "phrase repeated within description", "detail": sorted(set(grams))})
    for part in parts[:3]:
        sentences = re.split(r"(?<=[.!?])\s+", part)
        heads = [" ".join(x.lower().split()[:2]) for x in sentences]
        repeated = [heads[i] for i in range(1, len(heads)) if heads[i] == heads[i - 1]]
        if repeated:
            warnings.append({"row": row, "type": "sentence opening repeated", "detail": repeated})
    if problems:
        errors.append({"row": row, "code": code, "problems": problems})
    body_map[body.lower()].append(row)

duplicates = [v for v in body_map.values() if len(v) > 1]
result = {
    "rows": len(rows),
    "unique_product_ids": len(codes),
    "unique_urls": len(urls),
    "body_word_min_median_max": [min(len(x["after"].split("Product ID:")[0].split()) for x in rows),
                                 statistics.median(len(x["after"].split("Product ID:")[0].split()) for x in rows),
                                 max(len(x["after"].split("Product ID:")[0].split()) for x in rows)],
    "errors": errors,
    "warnings": warnings,
    "duplicate_bodies": duplicates,
}
(ROOT / "qa.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"rows": len(rows), "errors": len(errors), "warnings": len(warnings),
                  "warning_types": dict(collections.Counter(w["type"] for w in warnings)),
                  "duplicate_bodies": duplicates,
                  "body_word_min_median_max": result["body_word_min_median_max"]}, indent=2))
