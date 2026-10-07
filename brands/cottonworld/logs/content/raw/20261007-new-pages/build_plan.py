"""Build conservative SEO proposals for unpublished SKU rows 394–429."""

import json
import re
from pathlib import Path


OUT = Path(__file__).parent
SKUS = [
    "L-BLOUSE-11180-21760-PEACH", "L-BLOUSE-17698-21864-PEACH",
    "L-BLOUSE-17751-21834-NAVY", "L-BLOUSE-17751-21846-WHITE",
    "L-BLOUSE-17912-21762-DENIM", "L-BLOUSE-18008-21759-BROWN",
    "L-DRESS-17452-21709-NAVY 1", "L-DRESS-17453-21708-BLUE",
    "L-DRESS-17994-21762-DENIM", "L-KPANTS-16646-21892-BLACK",
    "L-KPANTS-16646-21892-BROWN", "L-KPANTS-16646-21892-NAVY",
    "L-PANTS-17769-21805-MAROON", "L-PANTS-17769-21805-NAVY",
    "L-PANTS-17769-21805-OFFWHITE", "L-PANTS-17922-21822-MUSTARD",
    "L-PANTS-17922-21822-NAVY", "L-PANTS-17922-21822-OLIVE",
    "L-SKIRT-17888-21762-DENIM", "L-TSHIRT-17427-21911-LAVENDER",
    "L-TSHIRT-17427-21911-LT GREEN", "L-TSHIRT-17427-21911-WHITE",
    "L-TSHIRT-17427-21911-WINE", "L-TSHIRT-17428-21911-BROWN",
    "L-TSHIRT-17428-21911-NAVY", "L-TSHIRT-17428-21911-WINE",
    "M-SHIRTS-11409-21391-OFFWHITE", "M-SHIRTS-16162-21880-WHITE",
    "M-SHIRTS-16162-21903-NATURAL", "M-SHIRTS-50020-21882-WHITE",
    "M-SHIRTS-50020-21901-AQUA", "M-SHIRTS-50020-21902-GREEN",
    "M-TSHIRT-17093-21892-DARK GREY", "M-TSHIRT-17093-21892-NAVY",
    "M-TSHIRT-17093-21892-WINE", "M-TSHIRT-17963-21893-BLACK",
]

# Older public listings of the same style support these traits, but not the
# new SKU's fabric/print with certainty. The review status preserves that limit.
PROFILE = {
    "L-BLOUSE-11180": ("Women’s Linen Regular Fit Blouse Mandarin Collar", True),
    "L-BLOUSE-17698": ("Women’s Blouse", False),
    "L-BLOUSE-17751": ("Women’s Blouse", False),
    "L-BLOUSE-17912": ("Women’s Blouse", False),
    "L-BLOUSE-18008": ("Women’s Blouse", False),
    "L-DRESS-17452": ("Women’s Dress", False),
    "L-DRESS-17453": ("Women’s Dress", False),
    "L-DRESS-17994": ("Women’s Dress", False),
    "L-KPANTS-16646": ("Women’s Cotton Bamboo Elastane Regular Fit Knit Pant Elastic Waist", True),
    "L-PANTS-17769": ("Women’s Linen Viscose Regular Fit Pant Drawstring Elastic Waist", True),
    "L-PANTS-17922": ("Women’s Cotton Straight Fit Pant", True),
    "L-SKIRT-17888": ("Women’s Skirt", False),
    "L-TSHIRT-17427": ("Women’s Organic Cotton Regular Fit T-Shirt Round Neck", True),
    "L-TSHIRT-17428": ("Women’s Organic Cotton Regular Fit T-Shirt Round Neck Extended Sleeve", True),
    "M-SHIRTS-11409": ("Men’s Shirt", False),
    "M-SHIRTS-16162": ("Men’s Linen Regular Fit Shirt Regular Collar", True),
    "M-SHIRTS-50020": ("Men’s Regular Fit Shirt Full Sleeve", True),
    "M-TSHIRT-17093": ("Men’s Cotton Bamboo Elastane Regular Fit T-Shirt Polo", True),
    "M-TSHIRT-17963": ("Men’s T-Shirt", False),
}


def colour(raw):
    return {"OFFWHITE": "Off White", "LT GREEN": "Light Green",
            "DARK GREY": "Dark Grey", "NAVY 1": "Navy"}.get(raw, raw.title())


def slug(text):
    text = text.lower().replace("’", "").replace("t-shirt", "tshirt")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


plan = []
for row, sku in enumerate(SKUS, 394):
    match = re.fullmatch(r"([LM])-([A-Z]+)-(\d+)-(\d+)-(.+)", sku)
    assert match, sku
    key = "-".join(match.group(i) for i in (1, 2, 3))
    base, inherited = PROFILE[key]
    color_name = colour(match.group(5))
    h1 = f"{base} {color_name}"
    url = f"https://cottonworld.net/products/{slug(h1)}"
    if inherited:
        review = "Provisional: traits inferred from earlier public listings of this style; confirm this SKU’s fabric, fit and print before publishing."
    else:
        review = "Provisional: only gender, product type and colour follow the SKU; confirm fabric, fit and print before publishing."
    description = f"Explore Cottonworld’s {h1.lower()} for everyday wear, workdays and relaxed weekends."
    plan.append({"row": row, "sku": sku, "updated_url": url, "h1": h1,
                 "meta_title": h1 + " | Cottonworld", "meta_description": description,
                 "review_status": review, "inherited_style_traits": inherited})

with open(OUT / "change-plan.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
print(json.dumps({"count": len(plan), "max_description_length": max(len(x["meta_description"]) for x in plan),
                  "rows": [plan[0], plan[-1]]}, ensure_ascii=True))
