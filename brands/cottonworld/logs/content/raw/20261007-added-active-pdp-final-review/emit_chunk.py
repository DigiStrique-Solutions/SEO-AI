"""Emit bounded changed rows for a precise Google Sheets update."""

import json
import sys
from pathlib import Path

root = Path(__file__).parent
revised = {r["row"]: r["after"] for r in json.loads((root / "revised.json").read_text(encoding="utf-8"))}
changed = json.loads((root / "changes.json").read_text(encoding="utf-8"))
start, end = map(int, sys.argv[1:3])
print(json.dumps([[r["row"], revised[r["row"]]] for r in changed if start <= r["row"] <= end], ensure_ascii=False))
