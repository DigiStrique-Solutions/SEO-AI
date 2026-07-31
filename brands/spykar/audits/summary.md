# Spykar SEO audit summary

Run date: 2026-07-29
Target: https://spykar.com/
Status: **Partial** — 18 of 38 items are `not_applicable`, including explicit `not_checked_blocked` provider gaps.
Overall score: **0.60** across the five audits with at least one applicable item. Core Web Vitals is unscored because no required performance evidence was available.

## Score table

| Audit | Score | Pass | Fail | N/A or blocked | Status |
|---|---:|---:|---:|---:|---|
| Generic On-Page SEO | 1.00 | 5 | 0 | 2 | Partial |
| Content SEO | 0.85 | 5 | 1 | 1 | Partial |
| Site Architecture & Technical SEO | 1.00 | 5 | 0 | 2 | Partial |
| Core Web Vitals & Performance | Not scored | 0 | 0 | 6 | Blocked |
| Structured Data & Schema | 0.00 | 0 | 1 | 4 | Partial |
| AI SEO / AEO / GEO | 0.17 | 1 | 2 | 3 | Partial |
| **Total** | **0.60** | **16** | **4** | **18** | **Partial** |

## Top findings

- Search Console access is active for `https://spykar.com/` at owner level. The homepage, women collection, About page and blog index are all submitted and indexed, crawled as mobile, fetchable, robots-allowed and canonical-aligned.
- `robots.txt`, `sitemap.xml` and `llms.txt` return 200. The sitemap is submitted in GSC with no errors or warnings. Its zero-indexed counter conflicts with passing URL inspections and should be treated as an anomaly to monitor.
- Phase 2 now provides a 44-row keyword universe, 28 prioritized terms and nine clusters. The homepage maps cleanly to the navigational “spykar” cluster; transactional denim, fit, topwear, underjeans and local-store demand maps to dedicated collection or store-locator targets.
- The crawl exposed Product JSON-LD on a collection template and no content-type JSON-LD on the blog index. A fresh rendered validation was unavailable, so broader schema conclusions remain blocked.
- The homepage did not expose concise direct-answer or structured-answer blocks. This limits answer-engine extractability.

## Priority fixes

1. **High — measure performance:** restore PageSpeed/CrUX access and run mobile field plus lab checks. Until then, do not claim CWV performance.
2. **High — verify the entity graph:** inspect rendered homepage JSON-LD and add valid Organization and WebSite nodes if absent.
3. **High — improve answerability:** add concise, source-backed fit, sizing, care, shipping and returns answers on relevant pages.
4. **Medium — correct template schema:** keep Product markup on product detail pages and add appropriate editorial markup to article templates.
5. **Medium — strengthen proof:** link fit, craftsmanship, scale and sustainability claims to named, approved sources.
6. **Medium — complete crawl diagnostics:** generate a full metadata, image-alt, redirect and source-target link export to resolve the blocked on-page and architecture rows.

## Expected impact

- Better product/article rich-result eligibility after template schema is corrected and validated.
- Stronger AI-answer extractability from concise fit, care and policy answers.
- More defensible brand and sustainability claims through visible sources.
- A reliable performance and crawl baseline once blocked providers and complete exports are available.

## Evidence and limitations

Evidence is recorded under `brands/spykar/logs/audits/`, including the shared normalized site checks and run manifest. The run reused the prior 35-page Firecrawl crawl and rendered checks, added fresh Firecrawl and GSC evidence, and now cites the completed Phase 2 keyword universe, prioritized set and clusters. Keyword Planner volume and difficulty remain blocked, but the keyword workspace itself is no longer a blocker. No schema, mobile-usability, accessibility or CWV pass was inferred without the required evidence.
