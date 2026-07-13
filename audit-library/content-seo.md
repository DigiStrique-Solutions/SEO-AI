# Content SEO — Audit Definition

**ID:** `content-seo` · **Scope:** per URL · **Pairs with:** [content-seo.json](content-seo.json)

## What it checks
Whether the page's *content* earns the ranking — not just its tags.

| Section | Items |
|---------|-------|
| Purpose & Intent | One primary purpose · matches search intent of target keyword |
| Depth & Quality | Comprehensive coverage · natural keyword coverage · freshness |
| E-E-A-T & Linking | Experience/expertise signals · relevant internal links |

## Why it matters
On-page tags get a page *eligible*; content is what actually competes. Thin pages, intent mismatches, and missing expertise signals are the most common reasons good keywords never rank.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**.

## Output
- `audits/content-seo.json` — findings rows.
- Rolled into `audits/summary.json`.

## Uses
Pulls target keywords/intent from the brand's [keywords/](../brands/_template/keywords/) data to judge intent match and coverage.
