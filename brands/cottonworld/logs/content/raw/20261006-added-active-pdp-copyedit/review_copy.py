"""Copyedit the added Cottonworld PDP sheet against the prior source-backed draft.

This does not generate new product facts. It only changes repeated or awkward copy.
"""

import collections
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
PRIOR = ROOT.parent / "20261006-added-active-pdp" / "proposals.json"
source = json.loads(PRIOR.read_text(encoding="utf-8"))

solid_options = [
    "The plain finish leaves room for another texture or print.",
    "A solid colour keeps the focus on the cut and the pieces around it.",
    "The unpatterned surface works with tonal or contrasting separates.",
    "A single-colour finish offers a quiet base for different combinations.",
    "With no print, the garment's outline stays clear.",
    "The plain fabric pairs with both printed and unpatterned pieces.",
    "The uninterrupted colour allows another layer to stand out.",
    "A solid finish leaves room for a patterned accessory or layer.",
    "The unpatterned design sits comfortably beside a more detailed layer.",
    "A plain surface gives you room to vary colour and texture.",
    "The single-colour fabric suits either a tonal or contrasting pairing.",
    "The solid surface keeps the cut visible without competing with a print.",
]
pattern_options = [
    "The visible pattern pairs well with plain separates.",
    "A simpler piece beside it lets the surface detail show.",
    "Against a plain layer, its surface detail stands out.",
    "With a quiet counterpart, the surface detail stays in view.",
    "The surface detail provides a clear contrast with quieter layers.",
    "A plain counterpart keeps attention on the pattern.",
]

