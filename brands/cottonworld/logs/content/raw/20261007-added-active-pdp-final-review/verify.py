"""Verify the final live Sheet and review Doc readbacks against the copy audit."""

import json
from pathlib import Path

ROOT = Path(__file__).parent
before = json.loads((ROOT / "before-sheet.json").read_text(encoding="utf-8"))["values"]
after = json.loads((ROOT / "after-sheet.json").read_text(encoding="utf-8"))["values"]
revised = json.loads((ROOT / "revised.json").read_text(encoding="utf-8"))
qa = json.loads((ROOT / "qa.json").read_text(encoding="utf-8"))
flags = json.loads((ROOT / "source-flags.json").read_text(encoding="utf-8"))
doc = json.loads((ROOT / "review-doc-final.json").read_text(encoding="utf-8"))

assert len(before) == len(after) == 393
assert len(revised) == 392
assert before[0] == after[0]
assert not qa["issues"] and not qa["duplicate_bodies"] and not qa["colour_only_duplicate_bodies"]
assert len(flags) == 1 and flags[0]["row"] == 370
changed = []
for row in range(2, 394):
    b, a, expected = before[row - 1], after[row - 1], revised[row - 2]
    assert b[:2] == a[:2], row
    assert expected["row"] == row and a[2] == expected["after"], row
    if b[2] != a[2]:
        changed.append(row)
assert len(changed) == 147

tab = doc["tabs"][0]
content = tab.get("documentTab", tab)["body"]["content"]
body = "".join(e.get("textRun", {}).get("content", "") for p in content
               for e in p.get("paragraph", {}).get("elements", []))
heading = next(p for p in content if p.get("paragraph", {}).get("elements", [{}])[0].get("textRun", {}).get("content", "").startswith("Second copy review"))
assert heading["paragraph"]["paragraphStyle"]["namedStyleType"] == "HEADING_1"
assert "147 rows" in body and "median body length is 110 words" in body
assert "row 370 remains" in body and "rows 24 and 293–295" in body

result = {
    "status": "pass",
    "sheet_rows_checked": 392,
    "descriptions_changed": len(changed),
    "source_url_columns_preserved": True,
    "all_descriptions_match_revisions": True,
    "copy_issues": 0,
    "exact_or_colour_only_duplicate_bodies": 0,
    "review_doc_updated": True,
    "remaining_source_discrepancy": "Row 370 merchant colour field brown vs title and both supplied URLs olive",
    "other_source_limitations": "Rows 24 and 293–295 have incomplete current product records",
}
(ROOT / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
