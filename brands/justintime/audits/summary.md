# Just In Time SEO audit — 2026-09-29

**Status: Partial.** Overall score is withheld because sitewide coverage and Search Console/analytics evidence are incomplete. Five public content URLs were sampled; findings should not be generalized beyond their stated scope.

## Audit counts

| Audit | Pass | Fail | Not checked / blocked |
|---|---:|---:|---:|
| Generic On-Page SEO | 2 | 4 | 1 |
| Content SEO | 3 | 0 | 4 |
| Site Architecture & Technical SEO | 3 | 0 | 4 |
| Core Web Vitals & Performance | 1 | 3 | 2 |
| Structured Data & Schema | 2 | 1 | 2 |
| AI SEO / AEO / GEO | 3 | 0 | 3 |
| **Total** | **14** | **8** | **16** |

## Priority findings

1. **High — Mobile homepage performance:** CrUX field p75 LCP is 3.444 s, INP 259 ms, TTFB 1,825 ms and CLS 0.00. Separate Lighthouse mobile lab: performance 29, LCP 10.5 s, CLS 0.194, TBT 910 ms.
2. **High — Headings:** Homepage has an empty H1. The sampled men’s collection has three H1s, two identical.
3. **High — Titles and descriptions:** Sampled titles are 91–105 characters; descriptions are 161–222 characters.
4. **Medium — Structured data:** Men’s CollectionPage URL is correct, but its ItemList points to /collections/citizen-watches. Tissot product page carries a HowTo block about a Citizen Eco-Drive Chronograph.
5. **Medium — Store-count conflict:** Homepage metadata and llms.txt say “75+ stores”; About Us says “100+ stores.”

## Scope and method

Firecrawl fetched the homepage, About Us, men’s watches collection, one Tissot product, and the blog index; all five returned HTTP 200. A depth-2, 60-URL crawl timed out after 300 seconds. Rendered browser checks covered the homepage, collection, and product; the product page at 390 × 844 CSS px had no horizontal overflow. robots.txt, sitemap.xml, and llms.txt returned HTTP 200.

The three rendered page samples have self-referencing HTTPS canonicals. JSON-LD parsed without syntax errors in those samples; semantic and Google rich-result validation was not performed. Homepage mobile PageSpeed/CrUX results are not representative of collection/product performance. Field metrics and Lighthouse lab metrics are reported separately.

No verified GSC property for justintime.in was available. Search query/page performance, indexing coverage, analytics outcomes, keyword demand, live SERP comparisons, individual blog quality, sitewide URL counts, redirect chains, orphan pages, and full accessibility/mobile coverage remain unassessed.

## Next steps

**Immediate (0–30 days):** correct schema, H1s, sampled title/description tags, and store-count consistency; investigate homepage LCP, INP, and TTFB.

**Short term (30–60 days):** repeat field/lab checks after fixes; run segmented crawls for status codes, metadata, canonicals, links, redirects, and alt text; validate schema.

**Medium term (60–90 days):** add verified GSC and the correct analytics source, then map query/page outcomes to content and commercial opportunities; review target-market SERPs and individual blog pages.
