import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHEET_ID = '1IlMiV6ccSfYyngMLuWyrEd3HD94wP4hbwcWQhOPnqcw'
GID = '1979343695'
with gzip.open(ROOT / 'source-sheet.json.gz', 'rt', encoding='utf-8') as source_file:
    rows = json.load(source_file)['values']
groups = json.loads((ROOT / 'parsed-groups.json').read_text(encoding='utf-8'))['groups']
with gzip.open(ROOT / 'public-catalog.json.gz', 'rt', encoding='utf-8') as catalog_file:
    catalog = {p['handle']: p for p in json.load(catalog_file)['products']}

def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()

def features(attrs, tags=()):
    a = {k: clean(v).upper() for k, v in attrs.items()}
    out = []
    def add(s):
        if s and s not in out:
            out.append(s)
    neck = a.get('NECKCOLLOR', '')
    if neck and neck not in {'NA', 'N/A'}:
        add(neck.title().replace('V Neck', 'V-Neck').replace('Round Neck', 'Round Neck'))
    pattern = a.get('PRINT', '')
    if pattern == 'STRIPE': add('Striped')
    elif pattern == 'CHECK': add('Checked')
    elif pattern == 'PRINT': add('Printed')
    elif pattern == 'SOLID': add('Solid')
    sleeve = a.get('SLEEVE', '')
    sleeve_map = {'SLEEVELESS':'Sleeveless', 'SHORT SLEEVE':'Short Sleeve', 'EXTENDED SHORT SLEEVE':'Extended Short Sleeve', 'HALF SLEEVE':'Half Sleeve', 'HALF SLEEVES':'Half Sleeve', '3/4 SLEEVE':'Three-Quarter Sleeve', '3/4 SLEEVE WITH CUFF':'Cuffed Three-Quarter Sleeve', 'FULL SLEEVE':'Full Sleeve', 'FULL SLEEVES':'Full Sleeve', 'EXTENDED LONG SLEEVE':'Extended Long Sleeve', 'EXTENDED SLEEVES':'Extended Sleeve'}
    add(sleeve_map.get(sleeve, sleeve.title() if sleeve else ''))
    pocket = a.get('POCKET', '')
    pocket_map = {'FRONT POCKET':'Front Pocket','ONE POCKET':'Chest Pocket','ONE  POCKET':'Chest Pocket','2 FRONT POCKETS':'Two Front Pockets','2 FLAP POCKETS':'Two Flap Pockets','PATCH POCKETS':'Patch Pockets','SIDE SEAM POCKETS':'Side Pockets','SIDE SEAM AND BACK POCKETS':'Side and Back Pockets'}
    add(pocket_map.get(pocket, ''))
    if pocket == 'NO POCKETS' and a.get('TYPE','') in {'PANTS','PANT','PYJAMA'}: add('No Pockets')
    opening = a.get('OPENING', '')
    opening_map = {'BUTTON FRONT':'Button Front','FRONT OPEN':'Front Open','HALF OPEN WITH BUTTONS':'Half Button Placket','HALF OPEN WITH 02 BUTTONS':'Two-Button Placket','HALF OPEN':'Half Button Placket','REGULAR PLACKET':'Button Placket','FOLDED PLACKET':'Folded Placket','DETAILED PLACKET':'Detailed Placket','CONCEALED PLACKET':'Concealed Placket','EMBROIDERED FRONT':'Embroidered Front','FRONT YOKE':'Front Yoke','FRONT MOCK BUTTONS':'Mock Buttons','SIDE BUTTONS':'Side Buttons','ZIP FLY':'Zip Fly','BUTTON AND ZIP':'Button and Zip','DRAWSTRING':'Drawstring Waist','DRAWSTRING WITH ELASTIC':'Drawstring Elastic Waist','ELASTIC':'Elastic Waist','PULL ON':'Pull-On','PULL ON WITH BUTTON DETAIL':'Button-Detail Pullover'}
    add(opening_map.get(opening, ''))
    hem = a.get('HEMLINE', '')
    hem_map = {'CURVED HEM':'Curved Hem','ROUND HEM':'Round Hem','STRAIGHT HEM':'Straight Hem','STRAIGHT BOTTOM':'Straight Hem','STRAIGHT WITH SIDE SLIT':'Side-Slit Hem','STRAIGHT HEM WITH SLITS':'Side-Slit Hem','STRAIGHT HEM WITH BUTTON TAB':'Button-Tab Hem','ELASTICATED HEM':'Elasticated Hem','ASSYMETRIC HEMLINE':'Asymmetric Hem'}
    add(hem_map.get(hem, ''))
    composition = a.get('FABRIC COMPOSITION', '')
    if composition.startswith('50% LINEN 50% COTTON'): add('Equal Linen Cotton Blend')
    elif composition.startswith('60% LINEN 40% COTTON'): add('Linen-Rich Blend')
    elif composition.startswith('80% COTTON 20% LINEN'): add('Cotton-Rich Blend')
    elif composition.startswith('50% COTTON 50% LINEN'): add('Equal Cotton Linen Blend')
    tagset = {str(t).upper() for t in tags}
    for tag,label in [('BARREL LEG','Barrel Leg'),('STRAIGHT LEG','Straight Leg'),('ANKLE LENGTH','Ankle Length'),('FULL LENGTH','Full Length'),('REGULAR LENGTH','Regular Length'),('FOLDED HEM','Folded Hem')]:
        if tag in tagset: add(label)
    if 'HS' in tagset: add('Half Sleeve')
    if 'FS' in tagset: add('Full Sleeve')
    return out

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

