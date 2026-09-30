"""Compare proposed slugs, headings and metadata with current product facts."""
import gzip
import html
import json
import re
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
with gzip.open(root / 'source-sheet.json.gz', 'rt', encoding='utf-8') as file:
    sheet = json.load(file)['values']
with gzip.open(root / 'catalog.json.gz', 'rt', encoding='utf-8') as file:
    catalog = {p['handle']: p for p in json.load(file)['products']}

def tokens(value):
    value = value.lower().replace('’', '').replace("'", '')
    value = re.sub(r'(?<![a-z])t-shirt', 'tshirt', value)
    return re.findall(r'[a-z0-9]+', value)

def attrs(product):
    if not product:
        return {}
    output = {}
    for item in re.findall(r'<li\b[^>]*>(.*?)</li>', product.get('body_html') or '', flags=re.I | re.S):
        item = html.unescape(re.sub(r'<[^>]+>', '', item)).strip()
        if ':' in item:
            key, value = item.split(':', 1)
            output[key.strip().upper()] = value.strip()
    return output

issues = []
records = []
for rownum, row in enumerate(sheet[1:], 2):
    source, proposed, h1, title, description = row[:5]
    old_handle = source.split('/products/')[-1]
    new_handle = proposed.split('/products/')[-1]
    product = catalog.get(old_handle)
    values = attrs(product)
    url_tokens = tokens(new_handle)
    h1_tokens = tokens(h1)
    heading_mismatch = url_tokens != h1_tokens
    title_mismatch = h1 != re.sub(r'\s*\|\s*Cottonworld\s*$', '', title).strip()
    record = {
        'row': rownum, 'source_url': source, 'proposed_url': proposed,
        'h1': h1, 'meta_title': title, 'meta_description': description,
        'source_in_catalog': product is not None,
        'proposed_handle_in_catalog': new_handle in catalog,
        'product_title': product.get('title') if product else None,
        'attributes': values,
        'tags': product.get('tags') if product else [],
        'url_h1_mismatch': heading_mismatch,
        'h1_title_mismatch': title_mismatch,
        'only_in_url': [x for x in url_tokens if x not in h1_tokens],
        'only_in_h1': [x for x in h1_tokens if x not in url_tokens],
    }
    records.append(record)
    if heading_mismatch or title_mismatch:
        issues.append(record)

report = {
    'source': 'Boltworks sheet and Cottonworld public Shopify product catalog',
    'rows': len(records),
    'source_handles_found': sum(r['source_in_catalog'] for r in records),
    'proposed_handles_found': sum(r['proposed_handle_in_catalog'] for r in records),
    'url_h1_mismatches': sum(r['url_h1_mismatch'] for r in records),
    'h1_title_mismatches': sum(r['h1_title_mismatch'] for r in records),
    'duplicate_proposed_url_groups': sum(n > 1 for n in Counter(r['proposed_url'] for r in records).values()),
    'issues': issues,
}
(root / 'alignment-audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in report.items() if key != 'issues'}))
