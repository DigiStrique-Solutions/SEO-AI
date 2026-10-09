"""Check final Google Sheets readback against the approved copy and unchanged URLs."""

import hashlib
import json
from pathlib import Path

root = Path(__file__).parent
before = json.loads((root / "before-sheet.json").read_text(encoding="utf-8"))["values"]
after = json.loads((root / "verified-sheet.json").read_text(encoding="utf-8"))["values"]
revised = json.loads((root / "revised.json").read_text(encoding="utf-8"))
qa = json.loads((root / "qa.json").read_text(encoding="utf-8"))
assert len(before) == len(after) == 393
assert len(revised) == 392 and qa["issues"] == []
assert before[0] == after[0]
assert all(before[i][:2] == after[i][:2] for i in range(1, 393))
assert all(after[i][2] == revised[i-1]["after"] for i in range(1, 393))
assert all(before[i][2] != after[i][2] for i in range(1, 393))
result = {
    "spreadsheet_id": "1yZt5VrfS04g9Uz6rDkB6AtO5VYUsLK_h42sHg3gJow0",
    "sheet_name": "PDP Descriptions",
    "sheet_id": 1979343695,
    "range": "C2:C393",
    "description_rows_changed": 392,
    "url_columns_unchanged": True,
    "first_sentences_unique": qa["unique_first_sentences"],
    "copy_issues": len(qa["issues"]),
    "sha256_descriptions": hashlib.sha256("\n\0\n".join(x[2] for x in after[1:]).encode("utf-8")).hexdigest(),
    "source_ref": "brands/cottonworld/logs/content/raw/20261007-added-active-pdp-final-review/revised.json",
    "before_ref": str(root.relative_to(Path.cwd()) / "before-sheet.json").replace("\\", "/"),
    "readback_ref": str(root.relative_to(Path.cwd()) / "verified-sheet.json").replace("\\", "/"),
}
(root / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
