"""Verify saved Google Sheet and review Doc against the audited revisions."""

import json
from pathlib import Path

ROOT = Path(__file__).parent
before = json.loads((ROOT / "before-sheet.json").read_text(encoding="utf-8"))["values"]
after = json.loads((ROOT / "after-sheet.json").read_text(encoding="utf-8"))["values"]
revised = json.loads((ROOT / "revised.json").read_text(encoding="utf-8"))
qa = json.loads((ROOT / "qa.json").read_text(encoding="utf-8"))
doc = json.loads((ROOT / "review-doc-final.json").read_text(encoding="utf-8"))

assert len(before) == len(after) == 393
assert len(revised) == 392
assert before[0] == after[0]
assert before[0][2] == "Updated PDP Description"
assert not qa["errors"] and not qa["warnings"] and not qa["duplicate_bodies"]

changed = []
for row in range(2, 394):
    old, new, proposal = before[row - 1], after[row - 1], revised[row - 2]
    assert old[:2] == new[:2], row
    assert proposal["row"] == row
    assert new[2] == proposal["after"], row
    if old[2] != new[2]:
        changed.append(row)
assert len(changed) == 389
assert "men's olive T-shirt" in after[369][2]

tab = doc["tabs"][0]
content = tab.get("documentTab", tab)["body"]["content"]
body = "".join(e.get("textRun", {}).get("content", "") for c in content
               for e in c.get("paragraph", {}).get("elements", []))
assert "Copyedit recheck — 6 October 2026" in body
assert "description now says olive" in body
assert "median body length is 111 words" in body

result = {
    "status": "pass",
    "sheet_rows": len(revised),
    "sheet_changed_rows": len(changed),
    "sheet_unchanged_rows": [r for r in range(2, 394) if r not in changed],
    "source_columns_preserved": True,
    "all_descriptions_match": True,
    "copy_qa_errors": 0,
    "copy_qa_warnings": 0,
    "review_doc_updated": True,
    "colour_discrepancy": "row 370: merchant colour field brown; title and URLs olive; copy now olive",
}
(ROOT / "verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
