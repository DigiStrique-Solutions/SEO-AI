import json,hashlib,statistics
from pathlib import Path
R=Path(__file__).parent
before=json.loads((R/'before-write.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData']
after=[]
for i in [0,1]:
 after+=json.loads((R/f'after-{i}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData']
after[23]['values'][2]=json.loads((R/'row24-final.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData'][0]['values'][0]
after[0]['values'][2]=json.loads((R/'header-final.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData'][0]['values'][2]
pp=json.loads((R/'proposals.json').read_text(encoding='utf-8'))
assert len(pp)==392 and len(before)==len(after)==393
for p in pp:
 i=p['row']-1;a=after[i]['values'];b=before[i]['values']
 assert a[2]['userEnteredValue']['stringValue']==p['after'],p['row']
 assert a[2]['userEnteredFormat']['wrapStrategy']=='WRAP',p['row']
 assert a[:2]==b[:2],p['row']
 assert len(b)<=2 or not b[2].get('userEnteredValue'),p['row']
assert after[0]['values'][2]['userEnteredValue']['stringValue']=='Updated PDP Description'
assert after[0]['values'][2]['userEnteredFormat']==after[0]['values'][1]['userEnteredFormat']
src=Path(r'C:\Users\User\Downloads\Cottonworld verify')
result={'run_id':'20261006-added-active-pdp','rows_written':392,'range':'Boltworks sheet!C2:C393','exact_readback':True,'source_columns_preserved':True,'header_style_matches_existing':True,'wrap_verified':True,'rendered_sheet_checked':True,'source_export_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'source_counts':{'product_export':388,'historical_merchant_variant':3,'url_only':1},'source_limitations':['C24 product export absent; linen and boxy fit come from supplied URL, no composition percentage stated.','C293:C295 export absent; earlier merchant variant attributes support their descriptions. Proposed URLs for all four unmatched products returned 404 during verification.'],'editorial_qa':'qa.json: zero flagged issues and zero exact duplicate description bodies.','google_doc':'https://docs.google.com/document/d/1CM7eTVio_zv0DcN1dcGfcr2BW1gwHxassON8GnQ7IyQ/edit'}
(R/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
