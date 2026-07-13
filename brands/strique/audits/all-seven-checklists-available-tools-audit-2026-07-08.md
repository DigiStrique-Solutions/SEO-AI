# All Seven SEO Checklists: Available-Tools Audit

Date: 2026-07-08

Target URL: https://www.strique.io/

Scope: Strique homepage and available Strique site-level audit artifacts

Audit type: partial, available-tools only

## Per-Checklist Files

Each checklist task is also saved as its own Markdown file under `brands/strique/audits/available-tools-2026-07-08/`:

- `index.md`
- `generic-on-page-seo.md`
- `content-seo.md`
- `site-architecture-seo.md`
- `ai-seo-aeo-geo.md`
- `off-page-seo.md`
- `ecommerce-seo.md`
- `local-seo.md`

## Summary

This pass used the tools currently available in this workspace to review Strique against all seven checklist families:

- `generic-on-page-seo-checklist.md`
- `content-seo-checklist.md`
- `site-architecture-seo-checklist.md`
- `ai-seo-aeo-geo-checklist.md`
- `off-page-seo-checklist.md`
- `ecommerce-seo-checklist.md`
- `local-seo-checklist.md`

This is not a full completed audit. Google Search Console, GA4, Shopify or Merchant Center, Google Business Profile, CRM, backlink tooling, server logs, and PostHog were not active in this session. Items that require those sources should remain blocked until those sources are connected or refreshed.

## Tools Used

| Tool or artifact | Status | Used for |
| --- | --- | --- |
| Playwright | available | Rendered DOM, mobile viewport, metadata, headings, links, images, CTAs, robots.txt, sitemap fetch. |
| Firecrawl | available | Public crawl extraction, status, canonical, metadata, headings, links, visible content signals. |
| Raw HTTP fetch from Node | available | Confirmed raw HTML JSON-LD scripts. |
| Existing Strique audit JSON artifacts | available | Checklist-level item matrices for generic on-page, content SEO, site architecture, AI SEO/AEO/GEO, and off-page SEO. |
| Existing `site-checks.csv` | available | Historical public crawl, Playwright, Lighthouse, keyword, and GSC evidence summary from prior run. |
| Google Search Console via Composio | not active | Query/page CTR, indexing, URL Inspection, Discover, search appearance. |
| GA4 via Composio | not active | Landing page engagement, conversions, revenue or lead behavior. |
| Shopify, Merchant Center, GBP, CRM, backlink tools | not active | Ecommerce, local, product, review, feed, backlink, and local profile checks. |

## Fresh Live Evidence

Playwright rendered evidence:

- URL: `https://www.strique.io/`
- Title: `Agentic AI Marketing Platform for Growth Teams | Strique`
- Meta description: `Run paid media, SEO, content, lifecycle, and reporting from one agentic AI. The leading agentic AI for marketing — used by 1,247 marketers in 38 countries.`
- Canonical: `https://www.strique.io/`
- Robots meta: `index, follow`
- H1 count: 1
- H1: `Marketing Agents for Ecommerce Brands / That Actually Drive Revenue`
- H2 count: 9
- Rendered links: 37
- Rendered images: 55
- Missing alt attributes: 0
- Empty alt attributes: 5
- Estimated rendered body words: 923
- Mobile small tap-target candidates: 35

Robots and sitemap evidence:

- `robots.txt` allows `/`, disallows `/thank-you` and `/api/`.
- `robots.txt` declares sitemap: `https://www.strique.io/sitemap.xml`.
- `sitemap.xml` returned status `200`.
- Sitemap contained 51 `<loc>` entries.

Raw HTML structured data evidence:

- Raw HTML contains 2 `application/ld+json` scripts.
- Schema sample includes `Organization`, `ContactPoint`, `SoftwareApplication`, `Offer`, and `AggregateRating`.

Firecrawl evidence:

