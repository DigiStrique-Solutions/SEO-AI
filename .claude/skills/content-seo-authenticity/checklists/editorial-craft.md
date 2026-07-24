# Checklist — Editorial Craft

Load this when the task is to **produce or approve publish-ready customer-facing copy**, before `authenticity-gate.md`.

This is the only checklist that asks whether the draft is **good**. The others ask whether it is **wrong**.
Those are different questions, and a draft that clears every other gate can still be unpublishable.

Requires the voice contract from Step 0 (`references/brand-voice-contract.md`). Without it, skip to Step 0 — you cannot review voice against nothing.

> **Why this exists.** A draft that satisfies every prohibition and no positive standard converges on one register: short, flat, hedged, evidence-dense, structurally repetitive — an audit table set in prose. Reviewers describe it as *"reads like a product manual"*, *"lacks personality"*, *"the men's and women's sections are identical"*, *"focuses on what the products don't claim"*. Each of those is a craft failure with a check below.

## P1 — blocks publish (same weight as a failed authenticity gate)

### Voice

- [ ] **Matches the brand's voice contract** — the register in `brand_voice.description` is actually on the page, not just cited in the plan. Read the draft aloud against it.
- [ ] **Uses the brand's own patterns** — the specific framing, community language and proof points in `voice_patterns` appear where they fit. Not sprinkled as slogans; load-bearing.
- [ ] **Honors `knowledge.md` voice rules** — including its *prohibitions* (e.g. "avoid generic hype", "cite real tech names").
- [ ] **Could not be swapped to a competitor** by find-and-replacing the brand name. If it could, there is no voice on the page.

### Substance

- [ ] **The reader gets what the headline promised** — and the promise is specific enough to make.
- [ ] **Category payload is present** — the thing a reader of *this* genre came for. For fashion/lifestyle/athleisure: **styling and outfit ideas, occasions, what it goes with**. A guide that never says how to wear the thing has not done its job.
- [ ] **Products are woven in, not bolted on** — each mention earns its place by answering the reader's live question. If a product name could be deleted without loss, delete it.
- [ ] **Concrete over abstract** — real mechanisms, names, occasions, customer language. Not benefit-stacking.

### Structure

- [ ] **Sections earn their place.** Every section makes a point the others don't. **No parallel scaffolding** — do not template one section per segment (men's / women's, beginner / advanced) and swap the nouns. If two sections differ only in product names, merge them or give each a genuinely different job. *(Mechanically checked: `craft-report` → `near_duplicate_sections`.)*
- [ ] **Ideas advance, they don't recur.** Each point is made once, in the place it belongs. Re-explaining a caveat in three sections is the clearest symptom of a draft with no spine.
- [ ] **The hook creates a reason to keep reading** — a specific scene, tension or stake, not a definition of the topic.
- [ ] **Transitions carry the argument** — sections connect. Removing every connective to dodge "formulaic transitions" leaves a list of assertions; that is a different failure, not a fix.
- [ ] **Paragraphs are as long as their idea, and no longer.**

### Stance

- [ ] **No defensive hedging in reader-facing copy.** No "the brand doesn't claim", "we can't verify", "check the product page". A reader cannot act on our evidence gaps. Unbacked → cut and pivot (`authenticity-gate.md` §B); the caveat goes to the authenticity log. *(Mechanically checked: `craft-report` → `defensive_hedging`.)*
- [ ] **No unresolved markers** — `[needs source]` and friends are drafting scaffolding. One in published copy is a hard fail. *(Mechanically checked: `craft-report` → `unresolved_placeholder`.)*

### House style

- [ ] **No en dashes (`–`) or em dashes (`—`). Ever.** Including ranges: "sizes 12-14" or "12 to 14", never "12–14". *(Mechanically checked: `craft-report` → `en_em_dash`; one is a hard fail.)*
      **Fix it by recasting, not substituting.** An em dash usually joins two thoughts that want to be two sentences, or fences an aside that wants parentheses. Swapping every `—` for a comma produces long limp sentences and is a worse draft than the one you started with. Read the sentence, decide what the dash was doing, then rebuild it: full stop if the second half is its own thought, colon if it delivers a payoff, parentheses if it's genuinely an aside, comma only if it's a light apposition.
- [ ] **Written from what we know, not around what we don't.** The draft's centre of gravity is the reader's problem and the brand's real strengths — not the perimeter of our evidence.

## P2 — fix before shipping

- [ ] Opening lines of consecutive sections vary in shape.
- [ ] Verbs are specific; weak verb + abstract noun replaced with the real action.
- [ ] Scannable structure preserved for SEO and AI search (but not written "for AI" separately).
- [ ] The ending helps the reader decide or act.

## Output for this review

```text
Verdict: pass | fix | block
Voice contract used:     # file + the patterns actually applied
Craft findings:          # failed P1/P2 items, each with the line or section
Concrete fixes:          # what to change, not "add personality"
Craft score:             # craft-report score + features (a pass is not a verdict)
```

`block` — any P1 fails. A draft that is accurate, on-topic, under 20 on both scores and **boring** is `block`, not `ship`.

## Reviewing this checklist honestly

Do not report a craft item as passing because the harness score is low. `craft-report` measures two things: hedging density and cloned sections. Voice, hook, spine, payload and product integration are **not measured anywhere** — they are yours to judge, and they are the ones reviewers complain about first.
