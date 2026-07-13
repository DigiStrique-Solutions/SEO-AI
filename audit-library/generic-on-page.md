# Generic On-Page SEO — Audit Definition

**ID:** `generic-on-page` · **Scope:** per URL · **Pairs with:** [generic-on-page.json](generic-on-page.json)

## What it checks
Baseline on-page hygiene every indexable page should pass before anything fancier matters.

| Section | Items |
|---------|-------|
| Titles & Meta | Unique `<title>` (30–60 chars) · meta description (70–160 chars) |
| Headings | Exactly one H1 · logical heading order |
| Media, Canonicals & Status | Image alt text · valid canonical · HTTP 200 |

## Why it matters
These are the cheapest, highest-certainty wins. A missing title, a double H1, or a broken canonical quietly caps how well a page can ever rank — and they're trivial to fix.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**. Score = passed weight ÷ applicable weight.

## Output
- `audits/generic-on-page.json` — one row per item: `status` (pass/fail/not_applicable), `result`, `next_action`.
- Rolled into `audits/summary.json` as `{ items, pass, fail, not_applicable, score }`.