- Final URL: `https://www.strique.io/`
- Status: `200`
- Canonical: `https://www.strique.io/`
- Robots meta: `index, follow`
- H1: `Marketing Agents for Ecommerce Brands That Actually Drive Revenue`
- Firecrawl-reported schema types: `Website`, `Organization`, `Product`
- Firecrawl-reported CTAs: `Get started`, `Read case`, `Launch your campaign`, `Pricing`
- Firecrawl-reported trust signals: `4.4 on G2`, `4.6 on Shopify App Store`, `ISO 27001:2022 Certified`

## Existing Item-Level Matrix Coverage

These item-level matrices already exist in `brands/strique/audits/` and should be treated as the detailed evidence matrix for the available-tool audit rows:

| Checklist | Matrix file | Items | Pass | Fail | Not applicable | Blocked |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AI SEO/AEO/GEO | `ai-seo-aeo-geo-google-visible-audit.json` | 133 | 96 | 9 | 28 | 0 |
| Content SEO | `content-seo-google-visible-audit.json` | 173 | 146 | 12 | 15 | 0 |
| Generic On-Page SEO | `generic-on-page-google-visible-audit.json` | 381 | 255 | 89 | 37 | 0 |
| Off-Page SEO | `off-page-seo-google-visible-audit.json` | 148 | 97 | 4 | 47 | 0 |
| Site Architecture SEO | `site-architecture-google-visible-audit.json` | 218 | 163 | 37 | 18 | 0 |

The blocked count is `0` in these stored matrices because they were resolved against the prior available evidence run. This current 2026-07-08 pass did not refresh GSC or GA4 because those connections were not active.

## Checklist Coverage Summary

| Checklist | Current status | Result from available tools | Next action |
| --- | --- | --- | --- |
| Generic On-Page SEO | fix | Homepage is indexable with title, meta, canonical, sitemap inclusion, internal links, and visible rendered content. Existing matrix still has sitewide failures around duplicate or weak H1 patterns, alt text, sitemap/canonical mismatches, performance, and mobile accessibility. | Fix sitewide template issues: one clear H1 per page, durable image alt handling, canonical/sitemap cleanup, mobile tap targets, and performance bottlenecks. |
| Content SEO | fix | Homepage title, meta, H1, trust signals, CTAs, case-study links, and FAQ content are visible. Section 7 result is saved separately. Existing matrix flags heading/scannability and image accessibility issues. | Keep Section 7 note, then refresh Section 2 search intent once primary query and GSC data are available. |
| Site Architecture SEO | fix | Sitemap is live with 51 URLs, robots.txt references it, and homepage internal links reach product, pricing, use cases, customers, integrations, trust, and legal pages. Existing matrix flags sitemap inclusion, canonical, URL hygiene, and inventory issues across discovered URLs. | Compare sitemap URLs against live crawl and fix canonical or missing sitemap entries for priority URLs. |
| AI SEO/AEO/GEO | fix | Homepage is extractable, has visible answer-style sections, FAQ content, trust signals, and raw JSON-LD. Existing matrix flags answerability, H1/heading semantics, accessibility, preview controls, and some sitemap/internal reachability issues. | Improve semantic headings, accessible controls, crawl-safe snippets, and machine-readable entity consistency. |
| Off-Page SEO | partial | Homepage links to social profiles and has trust badges/case studies. Existing off-page matrix mostly passes public checks, but backlink quality and local/profile/review checks need external data. | Connect backlink/reputation sources before making link-risk or authority claims. |
| Ecommerce SEO | not_applicable / blocked | Strique is a SaaS/AI marketing platform, not an ecommerce storefront. The homepage mentions ecommerce brands and Shopify but does not expose product catalog, PDP, cart, checkout, price, availability, reviews, Merchant Center feed, or shipping/returns content. | Mark storefront-specific ecommerce rows not applicable unless auditing Strique customers. If auditing Shopify/App Store acquisition, connect Shopify/App Store/Merchant Center sources. |
| Local SEO | not_applicable / blocked | Strique appears to be an online SaaS/product company, not a local storefront or service-area business. Homepage does not expose local NAP, hours, directions, local landing pages, or GBP signals. | Mark local-business rows not applicable unless Strique has a local visibility goal. Connect GBP/Maps only if local profile optimization is in scope. |

