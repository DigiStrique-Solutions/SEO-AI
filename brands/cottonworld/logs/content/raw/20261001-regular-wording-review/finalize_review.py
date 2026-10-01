"""Finalize the verified Boltworks sheet snapshot and reproducible QA record."""

import gzip
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


root = Path(__file__).resolve().parent
read_gz = lambda name: json.load(gzip.open(root / name, "rt", encoding="utf-8"))
source = read_gz("source-sheet.json.gz")
final = read_gz("final-sheet.json.gz")
fixes = json.loads((root / "description-fixes.json").read_text(encoding="utf-8"))
for fix in fixes:
    current = final["values"][fix["row"] - 1][4]
    if current not in {fix["before"], fix["after"]}:
        raise ValueError(f"Unexpected description at row {fix['row']}")
    final["values"][fix["row"] - 1][4] = fix["after"]
with gzip.open(root / "final-sheet.json.gz", "wt", encoding="utf-8") as out:
    json.dump(final, out, ensure_ascii=False)

subprocess.run([sys.executable, str(root / "print_audit.py")], check=True)
print_audit = json.loads((root / "print-audit.json").read_text(encoding="utf-8"))
planned = json.loads((root / "change-plan.json").read_text(encoding="utf-8"))["changes"]
changed_rows = {item["row"] for item in planned} | {item["row"] for item in fixes}
assert len(source["values"]) == len(final["values"]) == 393


def slugify(value):
    value = value.lower().replace("’", "").replace("'", "").replace("t-shirt", "tshirt")
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", value))


issues = []
unexpected = []
indexed = defaultdict(lambda: defaultdict(list))
for row_num, (before, after) in enumerate(zip(source["values"], final["values"]), 1):
    for col_num, (old, new) in enumerate(zip(before, after), 1):
        if old != new and row_num not in changed_rows:
            unexpected.append({"row": row_num, "column": col_num})
        if old != new and col_num not in {2, 3, 4, 5}:
            unexpected.append({"row": row_num, "column": col_num})
    if row_num == 1:
        continue
    url, h1, title, description = after[1:5]
    handle = url.removeprefix("https://cottonworld.net/products/")
    if handle != slugify(h1):
        issues.append({"row": row_num, "type": "url_h1_mismatch"})
    if title != f"{h1} | Cottonworld":
        issues.append({"row": row_num, "type": "title_h1_mismatch"})
    if re.search(r"\b(regular regular|fit fit|shirt shirt|t-shirt t-shirt)\b", h1, re.I):
        issues.append({"row": row_num, "type": "repeated_h1_word"})
    if re.search(r"\bwith (checked|striped|printed|check|stripe|print)\b", description, re.I):
        issues.append({"row": row_num, "type": "print_grammar"})
    if re.search(r"\b(m-tshirt|w-tshirt|\d{4,}[- ]\d{4,})\b", title + " " + description, re.I):
        issues.append({"row": row_num, "type": "product_code_in_meta"})
    if re.search(r"\bbuy\b", title, re.I):
        issues.append({"row": row_num, "type": "buy_in_meta_title"})
    for field, value in (("url", url), ("h1", h1), ("title", title), ("description", description)):
        indexed[field][value.casefold()].append(row_num)

duplicates = {
    field: rows
    for field, values in indexed.items()
    for rows in values.values()
    if len(rows) > 1
}
assert not issues and not unexpected and not duplicates, (issues, unexpected, duplicates)
flagged = [item for item in print_audit if item["flags"]]
assert {item["row"] for item in flagged} == {174, 175, 192, 193, 195, 209, 210}

verification = {
    "run_id": "20261001-regular-wording-review",
    "sheet_url": "https://docs.google.com/spreadsheets/d/1IlMiV6ccSfYyngMLuWyrEd3HD94wP4hbwcWQhOPnqcw/edit?gid=1979343695",
    "rows_audited": 392,
    "rows_changed": sorted(changed_rows),
    "source_snapshot": "source-sheet.json.gz",
    "final_snapshot": "final-sheet.json.gz",
    "catalog_source": "20261001-url-h1-meta-reaudit/catalog.json.gz",
    "catalog_fresh_fetch": "Timed out; same-day prior catalog snapshot used",
    "url_h1_title_mismatches": 0,
    "repeated_h1_wording": 0,
    "duplicate_url_h1_title_description_groups": 0,
    "print_grammar_errors": 0,
    "product_codes_in_meta": 0,
    "buy_in_meta_title": 0,
    "unexpected_cell_changes": 0,
    "print_named_rows_checked": len(print_audit),
    "print_direct_merchant_match": len(print_audit) - len(flagged),
    "graphic_prints_supported_by_photos_despite_generic_solid_field": [174, 192, 193, 195, 209, 210],
    "source_unavailable_print_not_verified": [175],
    "limitations": "Proposed URLs are a content plan; this check does not establish publication or live redirects. Row 175's source product was unavailable for print verification.",
}
(root / "verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding="utf-8")

activity = root.parent.parent / "activity.jsonl"
entry = {
    "run_id": verification["run_id"],
    "timestamp": "2026-10-01",
    "category": "content",
    "action": "verify_and_correct_boltworks_product_differentiators_and_repeated_fit_wording",
    "provider": "google_drive.get_spreadsheet_cells + google_drive.batch_update_spreadsheet + same_day_cottonworld_products_json + product_images",
    "status": "complete_with_one_unverified_source_product",
    "sheet_url": verification["sheet_url"],
    "rows_audited": 392,
    "rows_changed": len(changed_rows),
    "print_named_rows_checked": len(print_audit),
    "source_unavailable_print_not_verified": [175],
    "raw_ref": "raw/20261001-regular-wording-review/verification.json",
}
with activity.open("r", encoding="utf-8") as file:
    existing_ids = {json.loads(line).get("run_id") for line in file if line.strip()}
if entry["run_id"] not in existing_ids:
    with activity.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=False) + "\n")
print(json.dumps(verification, ensure_ascii=False))
