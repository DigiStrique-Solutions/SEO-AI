# Checklist — Authenticity Gate

Load this when the task is to produce, rewrite, or approve **publish-ready customer-facing copy**.
It gates *claims*, not style. Style/AI-pattern review lives in `ai-pattern-review.md`.

The gate is enforced mechanically by the harness (`verify-authenticity` / `write-content`, threshold `< 20`).
This checklist is what you verify **before** and **around** that command — the harness cannot judge whether a claim is source-backed; you must.

## A. Evidence logged (do this first)

Every claim in the draft must trace to a logged source in the authenticity log.

- [ ] **Authenticity log exists** — created via `init-authenticity --target <target>`.
- [ ] **Every source recorded** with `source_id`, `source_type`, `source_ref`, and extracted facts.
      Allowed `source_type`: `brand_dna` · `gsc` · `product_page` · `competitor_page` · `serp` · `customer_note` · `human_context` (add PostHog-backed notes as `human_context` when claiming behavior/engagement/conversion).
- [ ] **Smallest sufficient set** — only sources that actually prove the claims being made; don't log filler.

## B. Claim gating (block until each is source-backed)

Every item below is `pass` only with a matching logged source. If unbacked → rewrite the claim out, soften to what's provable, or mark `[needs source]`. **Never invent.**

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

`ship` — all claims backed, score `< 20`.
`fix` — backed but score `>= 20` or pattern issues (send to `ai-pattern-review.md`).
`block` — publish-ready was requested but required claims are unbacked or evidence is missing.