## Top Available-Tool Findings

### 1. Sitewide H1 And Heading Template Issues

Severity: high

Evidence source: existing Firecrawl matrices, Playwright homepage render

Affected scope: sitewide templates in stored audit; homepage looks correct in the fresh Playwright check

Issue:

Stored matrices repeatedly flag pages with more than one H1. The fresh homepage render shows one H1, so this needs a fresh sitewide crawl before changing homepage code.

Recommended fix:

Run a new Playwright or Firecrawl crawl across the sitemap, then fix templates where pages still render multiple H1s.

Owner: engineering

Confidence: medium

### 2. Canonical And Sitemap Mismatch Across Discovered URLs

Severity: high

Evidence source: existing generic on-page, site architecture, off-page, and AI SEO matrices

Affected scope: sitewide

Issue:

Stored matrices report failures where canonical URLs and sitemap inclusion do not align for some discovered URLs.

Recommended fix:

Compare `sitemap.xml` against a fresh crawl. Keep only canonical, indexable URLs in the sitemap and normalize duplicate/contact-parameter variants.

Owner: engineering

Confidence: medium

### 3. Mobile Accessibility Needs Review

Severity: medium

Evidence source: fresh Playwright mobile render and existing Playwright artifacts

Affected URL: `https://www.strique.io/`

Issue:

Fresh Playwright found 35 small mobile tap-target candidates. Existing stored checks also mention small/crowded mobile tap targets and some low contrast samples.

Recommended fix:

Increase mobile tap target sizing or spacing for footer/nav links, card actions, and compact controls. Re-run Playwright mobile checks after changes.

Owner: engineering

Confidence: medium

### 4. Structured Data Is Present But Should Be Validated

Severity: medium

Evidence source: raw HTML fetch, Firecrawl

Affected URL: `https://www.strique.io/`

Issue:

Raw HTML includes JSON-LD for organization and software application entities. Firecrawl reports schema types. A dedicated rich result validation was not run in this pass.

Recommended fix:

Validate Organization, SoftwareApplication, Website, FAQ, Offer, AggregateRating, and ContactPoint fields with a schema validator and confirm claims such as ratings/review counts are source-backed.

Owner: engineering or marketing

Confidence: medium

### 5. Ecommerce And Local Checklists Are Mostly Out Of Scope For The Homepage

Severity: low

Evidence source: Playwright, Firecrawl

Affected URL: `https://www.strique.io/`

Issue:

The homepage targets ecommerce brands but is not itself an ecommerce storefront or local business page.

Recommended fix:

Use ecommerce and local checklists only when auditing Strique customer sites or specific Strique app marketplace/local visibility surfaces.

Owner: SEO or strategy

Confidence: high

## Evidence Matrix

Checklist: Generic On-Page SEO

Section: all sections in stored matrix

Item: 381 item-level rows in `generic-on-page-google-visible-audit.json`

Status: partial, with failures

Evidence source: Firecrawl, Playwright, Lighthouse, public HTTP, GSC from prior artifact

Command, tool, report, or data source: existing audit JSON plus fresh Playwright homepage check

Result: 255 pass, 89 fail, 37 not applicable

Blocker: GSC and GA4 were not refreshed in this session

Next action: refresh crawl and connector evidence, then fix H1, canonical, sitemap, image alt, performance, and mobile issues

Checklist: Content SEO

Section: all sections in stored matrix, with fresh Section 7 note

Item: 173 item-level rows in `content-seo-google-visible-audit.json`

Status: partial, with failures

Evidence source: Firecrawl, Playwright, keyword artifacts, prior GSC artifact

Command, tool, report, or data source: existing audit JSON, `content-seo-section-7-homepage-serp-promise-2026-07-08.md`, fresh Playwright homepage check

Result: 146 pass, 12 fail, 15 not applicable

Blocker: GSC was not refreshed in this session

Next action: choose primary homepage query and refresh GSC query/page CTR before final intent/CTR judgment

Checklist: Site Architecture SEO

Section: all sections in stored matrix

Item: 218 item-level rows in `site-architecture-google-visible-audit.json`

