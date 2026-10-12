import json
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup


OUT = Path(__file__).parent
URLS = {
    "serp_1": "https://www.lindapaige.com/blog/first-5-pieces-capsule-wardrobe",
    "serp_2": "https://www.dressingwizard.com/looks/capsule-wardrobe-10-outfits-5-pieces",
    "serp_3": "https://cosmosandclover.com/blogs/style-trends/how-to-build-10-outfits-from-5-pieces-without-a-closet-full-of-clothes",
    "womens_tshirts": "https://cottonworld.net/collections/women-tshirts",
    "mens_tshirts": "https://cottonworld.net/collections/mens-tshirts",
    "womens_tops": "https://cottonworld.net/collections/women-tops-1",
    "mens_shirts": "https://cottonworld.net/collections/mens-shirts",
    "womens_pants": "https://cottonworld.net/collections/womens-pants",
    "mens_pants": "https://cottonworld.net/collections/mens-pants-2",
    "womens_kurtas": "https://cottonworld.net/collections/women-kurtas-tunics",
    "mens_kurtas": "https://cottonworld.net/collections/men-kurtas",
    "womens_dresses": "https://cottonworld.net/collections/women-dresses-jumpsuits",
    "womens_jackets": "https://cottonworld.net/collections/women-jackets-1",
    "mens_jackets": "https://cottonworld.net/collections/men-jackets",
}

results = {}
for key, url in URLS.items():
    try:
        response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        for node in soup(["script", "style", "nav", "footer", "header"]):
            node.decompose()
        main = soup.find("article") or soup.find("main") or soup.body or soup
        lines = [re.sub(r"\s+", " ", line).strip() for line in main.get_text("\n").splitlines()]
        lines = [line for line in lines if line]
        headings = [re.sub(r"\s+", " ", h.get_text(" ")).strip() for h in main.find_all(["h1", "h2", "h3"])]
        text = "\n".join(lines)
        (OUT / f"{key}.txt").write_text(text, encoding="utf-8")
        results[key] = {
            "url": url,
            "status_code": response.status_code,
            "final_url": response.url,
            "title": soup.title.get_text(" ", strip=True) if soup.title else "",
            "headings": headings[:45],
            "approx_word_count_main": len(re.findall(r"\b[\w’-]+\b", text)),
            "first_1200_chars": text[:1200],
        }
    except Exception as exc:
        results[key] = {"url": url, "error": str(exc)}

payload = {
    "captured_at": datetime.now(timezone.utc).isoformat(),
    "query": "A Full Wardrobe, Nothing to Wear? Five Everyday Pieces to Start With",
    "serp_method": "Live web search; first three relevant organic blog results after excluding news, shopping pages, and forum posts",
    "results": results,
}
(OUT / "captures.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
for key, value in results.items():
    print(key, value.get("status_code", "ERROR"), value.get("final_url", value.get("error")), value.get("approx_word_count_main", ""), value.get("headings", [])[:8])
