"""Create a private visual comparison of products with indistinct catalog attributes."""
import gzip
import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen

from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent
with gzip.open(root / 'source-sheet.json.gz', 'rt', encoding='utf-8') as file:
    rows = json.load(file)['values']
with gzip.open(root / 'catalog.json.gz', 'rt', encoding='utf-8') as file:
    catalog = {p['handle']: p for p in json.load(file)['products']}
groups = [[27, 28], [183, 213], [351, 356], [387, 393], [254, 260], [198, 200]]
selected = [row for group in groups for row in group]

def get_image(row):
    handle = rows[row - 1][0].split('/products/')[-1]
    product = catalog.get(handle)
    if not product or not product.get('images'):
        return row, None
    url = product['images'][0]['src'] + '&width=260'
    try:
        with urlopen(url, timeout=25) as response:
            image = Image.open(io.BytesIO(response.read())).convert('RGB')
        image.thumbnail((225, 250))
        return row, image
    except Exception:
        return row, None

with ThreadPoolExecutor(max_workers=6) as pool:
    images = dict(pool.map(get_image, selected))

width, height = 225, 280
canvas = Image.new('RGB', (width * 4, height * ((len(selected) + 3) // 4)), 'white')
draw = ImageDraw.Draw(canvas)
for index, row in enumerate(selected):
    x, y = (index % 4) * width, (index // 4) * height
    image = images[row]
    if image:
        canvas.paste(image, (x + (width - image.width) // 2, y))
    draw.text((x + 5, y + 254), f'Row {row}: {rows[row - 1][0].split("/products/")[-1]}', fill='black')
canvas.save(root / 'comparison.png')
print(json.dumps({'images_loaded': sum(image is not None for image in images.values()), 'selected': len(selected)}))
