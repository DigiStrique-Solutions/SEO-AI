"""Edit the new SEO copy to match the existing Cottonworld sheet's voice."""

import json
import re
from pathlib import Path


OUT = Path(__file__).parent
SOURCE = OUT.parent / "20261007-new-pages" / "change-plan.json"
plan = json.load(open(SOURCE, encoding="utf-8"))

# The older 17751 listing supports the silhouette, though these SKUs are not
# public. Older 16162 listings vary in fabric, so omit its unverified material.
h1_updates = {
    396: "Women’s Regular Fit Blouse Sleeveless Navy",
    397: "Women’s Regular Fit Blouse Sleeveless White",
    421: "Men’s Regular Fit Shirt White",
    422: "Men’s Regular Fit Shirt Natural",
}

descriptions = {
    394: "Choose Cottonworld’s women’s linen regular fit blouse in peach with a mandarin collar for workdays, travel and relaxed weekends.",
    395: "Explore Cottonworld’s women’s blouse in peach for everyday outfits, easy workdays and unhurried weekends.",
    396: "Cottonworld’s women’s regular fit blouse in navy has a sleeveless shape for everyday dressing, travel and relaxed plans.",
    397: "Bring Cottonworld’s women’s regular fit sleeveless blouse in white into the week for work, travel and time off.",
    398: "Explore Cottonworld’s women’s blouse in denim for everyday dressing, from workdays to relaxed weekends.",
    399: "Add Cottonworld’s women’s blouse in brown to an everyday wardrobe for work, travel and quieter days.",
    400: "Choose Cottonworld’s women’s dress in navy for a straightforward outfit on workdays, trips and relaxed weekends.",
    401: "Explore Cottonworld’s women’s dress in blue for everyday dressing, afternoon plans and unhurried weekends.",
    402: "Wear Cottonworld’s women’s dress in denim through busy days and relaxed plans, with simplicity at the centre.",
    403: "Cottonworld’s women’s cotton bamboo elastane regular fit knit pant in black has an elastic waist for workdays and weekends.",
    404: "Choose Cottonworld’s women’s cotton bamboo elastane regular fit knit pant in brown with an elastic waist for everyday wear.",
    405: "Explore Cottonworld’s women’s cotton bamboo elastane regular fit knit pant in navy with an elastic waist for easy days.",
    406: "Wear Cottonworld’s women’s linen viscose regular fit pant in maroon with a drawstring elastic waist for work and travel.",
    407: "Choose Cottonworld’s women’s linen viscose regular fit pant in navy with a drawstring elastic waist for everyday wear.",
    408: "Explore Cottonworld’s women’s linen viscose regular fit pant in off white with a drawstring elastic waist for relaxed days.",
    409: "Choose Cottonworld’s women’s cotton straight fit pant in mustard for everyday wear, workdays and travel.",
    410: "Wear Cottonworld’s women’s cotton straight fit pant in navy through workdays, weekends and journeys away.",
    411: "Explore Cottonworld’s women’s cotton straight fit pant in olive for everyday dressing, travel and time off.",
    412: "Add Cottonworld’s women’s skirt in denim to an everyday wardrobe for workdays, travel and relaxed weekends.",
    413: "Cottonworld’s women’s organic cotton regular fit t-shirt in lavender has a round neck for everyday dressing and weekends.",
    414: "Explore Cottonworld’s women’s organic cotton regular fit round neck t-shirt in light green for easy workdays and travel.",
    415: "Choose Cottonworld’s women’s organic cotton regular fit t-shirt in white with a round neck for work and relaxed days.",
    416: "Wear Cottonworld’s women’s organic cotton regular fit round neck t-shirt in wine through workdays and weekends.",
    417: "Explore Cottonworld’s women’s organic cotton regular fit t-shirt in brown with a round neck and extended sleeves.",
    418: "Choose Cottonworld’s women’s organic cotton regular fit t-shirt in navy with a round neck and extended sleeves for everyday wear.",
    419: "Cottonworld’s women’s organic cotton regular fit t-shirt in wine pairs a round neck with extended sleeves for easy days.",
    420: "Explore Cottonworld’s men’s shirt in off white for everyday dressing, from the working week to relaxed weekends.",
    421: "Choose Cottonworld’s men’s regular fit shirt in white for workdays, travel and the quieter hours in between.",
    422: "Bring Cottonworld’s men’s regular fit shirt in natural into an everyday wardrobe for work, weekends and travel.",
    423: "Cottonworld’s men’s regular fit shirt in white has full sleeves for everyday dressing, workdays and time off.",
    424: "Explore Cottonworld’s men’s regular fit shirt in aqua with full sleeves for work, travel and relaxed weekends.",
    425: "Choose Cottonworld’s men’s regular fit shirt in green with full sleeves for everyday wear and unhurried days.",
    426: "Wear Cottonworld’s men’s cotton bamboo elastane regular fit t-shirt in dark grey with a polo neckline through busy days.",
    427: "Explore Cottonworld’s men’s cotton bamboo elastane regular fit t-shirt in navy with a polo neckline for everyday wear.",
    428: "Choose Cottonworld’s men’s cotton bamboo elastane regular fit t-shirt in wine with a polo neckline for relaxed days.",
    429: "Explore Cottonworld’s men’s t-shirt in black for easy everyday dressing, from workdays to relaxed weekends.",
}

overlaps = {403: [119], 404: [120], 413: [187], 415: [182, 193],
            416: [189], 417: [198], 422: [263], 425: [317]}

def slug(text):
    text = text.lower().replace("’", "").replace("t-shirt", "tshirt")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


assert len(plan) == len(descriptions) == 36
for item in plan:
    row = item["row"]
    if row in h1_updates:
        item["h1"] = h1_updates[row]
        item["updated_url"] = "https://cottonworld.net/products/" + slug(item["h1"])
        item["meta_title"] = item["h1"] + " | Cottonworld"
        if row in (396, 397):
            item["review_status"] = "Provisional: fit and sleeve inferred from an older listing of this style; confirm this SKU’s fabric, fit and print before publishing."
    item["meta_description"] = descriptions[row]
    if row in overlaps:
        prior = " and ".join(str(x) for x in overlaps[row])
        noun = "row" if len(overlaps[row]) == 1 else "rows"
        item["review_status"] += f" Same style and colour also occur in {noun} {prior}; confirm the distinguishing product detail."

with open(OUT / "change-plan.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
print(json.dumps({"rows": len(plan), "max_description_length": max(len(x["meta_description"]) for x in plan),
                  "h1_updates": sorted(h1_updates), "overlap_rows": sorted(overlaps)}, ensure_ascii=True))
