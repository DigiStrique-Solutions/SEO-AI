import collections, html, json, re
from pathlib import Path
R=Path(__file__).parent
rows=json.loads((R/'current.json').read_text(encoding='utf-8'))
records={x['row']:x for x in json.loads((R.parent/'20261006-added-active-pdp/records.json').read_text(encoding='utf-8'))}
fields_by_row={}
diff=[]
for x in rows:
    p=records[x['row']]['product']
    if not p:continue
    fields={re.sub(r'\s+',' ',k.strip().upper()):re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',v)).strip().upper()) for k,v in re.findall(r'<li>\s*([^:<]+):\s*(.*?)\s*</li>',p.get('Body (HTML)',''),re.I|re.S)}
    fields_by_row[x['row']]=fields
    for name,keys in {'neck':['NECKCOLLOR'],'sleeve':['SLEEVE'],'opening':['OPENING'],'hem':['HEMLINE','HEMLINE BOTTOM'],'pocket':['POCKET'],'waist':['WAIST'],'leg':['LEG']}.items():
        raw=next((fields[k] for k in keys if fields.get(k)),None)
        if raw and raw!=x['facts']['attr'][name]:
            diff.append({'row':x['row'],'attribute':name,'source':raw,'prior':x['facts']['attr'][name]})
(R/'raw-fields.json').write_text(json.dumps(fields_by_row,indent=2),encoding='utf-8')
(R/'unmapped-source-details.json').write_text(json.dumps(diff,indent=2),encoding='utf-8')
print(json.dumps(diff,indent=2))
