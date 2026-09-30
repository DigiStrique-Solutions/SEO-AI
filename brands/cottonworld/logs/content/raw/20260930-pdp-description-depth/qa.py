import json,re,collections
from pathlib import Path
R=Path(__file__).parent
rr=json.loads((R/'proposals.json').read_text(encoding='utf-8'))
checks=[]
for r in rr:
 t=r['after']; body=t.split('\n\nProduct ID:')[0]; intro=t.split('\n\n')[0]; s=r['facts']; problems=[]
 if t.split('\n\n')[-1]!='Product ID: '+r['code']: problems.append('product_id')
 if len(t.split('\n\n'))!=4: problems.append('paragraph_structure')
 if len(re.findall(r'(?<!\w)'+re.escape(s['colour'])+r'(?!\w)',body,re.I))!=1: problems.append('repeated_colour')
 for f in ['cotton','linen','elastane','lycra','bamboo','polyester','viscose','modal','lyocell','polyamide','excel','lurex','flax']:
  if len(re.findall(r'\b'+f+r'\b',body,re.I))>1: problems.append('repeated_fibre_'+f)
 if re.search(r'\b(\w+)\s+\1\b',body,re.I): problems.append('adjacent_repeated_word')
 if re.search(r'\ba (?:off-white|elasticated|open|oversized)',body): problems.append('article')
 if s['noun']=='skirt' and 'legs' in body: problems.append('skirt_legs')
 if s['noun'] in ['trousers','shorts','tights','culottes','track pants'] and re.search(r'(?:Pair|Wear|Try) them with (?:an? |plain )?(?:off-white |navy )?(?:trousers|shorts|jeans|culottes)',body): problems.append('bottom_with_bottom')
 if any(x in body for x in ['considered, easy-to-style foundation','timeless addition','without adding fuss','effortless comfort','Construction details include','darkoliveg','white a shirt']): problems.append('stock_or_raw_copy')
 if not 100 <= r['words'] <= 140: problems.append('body_length')
 if s['fabric'] not in body: problems.append('fabric_not_preserved')
 checks.append({'batch':r['batch'],'row':r['row'],'code':r['code'],'status':'pass' if not problems else 'fail','problems':problems,'evidence':'proposals.json; ../20260930-pdp-batches234-review/records.json product export and exact product-code/handle match','scope':'editorial and automated consistency QA; not an external AI-detector test'})
dups=collections.defaultdict(list)
for r in rr: dups[r['after'].split('\n\nProduct ID:')[0]].append([r['batch'],r['row']])
result={'rows':len(rr),'failed':[r for r in checks if r['problems']],'exact_duplicate_bodies':[v for v in dups.values() if len(v)>1],'checks':checks}
(R/'editorial-qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False,indent=2))
