"""Check final copy edits without changing sourced product introductions or details."""

import collections
import json
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).parent
PRIOR = ROOT.parent / "20261006-added-active-pdp-copyedit" / "revised.json"
prior = {r["row"]: r for r in json.loads(PRIOR.read_text(encoding="utf-8"))}
rows = json.loads((ROOT / "revised.json").read_text(encoding="utf-8"))
stop = set("a an and are as at be by for from has have in into is it of on or the their there these this to with you your when where that then them its".split())
issues = []
bodies = collections.defaultdict(list)
normalized = collections.defaultdict(list)
changed = []

for item in rows:
    row, code = item["row"], item["code"]
    old = prior[row]
    text = item["after"]
    parts = text.split("\n\n")
    body = "\n\n".join(parts[:3])
    problems = []
    if len(parts) != 4 or parts[3] != "Product ID: " + code:
        problems.append("description structure or Product ID")
    if item["code"] != old["code"] or item["url"] != old["url"] or item["facts"] != old["facts"]:
        problems.append("product identity or facts changed")
    if parts[:2] != old["after"].split("\n\n")[:2]:
        problems.append("source-backed introduction or details changed")
    if text != old["after"]:
        changed.append(row)
    if re.search(r"\b(\w+)\s+\1\b", body, re.I):
        problems.append("adjacent repeated word")
    if re.search(r"  +|,,|;;|\.\.|\s[.,;]", body):
        problems.append("spacing or punctuation")
    if any(p in body for p in ["Keep the jacket and accessories simple", "without adding another layer", "rather than several extra layers"]):
        problems.append("unresolved styling mismatch")
    if item["facts"]["gender"] == "men":
        style = parts[2]
        if "flat shoes" in style:
            problems.append("generic flat shoes in mens styling")
        if item["facts"]["noun"] == "trousers" and any(p in style for p in ["flat sandals", "knit top", "plain navy top", "plain off-white top"]):
            problems.append("inconsistent mens trouser styling")
    nwords = len(body.split())
    if not 80 <= nwords <= 145:
        problems.append("description length")

    words = re.findall(r"[a-z]+(?:'[a-z]+)?", body.lower())
    frequent = {w: n for w, n in collections.Counter(w for w in words if w not in stop and len(w) > 3).items() if n >= 3}
    if frequent:
        problems.append("word repeated three times: " + str(frequent))
    seen = {}
    for i in range(len(words) - 2):
        chunk = words[i:i+3]
        if all(w in stop for w in chunk):
            continue
        key = " ".join(chunk)
        if key in seen and i - seen[key] >= 3:
            problems.append("repeated phrase: " + key)
            break
        seen[key] = i
    if problems:
        issues.append({"row": row, "code": code, "problems": problems})
    bodies[body.lower()].append(row)
    colour_only = re.sub(r"\b(?:black|white|off-white|navy|blue|denim|red|pink|khaki|brick|cream|grey|gray|beige|green|yellow|brown|purple|maroon|olive|coffee|mustard|rust|orange|indigo|wine|peach|ivory|teal|charcoal|stone|coral|aqua|lavender|lilac|sand|mint|tan|sage|natural|dark-grey)\b", "[colour]", body.lower())
    normalized[re.sub(r"\d+%", "[pct]", colour_only)].append(row)

result = {
    "rows": len(rows),
    "changed": len(changed),
    "unique_ids": len({r["code"] for r in rows}),
    "unique_urls": len({r["url"] for r in rows}),
    "body_word_min_median_max": [min(r["words"] for r in rows), statistics.median(r["words"] for r in rows), max(r["words"] for r in rows)],
    "issues": issues,
    "duplicate_bodies": [v for v in bodies.values() if len(v) > 1],
    "colour_only_duplicate_bodies": [v for v in normalized.values() if len(v) > 1],
}
(ROOT / "qa.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"rows": result["rows"], "changed": result["changed"], "issues": issues[:40],
                  "duplicate_bodies": result["duplicate_bodies"], "colour_only_duplicate_bodies": result["colour_only_duplicate_bodies"],
                  "body_word_min_median_max": result["body_word_min_median_max"]}, ensure_ascii=False, indent=2))
