# Checklist — Authenticity Gate

Load this when the task is to produce, rewrite, or approve **publish-ready customer-facing copy**.
It gates *claims*. Craft lives in `editorial-craft.md`; AI-pattern review in `ai-pattern-review.md`.

The gate is enforced mechanically by the harness (`verify-authenticity` / `write-content`, threshold `< 20`).
This checklist is what you verify **before** and **around** that command — the harness cannot judge whether a claim is source-backed; you must.

## §0. First: is this even a claim?

Read this before §B or you will gate the whole draft and strangle it.

**Claim-space (needs a logged source):**
product specs, materials, performance, prices, availability · statistics and counts · superlatives and comparisons · customer proof · results.

**Not claim-space (needs no source, gate it and the copy dies):**

| Prose | Example |
|---|---|
| **Reader experience** — what the reader already lives | "A soaked cotton tee stays soaked all morning." |
| **Styling and editorial judgement** — the writer's job | "Go dark on the colour through the monsoon; it hides the splashes." |
| **Occasions and use cases** | "Wear it for the commute, not the wedding." |
| **Category common knowledge** | "A wide heel base is steadier than a stiletto point." |
| **Brand-sanctioned mechanisms** — already approved in `knowledge.md` | `Wiktech®` — "faster moisture evaporation" |

That last row matters most: **check `knowledge.md` before declaring an evidence gap.** The sanctioned answer is often already on disk, and hedging about it is an unread-file bug, not caution.

Treating all prose as claim-space is what makes a draft read like a product manual. Universal human experience is not a statistic.

## A. Evidence logged (do this first)

Every claim in the draft must trace to a logged source in the authenticity log.

- [ ] **Authenticity log exists** — created via `init-authenticity --target <target>`.
- [ ] **Every source recorded** with `source_id`, `source_type`, `source_ref`, and extracted facts.
      Allowed `source_type`: `brand_dna` · `gsc` · `product_page` · `competitor_page` · `serp` · `customer_note` · `human_context` (add PostHog-backed notes as `human_context` when claiming behavior/engagement/conversion).
- [ ] **Smallest sufficient set** — only sources that actually prove the claims being made; don't log filler.

## B. Claim gating (block until each is source-backed)

Every item below is `pass` only with a matching logged source — but only if §0 says it's a claim at all.

### When a claim is unbacked: cut and pivot

**Never invent.** And never hedge at the reader. In order:

1. **Check `knowledge.md` first** — the brand may already sanction the mechanism. Then it's backed, and you cite it by name.
2. **Cut it.** The claim leaves the copy entirely.
3. **Pivot.** Move to something that needs no claim (§0) — reader experience, styling, occasion — and keep the narrative moving.
4. **Log it.** The caveat goes in the authenticity log, and the gap in `open_questions`. **Not in front of the reader.**

**Do not "soften to what's provable" in the copy.** That is how a draft ends up describing what the products *don't* claim — "the page doesn't state it's quick-dry", "check the product page", "we can't verify the fabric". Softening leaves the shape of a claim we can't make, wearing a disclaimer. Readers can't act on our evidence gaps; the copy just goes cautious and cold.

`[needs source]` is a **drafting** marker. It must never survive into published copy — `craft-report` fails a draft that ships one. Resolve it, or cut the sentence.

Absence of evidence is invisible to a good reader. It should be invisible in the copy too.

- [ ] **Statistics / numbers** (traffic, %, counts, prices) — backed by `gsc`, `product_page`, or `human_context`.
- [ ] **"Best" / "top" / "leading" / superiority** — backed by explicit criteria + evidence, not asserted.
- [ ] **Customer proof / reviews / quotes** — backed by a real `customer_note` or `product_page` review.
- [ ] **Performance / results claims** — backed by analytics (`gsc`, PostHog note), not aspiration.
- [ ] **Comparisons / competitor claims** — backed by `competitor_page` or `serp` evidence.
- [ ] **Product facts** (specs, materials, variants, availability) — backed by `product_page` / `brand_dna`.

## C. Gate result

- [ ] **Harness gate run** — `verify-authenticity` (read-only) or `write-content` (writes the file) with `--max-ai-detector-score 20`.
- [ ] **Score `< 20`** — a score `>= 20` blocks publish-ready output. Do **not** lower it with errors, filler, or fake detail.
- [ ] **Detector note (always run)** — run `zerogpt-check` on **every** publish-ready draft; its result is recorded in `detector_notes` as a *weak signal*, never as proof. If ZeroGPT is unreachable (paywall/403/network), the harness falls back to the local score and records `source: local_fallback` — that fallback note satisfies this step; do **not** block publish on ZeroGPT being down.

## Verdict

`ship` — all claims backed, `ai_text_risk < 20`, `craft < 20`, and `editorial-craft.md` passed on judgement.
`fix` — backed but a score is `>= 20`, or pattern issues (→ `ai-pattern-review.md`), or craft issues (→ `editorial-craft.md`).
`block` — publish-ready was requested but required claims are unbacked or evidence is missing.

Backed and boring is not `ship`. Accuracy is the floor here, not the bar — see `editorial-craft.md`.
