import concurrent.futures, json, requests
from pathlib import Path
R=Path(__file__).parent
records={x['row']:x for x in json.loads((R.parent/'20261006-added-active-pdp/records.json').read_text(encoding='utf-8'))}
targets=[3,18,24,43,44,51,80,91,93,94,118,200,219,249,278,279,293,294,295,317,318,370,110,111,121,122,169,179,255,256,52,53,81,84,85,86,87]
cached=json.loads((R/'live-products.json').read_text(encoding='utf-8')) if (R/'live-products.json').exists() else []
by_row={x['row']:x for x in cached}
def fetch(row):
    rec=records[row]
    result={'row':row,'attempts':[]}
    for url in dict.fromkeys([rec['original_url']+'.js',rec['updated_url']+'.js']):
        try:
            res=requests.get(url,timeout=25)
            attempt={'url':url,'status':res.status_code,'final_url':res.url,'body':res.text}
            result['attempts'].append(attempt)
            if res.status_code==200:
                payload=res.json()
                result['product']=payload
                break
        except Exception as exc: result['attempts'].append({'url':url,'error':str(exc)})
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for item in pool.map(fetch,[row for row in targets if row not in by_row]):by_row[item['row']]=item
data=[by_row[row] for row in targets]
(R/'live-products.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
for x in data:print(x['row'],[a.get('status',a.get('error')) for a in x['attempts']],x.get('product',{}).get('title',''))
