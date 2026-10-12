import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).parent
DRAFT = ROOT / "brands/cottonworld/blogs/drafts/a-full-wardrobe-nothing-to-wear-five-pieces.md"
markdown = DRAFT.read_text(encoding="utf-8")
capture = json.loads((OUT / "captures.json").read_text(encoding="utf-8"))
title = markdown.splitlines()[0].removeprefix("# ")
body_md = markdown.split("**Suggested URL:**", 1)[1].split("\n\n", 1)[1].strip()
plain_body = re.sub(r"\[([^]]+)\]\(https://cottonworld\.net/[^)]+\)", r"\1", body_md)
plain_body = re.sub(r"(?m)^## ", "", plain_body)
plain_body = re.sub(r"\*\*", "", plain_body)
final_text = title + "\n\n" + plain_body + "\n"
(OUT / "final-body.txt").write_text(final_text, encoding="utf-8")

benchmarks = [
    {
        "rank_among_relevant_organic_blogs": 1,
        "url": "https://www.lindapaige.com/blog/first-5-pieces-capsule-wardrobe",
        "tone": "Direct, empathetic coaching; speaks to the closet-full problem and recommends foundations.",
        "approx_page_main_words": capture["results"]["serp_1"]["approx_word_count_main"],
        "structure": "Problem opening, why foundations matter, five named pieces, how pieces work together, next steps and questions.",
        "source_capture": "serp_1.txt",
    },
    {
        "rank_among_relevant_organic_blogs": 2,
        "url": "https://www.dressingwizard.com/looks/capsule-wardrobe-10-outfits-5-pieces",
        "tone": "Formula-led and instructional, with a strong outfit-combination focus and US shopping context.",
        "approx_page_main_words": capture["results"]["serp_2"]["approx_word_count_main"],
        "structure": "Explains the premise, introduces five pieces, maps ten outfits, then covers shopping, expansion, maintenance and FAQs.",
        "source_capture": "serp_2.txt",
    },
    {
        "rank_among_relevant_organic_blogs": 3,
        "url": "https://cosmosandclover.com/blogs/style-trends/how-to-build-10-outfits-from-5-pieces-without-a-closet-full-of-clothes",
        "tone": "Conversational and boutique-led, with immediate product examples.",
        "approx_page_main_words": capture["results"]["serp_3"]["approx_word_count_main"],
        "structure": "Short problem opening, five linked garments, ten numbered outfits and a shopping close.",
        "source_capture": "serp_3.txt",
    },
]
benchmark = {
    "query": capture["query"],
    "access_date": "2026-10-12",
    "captured_at": capture["captured_at"],
    "selection": capture["serp_method"],
    "results": benchmarks,
    "editorial_application": "Aim for a 1,200–1,700 word Cottonworld article with a real-life opening, five concrete roles, outfit combinations and targeted shopping paths. Preserve Cottonworld's calm first-person brand voice; do not reproduce another article's wording or exact structure.",
    "user_supplied_flow_references_also_considered": [
        "https://www.thefemaleceo.com/blog/a-wardrobe-full-of-clothes-and-nothing-to-wear",
        "https://tamarakalinic.substack.com/p/closet-full-of-clothes-and-nothing",
        "https://inspo.thedrobe.com/foundations/15-reasons-full-wardrobe-and-nothing-to-wear/",
    ],
}
(OUT / "benchmark.json").write_text(json.dumps(benchmark, indent=2, ensure_ascii=False), encoding="utf-8")

links = []
for anchor, url in re.findall(r"\[([^]]+)\]\((https://cottonworld\.net/[^)]+)\)", body_md):
    match = next((v for v in capture["results"].values() if v["url"] == url), None)
    links.append({
        "anchor": anchor,
        "url": url,
        "status_code": match.get("status_code") if match else None,
        "final_url": match.get("final_url") if match else None,
        "verified_live_and_direct": bool(match and match.get("status_code") == 200 and match.get("final_url") == url),
    })
link_map = {
    "checked_at": capture["captured_at"],
    "source": "Direct GET of Cottonworld categories; see captures.json and category text captures",
    "body_link_count": len(links),
    "distinct_target_count": len({x["url"] for x in links}),
    "contains_unwanted_all_collections_link": "https://cottonworld.net/collections)" in body_md or "https://cottonworld.net/collections/all" in body_md,
    "roles": {
        "contextual_product_or_collection": "T-shirt categories in piece 1",
        "supporting_category": "Shirts, tops, pants and other relevant categories in pieces 2–5",
        "commercial_next_step": "Specific top and pants categories in the conclusion",
    },
    "links": links,
}
(OUT / "internal-link-map.json").write_text(json.dumps(link_map, indent=2, ensure_ascii=False), encoding="utf-8")

checks = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "draft_path": str(DRAFT.relative_to(ROOT)).replace("\\", "/"),
    "document_url": "https://docs.google.com/document/d/1Jw4TuMCqLxueBf2KiFLPjDOEbQ6-bKDrt8PBEMowh-M/edit",
    "title": title,
    "body_word_count": len(re.findall(r"\b[\w’-]+\b", plain_body)),
    "detector_input_word_count": len(re.findall(r"\b[\w’-]+\b", final_text)),
    "detector_input_char_count": len(final_text),
    "detector_input_sha256": hashlib.sha256(final_text.encode("utf-8")).hexdigest(),
    "first_person_brand_voice": "our" in body_md.lower(),
    "has_third_person_fabric_phrase": "its fabrics" in body_md.lower(),
    "all_category_targets_live_direct": all(x["verified_live_and_direct"] for x in links),
    "body_links": len(links),
}
(OUT / "draft-checks.json").write_text(json.dumps(checks, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(checks, indent=2))
