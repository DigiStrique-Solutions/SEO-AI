"""Check a bounded sample of proposed product URLs after sheet corrections."""
import json
import gzip
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

root = Path(__file__).resolve().parent
sheet = json.load(gzip.open(root / "source-sheet.json.gz", "rt", encoding="utf-8"))["values"]
plan = {item["row"]: item["after"] for item in json.loads((root / "change-plan.json").read_text(encoding="utf-8"))["changes"]}
results = []
for row in [2, 8, 28, 72, 169, 370, 381]:
    url = plan.get(row, {}).get("url", sheet[row-1][1])
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-QA/1.0)"})
    try:
        with urlopen(request, timeout=15) as response:
            status, final_url = response.status, response.url
    except HTTPError as error:
        status, final_url = error.code, error.url
    except URLError as error:
        status, final_url = None, url
    results.append({"row": row, "proposed_url": url, "http_status": status, "final_url": final_url})
(root / "live-url-sample.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
print(json.dumps(results))
