---
name: content-seo-authenticity
description: Use when auditing, rewriting, or producing SEO content that must be source-backed, brand-voice aligned, less likely to trigger detector concerns, and publish-ready. Trigger for content SEO, humanization, ZeroGPT or GPTZero concerns, AI plagiarism concerns, content authenticity, blog or landing page refreshes, and Strique content recommendations.
---

# Content SEO Authenticity

Strique-local skill for content SEO where the output must sound human, stay factual, and hold up in editorial review.
Keep this file lean — it routes. Load the **one** checklist/reference the current task needs; don't read everything up front.

## Non-negotiables (always apply)

- Detector scores are weak signals, not proof of authorship or publish-readiness. Working target `< 20`, never a promise.
- Never invent sources, stats, prices, results, rankings, reviews, quotes, or competitor claims. Missing → `[needs source]`.
- Never beat a detector by adding errors, filler, awkward phrasing, or fake anecdotes. Fix by adding source-backed specificity.
- Publish-ready content needs concrete evidence in the authenticity log, or the missing source is marked.

## Pick the task, load only what it needs

| Task | Load (checklist) | Load (reference) | Main harness step |
|---|---|---|---|
| Produce / approve publish-ready copy | `checklists/authenticity-gate.md` | `references/harness-commands.md` | `write-content` |
| Review copy for AI-pattern / humanize | `checklists/ai-pattern-review.md` | `references/ai-pattern-signals.md` | `verify-authenticity` |
| Assess on-page content quality | `checklists/content-seo-onpage.md` | — (uses `audit-library/content-seo`) | evaluate `audit-library/content-seo` (brand-setup Phase 4) |

A full content rewrite uses all three in order: on-page → authenticity-gate → ai-pattern-review.

## The main task: generate, then gate through the harness

Generation is not done until it passes the harness. The harness steps are discrete tools — call only what you need, in order
(full signatures in `references/harness-commands.md`):

1. **Scope** — target page, reader, primary + secondary keywords, intent, desired action.
2. **`init-authenticity --target <target>`** — start the log; then record every source used (`source_id`, `source_type`, `source_ref`, facts).
3. **Gate claims** — before rewriting, every stat / "best" / proof / performance / comparison claim needs a logged source (`checklists/authenticity-gate.md`).
4. **Write / rewrite** using concrete source detail; preserve useful SEO structure, cut generic phrasing.
5. **`verify-authenticity --rewrite-file <draft> --max-ai-detector-score 20`** — read-only gate; loop on `ai_text_risk.score` until `< 20`.
6. **`zerogpt-check` (always run)** — record an external detector note on every publish-ready draft, as a weak signal only. Falls back to the local score if ZeroGPT is unreachable; a fallback note still satisfies the step.
7. **`write-content --draft-file <draft> --content-output <final> --authenticity <log> --max-ai-detector-score 20`** — the gated publish step; writes only when checks pass and score `< 20`.

## Inputs to gather (smallest set that proves the claims)

Brand DNA + product-marketing context · target-URL crawl (Firecrawl/Playwright) · site evidence manifest / URL inventory ·
GSC queries & pages · keyword universe / tracker · PostHog behavior evidence (engagement/funnels/conversion) ·
SERP or competitor pages (comparison/gap claims) · human notes (sales, support, founders, SMEs).

## Output shape

```text
Verdict: ship | fix | block
Target URL:
Primary keyword:
Intent:
Evidence used:
Content SEO findings:
Authenticity risks:
Recommended edits:
Detector notes:
Next action:
```

Use `block` when publish-ready is requested but concrete evidence is missing, required claims are unsupported, or a recorded score is `>= 20`.

## Definition of done

Every factual claim traces to a logged source · `verify-authenticity`/`write-content` passed at `< 20` ·
on-page assessment used `audit-library/content-seo` (not a re-listed copy) · output follows the shape above.
