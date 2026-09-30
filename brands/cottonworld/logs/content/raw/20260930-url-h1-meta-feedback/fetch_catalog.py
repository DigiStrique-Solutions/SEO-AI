"""Capture Cottonworld's public Shopify catalog for row-level SEO fact checks."""
import gzip
import json
from pathlib import Path
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parent
pages = []
products = []
for page in range(1, 20):
    url = f'https://cottonworld.net/products.json?limit=250&page={page}'
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0 SEO fact check'})
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
    current = payload.get('products', [])
    pages.append({'url': url, 'count': len(current)})
    products.extend(current)
    if len(current) < 250:
        break
out = {'source': 'Cottonworld public Shopify products.json', 'pages': pages, 'products': products}
with gzip.open(root / 'catalog.json.gz', 'wt', encoding='utf-8') as file:
    json.dump(out, file, ensure_ascii=False, separators=(',', ':'))
print(json.dumps({'pages': pages, 'products': len(products)}))
