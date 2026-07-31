# Winn Foods SEO Audit — 2026-07-27

## Summary

This is a **partial full-audit run**. Five audits have evidence-backed weighted scores; Core Web Vitals remains unscored because field and lab providers could not run. The current scored-audit average is **0.38**.

| Audit | Score | Pass | Fail | N/A | Blocked |
|---|---:|---:|---:|---:|---:|
| Generic On-Page | 0.59 | 4 | 3 | 0 | 0 |
| Content SEO | 0.55 | 3 | 2 | 2 | 0 |
| AI SEO / AEO / GEO | 0.45 | 3 | 2 | 0 | 1 |
| Site Architecture | 0.30 | 1 | 3 | 0 | 3 |
| Structured Data | 0.00 | 0 | 5 | 0 | 0 |
| Core Web Vitals | Not scored | 0 | 0 | 0 | 6 |

Totals: **38 items · 11 pass · 15 fail · 2 not applicable · 10 not checked/blocked**.

## Top findings

1. **Structured data coverage is the clearest implementation gap.** Homepage Organization/WebSite JSON-LD is present, but Organization `sameAs` contains empty values. Sampled product and editorial templates exposed no Product, Article/BlogPosting, or BreadcrumbList JSON-LD.
2. **Search Console contains stale and inconsistent technical signals.** GSC lists an old sitemap index plus a page sitemap with 1 error, 2 warnings, and 0 indexed web URLs. Search Analytics also shows HTTP, www, and parameterized variants.
3. **Homepage metadata undersells the commercial intent.** The rendered title is only “Winn Foods,” the meta description is absent, and the single H1 is empty.
4. **The site has useful answer-engine foundations.** Public content is crawlable, `llms.txt` returns 200, agent/UCP discovery is documented, and FAQs/lists exist. Entity consistency and direct top-of-page answers still need work.
5. **Connected performance data is now available.** The GSC property is `sc-domain:winn-foods.com`; the GA4 property is `properties/533748438`. The 2026-04-25 to 2026-07-24 GA4 report recorded 13,238 sessions, 11,267 active users, 87 key events, and INR 19,467.999743 purchase revenue. These figures are evidence, not forecasts.

## Priority fixes

- **High · Shopify/SEO:** submit the current `/sitemap.xml` in GSC, remove obsolete submissions, and resolve page-sitemap errors/warnings.
- **High · Engineering:** enforce one HTTPS non-www host and 301 HTTP/www, typo, copy-suffix, malformed, and obsolete URL variants.
- **High · SEO/content:** replace the short homepage title, populate its empty H1, and add an intent-aligned meta description.
- **High · SEO/engineering:** implement and validate Product, Article/BlogPosting, and BreadcrumbList markup; clean Organization `sameAs`.
- **Medium · Content/merchandising:** add descriptive alt text to meaningful category, product, trust, and editorial images.
- **High · Analytics/engineering:** restore PageSpeed/CrUX or Lighthouse access and measure field and lab CWV separately before prioritizing performance fixes.

## Expected impact

The first four fixes should improve crawl/index signal consistency, search-result presentation, entity understanding, and rich-result eligibility. CWV impact cannot be estimated until real measurements are collected.

## Blockers and next actions

- **CWV:** Google API DNS failed; no Lighthouse or in-app browser session was available. Re-run mobile PageSpeed + CrUX and a local Lighthouse audit.
- **Internal-link depth/orphans:** run a complete uncapped link-graph crawl and reconcile with sitemap, GSC, and GA4 inventories.
- **Indexation coverage:** export GSC Page Indexing data and inspect representative URLs.
- **AI mentions:** define priority prompts and capture dated results from major answer engines.

## Evidence

- Firecrawl crawl/render/robots/llms evidence: `logs/audits/raw/20260727T073600Z-firecrawl-site-checks.json`
- GSC and GA4 evidence: `logs/audits/raw/20260727T073600Z-connected-data-evidence.json`
- Provider blockers: `logs/audits/raw/20260727T073600Z-provider-blockers.json`
- Keyword intent inputs: `keywords/clusters.json`, `keywords/research-summary.json`
- Existing content patterns: `blogs/summary.md`
