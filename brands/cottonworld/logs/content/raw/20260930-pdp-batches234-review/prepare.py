import csv,json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).parent
src=Path(r'C:\Users\User\Downloads\Cottonworld verify')
with src.open(encoding='utf-8-sig',newline='') as f: products=[r for r in csv.DictReader(f) if r['Title']]
def key(r,n):
    return next((v for k,v in r.items() if k.startswith(n+' (')), '')
bycode={key(p,'Style Code').lower():p for p in products if key(p,'Style Code')}
byhandle={p['Handle']:p for p in products}
records=[]
for b,end in [(1,151),(2,136),(3,117),(4,84)]:
    data=json.loads((ROOT/f'before-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData']
    for i,r in enumerate(data[1:end],2):
        vals=[c.get('userEnteredValue',{}).get('stringValue','') for c in r['values']]
        if not vals[0]: continue
        code,url,old=vals[:3]
        p=bycode.get(code.lower()) or byhandle.get(url.rsplit('/',1)[-1])
        records.append(dict(batch=b,row=i,code=code,url=url,old=old,comment=vals[3] if len(vals)>3 else '',product=p))
(ROOT/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'records':len(records),'unmatched':[{k:r[k] for k in ['batch','row','code','url']} for r in records if not r['product']],'statuses':{s:sum(r['product'] and r['product']['Status']==s for r in records) for s in ['active','draft','archived']}},indent=2))
for b in [2,3,4]:
    rr=[r for r in records if r['batch']==b]
    print('BATCH',b,'count',len(rr))
    for n in ['Fabric Composition','Fit Type','Neck Collar','Sleeve','Opening','Hemline','Pocket','Pockets','Leg','Waist','Fabric Print','Woven or Knit ']:
        print(n,sorted(set(key(r['product'],n) for r in rr if r['product'])))
