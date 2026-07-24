---
name: content-seo-authenticity
description: Use when auditing, rewriting, or producing SEO content that must be source-backed, brand-voice aligned, less likely to trigger detector concerns, and publish-ready. Trigger for content SEO, humanization, ZeroGPT or GPTZero concerns, AI plagiarism concerns, content authenticity, blog or landing page refreshes, and Strique content recommendations.
---

# Content SEO Authenticity

Strique-local skill for content SEO where the output must **read like the brand wrote it**, stay factual, and hold up in editorial review.
Keep this file lean — it routes. Load the **one** checklist/reference the current task needs; don't read everything up front.

Two things have to be true at once, and the second is the one that gets dropped:

1. **Nothing is invented.** Every claim traces to a logged source.
2. **Someone wants to read it.** In the brand's voice, with a spine, earning each section.

A draft that satisfies only (1) is a compliance artifact, not content. It will pass the harness and fail the reader.
Accuracy is a floor, not the goal — never trade (2) away to buy (1). The gates below only detect *bad*; they cannot make a draft good.

## Step 0 — Brand Context Protocol (before writing a word)

Not optional, and not the same as gathering evidence. Per `CLAUDE.md`, any brand-related action loads the brand's own files first:

1. **`brands/<brand_id>/context.md`** — the index; tells you what else to load.
2. **`brands/<brand_id>/knowledge.md`** — brand-specific rules **override generic defaults**. This is where sanctioned mechanisms, proprietary tech names, market and platform constraints live.
3. **`brands/<brand_id>/brand-dna.json`** — read `brand_voice`, `voice_patterns`, `brand_aesthetic`, `target_audience`. These are a **style contract**, not just facts.

Then write the voice contract down before drafting (`references/brand-voice-contract.md`).

**Why this step exists.** A monsoon activewear draft once hedged for paragraphs about unverified "quick-dry" fabric claims while the brand's own `knowledge.md` named the approved mechanism — `Wiktech®`, "faster moisture evaporation" — and instructed *"cite real tech names; avoid generic hype."* The answer was on disk. Nobody read it. **Hedging is usually an unread-file bug, not an evidence gap.**

If a brand file contradicts your prior, the file wins — surface the discrepancy rather than writing around it.

## Pick the task, load only what it needs

| Task | Load (checklist) | Load (reference) | Main harness step |
|---|---|---|---|
| Produce / approve publish-ready copy | `checklists/editorial-craft.md` + `checklists/authenticity-gate.md` | `references/brand-voice-contract.md` · `references/harness-commands.md` | `write-content` |
| Review copy for AI-pattern / humanize | `checklists/ai-pattern-review.md` | `references/ai-pattern-signals.md` | `verify-authenticity` |
| Assess on-page content quality | `checklists/content-seo-onpage.md` | — (uses `audit-library/content-seo`) | evaluate `audit-library/content-seo` (brand-setup Phase 4) |

A full content rewrite uses them in order: on-page → **editorial-craft** → authenticity-gate → ai-pattern-review.

## Non-negotiables (always apply)

- **Never invent** sources, stats, prices, results, rankings, reviews, quotes, or competitor claims.
- **Unbacked → cut and pivot.** The claim leaves the copy; the narrative moves to something that needs no claim. Caveats go in the authenticity log, **never in front of the reader**. `[needs source]` is a *drafting* marker — a published draft containing one is a failure, not a hedge (`authenticity-gate.md` §B).
- **Not everything is a claim.** Reader experience, styling advice and editorial judgement need no source (`authenticity-gate.md` §0). Treating all prose as claim-space is what makes copy read like a product manual.
- **Never use an en dash (`–`) or em dash (`—`) in customer-facing copy.** No exceptions, ranges included: write "sizes 12-14" or "12 to 14", never "12–14". Recast the sentence with a comma, colon, parentheses, or a full stop — an em dash is almost always joining two thoughts that read better as two sentences. House rule, mechanically enforced (`craft-report` → `en_em_dash`); a single one blocks. Applies to the deliverable, not to internal notes, checklists or logs.
- **Never beat a detector** by adding errors, filler, awkward phrasing, or fake anecdotes. Fix by adding source-backed specificity.
- Detector scores are weak signals, not proof of authorship or publish-readiness. Working target `< 20`, never a promise.

## The main task: generate, then gate through the harness

Generation is not done until it passes the harness. Steps are discrete tools — call what you need, in order
(full signatures in `references/harness-commands.md`):

1. **Step 0** — Brand Context Protocol above; write the voice contract.
2. **Scope** — target page, reader, primary + secondary keywords, intent, desired action.
3. **`init-authenticity --target <target>`** — start the log; record every source used (`source_id`, `source_type`, `source_ref`, facts).
4. **Gate claims** — every stat / superlative / proof / performance / comparison claim needs a logged source (`authenticity-gate.md`).
5. **Write** to the voice contract, against `checklists/editorial-craft.md`.
6. **`verify-authenticity --rewrite-file <draft>`** — read-only. Reports `ai_text_risk` (gate at `< 20`) and `craft` (report-only here).
7. **`zerogpt-check` (always run)** — external detector note on every publish-ready draft, weak signal only. Falls back to the local score if unreachable; a fallback note still satisfies the step.
8. **`write-content --draft-file <draft> --content-output <final> --authenticity <log>`** — the gated publish step. Writes only when claims check out, `ai_text_risk < 20`, **and** `craft < 20`.

**What the harness cannot see:** voice, hook, narrative, whether a section earns its place, whether the reader got what the headline promised. `craft-report` catches hedging and cloned sections — the two failures worth automating. Everything else in `editorial-craft.md` is your judgement, and a passing score is not a verdict.

## Inputs to gather (smallest set that proves the claims)

Brand context (Step 0 — always) · target-URL crawl (Firecrawl/Playwright) · site evidence manifest / URL inventory ·
GSC queries & pages · keyword universe / tracker · PostHog behavior evidence (engagement/funnels/conversion) ·
SERP or competitor pages (comparison/gap claims) · human notes (sales, support, founders, SMEs) ·
the brand's own published posts (`blogs/references/` + their `voice_notes`) as the voice corpus.

## Output shape

```text
Verdict: ship | fix | block
Target URL:
Primary keyword:
Intent:
Voice contract:         # brand_voice/voice_patterns applied, and the source file
Evidence used:
Content SEO findings:
Craft findings:         # voice, spine, section differentiation, hook, payload
Authenticity risks:
Recommended edits:
Detector notes:
Next action:
```

Use `block` when publish-ready is requested but concrete evidence is missing, required claims are unsupported, or a recorded `ai_text_risk`/`craft` score is `>= 20`.

## Definition of done

Brand context loaded and voice contract written · every factual claim traces to a logged source ·
no caveat or `[needs source]` marker survives into reader-facing copy · `editorial-craft.md` passed on judgement, not just score ·
`write-content` passed at `ai_text_risk < 20` **and** `craft < 20` ·
on-page assessment used `audit-library/content-seo` (not a re-listed copy) · output follows the shape above.

AI detector scores are weak editorial signals — never proof of authorship, and never the reason a draft is good.
