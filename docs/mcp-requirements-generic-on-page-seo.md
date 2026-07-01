# MCP Requirements For Generic On-Page SEO

Updated: 2026-06-29

This is the MCP capability map for the generic on-page SEO agent. Start with the core set, then add vertical MCPs only when the current SEO task needs them.

## Access Model

All agents in this repo can see and call all configured MCP tool ids by default. Stable tool ids are still required for routing, logging, and auditability. MCP connections must remain scoped by org, user, account, and property, and raw credentials must never be passed to the model.

## Recommendation

Build 8 core MCP/tool groups first:

1. Web crawl and render: Firecrawl as the v1 renderer, plus a lower-level browser tool only when precision control is needed.
2. Google Search Console: performance, indexing, sitemaps, URL inspection.
3. GA4: landing page behavior and conversion quality.
4. Google Ads Keyword Planner: search demand and keyword variants.
5. PageSpeed, Lighthouse, and CrUX: Core Web Vitals and performance diagnostics.
6. Structured data validator: JSON-LD extraction, Schema.org validation, Google rich result eligibility checks.
7. Free SERP and intent evidence: GSC search appearance, manual SERP review, user-provided screenshots, and free search surfaces where compliant.
8. CMS or code implementation surface: WordPress, Shopify, Webflow, GitHub, or whatever owns the page.

Then add vertical MCPs:

- Local: Google Business Profile, Google Maps Places, Bing Places if needed.
- Ecommerce: Shopify, Google Merchant Center, product feed, reviews.
- Lead gen: HubSpot or CRM, form and call tracking, calendar booking.
- App installs: App Store Connect, Google Play Console, app listing intelligence.

## Connector Decisions

- Use Firecrawl plus Playwright for browser rendering.
- Firecrawl is the default public-page crawl, render, extraction, screenshot, and simple interaction layer.
- Playwright is the fallback precision browser layer for authenticated flows, local dev pages, custom viewport matrices, console/network tracing, reproducible visual QA, and exact DOM assertions.
- Use CrUX API plus Lighthouse for Core Web Vitals and performance diagnostics in v1.
- CrUX API is the field-data source for public URL or origin Core Web Vitals.
- Local Lighthouse CLI or a Node runner is the lab-diagnostics source for performance, accessibility, best practices, and SEO checks.
- Do not use Firecrawl as the PageSpeed, Lighthouse, or CrUX source of truth. Firecrawl can provide rendered-page evidence, screenshots, and raw page inputs, but Core Web Vitals and Lighthouse audits should come from Google PageSpeed Insights, the CrUX API, or local Lighthouse where needed.

## Tier 0: Already Mentioned, Keep Them

### Google Search Console

Purpose:

- Queries, pages, impressions, clicks, CTR, average position.
- Page indexing status.
- Sitemap status.
- Enhancement reports where exposed.
- URL Inspection for managed properties.

Needed for:

- Indexability checks.
- Query-to-page mapping.
- Cannibalization.
- Decay detection.
- Page-level opportunities.
- Validating whether Google knows and indexes the page.

Official docs:

- [Search Console URL Inspection API](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)
- [Google URL Inspection API announcement](https://developers.google.com/search/blog/2022/01/url-inspection-api)

Notes:

- URL Inspection API is quota-limited and only covers properties the user manages.
- It returns indexed or indexable status for Google's indexed version, not a full live crawl test.

### GA4

Purpose:

- Landing page traffic.
- Engagement.
- Conversions.
- Revenue or lead events.
- Channel and source quality.

Needed for:

- Prioritizing pages by business impact.
- Distinguishing ranking problems from conversion problems.
- Finding pages with traffic but weak engagement or conversion.

Official docs:

- [Google Analytics Data API overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [GA4 runReport method](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)

### Google Ads Keyword Planner

Purpose:

- Keyword ideas from seed terms or page URLs.
- Average monthly searches.
- Competition.
- Location and language targeting.

Needed for:

- Keyword mapping.
- SERP intent planning.
- Title and heading opportunity framing.
- Page expansion ideas.

Official docs:

- [Google Ads API keyword ideas](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas)

Notes:

- Useful for demand, not truth. It is ads-oriented and can group or bucket volumes.

### Firecrawl Or Website Crawl

Purpose:

- Crawl public pages.
- Extract raw HTML and rendered content where supported.
- Discover links, sitemaps, metadata, headings, status codes, canonicals, and content.
- Capture screenshots.
- Use simple browser actions such as wait, click, scroll, press, and screenshot before extraction.

Needed for:

- Generic on-page audit.
- Crawlability.
- Internal links.
- Metadata extraction.
- Page inventory.
- Competitor page inspection.

Notes:

- Firecrawl can be the v1 browser-rendering layer for generic SEO audits. Its docs describe JavaScript rendering, mobile emulation, screenshots, raw HTML, rendered HTML, links, images, and browser actions.
- Keep a lower-level browser tool available for precision cases: authenticated flows, custom viewport/device matrices, exact DOM assertions, console/network tracing, local file inspection, long interactive sessions, and reproducible visual QA.

### Google Business Profile

Purpose:

- Business profile data.
- Locations.
- Reviews.
- Local posts.
- Local performance reports where available.

Needed for:

- Local SEO.
- NAP consistency.
- Review and profile completeness.
- Local landing page validation.

Official docs:

- [Google Business Profile APIs](https://developers.google.com/my-business/ref_overview)

### Google Maps Places

Purpose:

- Place details.
- Nearby competitors.
- Local categories.
- Place photos.
- Address and location metadata.

Needed for:

- Local SEO.
- Competitor discovery around a location.
- Location page validation.

Official docs:

- [Places API overview](https://developers.google.com/maps/documentation/places/web-service/overview)

## Tier 1: Add For The Generic On-Page Agent

### Browser Rendering MCP

Purpose:

- Render page as Google-like browser.
- Inspect DOM after JavaScript.
- Run selectors for title, meta, canonical, robots, headings, links, JSON-LD, images, and visible text.
- Capture desktop and mobile screenshots.

Needed for:

- JavaScript SEO.
- Schema detection.
- Mobile parity.
- Screenshot evidence.
- Popup and interstitial detection.
- Hidden or client-rendered content checks.

Implementation:

- Use Firecrawl first for v1 public-page rendering, screenshots, and simple interactions.
- Use Playwright internally when Firecrawl output is not precise enough or when tests need local browser control.
- Expose read-only tools first: `render_url`, `extract_dom`, `query_selector_all`, `screenshot`, `compare_mobile_desktop`.

### PageSpeed, Lighthouse, And CrUX MCP

Purpose:

- Field Core Web Vitals from CrUX.
- Lab diagnostics from Lighthouse.
- PageSpeed reports for LCP, INP, CLS, accessibility, SEO, and best practices.

Needed for:

- Page experience scoring.
- Performance root-cause hints.
- LCP element detection.
- Lab vs field diagnosis.

Official docs:

- [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started)
- [CrUX API](https://developer.chrome.com/docs/crux/api/)
- [CrUX overview](https://developer.chrome.com/docs/crux)
- [Firecrawl scrape endpoint](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
- [Firecrawl homepage](https://www.firecrawl.dev/)

Note:

- Google says PageSpeed Insights plans to discontinue including CrUX real-world data in that API. Use CrUX API directly for field data.
- Firecrawl is not a replacement for PageSpeed, Lighthouse, or CrUX. Firecrawl's documented outputs cover rendered content, raw HTML, screenshots, links, metadata, status code, product/menu extraction, and browser actions. It does not provide Google's field Core Web Vitals dataset or a Lighthouse audit result as its core API contract.
- Use Firecrawl output as supporting evidence for performance work, for example to identify visible hero images, blocking embeds, popup behavior, rendered DOM, and screenshot context.
- Use PageSpeed Insights API for Google-hosted Lighthouse lab diagnostics and PageSpeed report shape.
- Use CrUX API directly for field Core Web Vitals at page or origin level.
- Use local Lighthouse through Playwright or a worker only when PageSpeed Insights is unavailable, when testing local/staging URLs, or when controlling auth, device, throttling, and repeatability matters.

Free or open-source stack:

- Lighthouse is open source and can run from Chrome DevTools, CLI, or Node. Use it for lab audits and diagnostics.
- Lighthouse CI is free tooling for repeatedly running, storing, and asserting Lighthouse results in CI.
- CrUX API is the free Google field-data source for real-user Core Web Vitals where the URL or origin has enough Chrome user data.
- `web-vitals` is Google's open-source JavaScript library for collecting LCP, INP, CLS, and related metrics from real users.
- sitespeed.io is open source and can run Lighthouse, Browsertime, video, HAR waterfall, and monitoring dashboards. Use it when Strique wants self-hosted repeated tests and Grafana-style trend monitoring.

Recommended v1:

1. CrUX API for public field Core Web Vitals.
2. Local Lighthouse CLI or Node runner for lab diagnostics.
3. `web-vitals` only if the customer can install a small script or already has a first-party analytics pipeline.

Recommended v2:

1. Lighthouse CI for regression budgets on code-owned sites.
2. sitespeed.io for scheduled self-hosted monitoring across many pages or journeys.

### Structured Data Validator MCP

Purpose:

- Extract JSON-LD, Microdata, and RDFa from rendered pages.
- Validate JSON syntax.
- Validate Schema.org vocabulary.
- Check Google rich result eligibility.
- Compare schema against visible content.

Needed for:

- Article, Product, BreadcrumbList, Organization, LocalBusiness, FAQPage, VideoObject, ReviewSnippet, Event, Recipe, and other eligible markup.
- Catching fake or stale schema.

Implementation:

- Internal MCP is fine.
- Use browser-rendered DOM plus Schema.org validation.
- For Google rich result eligibility, use manual or browser automation where no official public batch API fits.

Official docs:

- [Schema.org](https://schema.org/)
- [Google structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

### Free SERP And Intent Evidence

Purpose:

- Observed Google result appearance where available.
- Search appearance from GSC.
- SERP features from manual or user-provided evidence.
- Top visible competitors from free/manual checks.
- Intent classification from the actual results.
- Page type expectations.

Needed for:

- Deciding whether a page matches SERP intent.
- Competitor title/H1/content comparison.
- Cannibalization and opportunity sizing.
- AI overview or rich result observation if provider supports it.

Free-first v1 sources:

- GSC Performance and search appearance data.
- GKP keyword ideas for demand and variants.
- Firecrawl and Playwright for known competitor URLs provided by the user or discovered through free/manual review.
- Manual/free SERP checks for priority queries.
- User-provided screenshots or exports from Google Search, Bing, or Search Console.

Notes:

- Google does not provide a general organic SERP API. Do not make DataForSEO, Semrush, Ahrefs, SerpAPI, or similar paid databases part of generic v1.
- If automated live SERP snapshots are required later, treat that as an explicit paid v2 decision with legal, ToS, and cost review.
- For v1, the SEO agent should degrade gracefully: use GSC/GKP/known URLs first, then ask for a screenshot or competitor URL when live SERP evidence is missing.

### HTML, Accessibility, And Link QA MCP

Purpose:

- HTML validation.
- Broken links.
- Accessibility checks with axe-core or equivalent.
- Image alt audit.
- Heading and landmark validation.

Needed for:

- On-page quality.
- Accessibility signals that overlap with SEO.
- Evidence generation for engineering fixes.

Implementation:

- Can be internal, powered by rendered HTML.
- No need for a heavy third-party MCP first.

## Tier 2: Add For Vertical Or Advanced Work

### Bing Webmaster MCP

Purpose:

- Bing indexing data.
- Sitemap submission.
- URL submission.
- Site-level search diagnostics.

Needed for:

- Brands that care about Bing, Copilot, Windows search, or older B2B audiences.
- Secondary search engine coverage.

Official docs:

- [Bing Webmaster API](https://learn.microsoft.com/en-us/bingwebmaster/)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

### Google Merchant Center MCP

Purpose:

- Product feed health.
- Product status.
- Merchant reports.
- Shopping surfaces.
- Product data issues.

Needed for:

- Ecommerce SEO.
- Product page SEO.
- Product schema/feed consistency.
- Free listings and Shopping diagnostics.

Official docs:

- [Merchant API](https://developers.google.com/merchant/api/reference/rest)
- [Merchant Reports API](https://developers.google.com/merchant/api/guides/reports/overview)

### Shopify MCP

Purpose:

- Products.
- Collections.
- Pages.
- Blogs.
- Redirects.
- Themes or storefront data.

Needed for:

- Ecommerce audits and implementation.
- Product metadata fixes.
- Collection SEO.
- Duplicate/faceted URL checks.

### WordPress MCP

Purpose:

- Posts, pages, taxonomies, media, redirects, SEO plugin fields where accessible.

Needed for:

- Implementing fixes for a large share of content sites.
- Updating titles, descriptions, headings, internal links, alt text, and schema settings.

### Webflow MCP

Purpose:

- CMS items.
- Static pages.
- Slugs.
- SEO fields.
- Publishing workflows.

Needed for:

- SaaS and lead gen sites hosted on Webflow.

### GitHub Or Codebase MCP

Purpose:

- Read and edit code-owned pages.
- Inspect Next.js, Remix, Astro, Nuxt, Rails, Django, or static site metadata.
- Patch templates causing duplicate SEO issues.

Needed for:

- Strique implementation mode.
- Fixing metadata generation, schema, internal links, sitemaps, robots, and rendering bugs.

### HubSpot Or CRM MCP

Purpose:

- Landing pages, forms, contacts, lead quality, campaign attribution, CRM lifecycle.

Needed for:

- Lead generation SEO.
- Prioritizing pages by lead quality rather than traffic alone.
- Validating form conversion.

### Google Tag Manager MCP

Purpose:

- Container tags.
- Trigger and variable inspection.
- Conversion tags.
- Consent setup.

Needed for:

- Analytics implementation audit.
- Conversion tracking issues.

### Log File Or CDN MCP

Purpose:

- Googlebot and Bingbot crawl logs.
- Status codes at scale.
- Crawl frequency.
- Edge redirects and cache behavior.

Possible sources:

- Cloudflare.
- Fastly.
- AWS CloudFront.
- GCP logs.
- Nginx or server logs.

Needed for:

- Enterprise technical SEO.
- Crawl budget issues.
- Large sites.

### Backlink And Authority MCP

Purpose:

- Backlinks.
- Referring domains.
- Anchor text.
- Competitor authority.

Free-first v1 sources:

- GSC links report where the customer owns the property.
- Bing Webmaster link data where available.
- Manual/free review of visibly cited sources, partner pages, directories, and press mentions.

Needed for:

- Prioritization and competitor context.
- Not required for generic on-page checks.

Notes:

- Paid backlink databases are out of scope for generic v1. Add them only as an explicit premium connector decision.

### AI Search Visibility MCP

Purpose:

- Test prompt sets across ChatGPT, Perplexity, Gemini, Copilot, and Claude where permitted.
- Capture cited sources.
- Compare brand and competitor mentions.

Needed for:

- AI SEO.
- Not required for Google's AI features, because Google says normal SEO foundations still apply.

Notes:

- Keep this separate from generic on-page SEO. It is slow, provider-specific, and can get expensive.

### App Store And Play Console MCPs

Purpose:

- App listing metadata.
- Screenshots.
- Ratings and reviews.
- Store performance.
- Keyword/listing analysis.

Needed for:

- App install and ASO work.
- ASO, not generic web on-page SEO.

## What Not To Build First

- A custom crawler if Firecrawl plus browser rendering covers v1.
- A separate MCP for every SEO checklist item.
- Google Ads campaign write tools for generic SEO. Keyword Planner read access is enough.
- Link-building automation.
- AI crawler manipulation tools.
- `llms.txt` generation as a core requirement. Useful later, but not a generic on-page dependency.

## V1 Tool Contracts

Minimum generic SEO MCP interface:

```text
crawl_url(url) -> status, headers, raw_html, rendered_text, links, images, metadata
render_url(url, viewport) -> screenshot, rendered_html, dom_summary, console_errors
inspect_gsc_url(site_url, inspection_url) -> index_status, canonical, robots, coverage
query_gsc(site_url, dimensions, filters, date_range) -> rows
query_ga4(property_id, dimensions, metrics, filters, date_range) -> rows
generate_keyword_ideas(seed_terms, seed_url, location, language) -> ideas
get_pagespeed(url, strategy) -> lighthouse, opportunities
get_crux(url_or_origin, form_factor) -> lcp, inp, cls, distributions
validate_schema(url_or_html) -> entities, errors, warnings, rich_result_candidates
serp_snapshot(query, location, language, device) -> results, features, inferred_intent
```

If write tools are configured, expose them by default like other MCPs, but require explicit confirmation for high-risk or externally visible actions.

## Priority Order

1. Firecrawl plus browser rendering.
2. GSC.
3. GA4.
4. PageSpeed plus CrUX.
5. Keyword Planner.
6. Structured data validator.
7. Free SERP and intent evidence.
8. CMS/code implementation MCPs.
9. Local, ecommerce, lead gen, and app install MCPs.
