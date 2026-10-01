"""Check HTTP availability of rows whose proposed handles exist in the catalog."""
import gzip
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

root=Path(__file__).resolve().parent
pairs=json.loads((root/"parallel-live-products.json").read_text(encoding="utf-8"))
def check(job):
    row,kind,url=job
    request=Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; Cottonworld-SEO-QA/1.0)"})
    try:
        with urlopen(request,timeout=20) as response:
            return {"row":row,"kind":kind,"url":url,"status":response.status,"final_url":response.url}
    except HTTPError as error:
        return {"row":row,"kind":kind,"url":url,"status":error.code,"final_url":error.url}
    except URLError as error:
        return {"row":row,"kind":kind,"url":url,"status":None,"error":str(error.reason)}
jobs=[(pair["row"],kind,pair[kind+"_url"]) for pair in pairs for kind in ["original","proposed"]]
with ThreadPoolExecutor(max_workers=8) as pool:
    results=list(pool.map(check,jobs))
(root/"live-url-status.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"checked":len(results),"statuses":{str(v):sum(r["status"]==v for r in results) for v in {r["status"] for r in results}}}))
