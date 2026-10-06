"""Emit a bounded set of revised descriptions for connector writes."""

import json
import sys
from pathlib import Path

rows = json.loads((Path(__file__).parent / "revised.json").read_text(encoding="utf-8"))
start, end = map(int, sys.argv[1:3])
print(json.dumps([[x["row"], x["after"]] for x in rows if start <= x["row"] <= end], ensure_ascii=False))
