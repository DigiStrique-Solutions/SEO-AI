"""Check whether edited proposed handles are already served by Cottonworld."""

import concurrent.futures
import json
import urllib.error
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parent
changes = json.loads((root / "change-plan.json").read_text(encoding="utf-8"))["changes"]


def check(item):
    url = item["after"]["url"]
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return {"row": item["row"], "url": url, "status": response.status, "final_url": response.url}
    except urllib.error.HTTPError as exc:
        return {"row": item["row"], "url": url, "status": exc.code, "final_url": exc.url}
    except Exception as exc:
        return {"row": item["row"], "url": url, "error": str(exc)}


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    results = sorted(pool.map(check, changes), key=lambda item: item["row"])
(root / "proposed-url-head-results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"counts": {str(code): sum(x.get("status") == code for x in results) for code in sorted({x.get("status") for x in results if x.get("status")})}, "errors": [x["row"] for x in results if "error" in x], "live": [x["row"] for x in results if x.get("status") == 200]}))
