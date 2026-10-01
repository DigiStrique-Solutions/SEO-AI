"""Compare existing original and proposed Shopify product records."""
import gzip
import json
from pathlib import Path

root = Path(__file__).resolve().parent
sheet = json.load(gzip.open(root / "source-sheet.json.gz", "rt", encoding="utf-8"))["values"]
catalog = {p["handle"]: p for p in json.load(gzip.open(root / "catalog.json.gz", "rt", encoding="utf-8"))["products"]}
pairs = []
for rownum, row in enumerate(sheet[1:], 2):
    original = catalog.get(row[0].split("/products/")[-1])
    proposed = catalog.get(row[1].split("/products/")[-1])
    if original is None or proposed is None:
        continue
    original_images = {image.get("src", "").split("?")[0] for image in original.get("images", [])}
    proposed_images = {image.get("src", "").split("?")[0] for image in proposed.get("images", [])}
    original_skus = {variant.get("sku") for variant in original.get("variants", []) if variant.get("sku")}
    proposed_skus = {variant.get("sku") for variant in proposed.get("variants", []) if variant.get("sku")}
    pairs.append({
        "row": rownum,
        "original_url": row[0],
        "proposed_url": row[1],
        "original_id": original["id"],
        "proposed_id": proposed["id"],
        "same_product_id": original["id"] == proposed["id"],
        "original_title": original["title"],
        "proposed_title": proposed["title"],
        "image_overlap": sorted(original_images & proposed_images),
        "sku_overlap": sorted(original_skus & proposed_skus),
        "original_image_count": len(original_images),
        "proposed_image_count": len(proposed_images),
    })
(root / "parallel-live-products.json").write_text(json.dumps(pairs, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"paired_rows": len(pairs), "different_product_ids": sum(not p["same_product_id"] for p in pairs), "shared_image_pairs": sum(bool(p["image_overlap"]) for p in pairs), "shared_sku_pairs": sum(bool(p["sku_overlap"]) for p in pairs)}))
print(json.dumps([{"row": p["row"], "image_overlap": len(p["image_overlap"]), "sku_overlap": len(p["sku_overlap"])} for p in pairs]))
