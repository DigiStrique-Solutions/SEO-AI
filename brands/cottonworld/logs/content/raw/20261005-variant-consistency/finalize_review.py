"""Verify the variant naming change and record its provenance."""

import gzip
import json
import re
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
source = json.load(gzip.open(root / "source-sheet.json.gz", "rt", encoding="utf-8"))
values = [row[:] for row in source["values"]]
plan = json.loads((root / "change-plan.json").read_text(encoding="utf-8"))["changes"]
statuses = json.loads((root / "status-updates.json").read_text(encoding="utf-8"))
groups = json.loads((root / "variant-groups.json").read_text(encoding="utf-8"))
url_checks = json.loads((root / "proposed-url-head-results.json").read_text(encoding="utf-8"))

for item in plan:
    row = values[item["row"] - 1]
    for col, field in enumerate(("url", "h1", "title", "description"), 1):
        assert row[col] == item["before"][field], (item["row"], field)
        row[col] = item["after"][field]
for item in statuses:
    row = values[item["row"] - 1]
    assert row[8] == item["before"], item["row"]
    row[8] = item["after"]


def slugify(value):
    value = value.lower().replace("’", "").replace("'", "").replace("t-shirt", "tshirt")
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", value))


issues = []
indexed = defaultdict(lambda: defaultdict(list))
for row_num, row in enumerate(values[1:], 2):
    url, h1, title, description = row[1:5]
    if url != "https://cottonworld.net/products/" + slugify(h1):
        issues.append((row_num, "url_h1"))
    if title != h1 + " | Cottonworld":
        issues.append((row_num, "title_h1"))
    if re.search(r"\b(regular regular|fit fit|shirt shirt)\b", h1, re.I):
        issues.append((row_num, "repetition"))
    if re.search(r"\bwith (checked|striped|printed)\b", description, re.I):
        issues.append((row_num, "print_grammar"))
    if re.search(r"-\d{4,}-\d{4,}", title + " " + description):
        issues.append((row_num, "product_code_in_meta"))
    if re.search(r"\bbuy\b", title, re.I):
        issues.append((row_num, "buy_in_title"))
    for field, value in (("url", url), ("h1", h1), ("title", title), ("description", description)):
        indexed[field][value.casefold()].append(row_num)
duplicate_groups = {field: [v for v in entries.values() if len(v) > 1] for field, entries in indexed.items()}
assert not issues and not any(duplicate_groups.values()), (issues, duplicate_groups)


def stem(row_num, original_color, group_key, rows):
    handle = rows[row_num - 1][1].split("/products/")[-1]
    colors = {"offwhite": "off-white", "dk-green": "dark-green", "darkgreen": "dark-green"}
    color = colors.get(original_color, original_color)
    if group_key == "m-tshirt-17444-21765":
        color = "light-blue" if row_num == 381 else "chocolate-brown"
    assert handle.endswith("-" + color), (row_num, handle, color)
    return handle[: -len(color) - 1]


before_groups = []
after_groups = []
for group in groups:
    variants = group["variants"]
    initial = {stem(v["row"], v["original_color"], group["group"], source["values"]) for v in variants}
    final = {stem(v["row"], v["original_color"], group["group"], values) for v in variants}
    if len(initial) > 1:
        before_groups.append(group["group"])
    if len(final) > 1:
        after_groups.append(group["group"])
assert len(before_groups) == 44 and not after_groups, (before_groups, after_groups)
assert len(url_checks) == len(plan) == 101
assert all(item.get("status") == 404 for item in url_checks)
assert len(statuses) == 19

final = {"spreadsheetId": source["spreadsheetId"], "sheet": source["sheet"], "values": values}
with gzip.open(root / "final-sheet.json.gz", "wt", encoding="utf-8") as output:
    json.dump(final, output, ensure_ascii=False)
verification = {
    "run_id": "20261005-variant-consistency",
    "sheet_url": "https://docs.google.com/spreadsheets/d/1IlMiV6ccSfYyngMLuWyrEd3HD94wP4hbwcWQhOPnqcw/edit?gid=1979343695",
    "rows_audited": 392,
    "variant_families_audited": len(groups),
    "variant_rows_audited": sum(len(group["variants"]) for group in groups),
    "inconsistent_variant_families_before": len(before_groups),
    "inconsistent_variant_families_after": len(after_groups),
    "rows_corrected": len(plan),
    "review_status_rows_corrected": len(statuses),
    "url_h1_title_mismatches_after": 0,
    "duplicate_url_h1_title_description_groups_after": 0,
    "unexpected_live_cell_changes_after_readback": 0,
    "proposed_urls_404": len(url_checks),
    "source_fact_conflicts": [
        {
            "rows": [253, 254],
            "issue": "Merchant PRINT field says CHECK; current product photos show solid black and off-white shirts.",
            "evidence": ["m-shirts-13484-21611-black.jpg", "m-shirts-13484-21611-offwhite.jpg", "print-variant-comparison.jpg"],
            "next_action": "Correct merchant print data and confirm before publishing."
        }
    ],
    "source_unavailable_inferred_variant_detail": [201],
    "limitations": "The changed proposed URLs return 404 and require storefront publication. Row 201's source product is unavailable; standard length is inferred from its same-style brown variant and needs identity confirmation.",
    "source_snapshot": "source-sheet.json.gz",
    "final_snapshot": "final-sheet.json.gz",
    "catalog_snapshot": "../20261001-url-h1-meta-reaudit/catalog.json.gz",
    "current_public_page_checked": ["https://cottonworld.net/products/m-shirts-13484-21611-black", "https://cottonworld.net/products/m-shirts-13484-21611-offwhite"],
    "current_public_page_raw": ["m-shirts-13484-21611-black.html.gz", "m-shirts-13484-21611-offwhite.html.gz"],
    "visual_contact_sheet": "print-variant-comparison.jpg",
}
(root / "verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding="utf-8")

activity = root.parent.parent / "activity.jsonl"
entry = {
    "run_id": verification["run_id"],
    "timestamp": "2026-10-05",
    "category": "content",
    "action": "standardize_product_variant_differentiators_and_placement",
    "provider": "google_drive.get_spreadsheet_cells + google_drive.batch_update_spreadsheet + cottonworld_product_catalog + public_product_pages + product_images + public_url_head",
    "status": "complete_with_storefront_publication_and_source_data_followups",
    "sheet_url": verification["sheet_url"],
    "rows_audited": 392,
    "rows_corrected": len(plan),
    "variant_families_audited": len(groups),
    "raw_ref": "raw/20261005-variant-consistency/verification.json",
}
with activity.open("r", encoding="utf-8") as file:
    known = {json.loads(line).get("run_id") for line in file if line.strip()}
if entry["run_id"] not in known:
    with activity.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=False) + "\n")
print(json.dumps(verification, ensure_ascii=True))
