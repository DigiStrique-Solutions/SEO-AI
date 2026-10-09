"""Replace stock PDP openings with varied, source-backed product introductions."""

import collections
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
PRIOR = ROOT.parent / "20261007-added-active-pdp-final-review" / "revised.json"
source = json.loads(PRIOR.read_text(encoding="utf-8"))
out = copy.deepcopy(source)

def product_parts(facts, old_first):
    noun = facts["noun"]
    plural = noun in {"culottes", "trousers", "shorts", "pyjama bottoms", "track pants"}
    determiner = "these" if plural else "this"
    pattern = {"CHECK": "checked", "PRINT": "printed", "STRIPE": "striped"}.get(facts["pattern"], "")
    if pattern and " " + pattern + " " not in " " + old_first.lower() + " ":
        pattern = ""
    display_colour = {"darkgreen": "dark green", "dk green": "dark green", "dk olive": "dark olive", "dark-grey": "dark grey"}.get(facts["colour"], facts["colour"])
    words = [determiner, facts["gender"] + "'s", display_colour, pattern, noun]
    subject = " ".join(word for word in words if word)
    fit = {"barrel leg": "barrel-leg cut", "wide leg": "wide-leg cut", "a line": "A-line shape"}.get(facts["fit"], facts["fit"])
    fit_with_article = ("an" if fit.startswith("A-") else "a") + " " + fit
    return subject, subject[0].upper() + subject[1:], fit_with_article, "have" if plural else "has", "combine" if plural else "combines", "are" if plural else "is", "come" if plural else "comes"

def removable_feature(details, fit):
    first, sep, rest = details.partition(". ")
    if not sep or not rest.strip() or rest.startswith(("Machine wash", "Hand wash")):
        return None
    first += "."
    fragment = None
    for prefix in ("It has ", "They have ", "It features ", "They feature "):
        if first.startswith(prefix):
            fragment = first[len(prefix):-1]
            break
    if fragment is None:
        m = re.fullmatch(r"A (.+) is paired with (.+)\.", first)
        if m:
            fragment = "a " + m.group(1) + " and " + m.group(2)
    if not fragment or len(fragment) > 85:
        return None
    # The fit is already stated in the first paragraph; do not state it twice.
    if any(word in fragment.lower() for word in ("barrel-leg", "wide-leg", "regular fit", "slim fit")):
        return None
    return fragment, rest

used_first = set()
changes = []
template_counts = collections.Counter()
for item in out:
    row = item["row"]
    intro, details, styling, product_id = item["after"].split("\n\n")
    first_old, fabric_sentence, surface_sentence = intro.split(". ", 2)
    first_old += "."
    facts = item["facts"]
    subject, subject_cap, fit, verb, combine_verb, be_verb, come_verb = product_parts(facts, first_old)
    feature = removable_feature(details, facts["fit"])
    feature_choices = []
    if feature:
        fragment, remaining = feature
        feature_choices = [
            ("feature-first", f"With {fragment}, {subject} {verb} {fit}.", remaining),
            ("feature-after-fit", f"{subject_cap} {verb} {fit}, along with {fragment}.", remaining),
            ("feature-combined", f"{subject_cap} {combine_verb} {fragment} with {fit}.", remaining),
            ("feature-paired", f"{subject_cap} pair{'s' if verb == 'has' else ''} {fit} with {fragment}.", remaining),
            ("feature-cut", f"Cut in {fit}, {subject} {verb} {fragment}.", remaining),
            ("feature-in-fit", f"In {fit}, {subject} {verb} {fragment}.", remaining),
        ]
    generic_choices = [
        ("direct-fit", f"{subject_cap} {verb} {fit}.", details),
        ("fit-defines", f"{fit[0].upper() + fit[1:]} defines {subject}.", details),
        ("cut-for", f"{subject_cap} {be_verb} cut for {fit}.", details),
        ("comes-in", f"{subject_cap} {come_verb} in {fit}.", details),
        ("designed-with", f"{subject_cap} {be_verb} designed with {fit}.", details),
        ("fit-shapes", f"{fit[0].upper() + fit[1:]} shapes {subject}.", details),
    ]
    digest = hashlib.sha256(item["code"].encode()).digest()
    seed = int.from_bytes(digest[:4], "big")
    choice_seed = int.from_bytes(digest[4:8], "big")
    prefer_feature = bool(feature_choices) and seed % 5 < 3
    preferred = feature_choices if prefer_feature else generic_choices
    fallback = generic_choices if prefer_feature else feature_choices
    ordered = preferred[choice_seed % len(preferred):] + preferred[:choice_seed % len(preferred)] if preferred else []
    if fallback:
        ordered += fallback[choice_seed % len(fallback):] + fallback[:choice_seed % len(fallback)]
    choice = next(((label, sentence, remainder) for label, sentence, remainder in ordered if sentence not in used_first), None)
    if choice is None:
        choice = ordered[0]
    label, first_new, details_new = choice
    used_first.add(first_new)
    template_counts[label] += 1
    intro_new = " ".join((first_new, fabric_sentence + ".", surface_sentence))
    after = "\n\n".join((intro_new, details_new, styling, product_id))
    assert after != item["after"]
    item["after"] = after
    item["words"] = len(after.split("Product ID:")[0].split())
    changes.append({"row": row, "code": item["code"], "template": label, "feature_moved": bool(feature and details_new != details)})

(ROOT / "revised.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "changes.json").write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"rows": len(out), "unique_first_sentences": len(used_first),
                  "feature_moved": sum(c["feature_moved"] for c in changes),
                  "templates": dict(template_counts),
                  "body_words": [min(x["words"] for x in out), sorted(x["words"] for x in out)[len(out)//2], max(x["words"] for x in out)]}, indent=2))
