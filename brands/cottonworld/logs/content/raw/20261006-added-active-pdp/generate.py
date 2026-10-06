"""Build source-backed descriptions for the added Cottonworld product list."""
import json, re, html, statistics, collections, copy
from pathlib import Path

R = Path(__file__).parent
PRIOR = R.parent / '20260930-pdp-batches234-review' / 'rewrite.py'
DEPTH = R.parent / '20260930-pdp-description-depth' / 'expand.py'
rows = json.loads((R/'records.json').read_text(encoding='utf-8'))

# Load the established editorial vocabulary without executing either older run.
core = {'__file__': str(PRIOR)}
exec(PRIOR.read_text(encoding='utf-8').split('proposals=')[0], core)
depth = {'__file__': str(DEPTH)}
exec(DEPTH.read_text(encoding='utf-8').split('out=[]')[0], depth)
depth['records'] = {(5,r['row']):r for r in rows}
core['types'].update({'JUMPSUIT':'jumpsuit','JUMPSUITS':'jumpsuit','KVEST':'vest','KVESTS':'vest'})
core['neck'].update({'MANDARIN COLLAR':'a mandarin collar','BOAT NECK':'a boat neckline','LAPEL COLLAR':'a lapel collar'})

variant = json.loads((R.parent/'20261005-variant-consistency'/'variant-groups.json').read_text(encoding='utf-8'))
variant_groups = variant.get('groups',variant) if isinstance(variant,dict) else variant
if not isinstance(variant_groups,list): variant_groups=[]
group_map = {g.get('group'):g for g in variant_groups}

def hydrate(p, row):
    p=copy.deepcopy(p)
    body=core['getbody'](p)
    fabric=core['meta'](p,'Fabric Composition')
    if not fabric:
        fabric=body.get('FABRIC COMPOSITION','')
    if not fabric:
        # A few legacy descriptions lack structured fields; use only explicit title facts.
        m=re.search(r'\b(\d+%\s+(?:cotton|linen|viscose|modal|bamboo|elastane))\b',p['Title'],re.I)
        if m:fabric=m.group(1)
    p['Fabric Composition (product.metafields.custom.fabric_composition)']=fabric
    if not core['meta'](p,'Woven or Knit '):
        mode='Knit' if re.search(r'\bKNIT\b',body.get('FABRIC COMPOSITION',''),re.I) else 'Woven' if re.search(r'\bWOVEN\b',body.get('FABRIC COMPOSITION',''),re.I) else ''
        p['Woven or Knit  (product.metafields.custom.woven_or_knit)']=mode
    if not body.get('TYPE') and not core['meta'](p,'Product Type'):
        p['Product Type (product.metafields.custom.product_type)']=row['code'].split('-')[1].upper()
    if not body.get('FIT TYPE') and not core['meta'](p,'Fit Type'):
        m=re.search(r'\b(regular|slim|boxy|relaxed|loose)\s+fit\b',p['Title'],re.I)
        if m:p['Fit Type (product.metafields.custom.fit_type)']=m.group(0)
    return p

def manual_facts(row):
    code=row['code'];slug=row['updated_url'].split('/')[-1]
    # The four missing products have no current page or full product export.
    # Three shirt variants have earlier merchant attributes; the blouse has URL facts only.
    gender='women' if code.startswith('l-') else 'men'
    noun='blouse' if 'blouse' in slug else 'shirt'
    colour=code.split('-')[-1]
    fabric='linen' if 'linen' in slug else '100% cotton' if 'cotton' in slug else ''
    fit='boxy fit' if 'boxy-fit' in slug else 'regular fit' if 'regular-fit' in slug else ''
    assert fabric and fit
    g=group_map.get('-'.join(code.split('-')[:-1]))
    merchant=next((v.get('merchant_attributes',{}) for v in g.get('variants',[]) if v.get('row')==row['row']),{}) if g else {}
    return dict(noun=noun,gender=gender,colour=colour,fabric=fabric,fit=fit,pattern=merchant.get('PRINT',''),attr={'neck':merchant.get('NECKCOLLOR',''),'sleeve':merchant.get('SLEEVE',''),'opening':merchant.get('OPENING',''),'hem':merchant.get('HEMLINE',''),'pocket':merchant.get('POCKET',''),'waist':'','leg':''},knit=False),('merchant_variant' if merchant else 'url_only')

