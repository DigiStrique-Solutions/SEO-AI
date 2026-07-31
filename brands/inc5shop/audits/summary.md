# SEO Audit Summary — Inc.5 (inc5shop.com)

> **Latest off-page review (2026-07-31):** A partial backlink audit verified 13 page-level links, one asset hotlink and five high-relevance unlinked media mentions. Canonical/www/legacy-domain consolidation passes. Profile-wide quality, anchors, velocity, lost links, manual-action status and competitor gaps remain blocked without a row-level backlink export and Search Console access. See `backlink-audit-20260731.json`.

> **Latest technical crawl (2026-07-23):** Screaming Frog found 11 verified issue groups, led by 351 sitemap collections (88 conservative review candidates), 1,117 images over 100 KB, missing image attributes, a broken app JavaScript asset and indexable `/cart`. The crawl is **partial** because 712 HTML requests were throttled with HTTP 429. See `technical-screamingfrog-20260723.md`.

**Run date:** 2026-07-13 · **Target:** https://inc5shop.com · **Overall score: 0.75** (avg of 5 scored audits)
**Totals:** 38 items — 24 pass · 7 fail · 7 not_applicable
**Evidence:** Firecrawl rendered checks (homepage, collection, PDP), robots.txt, sitemap.xml, llms.txt, and GSC query/page data (300 queries / 100 pages). Provenance: `logs/audits/raw/20260713T095500Z-site-checks.json`.

> **Core Web Vitals is BLOCKED** — no CrUX/PageSpeed/Lighthouse is connected, so all 6 CWV items are `not_applicable` and the audit is unscored and excluded from the overall. This is **not** a pass; CWV is currently unmeasured.

## Scores by audit

| Audit | Score | Pass | Fail | N/A |
|-------|:-----:|:----:|:----:|:---:|
| Content SEO | 0.86 | 6 | 1 | 0 |
| Site Architecture & Technical SEO | 0.82 | 6 | 1 | 0 |
| AI SEO / AEO / GEO | 0.73 | 4 | 1 | 1 |
| Generic On-Page SEO | 0.71 | 5 | 2 | 0 |
| Structured Data & Schema | 0.64 | 3 | 2 | 0 |
| Core Web Vitals & Performance | — (blocked) | 0 | 0 | 6 |

## Top fixes (ranked)

| # | Severity | Audit | Fix |
|---|----------|-------|-----|
| 1 | **high** | structured-data | Add Organization + WebSite JSON-LD (name, url, logo, sameAs, SearchAction) to the homepage. |
| 2 | **high** | ai-seo-aeo-geo | Define the brand entity for AI — Organization schema + consistent "Inc.5" naming to fix "5 inch"/"inch 5" confusion. |
| 3 | **high** | site-architecture | Noindex/unpublish 100+ dated "dark" collections; scope the sitemap to canonical shoppable collections. |
| 4 | **high** | generic-on-page | Fix multiple H1s on the homepage (nav category labels are `<h1>`); keep one descriptive H1. |
| 5 | **high** | core-web-vitals | Connect PageSpeed/CrUX — LCP/INP/CLS are currently unmeasured. |
| 6 | medium | generic-on-page | Add alt text to homepage banner images (8/11 missing) and flagged collection images. |
| 7 | medium | content-seo | Add author bylines/bios to blog posts for topical E-E-A-T. |
| 8 | low | structured-data | Add BreadcrumbList schema to collection and product templates. |
| 9 | low | core-web-vitals | Serve hero banners as WebP/AVIF and lazy-load below the fold. |

## What's strong

- **Product schema is rich** — PDPs emit valid Product markup with offers, INR price, availability, brand, and aggregateRating/reviewCount (merchant-listing eligible).
- **Category pages are well-optimized** — good unique titles/meta, self-canonicals, intent-rich intro copy, breadcrumb nav, and rel next/prev pagination.
- **Crawl hygiene basics** — robots.txt handles Shopify crawl traps; sitemap index is valid and includes `sitemap_agentic_discovery.xml`.
- **AI-visibility foundation** — valid `llms.txt` (Shopify UCP) + AI crawlers unblocked + agentic-discovery sitemap.
- **Demand is large and winnable** — head terms like *heels for women* (495k impr) and *sandals for women* (421k impr) rank ~pos 5–9; on-page + schema fixes should lift them into the top 3. Biggest CTR gap: *shoulder bags for women* (79k impr, 31 clicks).

## What's blocked / needs connection

- **Core Web Vitals** — connect PageSpeed Insights + CrUX (field) and Lighthouse (lab) to score LCP/INP/CLS/TTFB.
- **AI mentions** — run manual brand-visibility prompt checks in ChatGPT/Perplexity/AI Overviews.
- **GSC sitemap submission** & **homepage canonical** — quick verifications flagged in the relevant audits.

See per-audit files in this folder (`generic-on-page.json`, `content-seo.json`, `site-architecture.json`, `core-web-vitals.json`, `structured-data.json`, `ai-seo-aeo-geo.json`) for item-level status, evidence, and next actions.
