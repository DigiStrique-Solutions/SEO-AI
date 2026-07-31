# Surabhi Foods — SEO audit summary

Run date: 27 July 2026

Run ID: `surabhi-audits-20260727T074000Z`

Overall score: **50.8/100**

This is a complete six-definition crawl and rendered-page audit. Six rows remain `not_applicable` because the required GSC, demand, rich-result, or controlled AI-answer evidence was unavailable; none was silently treated as a pass.

## Scores

| Audit | Score | Pass | Fail | Not applicable |
|---|---:|---:|---:|---:|
| Generic on-page | 35.29 | 2 | 5 | 0 |
| Content SEO | 44.44 | 2 | 3 | 2 |
| Site architecture | 81.82 | 4 | 1 | 2 |
| Core Web Vitals | 78.57 | 4 | 2 | 0 |
| Structured data | 55.56 | 2 | 2 | 1 |
| AI SEO / AEO / GEO | 9.09 | 1 | 4 | 1 |
| **Total** | **50.8** | **15** | **17** | **6** |

## Top findings

1. **High — entity and homepage schema:** the homepage has no Organization or WebSite JSON-LD. Naming varies among Surabhi, Surabhi Foods, Surabhi Sauces, and Adinath Agro Processed Foods, while the official 1989/2006 history conflict remains unresolved.
2. **High — titles and headings:** key titles exceed the 30–60 character audit criterion, and the sampled product template contains two DOM H1 elements.
3. **Medium — image accessibility:** at least 20 of 36 visible homepage images and 13 of 20 visible product images lacked non-empty alt text in the rendered checks.
4. **Medium — old-domain links:** homepage “View All” links for recipes and blogs point to `surabhisauces.com`, not the canonical `surabhi-foods.com` host.
5. **Medium — lab performance:** real-user mobile LCP (2.063 s), INP (130 ms at origin), CLS (0.00), and TTFB (716 ms) pass. Cold-load lab performance is weak: performance 37 and LCP about 10.8–11.6 s, with render-blocking and image-delivery opportunities.
6. **Medium — content and answerability:** the sampled article has no visible author or sources, only weak topical internal links, and a rendered H1→H3/H4 heading jump. It lacks a concise answer block or comparison table.

## Priority fixes

1. Confirm the approved brand/corporate hierarchy and history, then add canonical Organization + WebSite schema with verified `sameAs`.
2. Rewrite long template titles/descriptions and remove the duplicate product H1.
3. Connect the exact `surabhi-foods.com` GSC property and restore permitted keyword-demand/SERP evidence; rerun the six blocked provider rows.
4. Add alt text to meaningful Shopify product-card, gallery, banner, and article images.
5. Replace legacy-domain recipe/blog links with same-domain URLs and crawl for remaining old-host links.
6. Optimise the hero/LCP image, responsive image delivery, critical CSS, and noncritical theme/app scripts.
7. Upgrade articles with visible attribution, sources, semantic H2 sections, comparison tables, concise direct answers, and contextual product/recipe links.

## Evidence and limits

- Firecrawl completed 40 pages at depth 3.
- Playwright rendered and evaluated homepage, product, and article templates; the article also passed a 390 px no-horizontal-overflow check.
- PageSpeed/CrUX and a complete local Lighthouse JSON report supplied mobile performance evidence.
- GSC, validated keyword demand/SERP intent, Google rich-result reporting, and controlled AI-engine visibility evidence were unavailable. Those rows are explicitly `not_applicable` with next actions.
