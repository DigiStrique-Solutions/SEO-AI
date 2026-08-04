# Nova Dairy SEO audit summary

Run date: 4 August 2026
Target: https://steragro.com/
Run ID: `nova-dairy-audits-20260804`

## Summary

Nova Dairy's evidence-weighted audit score is **57.18/100**. This is a **partial audit**, not a complete pass: 26 of 38 rows were evaluable (68.42%), while 12 remain `not_checked_blocked` because specific Search Console audit APIs, competitor-depth benchmarking, full-crawl diagnostics, rich-result validation, AI-answer monitoring, or detailed Lighthouse diagnostics were not run.

The strongest verified signals are crawlability of robots.txt, clean sampled URLs, self-canonicals, responsive field INP, and passing field CLS. The most important verified weaknesses are slow mobile LCP/TTFB, incomplete entity schema, a broken heading hierarchy, low image-alt coverage, a product metadata mismatch, weak author/source signals, and a missing llms.txt.

## Audit scores

| Audit | Score | Pass | Fail | Blocked | Coverage note |
|---|---:|---:|---:|---:|---|
| Generic on-page | 52.94 | 3 | 4 | 0 | Fully evaluated for the sampled scope |
| Content SEO | 83.33 | 5 | 1 | 1 | Homepage cluster evaluated; competitor depth benchmark blocked |
| Site architecture | 100.00 | 2 | 0 | 5 | Only two rows evaluable; not a complete technical pass |
| Core Web Vitals | 54.55 | 2 | 2 | 2 | Field CWV available; detailed audits incomplete |
| Structured data | 25.00 | 1 | 1 | 3 | Rendered graph inspected; validators unavailable |
| AI SEO / AEO / GEO | 27.27 | 1 | 4 | 1 | AI-answer benchmark not run |

## Top findings and priority fixes

1. **High — Mobile loading is slow.** Field LCP is 3.662s and field TTFB is 1.745s; mobile Lighthouse performance is 45. Engineering should profile origin/cache/CDN latency and optimize the true LCP element. Expected impact: faster landing pages and improved page experience.
2. **High — Machine-readable entity data is incomplete.** Organization schema has no `sameAs`, uses an unverified page-primary image as its logo, and the WebSite description is empty. SEO, engineering, and brand should correct and validate the entity graph.
3. **High — The heading hierarchy is semantically broken.** The rendered homepage begins with H2/H3 and uses “Fresh Milk Collection” as the only H1. Frontend/content should make the primary proposition the H1 and nest sections consistently.
4. **Medium — Accessibility evidence shows material gaps.** Sixty-four of 94 homepage images have missing/empty alt attributes, zoom is disabled in the viewport, and the mobile Lighthouse accessibility score is 79. Frontend/content should repair image semantics and zoom behavior, then run a full accessibility audit.
5. **Medium — Product metadata is mismatched.** The Shudh Ghee URL's description talks about Dahi. SEO/content should correct it and crawl all pages for similar template or field errors.
6. **Medium — Editorial trust signals are weak.** The sampled Nutrition Centre surface has no author or source signals. Content/legal should add accountable author/reviewer information, relevant credentials, sources, and an editorial policy.
7. **Medium — AI-readiness is incomplete.** `/llms.txt` returns 404, entity schema is incomplete, and AI mentions were not benchmarked. SEO/legal/brand should first approve crawler policy and priority prompts.

## Evidence

- Rendered 20-page crawl: `logs/audits/raw/20260804T074900Z-site-crawl.json`
- Mobile PageSpeed and CrUX: `logs/audits/raw/20260804T075048Z-cwv-mobile.json`
- Rendered desktop/mobile/schema checks: `logs/audits/raw/20260804T075100Z-rendered-page-checks.json`
- robots.txt, sitemap, and llms.txt: `logs/audits/raw/20260804T075200Z-robots-sitemap-llms.json`
- Provider and coverage blockers: `logs/audits/raw/20260804T075300Z-provider-blockers.json`
- Phase 2 dependency refresh: `logs/audits/raw/20260804T081500Z-dependency-refresh.json`

## Open blockers

- The Nova Dairy Search Console property is verified with `siteOwner` permission and supplied 986 India query/page rows (649 unique queries), but run the sitemap, URL Inspection/index coverage, and enhancement-report checks before closing those rows.
- Phase 2 supplied 50 universe rows, 32 curated keywords, and 11 clusters; live competitor-depth benchmarking and AI-answer monitoring are still required for their specific rows.
- Run a complete sitemap-versus-crawl inventory with redirect chains, inbound-link counts, click depth, canonicals, and noindex signals.
- Run full Lighthouse diagnostic exports plus Schema.org Validator and Google Rich Results Test results for representative templates.
- Repeat manual mobile and accessibility checks when a supported browser/assistive-technology test surface is available.

## Expected impact

Addressing the verified performance, metadata, semantic, accessibility, and entity-schema defects should improve crawl interpretation, snippet accuracy, mobile usability, and machine understanding. Search growth impact cannot be quantified until Search Console and approved analytics are connected.