def rewrite(item):
    row = item["row"]
    facts = item["facts"]
    text = item["after"]
    why = []

    # The merchant colour field contradicts both the product title and both URLs.
    if row == 370:
        assert facts["colour"] == "brown" and "men's brown T-shirt" in text
        facts["colour"] = "olive"
        text = text.replace("men's brown T-shirt", "men's olive T-shirt")
        why.append("colour corrected from product title and URL")
    if row == 93:
        assert facts["colour"] == "off-white  and  wine"
        facts["colour"] = "off-white and wine"
        text = text.replace("off-white  and  wine", "off-white and wine")
        why.append("double spaces in colour")

    old = "The solid finish is easy to coordinate with the rest of your wardrobe."
    if old in text:
        assert facts["pattern"] == "SOLID", (row, facts["pattern"])
        text = text.replace(old, solid_options[row % len(solid_options)])
        why.append("repetitive generic solid-finish sentence")
    old = "The surface detailing brings a point of interest to an otherwise straightforward silhouette."
    if old in text:
        assert facts["pattern"] in {"PRINT", "STRIPE", "CHECK"}, (row, facts["pattern"])
        text = text.replace(old, pattern_options[row % len(pattern_options)])
        why.append("repetitive generic pattern sentence")

    if "regular collar" in text:
        text = text.replace("A regular collar is paired with", "It has a collar and")
        text = text.replace("a regular collar", "a collar")
        why.append("repeated regular")
    if "regular placket" in text:
        text = text.replace("regular placket", "placket")
        why.append("repeated regular")
    if "The design has" in text:
        text = text.replace("The design has", "It has")
        why.append("repeated sentence opening")
    if "It has a sleeveless cut." in text:
        text = re.sub(r"It has (a [^.]*(?:neckline|collar))\. It has a sleeveless cut\.",
                      r"It has \1 and a sleeveless cut.", text)
        why.append("repeated it has opening")
    if "The shape finishes with" in text:
        text = re.sub(r"The shape finishes with an? (\w+) hem\.", r"The hem is \1.", text)
        why.append("repeated shape")
    if "The shape leaves room for simple styling choices." in text:
        text = text.replace(
            "The shape leaves room for simple styling choices.",
            "The outline is straightforward, leaving room for different styling choices.",
        )
        why.append("repeated shape or simple")
    if "Its familiar shape is simple to wear with pieces already in your wardrobe." in text:
        text = text.replace(
            "Its familiar shape is simple to wear with pieces already in your wardrobe.",
            "It works with pieces already in your wardrobe.",
        )
        why.append("repeated shape or simple")
    if "The simple silhouette leaves room" in text:
        text = text.replace("The simple silhouette leaves room", "The silhouette leaves room")
        why.append("repeated simple")
    if row == 294:
        text = text.replace("For a simple change from familiar separates", "For a change from familiar separates")
        why.append("repeated simple")
    if facts["noun"] == "shirt" and "An unbuttoned shirt or light jacket adds another layer" in text:
        text = text.replace("An unbuttoned shirt or light jacket adds another layer", "A light jacket adds another layer")
        why.append("shirt layered over shirt")
    if "offer a barrel leg" in text:
        text = text.replace("offer a barrel leg", "have a barrel-leg cut")
        text = text.replace(" and a barrel-leg shape", "")
        why.append("repeated and awkward barrel-leg wording")
    if row == 143:
        text = text.replace("an elasticated drawstring waist and straight legs", "an elasticated drawstring waist")
        why.append("repeated straight")
    if row in {84, 88}:
        text = text.replace("for daytime plans. Add a short jacket", "for a daytime outfit. Add a short jacket")
        why.append("repeated daytime plans")
    if row == 156:
        text = text.replace("and slippers for evenings at home", "and slippers at home")
        why.append("repeated evenings at home")
    if row in {163, 335, 339}:
        text = text.replace("For a walk or a day of errands, switch", "For errands, switch")
        why.append("repeated walk or a")
    if row in {218, 295}:
        text = text.replace("for a day off", "on a day off").replace("For a day off", "On a day off")
        why.append("repeated for a day")
    if row in {108, 109, 214}:
        text = text.replace("Keep the layer underneath simple so the front detailing and outline remain easy to see.",
                            "Keep the top underneath plain so the opening and outline remain visible.")
        why.append("repeated front or layer")
    if row == 108:
        text = text.replace("Keep the top underneath plain", "Keep the top underneath simple")
        why.append("repeated plain")
    if row == 293:
        text = text.replace("A light jacket adds another layer without taking attention away from the shape.",
                            "A light jacket adds another layer without hiding the rounded hem. Keep the full sleeves down for a tidier outline, or turn them back for a relaxed afternoon.")
        why.append("source-limited description depth")
    # These introductions were otherwise identical after the colour changed.
    opening_edits = {
        194: ("For days when a few familiar pieces are enough", "For a relaxed day built around simple layers"),
        370: ("For days when a few familiar pieces are enough", "For a low-key weekend outfit"),
        372: ("For a morning out or an afternoon close to home", "For casual plans close to home"),
        373: ("For everyday plans that call for simple combinations", "For errands followed by an informal lunch"),
        374: ("For days when a few familiar pieces are enough", "For a weekend outfit with room to layer"),
        375: ("For a weekend walk, coffee or time at home", "For a relaxed weekend lunch"),
        376: ("For a morning out or an afternoon close to home", "For a laid-back afternoon"),
        382: ("For days when a few familiar pieces are enough", "For a casual day built around lighter layers"),
    }
    if row in opening_edits:
        old, new = opening_edits[row]
        assert old in text, (row, text[:100])
        text = text.replace(old, new, 1)
        why.append("description matched another colour variant")
    return text, why


out = copy.deepcopy(source)
changes = []
for item in out:
    text, why = rewrite(item)
    if text != item["after"]:
        changes.append({"row": item["row"], "code": item["code"], "reasons": why})
        item["after"] = text
        item["words"] = len(text.split("Product ID:")[0].split())

def normalized_body(item):
    body = item["after"].split("\n\nProduct ID:")[0].lower()
    body = re.sub(r"\b(?:black|white|off-white|navy|blue|denim|red|pink|khaki|brick|cream|grey|gray|beige|green|yellow|brown|purple|maroon|olive|coffee|mustard|rust|orange|indigo|wine|peach|ivory|teal|charcoal|stone|coral|aqua|lavender|lilac|sand|mint|tan|sage|natural|dark-grey)\b", "[colour]", body)
    return re.sub(r"\d+%", "[pct]", body)

dupes = collections.defaultdict(list)
for item in out:
    dupes[normalized_body(item)].append(item["row"])
duplicates = [v for v in dupes.values() if len(v) > 1]

(ROOT / "revised.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"rows": len(out), "changed": len(changes), "duplicate_groups_after_color_normalization": duplicates,
                  "reason_counts": dict(collections.Counter(reason for c in changes for reason in c["reasons"]))}, indent=2))
