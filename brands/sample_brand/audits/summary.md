# SEO Audit Summary — Sample Brand (Strique)

**Site:** https://www.strique.io · **Run date:** 2026-07-13 · **Overall score: 78 / 100**
**Totals:** 38 checks → ✅ 27 pass · ❌ 10 fail · ➖ 1 n/a

> Machine-readable version: [summary.json](summary.json). Each audit's findings are in its own file.

## Scores by audit

| Audit | Score | ✅ | ❌ | ➖ | Findings |
|-------|:-----:|:--:|:--:|:--:|----------|
| Structured Data & Schema | 91 | 4 | 1 | 0 | [structured-data.json](structured-data.json) |
| Site Architecture & Technical | 88 | 6 | 1 | 0 | [site-architecture.json](site-architecture.json) |
| Content SEO | 86 | 6 | 1 | 0 | [content-seo.json](content-seo.json) |
| AI SEO / AEO / GEO | 73 | 3 | 2 | 1 | [ai-seo-aeo-geo.json](ai-seo-aeo-geo.json) |
| Generic On-Page SEO | 71 | 5 | 2 | 0 | [generic-on-page.json](generic-on-page.json) |
| Core Web Vitals & Performance | 57 | 3 | 3 | 0 | [core-web-vitals.json](core-web-vitals.json) |

## Top fixes (ranked by impact)

| # | Fix | Audit | Severity |
|---|-----|-------|:--------:|
| 1 | Demote the secondary H1 to H2 on homepage and /product | generic-on-page | 🔴 high |
| 2 | Cut LCP from 3.1s to under 2.5s (preload hero, reduce main-thread work) | core-web-vitals | 🔴 high |
| 3 | Defer/async non-critical JS and inline critical CSS | core-web-vitals | 🟠 medium |
| 4 | Add alt text to the 16 flagged images | generic-on-page | 🟠 medium |
| 5 | Add author bylines + E-E-A-T signals to blog posts | content-seo | 🟠 medium |
| 6 | Add credible outbound citations; pursue third-party mentions | ai-seo-aeo-geo | 🟠 medium |
| 7 | Link the 3 orphan blog posts from the index / related posts | site-architecture | 🟠 medium |
| 8 | Serve WebP/AVIF responsive images, lazy-load below the fold | core-web-vitals | 🟡 low |
| 9 | Publish an llms.txt describing key pages | ai-seo-aeo-geo | 🟡 low |
| 10 | Add BreadcrumbList schema to blog and product templates | structured-data | 🟡 low |

## Where to focus
**Core Web Vitals (57)** is the weakest area and carries two high/medium performance fixes — biggest score lever. **Generic On-Page (71)** has the single highest-severity item (multiple H1) and is a quick win. Structured data, site architecture, and content are in good shape.
