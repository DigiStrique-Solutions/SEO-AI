# SEO Audit — OFFLIMITS (offlimits.co.in)

**Run:** 2026-07-13 · **Platform:** Shopify · **Scope:** in-depth, evidence-backed · **Overall (verifiable): 0.81**

> Score is a weighted pass ratio over **verifiable** items. 5 items are blocked (field Core Web Vitals ×3, GSC indexation ×1, AI-mentions ×1) and excluded — this is a **partial** full-audit until GSC + a PageSpeed/CrUX key are connected. Templates sampled: homepage, product (STRATA-01), collection (men-running-shoes), blog (styling-sneakers).

## Summary

OFFLIMITS is a technically **above-average Shopify D2C** for SEO. Crawlability, canonicalization, redirects, and schema coverage are genuinely strong — and its **AI/AEO readiness is a standout** (FAQPage schema on collections + blogs, an `llms.txt`, an agentic-discovery sitemap, and UCP/MCP endpoints). The value is being left on the table in three places: **performance (app/JS bloat)**, **product-page title tags at catalog scale**, and **image alt text**. Content is competent but leans promotional with a placeholder blog author, which caps E-E-A-T and AI-citation potential.

## Scorecard

| Audit | Score | Pass / Fail / Blocked |
|-------|-------|-----------------------|
| Site Architecture & Technical SEO | 1.00 *(partial)* | 6 / 0 / 1 |
| Content SEO | 0.86 | 6 / 1 / 0 |
| Structured Data & Schema | 0.82 | 4 / 1 / 0 |
| AI SEO / AEO / GEO | 0.82 *(partial)* | 4 / 1 / 1 |
| Generic On-Page SEO | 0.71 | 5 / 2 / 0 |
| Core Web Vitals & Performance | 0.40 *(partial, lab only)* | 1 / 2 / 3 |
| **Totals** | **0.81** | **26 / 7 / 5** |

## What's strong (keep)

- **Technical foundation** — single canonical host, http→https & www→non-www single-hop 301s, real 404s, valid robots.txt that blocks only faceted/checkout URLs, healthy sitemaps (1,516 products · 122 collections · 68 blogs · 17 pages).
- **Schema** — OnlineStore entity (logo, sameAs×5, address, contact, return policy); Product with full offers; FAQPage + Article + BreadcrumbList. Above typical Shopify.
- **AEO/AI readiness** — FAQ structures, `llms.txt`, agentic-discovery sitemap, unblocked AI crawlers.

## Priority fixes

1. **[High] Cut performance bloat** — homepage pulls 332 resources / **181 script requests** / 40 stylesheets (GoKwik, Snapmint, flash-speed, cdnjs, googleapis). Audit Shopify apps, defer/async non-critical JS, consolidate + inline critical CSS. *(Root cause behind likely-weak field LCP/INP.)*
2. **[High] Product title tags** — PDP titles are ~27 chars with no keyword or brand (e.g. `STRATA-01 - DARK BEIGE/NAVY`). Rewrite the pattern across ~1,516 products to `{Product} – {Type} for {Men/Women} | Off Limits`.
3. **[Medium] Image alt text** — ~50% of storefront images lack alt (home 55/113, collection 27/38, PDP 9/27). Map product-image alt to `{Product} {color} – {type}`.
4. **[Medium] Review-star schema** — add `aggregateRating`/`Review` to Product for review-star rich results (highest-CTR ecommerce enhancement); add WebSite `SearchAction` for the sitelinks searchbox.
5. **[Medium] Blog E-E-A-T** — replace placeholder author `SEO .` with real named authors + bios; add credible outbound citations to earn AI-engine trust/citations.
6. **[Low] Lazy-load + entity name** — only 2/113 homepage images lazy-load; standardize one brand spelling (`OFF LIMITS` / `Offlimits` / `Off Limits`) across titles, og, schema, socials.

## Data-quality flags

- **Broken analytics:** `analytics.gokwik.co` fails DNS (`ERR_NAME_NOT_RESOLVED`) — tracking may be dropping data.
- Theme JS null-reference errors on the blog template + a Snapmint popup error — non-blocking but worth cleaning.

## Blocked — needs connection before it can be verified

| Item | Why blocked | Unblock |
|------|-------------|---------|
| Field CWV (LCP/INP/CLS) | No CrUX/PSI key (PageSpeed 429), no GSC | Add PageSpeed/CrUX API key **or** connect GSC via Composio |
| Indexation coverage | GSC not connected | Connect Search Console via Composio |
| AI mentions | Manual prompt testing not run | Run AI-visibility prompt set across ChatGPT/Perplexity/AI Overviews |
| Keyword demand (exact volumes) | `GOOGLE_ADS_PLATFORM_ID` unset; no GSC fallback | Set platform-id for Keyword Planner or connect GSC |

## Provenance

- Crawl/render evidence → `logs/web_data/raw/20260713T113000Z-site-crawl.json`, `logs/web_data/activity.jsonl`
- Audit checks → `logs/audits/raw/20260713T113500Z-site-checks.json`, `logs/audits/activity.jsonl`
- Definitions → `audit-library/` (6 audits)
