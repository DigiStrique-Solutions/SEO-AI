import json,re,collections,html
from pathlib import Path
R=Path(__file__).parent
rs=json.loads((R/'records.json').read_text(encoding='utf-8'))
def body(r):
 return dict((html.unescape(re.sub('<[^>]+>','',a)).strip().upper(),html.unescape(re.sub('<[^>]+>','',b)).strip()) for a,b in re.findall(r'<li[^>]*>\s*(.*?):(.*?)</li>',r['product']['Body (HTML)'],re.S))
for b in [2,3,4]:
 rr=[r for r in rs if r['batch']==b]
 print('BATCH',b)
 for k in ['TYPE','PRINT','FABRIC COMPOSITION','NECKCOLLOR','SLEEVE','OPENING','HEMLINE','POCKET','WAIST','LEG']:
  vals=collections.Counter(body(r).get(k,'') for r in rr)
  print(k,dict(vals))
groups=collections.defaultdict(list)
for r in rs: groups[r['product']['Handle']].append([r['batch'],r['row'],r['code']])
print('DUPLICATES',json.dumps([v for v in groups.values() if len(v)>1]))
for b in [2,3,4]:
 text=[]
 for r in rs:
  if r['batch']==b:
   p=r['product']; facts=body(r)
   text.append(str(r['row'])+' | '+r['code']+' | '+p['Title']+' | '+json.dumps(facts,ensure_ascii=False))
 (R/f'facts-batch{b}.txt').write_text('\n'.join(text),encoding='utf-8')
