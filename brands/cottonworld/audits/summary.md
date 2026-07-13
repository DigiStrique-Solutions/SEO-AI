# SEO Audit — Cottonworld (cottonworld.net)

**Run date:** 2026-07-13 · **Platform:** Shopify (Cloudflare, edge Mumbai, en-IN)
**Overall score:** **0.59** *(weighted pass-ratio over assessed items — **PARTIAL**: 4 items blocked pending Google Search Console + field-performance access)*
**Scale:** 892 products · 157 collections · 101 pages · 5 blog URLs

## Summary

Cottonworld is a technically **well-built Shopify storefront** — clean crawlability, valid sitemaps, consistent canonicalization, single-hop redirects, fast server (TTFB 81ms), correct Product/Article schema, and above-baseline AI-crawler access (llms.txt / agents.md / UCP all live). The **foundation is strong**.

The damage is concentrated in **content and a few on-page templates**. Most urgently, the **blog is publishing broken, placeholder content live** — lorem-ipsum sections, missing/wrong meta descriptions (unrelated "JSW Defence" boilerplate), and zero H1s. Collection titles are keyword-stuffed to ~130 characters. Layout stability (CLS 0.155) and image formats (0/340 modern) drag performance. AI/answer-engine readiness scores lowest because there is little genuine, quotable content to surface.

| Audit | Score | Status |
|-------|-------|--------|
| Site Architecture & Technical SEO | **1.00** | ✅ Strong (1 item blocked: indexation) |
| Content SEO | **0.71** | ⚠️ Blog broken, thin collections |
| Structured Data & Schema | **0.64** | ⚠️ Product/Article good; missing WebSite/breadcrumb/reviews |
| Core Web Vitals (lab) | **0.50** | ⚠️ CLS + images (2 field items blocked) |
| Generic On-Page SEO | **0.47** | ❌ Titles, metas, H1 broken on content templates |
| AI SEO / AEO / GEO | **0.09** | ❌ No answer content / weak entity graph |

## Top findings (severity · evidence · fix · owner)

1. **CRITICAL — Blog is placeholder/broken content, live.** `/blogs/blog/*` posts render literal "WHAT IS LOREM IPSUM?" headings, wrong duplicated "JSW Defence / Indian Armed Forces" body copy, ~456 words, 0 H1. *Evidence:* rendered DOM on 4 posts. *Fix:* unpublish or fully rewrite all posts before doing anything else. *Owner:* Content.
2. **HIGH — Content/page templates emit 0 H1.** All 4 blog posts + `/pages/about-us` render no H1 (rendered-DOM confirmed). *Fix:* add single H1 (post/page title) to article + page templates. *Owner:* Dev/Theme.
3. **HIGH — Blog meta descriptions missing/wrong.** 2 of 4 posts have none; others carry a wrong 320-char boilerplate. *Fix:* template-level per-post meta (70–160 chars). *Owner:* Dev/Content.
4. **HIGH — Collection titles keyword-stuffed (~130 chars).** e.g. `/collections/linen` = "Linen - Men Clothing \| Women Clothing \| Shirts \| Pants \| T-Shirts \| Tops \| Leggings Online at Best Price in India- Cottonworld.net". *Fix:* 50–60 char `<Category> for Men & Women \| Cottonworld`. *Owner:* Merchandising/SEO.
5. **HIGH — CLS 0.155 (lab, > 0.10).** Layout shifts from hero/banner/image reflow. *Fix:* reserve width/height/aspect-ratio above the fold. *Owner:* Dev/Theme.
6. **HIGH — No WebSite schema, no Organization `sameAs`.** Homepage has Organization only. *Fix:* add WebSite (+SearchAction) and `sameAs` social profiles — also fixes AI entity clarity. *Owner:* Dev/SEO.
7. **MEDIUM — Images: 0/340 WebP/AVIF, ~4.7MB payload.** *Fix:* Shopify `image_url` WebP + responsive `srcset`. *Owner:* Dev/Theme.
8. **MEDIUM — No product reviews/aggregateRating.** Blocks star rich results and weakens E-E-A-T. *Fix:* enable a reviews app + Product `aggregateRating`. *Owner:* Merch/Dev.
9. **MEDIUM — No BreadcrumbList / CollectionPage schema.** *Fix:* emit on PDP/PLP templates. *Owner:* Dev.
10. **MEDIUM — No AEO/GEO answer content.** No FAQ, definitions, or tables. *Fix:* front-loaded answers + FAQPage on key templates. *Owner:* Content/SEO.

## What passed (don't touch)

robots.txt · sitemaps (real-time, 892 products indexed) · canonical host consistency · single-hop 301s · TTFB 81ms · minimal render-blocking · Product + Article schema validity · image alt coverage (≥95%) · internal linking (401 home links) · AI-crawler access (llms.txt/agents.md/UCP) · mobile render (clean, responsive).

## Blocked — needs access to complete the audit (currently PARTIAL)

| Item | Blocked because | Unblock via |
|------|-----------------|-------------|
| Indexation coverage (site-arch) | GSC not connected | Connect Google Search Console (Composio) |
| LCP field p75 (CWV) | PSI/CrUX keyless quota out, no GSC | PSI API key **or** GSC Core Web Vitals |
| INP field p75 (CWV) | No real-user field data | CrUX / GSC field report |
| AI mentions (AEO/GEO) | Not tested this run | Manual ChatGPT/Perplexity/AI-Overview prompt checks |

*Lab performance was measured on a warm-CDN desktop connection and is **not** representative of mobile-India field data — treat LCP/INP as unverified until field data is available.*

## Evidence & provenance

- Full evidence: [evidence/20260713/site-checks.json](evidence/20260713/site-checks.json)
- Mobile render: [evidence/20260713/mobile-home.jpeg](evidence/20260713/mobile-home.jpeg)
- Raw payloads: `../logs/audits/raw/` · Run log: `../logs/audits/activity.jsonl`
- Per-audit detail: [generic-on-page](generic-on-page.json) · [content-seo](content-seo.json) · [site-architecture](site-architecture.json) · [core-web-vitals](core-web-vitals.json) · [structured-data](structured-data.json) · [ai-seo-aeo-geo](ai-seo-aeo-geo.json)
