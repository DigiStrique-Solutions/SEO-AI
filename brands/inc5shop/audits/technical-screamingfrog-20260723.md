# Technical SEO Crawl — Inc.5

**Run:** `inc5shop-screamingfrog-20260723`

**Target:** `https://inc5shop.com/`

**Date:** 2026-07-23

**Status:** **partial** — Screaming Frog received HTTP 429 for 712 of 753 HTML URLs. Those responses are crawl throttling, not broken pages. Four representative throttled URLs returned 200 when retested slowly.

## Summary

The crawl verified 11 actionable issue groups. The largest risks are an oversized indexable collection footprint, heavy image payloads, missing image attributes, a broken Shopify app JavaScript asset, and indexable utility/template URLs. Homepage mobile field Core Web Vitals pass at p75, but the one-run mobile Lighthouse result is poor and exposes a substantial lab-performance gap.

The crawl encountered 2,327 URLs: 2,253 internal and 74 external. It successfully crawled 1,539 internal resources, including 41 HTML pages, 1,467 images, 26 JavaScript files and 5 CSS files. It received 712 HTTP 429 responses, no confirmed internal 404s, no 5xx responses and no internal redirects.

## Priority findings

### T01 — Sitemap/index bloat from operational collections

- **Severity:** high
- **Status:** fail
- **Evidence:** the live sitemap contains 3,251 URLs: 2,584 products, 351 collections, 217 pages, 97 blog URLs, the homepage and `agents.md`. A conservative handle-pattern review flagged 88 collection URLs for manual indexability review, including `/collections/test`, `/collections/testnew`, `/collections/full-fresh-aug-2023`, `/collections/zero-stock-25-09`, `/collections/creative-31-10-2023`, `/collections/put-in-draft-22-11-2023`, `/collections/shoot-pending-14-05-2025` and dated EOSS/edit collections.
- **Fix:** classify all 351 collections as permanent SEO landing page, temporary campaign, internal merchandising, or obsolete. Keep only canonical, useful landing pages indexable and in the sitemap. Unpublish obsolete collections; use `noindex,follow` for necessary internal merchandising pages that must remain live; remove non-indexable URLs from the sitemap.
- **Owner:** SEO + ecommerce merchandising + Shopify developer
- **Confidence:** high for the footprint; medium for individual removals until merchandising owners approve them.

### T02 — Image payload is excessive

- **Severity:** high
- **Status:** fail
- **Evidence:** 1,117 of 1,467 crawled images exceed 100 KB; 202 exceed 500 KB; 189 exceed 1 MB. The largest is 4,932,795 bytes. Several PNG product/creative assets are 2–4.9 MB.
- **Fix:** convert photographic PNGs to AVIF/WebP, cap source dimensions to the largest rendered breakpoint, use Shopify width parameters consistently, provide responsive `srcset`/`sizes`, preload only the true LCP image and lazy-load below-the-fold imagery.
- **Owner:** Shopify developer + creative/merchandising
- **Confidence:** high.

### T03 — Missing image alternative text and dimensions

- **Severity:** medium
- **Status:** fail
- **Evidence:** 235 image URLs have no `alt` attribute, 19 have an empty `alt`, and 241 images lack width/height attributes. High-volume source templates include `/collections/new-wallets`, `/collections/mens-june-eoss-2026`, `/collections/shop-our-bestsellers`, `/collections/bags-june-eoss-2026`, `/collections/flat-50` and `/collections/shop-wallets`.
- **Fix:** populate meaningful product/category alt text from verified product attributes; keep decorative images intentionally empty (`alt=""`); emit intrinsic width and height or a stable CSS aspect ratio from the Shopify image object.
- **Owner:** Shopify developer + content/merchandising
- **Confidence:** high.

### T04 — Broken Shopify app JavaScript asset

- **Severity:** medium
- **Status:** fail
- **Evidence:** `https://cdn.shopify.com/extensions/019f455a-4fa1-7c03-aea8-57ec03bc13c6/omni-storelocator-app-2-307/assets/map-style.js` returns 404 and is referenced by `/pages/contactus`, `/pages/payment-delivery-policy`, `/pages/about-us` and `/pages/refund-policy`.
- **Fix:** update/reinstall the Omni Store Locator app embed or remove the stale script reference. Regression-test the contact/store-locator experience after the fix.
- **Owner:** Shopify developer / app owner
- **Confidence:** high.

