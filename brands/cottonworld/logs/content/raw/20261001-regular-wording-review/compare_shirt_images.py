"""Visual QA of source shirts and print differentiators."""
import gzip, io, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parent
rows=json.load(gzip.open(root/"source-sheet.json.gz","rt",encoding="utf-8"))["values"]
catalog={p["handle"]:p for p in json.load(gzip.open(root.parent/"20261001-url-h1-meta-reaudit"/"catalog.json.gz","rt",encoding="utf-8"))["products"]}
selected=[260,262,272,280,291,292,302,303,310,318,353]
def fetch(row):
    product=catalog.get(rows[row-1][0].split("/products/")[-1])
    if not product or not product.get("images"):return row,None
    url=product["images"][0]["src"]+"&width=300"
    try:
        with urlopen(url,timeout=20) as response:im=Image.open(io.BytesIO(response.read())).convert("RGB")
        im.thumbnail((240,280));return row,im
    except Exception:return row,None
with ThreadPoolExecutor(max_workers=6) as pool:images=dict(pool.map(fetch,selected))
w,h=240,310
canvas=Image.new("RGB",(w*4,h*((len(selected)+3)//4)),"white")
draw=ImageDraw.Draw(canvas)
for i,row in enumerate(selected):
    x,y=(i%4)*w,(i//4)*h
    im=images[row]
    if im:canvas.paste(im,(x+(w-im.width)//2,y))
    draw.text((x+5,y+285),f"Row {row}",fill="black")
canvas.save(root/"shirt-print-comparison.png")
print(json.dumps({"loaded":sum(x is not None for x in images.values()),"selected":len(selected)}))
