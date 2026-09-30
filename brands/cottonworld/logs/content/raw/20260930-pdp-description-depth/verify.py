import json,statistics,itertools
from pathlib import Path
R=Path(__file__).parent
pp=json.loads((R/'proposals.json').read_text(encoding='utf-8'))
results=[]
for b in [1,2,3,4]:
 before=json.loads((R/f'before-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]
 after=json.loads((R/f'after-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]
 br=before['data'][0]['rowData'];ar=after['data'][0]['rowData']
 if b==3:
  ar[21]['values'][2]=json.loads((R/'after-preserved-highlight.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData'][0]['values'][0]
 expected={x['row']:x for x in pp if x['batch']==b}
 problems=[]
 for row,(a,z) in enumerate(itertools.zip_longest(br,ar,fillvalue={}),1):
  for col,(c,d) in enumerate(itertools.zip_longest(a.get('values',[]),z.get('values',[]),fillvalue={})):
   if col==2 and row in expected:
    assert d['userEnteredValue']['stringValue']==expected[row]['after'],(b,row,'copy differs')
    assert c['userEnteredValue']['stringValue']==expected[row]['before'],(b,row,'baseline differs')
    if b==3 and row==22:
     oldruns=c['textFormatRuns'];newruns=d['textFormatRuns']
     assert oldruns[-1]['format']==newruns[-1]['format']
     assert expected[row]['before'][oldruns[-1]['startIndex']:]==expected[row]['after'][newruns[-1]['startIndex']:]=='gree'
     c=dict(c,textFormatRuns=newruns)
    c={k:v for k,v in c.items() if k!='userEnteredValue'}
    d={k:v for k,v in d.items() if k!='userEnteredValue'}
   if c!=d:problems.append([row,col])
 assert not problems,(b,problems)
 assert before['properties']==after['properties']
 lengths=[x['words'] for x in expected.values()]
 results.append({'batch':b,'rows_updated':len(expected),'exact_readback':True,'other_cell_fields_and_values_preserved':True,'properties_preserved':True,'body_word_count':{'min':min(lengths),'median':statistics.median(lengths),'max':max(lengths)} if lengths else 'unchanged benchmark'})
result={'run_id':'20260930-pdp-description-depth','rows':333,'verification':results,'source':'Product facts and care: ../20260930-pdp-batches234-review/records.json; benchmark: before-batch1.json','scope':'Active sections of tracker; not a fresh inventory status audit. Batch 4 C6 duplicate-product note retained. Batch 3 C22 existing red ID suffix retained at its new offset.','editorial_qa':'333 rows pass length, ID, fabric preservation, repeated fibre/colour, consecutive-word and exact-body duplicate checks.','detector':'Not run; editorial correction, no publish-ready certification.','visual_qa':{'status':'not_checked_blocked','reason':'Native browser navigation to docs.google.com timed out. Cell wrap and text/format preservation verified through connector readback.'}}
(R/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
