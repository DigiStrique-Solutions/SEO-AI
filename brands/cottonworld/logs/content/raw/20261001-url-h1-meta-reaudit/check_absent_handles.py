"""Check absent catalog handles with a bounded HTTP sample."""
import gzip
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

root=Path(__file__).resolve().parent
sheet=json.load(gzip.open(root/"source-sheet.json.gz","rt",encoding="utf-8"))["values"]
catalog={p["handle"] for p in json.load(gzip.open(root/"catalog.json.gz","rt",encoding="utf-8"))["products"]}
source_absent=[(row,r[0]) for row,r in enumerate(sheet[1:],2) if r[0].split("/products/")[-1] not in catalog]
proposed_absent=[(row,r[1]) for row,r in enumerate(sheet[1:],2) if r[1].split("/products/")[-1] not in catalog]
step=max(1,len(proposed_absent)//25)
sample=proposed_absent[::step][:25]
jobs=[("original_absent",row,url) for row,url in source_absent]+[("proposed_absent_sample",row,url) for row,url in sample]
def check(job):
    kind,row,url=job
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; Cottonworld-SEO-QA/1.0)"})
    try:
        with urlopen(request,timeout=20) as response:
            return {"kind":kind,"row":row,"url":url,"status":response.status,"final_url":response.url}
    except HTTPError as error:
        return {"kind":kind,"row":row,"url":url,"status":error.code,"final_url":error.url}
    except URLError as error:
        return {"kind":kind,"row":row,"url":url,"status":None,"error":str(error.reason)}
with ThreadPoolExecutor(max_workers=8) as pool:
    results=list(pool.map(check,jobs))
(root/"absent-handle-http-sample.json").write_text(json.dumps({"source_absent_count":len(source_absent),"proposed_absent_count":len(proposed_absent),"results":results},ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"source_absent":len(source_absent),"proposed_absent":len(proposed_absent),"source_http":{str(v):sum(r["status"]==v and r["kind"]=="original_absent" for r in results) for v in {r["status"] for r in results}},"proposed_sample_http":{str(v):sum(r["status"]==v and r["kind"]=="proposed_absent_sample" for r in results) for v in {r["status"] for r in results}}}))