### T05 — Cart utility page is indexable

- **Severity:** medium
- **Status:** fail
- **Evidence:** `/cart` returns 200, has a self-referencing canonical and no robots directive. Screaming Frog classifies it as indexable.
- **Fix:** add `noindex,follow` to cart and other non-search utility templates; verify account, search, checkout and customer-authentication patterns separately once crawl throttling is removed.
- **Owner:** Shopify developer + SEO
- **Confidence:** high for `/cart`; other utility templates are not fully checked.

### T06 — Heading structure is inconsistent

- **Severity:** medium
- **Status:** fail
- **Evidence:** raw HTML has no H1 on `/pages/clearance-sale`, `/pages/care-instructions` and `/blogs/blog`; `/cart` and `/collections/mens-formals` contain multiple H1s; men’s and women’s sandals share the generic H1 `Collection: Sandals`; 36 of 41 successful pages have a non-sequential heading order. Rendered mobile checks found five H1s on the homepage and a promotional sale H1 instead of a descriptive blog H1 on `/blogs/blog`.
- **Fix:** enforce one descriptive page H1 per template, demote modal/loyalty/banner headings, make collection H1s unique, and correct theme heading order without choosing levels for visual styling.
- **Owner:** Shopify theme developer + SEO/content
- **Confidence:** high on the sampled templates; sitewide coverage is blocked by 429 responses.

### T07 — Metadata coverage and length need template cleanup

- **Severity:** medium
- **Status:** fail
- **Evidence:** among 41 successful HTML pages, 13 lack a meta description and 22 exceed 155 characters; 10 titles exceed 60 characters and 8 are below 30 characters. Missing descriptions include `/blogs/blog`, `/pages/care-instructions`, `/pages/clearance-sale`, `/collections/bags-june-eoss-2026`, `/collections/mens-june-eoss-2026`, `/collections/new-wallets`, `/collections/shop-wallets` and `/collections/latest-style-drop`.
- **Fix:** create template guardrails and write unique intent-led metadata for indexable pages. Noindex or unpublish temporary collections instead of optimizing metadata that should not rank.
- **Owner:** SEO/content + ecommerce merchandising
- **Confidence:** high for the successful sample; sitewide counts are blocked.

### T08 — Crawler throttling prevents a complete technical audit

- **Severity:** medium
- **Status:** not_checked_blocked for sitewide HTML checks
- **Evidence:** 712 internal HTML URLs returned 429 to Screaming Frog: 557 product, 101 collection, 50 blog, 2 page, 1 policy and 1 customer-authentication URL. Slow retests of a collection, product, blog index and FAQ returned 200.
- **Fix:** approve a crawl window and allowlist the audit IP plus Screaming Frog user agent, or provide a saved low-speed Screaming Frog configuration. Re-crawl at 1–2 threads with a delay, then rerun all response-code, canonical, pagination, duplicate-content and structured-data reports.
- **Owner:** ecommerce platform/infrastructure + SEO
- **Confidence:** high that 429 is throttling; no claim is made that the affected URLs are broken.

### T09 — Mobile lab performance is poor despite passing field CWV

- **Severity:** medium
- **Status:** fail (lab); pass (field Core Web Vitals)
- **Evidence:** PageSpeed mobile lab score 40; LCP 5.5 s, TBT 1,930 ms, interactive 28.8 s and speed index 7.6 s. URL-level mobile CrUX p75 for 2026-06-24 to 2026-07-21 passes LCP 1,752 ms, INP 159 ms and CLS 0.00; URL TTFB is 816 ms and classified average.
- **Fix:** prioritize JavaScript execution reduction and image delivery; audit third-party Shopify apps, defer non-critical scripts, remove unused app embeds, and optimize/preload the true LCP asset. Validate changes with repeat lab runs and monitor field p75 separately.
- **Owner:** Shopify performance developer
- **Confidence:** high for reported measurements; one lab run is diagnostic, not field proof.

### T10 — Low-level security and link hygiene issues

