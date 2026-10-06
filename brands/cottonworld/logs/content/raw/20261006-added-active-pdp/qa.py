import json,re,collections,statistics
from pathlib import Path
R=Path(__file__).parent
rr=json.loads((R/'proposals.json').read_text(encoding='utf-8'))
assert len(rr)==392 and len({r['row'] for r in rr})==392 and len({r['code'] for r in rr})==392
issues=[]
bodies=collections.defaultdict(list)
for r in rr:
 t=r['after'];body=t.split('\n\nProduct ID:')[0];s=r['facts'];err=[]
 if len(t.split('\n\n'))!=4:err.append('paragraph_count')
 if t.split('\n\n')[-1]!='Product ID: '+r['code']:err.append('product_id')
 if s['fabric'] not in body:err.append('fabric')
 if f"{s['gender']}'s" not in body:err.append('gender')
 if len(re.findall(r'\b'+re.escape(s['colour'])+r'\b',body,re.I))!=1:err.append('repeated_colour')
 for fibre in ['cotton','linen','viscose','modal','bamboo','lycra','elastane','polyester','lyocell','tencel']:
  if len(re.findall(r'\b'+fibre+r'\b',body,re.I))>1:err.append('repeated_'+fibre)
 if re.search(r'\b(\w+)\s+\1\b',body,re.I):err.append('adjacent_repeated_word')
 if any(x in body.lower() for x in ['product export','product listing','needs confirmation','100% sustainable','best quality','unmatched comfort']):err.append('internal_or_unsupported')
 if re.search(r'\ba a\b',body,re.I):err.append('article')
 if s['noun'] in ['trousers','shorts','culottes','pyjama bottoms'] and re.search(r'\b(?:Pair|Wear|Try) them with (?:an? |plain )?(?:off-white |navy )?(?:trousers|shorts|jeans|culottes)',body):err.append('bottom_with_bottom')
 if r['source_kind']=='product_export' and not 85<=r['words']<=140:err.append('depth')
 if err:issues.append({'row':r['row'],'code':r['code'],'problems':err})
 bodies[body].append(r['row'])
result={'rows':len(rr),'source_counts':dict(collections.Counter(r['source_kind'] for r in rr)),'body_words':{'min':min(x['words'] for x in rr),'median':statistics.median(x['words'] for x in rr),'max':max(x['words'] for x in rr)},'issues':issues,'duplicate_bodies':[v for v in bodies.values() if len(v)>1]}
(R/'qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
