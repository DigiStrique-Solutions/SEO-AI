"""Create a contact sheet for the variant groups with print-based names."""

import concurrent.futures
import io
import json
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent
groups = json.loads((root / "variant-groups.json").read_text(encoding="utf-8"))
keys = {
    "l-blouse-17863-21693",
    "l-blouse-17943-21557",
    "l-tshirt-17553-21628",
    "m-shirts-13484-21611",
    "m-shirts-13484-21732",
    "m-shirts-50019-21704",
    "m-tshirt-15906-21725",
}
items = [v for group in groups if group["group"] in keys for v in group["variants"]]


def fetch(item):
    try:
        data = urllib.request.urlopen(item["image"], timeout=30).read()
        image = Image.open(io.BytesIO(data)).convert("RGB")
        return item, image
    except Exception as exc:
        return item, str(exc)


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(fetch, items))
width, height = 210, 270
sheet = Image.new("RGB", (width * 5, height * ((len(results) + 4) // 5)), "white")
draw = ImageDraw.Draw(sheet)
for index, (item, result) in enumerate(results):
    x, y = index % 5 * width, index // 5 * height
    if isinstance(result, Image.Image):
        result.thumbnail((width - 8, height - 42))
        sheet.paste(result, (x + (width - result.width) // 2, y))
    else:
        draw.text((x + 4, y + 25), "IMAGE ERROR", fill="red")
    draw.text((x + 4, y + height - 38), f"Row {item['row']} {item['original_color']}", fill="black")
    draw.text((x + 4, y + height - 21), item["original_handle"].split("-")[-2], fill="black")
sheet.save(root / "print-variant-comparison.jpg", quality=88)
print(json.dumps({"images": len(results), "errors": [item["row"] for item, result in results if not isinstance(result, Image.Image)]}))
