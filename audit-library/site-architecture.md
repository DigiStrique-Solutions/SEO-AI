# Site Architecture & Technical SEO — Audit Definition

**ID:** `site-architecture` · **Scope:** per site · **Pairs with:** [site-architecture.json](site-architecture.json)

## What it checks
Whether search engines can crawl, understand, and index the site at all.

| Section | Items |
|---------|-------|
| Crawlability | Valid robots.txt · current, submitted XML sitemap |
| Structure | Clean URLs · no orphan pages / shallow depth · no redirect chains |
| Indexation | Consistent canonicalization · important pages indexed, none wrongly noindexed |

## Why it matters
This is site-wide, not per-page. One bad robots rule, a canonical conflict, or an accidental noindex can suppress hundreds of pages at once — the highest-blast-radius problems in SEO.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**.

## Output
- `audits/site-architecture.json` — findings rows.
- Rolled into `audits/summary.json`.