Status: partial, with failures

Evidence source: Firecrawl, Playwright, sitemap, prior GSC artifact

Command, tool, report, or data source: existing audit JSON plus fresh `robots.txt` and `sitemap.xml` fetch

Result: 163 pass, 37 fail, 18 not applicable

Blocker: GA4, CMS/code, and GSC were not refreshed in this session

Next action: compare fresh crawl URLs to the 51 sitemap URLs and normalize canonical/sitemap mismatches

Checklist: AI SEO/AEO/GEO

Section: all sections in stored matrix

Item: 133 item-level rows in `ai-seo-aeo-geo-google-visible-audit.json`

Status: partial, with failures

Evidence source: Firecrawl, Playwright, schema/raw HTML, prior GSC artifact

Command, tool, report, or data source: existing audit JSON plus fresh rendered/raw HTML checks

Result: 96 pass, 9 fail, 28 not applicable

Blocker: live AI answer visibility platforms and fresh GSC data were not connected

Next action: validate structured data and improve answerability/accessibility issues

Checklist: Off-Page SEO

Section: all sections in stored matrix

Item: 148 item-level rows in `off-page-seo-google-visible-audit.json`

Status: partial

Evidence source: Firecrawl, public website links, prior artifacts

Command, tool, report, or data source: existing audit JSON plus fresh rendered external links

Result: 97 pass, 4 fail, 47 not applicable

Blocker: backlink, PR, review, directory, social, GBP, and CRM data were not connected

Next action: connect backlink/reputation sources before off-page authority or risk claims

Checklist: Ecommerce SEO

Section: storefront, catalog, product, feed, Merchant Center, reviews, shipping, and checkout sections

Item: 169 checklist items in `ecommerce-seo-checklist.md`

Status: not_applicable or not_checked_blocked

Evidence source: Playwright, Firecrawl

Command, tool, report, or data source: fresh homepage checks

Result: Strique homepage is SaaS/product marketing, not an ecommerce storefront. No product catalog, PDP, cart, checkout, price, availability, reviews, shipping, returns, or Merchant Center feed was available from the homepage.

Blocker: Shopify, Merchant Center, product feed, and ecommerce platform access not connected

Next action: use this checklist for Strique customer stores or app marketplace surfaces, not the main SaaS homepage unless ecommerce functionality is added

Checklist: Local SEO

Section: local business, NAP, GBP, reviews, local pages, maps, citations, and local AI readiness sections

Item: 196 checklist items in `local-seo-checklist.md`

Status: not_applicable or not_checked_blocked

Evidence source: Playwright, Firecrawl

Command, tool, report, or data source: fresh homepage checks

Result: Strique homepage does not present as a local storefront or service-area business. No local NAP, hours, map, directions, service-area pages, or GBP evidence was verified.

Blocker: Google Business Profile, Maps, citations, local reviews, and local ranking data not connected

Next action: mark local rows not applicable unless Strique has a local visibility objective

## Coverage Counts For This Available-Tools Pass

This pass references 1,418 checklist items across all seven checklist files.

| Bucket | Count |
| --- | ---: |
| Item-level rows already available in stored Strique matrices | 1,053 |
| Ecommerce checklist items not item-resolved for Strique homepage | 169 |
| Local checklist items not item-resolved for Strique homepage | 196 |
| Fresh live homepage checks performed in this pass | 1 URL |

Because ecommerce and local rows were not item-resolved into JSON matrices, and because several connector sources were unavailable, this remains a partial audit.

## Next Task Queue

1. Refresh sitewide crawl with Playwright and Firecrawl across the 51 sitemap URLs.
2. Rebuild item-level matrices for all seven checklists, marking ecommerce/local rows explicitly as `not_applicable` where they do not fit Strique.
3. Connect GSC and GA4, then refresh query/page, indexation, CTR, landing-page, and conversion checks.
4. Validate schema with a dedicated structured-data validator.
5. Fix repeated sitewide issues: H1 templates, canonical/sitemap mismatches, mobile tap targets, image alt handling, and performance.