def copy_for(row,facts,source_kind):
    n=facts['noun'];gender=facts['gender'];c=facts['colour'];plural=n in ['trousers','shorts','culottes','pyjama bottoms','track pants']
    if n in ['jumpsuit','vest']:
        moment=['For a simple daytime outfit','For plans that move from morning to evening','For a day built around familiar pieces','For a relaxed change from usual separates'][row['row']%4]
        first=f"{moment}, this {gender}'s {c} {n} has a {facts['fit']}."
        textile='knit' if facts['knit'] else 'woven'
        intro=f"{first} The {textile} fabric is {facts['fabric']}. The shape leaves room for simple styling choices."
        a=facts['attr'];details=[]
        if a['neck'] in core['neck']:details.append('It has '+core['neck'][a['neck']]+'.')
        if a['sleeve'] in core['sleeves']:details.append('The design has '+core['sleeves'][a['sleeve']]+'.')
        if a['pocket'] in core['pockets']:details.append('It includes '+core['pockets'][a['pocket']]+'.')
        if a['opening'] in core['openings']:details.append('It has '+core['openings'][a['opening']]+'.')
        if a['hem'] in core['hems']:details.append('The shape finishes with '+core['hems'][a['hem']]+'.')
        details=' '.join(details)
        if n=='jumpsuit':style='Wear it with flat sandals and a shoulder bag for daytime plans. Add an open shirt when you want another layer. For an evening out, switch to loafers and keep jewellery simple so the shape remains the focus.'
        else:style='Wear it over a plain T-shirt with straight trousers and trainers for a day off. A shirt and loafers offer another combination for lunch or an informal workday. Keep the layer beneath it simple so the neckline stays visible.'
    else:
        pseudo={'batch':5,'row':row['row'],'code':row['code'],'url':row['updated_url'],'old':'','comment':'','product':row['product']}
        if row['product']:
            try:base=core['rewrite'](pseudo)
            except ValueError as e:
                if 'no details' not in str(e):raise
                base={'batch':5,'row':row['row'],'facts':facts,'after':'\n\nThe product export does not provide further construction details.\n\n'}
            base['facts']=facts
            intro=depth['intro'](base)
            details=base['after'].split('\n\n')[1].replace('The shape is finished with','The design finishes with')
            style=depth['styling'](base)
        else:
            v=row['row']%4;moment=['For a day that may take you from work to lunch','For easy plans through the day','For a simple change from familiar separates','For a day when dressing can stay straightforward'][v]
            intro=f"{moment}, this {gender}'s {c} {n} has a {facts['fit']}. The fabric is {facts['fabric']}. Its familiar shape is simple to wear with pieces already in your wardrobe."
            details=''
            style=depth['styling']({'batch':5,'row':row['row'],'facts':facts})
    if facts['fit']=='a line':intro=intro.replace('offers a a line','has an A-line shape')
    if facts['pattern']=='DOBBY':intro=intro.replace('The solid finish is easy to coordinate with the rest of your wardrobe.','The dobby texture adds a quiet detail to the fabric.')
    if not facts['pattern']:intro=intro.replace('The solid finish is easy to coordinate with the rest of your wardrobe.','The colour works with familiar pieces for everyday dressing.')
    if source_kind=='url_only':
        details='The simple silhouette leaves room for patterned separates or a quieter tonal combination. Wear it on its own or beneath an open layer when the day calls for one.'
    if source_kind=='merchant_variant' and any(facts['attr'].values()):
        a=facts['attr'];parts=[]
        if a['neck'] in core['neck']:parts.append('It has '+core['neck'][a['neck']]+'.')
        if a['sleeve'] in core['sleeves']:parts.append('The design has '+core['sleeves'][a['sleeve']]+'.')
        if a['opening'] in core['openings']:parts.append('The front has '+core['openings'][a['opening']]+'.')
        if a['pocket'] in core['pockets']:parts.append('It includes '+core['pockets'][a['pocket']]+'.')
        if a['hem'] in core['hems']:parts.append('The shape finishes with '+core['hems'][a['hem']]+'.')
        details=' '.join(parts)
    p=row['product']
    if p:
        raw=html.unescape(re.sub('<[^>]+>',' ',p['Body (HTML)'])).lower()
        if 'hand wash' in raw:care='Hand wash separately; do not bleach. Remove promptly and dry in the shade.'
        elif 'machine wash cold' in raw:
            care='Machine wash cold and wash dark colours separately.'
            if 'no bleach' in raw:care+=' Do not bleach; remove promptly and dry in the shade.'
        else:care=''
        if care:details+=' '+care
    if 'The product export does not provide further construction details.' in details:
        details=details.replace('The product export does not provide further construction details.','').strip()
    if not details:details='The regular fit gives the garment a straightforward outline for everyday combinations.'
    result='\n\n'.join([intro,details,'Styling note - '+style,'Product ID: '+row['code']])
    return result

proposals=[];issues=[]
for row in rows:
    row=dict(row,batch=5,url=row['updated_url'],old='',comment='')
    if row['product']:
        row['product']=hydrate(row['product'],row)
        try:
            facts=core['source'](row);source_kind='product_export'
        except Exception as e:
            issues.append({'row':row['row'],'code':row['code'],'error':str(e)})
            continue
    else:facts,source_kind=manual_facts(row)
    after=copy_for(row,facts,source_kind)
    proposals.append({'row':row['row'],'code':row['code'],'url':row['updated_url'],'after':after,'facts':facts,'source_kind':source_kind,'words':len(after.split('Product ID:')[0].split())})
(R/'proposals.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'generation-issues.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
print('proposals',len(proposals),'issues',len(issues),'source_kinds',dict(collections.Counter(x['source_kind'] for x in proposals)))
if proposals:print('words',min(x['words'] for x in proposals),statistics.median(x['words'] for x in proposals),max(x['words'] for x in proposals))
print(issues[:20])
