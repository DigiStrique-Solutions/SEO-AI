"""Emit a bounded slice of revised descriptions for a Sheets batch update."""

import json
import sys
from pathlib import Path

rows = json.loads((Path(__file__).parent / "revised.json").read_text(encoding="utf-8"))
start, end = map(int, sys.argv[1:3])
print(json.dumps([item["after"] for item in rows[start:end]], ensure_ascii=False))
