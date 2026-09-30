import json,hashlib
from pathlib import Path
R=Path(__file__).parent
run='20260930-pdp-batches234-review'
source=Path(r'C:\Users\User\Downloads\Cottonworld verify')
sources={'run_id':run,'brand':'cottonworld','date':'2026-09-30','source_export':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_status_scope':'Snapshot used for product facts; active scope selected from current sheet sections, not a live stock audit.','workbook':'https://docs.google.com/spreadsheets/d/1g8ZO-R-7CPX_v6AdBA56mH72ky2Q3fi4rGyjI9-LXyM/edit','benchmark':'Batch 1','guidance':['brands/cottonworld/context.md','brands/cottonworld/knowledge.md'],'feedback':['Batch 3!D2','Batch 3!D3','Batch 3!D5','Batch 3!D7'],'status':'editorial corrections complete','detector':'Not run; no publication-readiness claim','raw_refs':['before-batch1.json','before-batch2.json','before-batch3.json','before-batch4.json','records.json','proposals.json','editorial-qa.json','source-issues.json','verification.json','api-responses.json','review-document.json'],'review_document':'https://docs.google.com/document/d/1XgkjUV5sV_dYT4cJCSXJdzBGgEqzjLeZQg_ha-UscyE/edit'}
(R/'sources.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
log=R.parent.parent/'activity.jsonl'
entries=[{'run_id':run,'timestamp':'2026-09-30','category':'content','action':'read_pdp_batches_and_feedback','provider':'google_drive.get_spreadsheet_cells + local_product_export','status':'complete','raw_ref':'raw/'+run+'/sources.json'}, {'run_id':run,'timestamp':'2026-09-30','category':'content','action':'rewrite_active_pdp_descriptions','provider':'google_drive.batch_update_spreadsheet','status':'complete','updated_rows':333,'batch_order':[2,3,4],'counts':[135,116,82],'raw_ref':'raw/'+run+'/proposals.json'}, {'run_id':run,'timestamp':'2026-09-30','category':'content','action':'verify_pdp_readback_preservation_and_visual_layout','provider':'google_drive.get_spreadsheet_cells + cua_browser','status':'pass','updated_rows':333,'unexpected_changes':0,'raw_ref':'raw/'+run+'/verification.json'}, {'run_id':run,'timestamp':'2026-09-30','category':'content','action':'create_pdp_review_google_doc','provider':'google_drive.create_file + batch_update_document','status':'complete','output_url':sources['review_document'],'raw_ref':'raw/'+run+'/review-document.json'}]
existing=log.read_text(encoding='utf-8')
if run not in existing:
 with log.open('a',encoding='utf-8') as f:
  for entry in entries:f.write(json.dumps(entry,separators=(',',':'))+'\n')
print('Sources and activity log saved.')
