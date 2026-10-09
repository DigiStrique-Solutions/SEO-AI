"""Verify product facts and copy integrity after introduction rewrites."""

import collections
import json
import re
from pathlib import Path

root = Path(__file__).parent
before = json.loads((root.parent / "20261007-added-active-pdp-final-review" / "revised.json").read_text(encoding="utf-8"))
after = json.loads((root / "revised.json").read_text(encoding="utf-8"))
changes = json.loads((root / "changes.json").read_text(encoding="utf-8"))
assert len(before) == len(after) == len(changes) == 392
issues = []
firsts = []
for old, new, change in zip(before, after, changes):
    row = old["row"]
    assert row == new["row"] == change["row"]
    for key in ("code", "url", "facts", "source_kind"):
        if old[key] != new[key]:
            issues.append([row, f"{key} changed"])
    old_paras = old["after"].split("\n\n")
    new_paras = new["after"].split("\n\n")
    if len(old_paras) != 4 or len(new_paras) != 4:
        issues.append([row, "paragraph count"])
        continue
    old_sentences = old_paras[0].split(". ")
    new_sentences = new_paras[0].split(". ")
    if old_sentences[1:] != new_sentences[1:]:
        issues.append([row, "fabric or surface sentence changed"])
    if old_paras[2:] != new_paras[2:]:
        issues.append([row, "styling or ID changed"])
    if change["feature_moved"]:
        moved, sep, remainder = old_paras[1].partition(". ")
        if not sep or new_paras[1] != remainder:
            issues.append([row, "feature relocation mismatch"])
        tokens = set(re.findall(r"[a-z]+", moved.lower())) - {"it", "they", "a", "is", "has", "have", "features", "feature", "paired", "with", "and"}
        if not tokens.issubset(set(re.findall(r"[a-z]+", new_sentences[0].lower()))):
            issues.append([row, "feature may be missing", sorted(tokens)])
    elif old_paras[1] != new_paras[1]:
        issues.append([row, "detail changed"])
    first = new_sentences[0] + "."
    firsts.append(first)
    if "for a morning out" in new["after"].lower():
        issues.append([row, "old awkward phrase"])
    if re.search(r"\b(\w+)(?:\s+|[-/])\1\b", new["after"], re.I):
        issues.append([row, "adjacent repeated word"])
    display_colour = {"darkgreen": "dark green", "dk green": "dark green", "dk olive": "dark olive", "dark-grey": "dark grey"}.get(new["facts"]["colour"], new["facts"]["colour"])
    if display_colour.lower() not in first.lower():
        issues.append([row, "colour missing from first sentence"])
    if new["facts"]["gender"].lower() not in first.lower():
        issues.append([row, "gender missing from first sentence"])
    if new["facts"]["noun"].lower() not in first.lower():
        issues.append([row, "product missing from first sentence"])
    if new["facts"]["fit"].lower() not in first.lower().replace("-", " "):
        issues.append([row, "fit missing from first sentence"])

duplicates = {k: v for k, v in collections.Counter(firsts).items() if v > 1}
if duplicates:
    issues.append(["all", "duplicate first sentence", duplicates])
stats = {
    "rows": len(after),
    "unique_first_sentences": len(set(firsts)),
    "first_sentence_patterns": dict(collections.Counter(x["template"] for x in changes)),
    "feature_sentences_moved": sum(x["feature_moved"] for x in changes),
    "body_word_min": min(x["words"] for x in after),
    "body_word_median": sorted(x["words"] for x in after)[len(after)//2],
    "body_word_max": max(x["words"] for x in after),
    "issues": issues,
}
(root / "qa.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(stats, ensure_ascii=False, indent=2))
