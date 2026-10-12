import json
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup


out = Path(__file__).parent
path = out / "internal-link-map.json"
link_map = json.loads(path.read_text(encoding="utf-8"))
urls = sorted({item["url"] for item in link_map["links"]})
checks = []
for url in urls:
    response = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    tag = soup.find("link", rel="canonical")
    canonical = tag.get("href") if tag else None
    checks.append({
        "url": url,
        "status_code": response.status_code,
        "final_url": response.url,
        "canonical_url": canonical,
        "direct_canonical_target": response.status_code == 200 and response.url == url and canonical == url,
    })
by_url = {item["url"]: item for item in checks}
for item in link_map["links"]:
    item["canonical_url"] = by_url[item["url"]]["canonical_url"]
    item["verified_live_direct_canonical"] = by_url[item["url"]]["direct_canonical_target"]
link_map["canonical_check_at"] = datetime.now(timezone.utc).isoformat()
link_map["all_targets_direct_canonical"] = all(item["direct_canonical_target"] for item in checks)
path.write_text(json.dumps(link_map, indent=2, ensure_ascii=False), encoding="utf-8")
(out / "canonical-check.json").write_text(json.dumps(checks, indent=2, ensure_ascii=False), encoding="utf-8")
print("Canonical targets verified:", len(checks), "all direct:", link_map["all_targets_direct_canonical"])