plan = []
unresolved = []
for url, items in groups.items():
    enriched = [(x, features(x.get('attrs') or {}, catalog.get(x['handle'],{}).get('tags') or ())) for x in items]
    chosen = {}
    for x, fs in enriched:
        if not x['found'] or not fs:
            unresolved.append({'row':x['row'],'reason':'Product details unavailable in current catalog','url':url})
            continue
        # Find the shortest feature phrase unique in this URL group; use a second
        # attribute only when one alone cannot distinguish the product.
        options = [(f,) for f in fs] + [(f,g) for i,f in enumerate(fs) for g in fs[i+1:]]
        others = [set(yfs) for y,yfs in enriched if y['row'] != x['row']]
        unique = [z for z in options if all(not set(z).issubset(o) for o in others)]
        if not unique:
            unresolved.append({'row':x['row'],'reason':'Catalog attributes do not distinguish this product from a sibling','url':url})
            continue
        # Prefer clear product attributes over generic hems/opening phrasing.
        selected = min(unique, key=lambda z:(len(z),sum(fs.index(t) for t in z),len(' '.join(z))))
        chosen[x['row']] = ' '.join(selected)
    for rownum, qualifier in chosen.items():
        old = rows[rownum-1]
        title = re.sub(r'\s+[–-]\s+.*?(?=\s*\| Cottonworld$)', '', old[2]).strip()
        title = re.sub(r'\s*\| Cottonworld$', '', title).strip()
        display_title = title.replace(' Tshirt ', ' T-Shirt ')
        if len(f'{display_title} – {qualifier} | Cottonworld') > 70:
            display_title = display_title.replace(' Regular Fit ', ' ')
        new_title = f'{display_title} – {qualifier} | Cottonworld'
        new_url = url.rstrip('/') + '-' + slug(qualifier)
        product = title.lower()
        detail = ('in a solid finish' if qualifier == 'Solid' else f'with {qualifier.lower()}')
        templates = [
            f'Explore Cottonworld’s {product} {detail}. A practical choice for everyday wear, weekends and travel.',
            f'Choose Cottonworld’s {product} {detail} for easy workdays, travel and relaxed weekends.',
            f'Bring Cottonworld’s {product} {detail} into an everyday wardrobe for work and time off.',
            f'Wear Cottonworld’s {product} {detail} through workdays, weekends and travel.',
        ]
        description = templates[rownum % len(templates)]
        plan.append({'row':rownum,'url':new_url,'title':new_title,'description':description,'qualifier':qualifier})

