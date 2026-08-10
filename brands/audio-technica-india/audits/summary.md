# Audio-Technica India SEO audit summary

Run date: 2026-08-10  
Target: https://audio-technica.co.in/

Overall score: **66.31 / 100**. This is a partial, evidence-gated result: 19 of 38 rows are not applicable because the required source was not available. It is not a full-site health score.

| Audit | Score | Pass | Fail | N/A |
|---|---:|---:|---:|---:|
| Generic on-page | 70.59 | 5 | 2 | 0 |
| Content SEO | 100.00 | 1 | 0 | 6 |
| Site architecture | 100.00 | 2 | 0 | 5 |
| Core Web Vitals | 27.27 | 1 | 3 | 2 |
| Structured data | 100.00 | 1 | 0 | 4 |
| AI SEO / AEO / GEO | 0.00 | 0 | 4 | 2 |

## Priority fixes

1. **High — improve mobile LCP.** URL-level CrUX LCP is 2.676 s (target <=2.5 s); mobile lab LCP is 41.5 s. Identify the LCP element and reduce server, image and render delay.
2. **High — reduce layout shift.** URL-level CrUX CLS is 0.23 (target <=0.1); reserve media/embed space and inspect dynamically injected header, consent and product-card UI.
3. **High — fix homepage heading hierarchy.** The sampled homepage has five H1 elements. Retain a single page-topic H1.
4. **High — strengthen entity consistency.** The sampled Organization schema has no `sameAs` and observed naming varies. Standardize governed entity fields and add only verified owned profiles.
5. **High — connect Google Search Console.** Sitemap submission, index coverage and rich-result eligibility remain unverified.
6. **Medium — address image alt coverage.** 44/52 sampled homepage images have non-empty alt text (84.6%), below the 95% criterion.

## Evidence and blockers

Public checks covered the homepage, robots.txt, sitemap index, category, blog and llms.txt endpoints. The homepage, category and blog returned HTTP 200; robots.txt is present and references a reachable sitemap index. `llms.txt` returned 404. Raw evidence is stored in `logs/audits/raw/`.

The audit could not verify Search Console data, full internal linking/redirects, rendered schema validity, AI-answer visibility, or content-to-SERP intent alignment. Those items are recorded as `not_applicable`, not passes.
