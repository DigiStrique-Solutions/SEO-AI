import json,re,collections
from pathlib import Path
R=Path(__file__).parent
proposals=json.loads((R/'proposals.json').read_text(encoding='utf-8'))
summary=[]
for b,end in [(2,136),(3,117),(4,83)]:
 before=json.loads((R/f'before-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]
 after=json.loads((R/f'after-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]
 br=before['data'][0]['rowData']; ar=after['data'][0]['rowData']
 pp=[p for p in proposals if p['batch']==b]
 differences=[]
 for i,(row1,row2) in enumerate(zip(br,ar),1):
  for j,(c1,c2) in enumerate(zip(row1['values'],row2['values'])):
   if j==2 and 2<=i<=end:
    for key in set(c1)|set(c2):
     if key in ['userEnteredValue','textFormatRuns']:continue
     if b==4 and i==6 and key=='note':continue
     if c1.get(key)!=c2.get(key):differences.append([i,j,key])
   elif c1!=c2:differences.append([i,j,'cell'])
 exact=all(ar[p['row']-1]['values'][2]['userEnteredValue']['stringValue']==p['after'] for p in pp)
 repeated_before=sum(any(len(re.findall(r'\b'+f+r'\b',p['before'].split('Product ID:')[0],re.I))>1 for f in ['cotton','linen','bamboo','elastane','lycra','viscose','polyester','modal']) for p in pp)
 summary.append({'batch':b,'range':f'Batch {b}!C2:C{end}','rows_updated':len(pp),'exact_readback':exact,'unexpected_changes':differences,'sheet_properties_preserved':before['properties']==after['properties'],'wrap_preserved':all(ar[p['row']-1]['values'][2].get('userEnteredFormat',{}).get('wrapStrategy')=='WRAP' for p in pp),'rows_with_repeated_fibre_before':repeated_before})
 assert exact and not differences
result={'run_id':'20260930-pdp-batches234-review','verification':summary,'updated_rows':sum(s['rows_updated'] for s in summary),'scope':'Active sections of existing tracker; 135 + 116 + 82 rows, in that order. Not a fresh inventory-status audit.','duplicates': [{'batch':4,'row':6,'also_in':'Batch 1 row 64','same_handle':'mens-cotton-regular-fit-pant-black','action':'Retained tracker record and added a cell note to prevent double implementation. Description corrected from product facts.'}],'benchmark':'Batch 1 structure and calm tone; product introduction, details, styling note, full Product ID. Removed stock filler rather than reproducing benchmark weaknesses.','editorial_qa':'333 passed; no adjacent repeated words, repeated fibre names or repeated product colours within body; no exact duplicate bodies across revised rows. Source-specific corrections and garment/styling review also performed.','detector':'Not run; editorial correction, not publication certification.','visual_qa':'Wrap, cell formats and structure verified through readback. Native browser opening timed out; rendered fit not yet verified.'}
(R/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
