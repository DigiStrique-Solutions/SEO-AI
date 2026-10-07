"""Resolve category-specific styling discrepancies in the active PDP copy."""

import collections
import copy
import json
from pathlib import Path

ROOT = Path(__file__).parent
PRIOR = ROOT.parent / "20261006-added-active-pdp-copyedit" / "revised.json"
prior = json.loads(PRIOR.read_text(encoding="utf-8"))
revised = copy.deepcopy(prior)
changes = []

for item in revised:
    original = item["after"]
    intro, details, styling, product_id = original.split("\n\n")
    reasons = []
    if "Keep the jacket and accessories simple so the pattern has room to stand out in either combination." in styling:
        styling = styling.replace(
            "Keep the jacket and accessories simple so the pattern has room to stand out in either combination.",
            "Keep any extra layer and accessories simple so the pattern remains visible.",
        )
        reasons.append("unintroduced jacket in styling note")
    if "A small shoulder bag keeps the outfit practical without adding another layer." in styling:
        styling = styling.replace(
            "A small shoulder bag keeps the outfit practical without adding another layer.",
            "A small shoulder bag carries the essentials without crowding the outfit.",
        )
        reasons.append("bag compared with clothing layer")
    if "rather than several extra layers" in styling:
        styling = styling.replace(
            "A crisp shirt offers another option for meeting friends; add a small bag and understated accessories rather than several extra layers.",
            "A crisp shirt offers another option for meeting friends; carry a small bag and keep accessories understated.",
        )
        reasons.append("accessories compared with extra layers")

    if item["facts"]["gender"] == "men":
        noun = item["facts"]["noun"]
        if noun == "trousers":
            for colour in ("navy", "off-white"):
                old = f"a plain {colour} top and flat sandals"
                if old in styling:
                    styling = styling.replace(old, f"a plain {colour} shirt and canvas trainers")
                    reasons.append("mens trouser outfit: generic top and flat sandals")
                article = "an" if colour == "off-white" else "a"
                old = f"{article} {colour} knit top and flat shoes"
                if old in styling:
                    styling = styling.replace(old, f"{article} {colour} shirt and loafers")
                    reasons.append("mens trouser outfit: generic knit top and flat shoes")
            if "A crisp shirt offers another option" in styling and "shirt and loafers" in styling:
                styling = styling.replace("A crisp shirt offers another option", "A plain polo offers another option")
                reasons.append("shirt suggested twice")
        if "flat shoes" in styling:
            styling = styling.replace("flat shoes", "loafers")
            reasons.append("mens top outfit: generic flat shoes")

    updated = "\n\n".join((intro, details, styling, product_id))
    if updated != original:
        item["after"] = updated
        item["words"] = len(updated.split("Product ID:")[0].split())
        changes.append({"row": item["row"], "code": item["code"], "reasons": reasons})

(ROOT / "revised.json").write_text(json.dumps(revised, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"rows": len(revised), "changed": len(changes),
                  "reason_counts": dict(collections.Counter(r for c in changes for r in c["reasons"]))}, indent=2))