- **Severity:** low
- **Status:** fail
- **Evidence:** representative HTML responses have HSTS, CSP, X-Frame-Options and `nosniff`, but no `Referrer-Policy`. Forty-one successful pages use protocol-relative resource links. Four source pages include `target="_blank"` external links without `noopener`/`noreferrer`. `/pages/payment-delivery-policy` links to `http://inc5shoes.co.in/`, which takes two redirects to reach `https://inc5shop.com/`.
- **Fix:** add `Referrer-Policy: strict-origin-when-cross-origin`; emit explicit HTTPS resource URLs; add `rel="noopener noreferrer"` to new-tab external links; replace the legacy HTTP domain link with the final Inc.5 URL.
- **Owner:** Shopify developer + content owner
- **Confidence:** high.

### T11 — Three `.webp` URLs are served as JPEG

- **Severity:** low
- **Status:** fail
- **Evidence:** `MEN_FOOTWEAR_800x.webp`, `BAGS_800x.webp` and `WOMEN_FOOTWEAR_800x.webp` return `Content-Type: image/jpeg`.
- **Fix:** re-export as true WebP or rename the assets to match their actual format, then refresh Shopify/CDN references.
- **Owner:** creative + Shopify developer
- **Confidence:** high.

## Check status

| Check | Status | Evidence/result |
|---|---|---|
| Crawl discovery | pass | 2,327 URLs encountered |
| Sitewide HTML response codes | not_checked_blocked | 712 HTML requests throttled with 429 |
| Confirmed internal 404/5xx | not_checked_blocked | none verified; 429s must not be counted as broken URLs |
| Internal redirects/chains | pass on observed set | zero internal 3xx; no internal redirect chains |
| External resources | fail | one JavaScript asset returns 404 on four pages |
| Robots handling | pass | two expected Shopify resources blocked; no indexable page proven blocked |
| Sitemap/index hygiene | fail | 351 collections; 88 conservative suspect-pattern matches |
| Canonicals | not_checked_blocked sitewide | sampled canonicals valid; one Screaming Frog warning was caused by a 429 target |
| Pagination | not_checked_blocked | 24 non-200/sequence warnings all depend on 429 page-2 responses |
| Utility indexation | fail | `/cart` indexable |
| Titles/meta | fail | length and missing-description issues in successful sample |
| Headings | fail | missing, multiple, duplicate and rendered-template issues |
| Exact/near duplicates | not_checked_blocked sitewide | none in the 41-page successful sample |
| Image optimization | fail | weight, alt and dimension issues |
| HTTPS/mixed content | pass | all internal URLs HTTPS; zero mixed-content URLs |
| Security headers | partial | HSTS/CSP/X-Frame-Options/nosniff pass on sampled HTML; Referrer-Policy missing |
| Structured data | not_checked_blocked | structured-data extraction was not enabled in this Screaming Frog configuration; retain prior rendered-schema audit evidence |
| JavaScript/mobile rendering | partial | four representative mobile rendered pages returned 200 with visible main content; not sitewide |
| Core Web Vitals | partial | homepage URL-level field CWV checked; other templates not checked |
| Accessibility | not_checked_blocked | no full rendered accessibility crawl was run |

## Screaming Frog warnings excluded as defects

- The 712 HTTP 429 responses are throttling, not verified broken URLs.
- The 24 pagination errors depend on page-2 URLs that returned 429.
- The non-indexable canonical warning for the filtered `like-mother-like-daughter` URL is caused by a 429 on its canonical target; a slow retest returned 200.
- `/collections/mens-boots` is a legitimate 200 collection with substantial content, not a soft 404.
- Screaming Frog’s missing CSP/X-Frame-Options totals include image/static-resource responses. Representative HTML responses contain both headers.
- Duplicate/multiple H2 warnings largely reflect repeated theme components and are not defects without page-specific context.

## Evidence

- Raw crawl and exports: `brands/inc5shop/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl/`
- Screaming Frog version: 24.3
- Crawl file: `crawl.seospider`
- Primary reports: `issues_overview_report.csv`, `crawl_overview.csv`, `internal_all.csv`, `all_inlinks.csv`, `images_all.csv`, `issues_reports/`
- Sitemap inventory: `sitemap-inventory.json`
- Rendered checks: `rendered-checks.json`
- PageSpeed/CrUX: `pagespeed-home-mobile.json`

## Next action

Allowlist the audit crawl or provide a low-speed configuration, then rerun. Until the 712 throttled HTML URLs are successfully crawled, this remains a partial audit and sitewide broken-link, canonical, pagination, duplicate-content, structured-data and accessibility claims remain blocked.
