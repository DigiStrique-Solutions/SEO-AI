"""Render source and occupied proposed-handle product images side by side."""
import gzip
import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parent
sheet=json.load(gzip.open(root/"source-sheet.json.gz","rt",encoding="utf-8"))["values"]
catalog={p["handle"]:p for p in json.load(gzip.open(root/"catalog.json.gz","rt",encoding="utf-8"))["products"]}
rows=[8,69,87,207,232,354,370]
selected=[(row,kind) for row in rows for kind in ["source","occupied"]]
def fetch(item):
    row,kind=item
    url=sheet[row-1][0 if kind=="source" else 1]
    p=catalog.get(url.split("/products/")[-1])
    if not p or not p.get("images"): return item,None
    imgurl=p["images"][0]["src"]+"&width=360"
    try:
        with urlopen(imgurl,timeout=25) as response:
            im=Image.open(io.BytesIO(response.read())).convert("RGB")
        im.thumbnail((270,310))
        return item,im
    except Exception:
        return item,None
with ThreadPoolExecutor(max_workers=6) as pool:
    images=dict(pool.map(fetch,selected))
w,h=270,340
canvas=Image.new("RGB",(w*4,h*((len(selected)+3)//4)),"white")
draw=ImageDraw.Draw(canvas)
for i,item in enumerate(selected):
    x,y=(i%4)*w,(i//4)*h
    im=images[item]
    if im: canvas.paste(im,(x+(w-im.width)//2,y))
    draw.text((x+8,y+315),f"Row {item[0]} {item[1]}",fill="black")
canvas.save(root/"occupied-comparison.png")
print(json.dumps({"images_loaded":sum(x is not None for x in images.values()),"selected":len(selected)}))