all_urls = [r[1] for r in rows[1:]]
for p in plan: all_urls[p['row']-2] = p['url']
url_dupes = {v:n for v,n in Counter(all_urls).items() if n>1}
title_dupes = {v:n for v,n in Counter((next((p['title'] for p in plan if p['row']==i),r[2]) for i,r in enumerate(rows[1:],2))).items() if n>1}
report = {'plan':plan,'unresolved':unresolved,'remaining_duplicate_urls':url_dupes,'remaining_duplicate_titles':title_dupes}
(ROOT/'plan.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'planned':len(plan),'unresolved':len(unresolved),'remaining_duplicate_url_groups':len(url_dupes),'remaining_duplicate_title_groups':len(title_dupes),'unresolved_rows':[x['row'] for x in unresolved]},ensure_ascii=False))

# Prepare exact cell changes, retaining every source and feedback column.
current = {i: {'url':r[1], 'title':r[2], 'description':r[3]} for i,r in enumerate(rows[1:],2)}
updated = {i:dict(v) for i,v in current.items()}
for p in plan:
    updated[p['row']].update({k:p[k] for k in ('url','title','description')})

# The catalog identifies this tee as organic cotton, unlike its similarly named
# 100% cotton sibling. This corrects the underlying title/URL discrepancy.
updated[171].update({
    'url':'https://cottonworld.net/products/womens-organic-cotton-regular-fit-tshirt-ecru-melan',
    'title':'Women’s Organic Cotton T-Shirt Ecru Melan | Cottonworld',
    'description':'Explore Cottonworld’s women’s organic cotton regular fit t-shirt in ecru melan for everyday comfort at work, at home and while travelling.'
})
unresolved = [x for x in unresolved if x['row'] != 171]

# Remove generic editorial labels when the product title is unique without them.
generic = re.compile(r'\s+[–-]\s+(Everyday|Workday|Weekend|Travel|Classic|Essential|Casual|Daily)\s*\| Cottonworld$',re.I)
for rownum, item in updated.items():
    short = generic.sub(' | Cottonworld', item['title'])
    if short != item['title'] and all(other['title'] != short for n,other in updated.items() if n != rownum):
        item['title'] = short

# Rewrite residual verbatim duplicate descriptions without manufacturing a
# product feature. These remain source-safe, though unresolved products retain
# a review flag in column G.
description_groups = defaultdict(list)
for n,v in updated.items(): description_groups[v['description']].append(n)
for text, numbers in description_groups.items():
    if len(numbers) < 2: continue
    for index,rownum in enumerate(numbers[1:],1):
        base = re.sub(r'\s+[–-]\s+.*?(?=\s*\| Cottonworld$)', '', updated[rownum]['title'])
        base = re.sub(r'\s*\| Cottonworld$', '', base).lower()
        alternatives = [
            f'Explore Cottonworld’s {base} for comfortable workdays, weekends and travel.',
            f'Choose Cottonworld’s {base} for everyday wear, from work to relaxed weekends.',
            f'Bring Cottonworld’s {base} into your wardrobe for work, travel and unhurried days.',
            f'Wear Cottonworld’s {base} through workdays, travel and relaxed time at home.',
        ]
        used = {v['description'] for n,v in updated.items() if n != rownum}
        choice = next((candidate for candidate in alternatives[index%4:]+alternatives[:index%4] if candidate not in used),None)
        if choice: updated[rownum]['description'] = choice

unresolved_by_row = {x['row']:x for x in unresolved}
planned_rows = {x['row'] for x in plan}|{171}
cell_changes=[]
for rownum in range(2,len(rows)+1):
    for col,key in [(1,'url'),(2,'title'),(3,'description')]:
        if updated[rownum][key] != current[rownum][key]:
            cell_changes.append({'row':rownum,'column':col,'value':updated[rownum][key]})
    if rownum in planned_rows:
        cell_changes.append({'row':rownum,'column':7,'value':'Source-backed distinction drafted; publish URL on site before use'})
    elif rownum in unresolved_by_row:
        status = ('Source product unavailable; confirm active product and attributes' if 'unavailable' in unresolved_by_row[rownum]['reason'] else 'Needs verified distinguishing product detail before URL change')
        cell_changes.append({'row':rownum,'column':7,'value':status})
cell_changes.append({'row':1,'column':7,'value':'Review status'})
final_urls = Counter(v['url'] for v in updated.values())
final_titles = Counter(v['title'] for v in updated.values())
final_descriptions = Counter(v['description'] for v in updated.values())
output={'cell_changes':cell_changes,'summary':{'changed_cells':len(cell_changes),'planned_product_urls':len(planned_rows),'unresolved_rows':len(unresolved),'duplicate_url_groups':sum(v>1 for v in final_urls.values()),'duplicate_title_groups':sum(v>1 for v in final_titles.values()),'duplicate_description_groups':sum(v>1 for v in final_descriptions.values()),'numeric_codes_in_titles':sum(bool(re.search(r'\b\d{4,}\b',v['title'])) for v in updated.values()),'numeric_codes_in_descriptions':sum(bool(re.search(r'\b\d{4,}\b',v['description'])) for v in updated.values()),'generic_differentiator_titles':sum(bool(generic.search(v['title'])) for v in updated.values())},'remaining_duplicate_urls':{u:n for u,n in final_urls.items() if n>1},'unresolved':unresolved}
(ROOT/'sheet_updates.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(output['summary']))
