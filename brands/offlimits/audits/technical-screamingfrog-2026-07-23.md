# OFFLIMITS technical SEO crawl — Screaming Frog

**Target:** `https://offlimits.co.in`  
**Run date:** 2026-07-23  
**Run ID:** `20260723T124121Z-screamingfrog-technical`  
**Platform:** Shopify  
**Status:** Partial full technical audit — complete navigation crawl with throttled URLs rechecked, sampled media crawl, and bounded rendered verification. Full XML-sitemap URL expansion, GSC index coverage, field Core Web Vitals, and full accessibility remain blocked/not checked.

## Summary

The audited navigation set contains no confirmed internal 4xx or 5xx URLs. The initial crawls triggered Shopify HTTP 429 responses; those rows were treated as crawler-pressure artifacts, not broken pages. All 39 throttled HTML/XML URLs were recrawled at one request per second and resolved to either `200 OK` or an intentional `301`.

The highest-impact technical problems are:

1. 26 collection pages return more than 2 MB of HTML, with the largest close to 4.9 MB.
2. Images are heavy and layout-unstable: 68 of 112 sampled assets exceed 100 kB, and 105 assets are used in 545 placements without intrinsic size attributes.
3. Collection pagination is not exposed through crawlable anchor links on 10 important collections.
4. Forty key commercial collections receive internal links marked `nofollow`.
5. GoKwik analytics fails DNS, while Snapmint/theme JavaScript throws rendered-page errors.
6. The sampled product title is non-descriptive, while 24 audited pages have titles wider than Screaming Frog's 561-pixel snippet estimate.
7. Site-wide header/navigation links lack accessible anchor names.

## Crawl scope and data quality

- **Primary navigation crawl:** 232 encountered URLs; 84 internal HTML URLs plus utility/resource URLs.
- **Throttled retry:** 39 seed URLs recrawled without link following; all resolved to `200` or intentional `301`. The retry encountered 45 URLs after redirect destinations were followed.
- **Sampled media/link crawl:** 1,431 encountered URLs and 112 image assets. Its HTTP 429 rows are excluded from defect counts; its successful asset/link rows provide the image evidence below.
- **Rendered verification:** mobile viewport checks on homepage, product, collection, and blog templates.
- **Robots-blocked URLs:** 123 internal utility/faceted URLs. The sampled paths are search, account, wishlist, cart/checkout, and related Shopify endpoints; blocking is expected and is not reported as an SEO defect.

## Priority findings

### 1. Collection-page HTML is extremely large

- **Severity:** high
- **Status:** fail
- **Evidence:** 26 successful HTML URLs exceed 2 MB. Largest examples:
  - `/collections/men-new-releases` — 4,850,765 bytes
  - `/collections/new-arrivals` — 4,822,030 bytes
  - `/collections/mens-shoes` — 4,799,891 bytes
  - `/collections/new-arrivals-2026` — 4,680,436 bytes
  - `/collections/all` — 4,582,377 bytes
- **Fix:** profile the Shopify collection template for repeated inline product JSON, duplicate app markup, oversized inline CSS/JS, and excessive product-card payloads. Paginate server-side, remove unused app snippets, and defer non-critical widgets. Set a practical HTML budget below 1 MB, then remeasure the heaviest collections.
- **Owner:** Shopify theme developer / ecommerce engineering
- **Confidence:** high
- **Expected impact:** faster TTFB/parse time, lower memory use, improved mobile performance and crawl efficiency.

### 2. Images are oversized and commonly lack intrinsic dimensions

- **Severity:** high
- **Status:** fail
- **Evidence:** the successful media sample contains 112 image assets; 68 exceed 100 kB. The largest is a 1,192,639-byte JPEG, and six repeated PNG assets are about 972,798 bytes each. Screaming Frog recorded 105 affected assets across 545 placements without size attributes. Rendered checks found:
  - homepage: 103 of 111 images missing `width` or `height`
  - product: 15 of 20
  - collection: 10 of 14
- **Fix:** serve right-sized Shopify CDN variants using `image_url`, `image_tag`, `srcset`, and `sizes`; prefer AVIF/WebP where appropriate; add accurate intrinsic `width`/`height` or stable `aspect-ratio`; lazy-load below-the-fold media. Start with shared product-card and homepage sections.
- **Owner:** Shopify theme developer / design
- **Confidence:** high for sampled/templates; catalogue-wide asset count was not completed.
- **Expected impact:** lower transfer size and layout-shift risk; likely LCP improvement.

### 3. Collection pagination is not crawlable through anchor links

- **Severity:** high
- **Status:** fail
- **Evidence:** 10 collections expose pagination URLs outside an `<a href>`:
  - `/collections/all`
  - `/collections/low-top-shoes-for-men`
  - `/collections/men`
  - `/collections/men-new-releases`
  - `/collections/men-shoes` and its trailing-slash variant
  - `/collections/mens-shoes`
  - `/collections/new-arrivals`
  - `/collections/new-arrivals-2026`
  - `/collections/women`
- **Fix:** render previous/next and numbered pagination as ordinary crawlable anchor links in the Shopify collection template. JavaScript may enhance them, but must not be the only discovery mechanism.
- **Owner:** Shopify theme developer
- **Confidence:** high
- **Expected impact:** more reliable product discovery and internal link equity beyond page one.

### 4. Key internal collection links are marked `nofollow`

- **Severity:** high
- **Status:** fail
- **Evidence:** 43 successfully audited source pages contain 238 `rel="nofollow"` internal-link placements pointing to 40 commercial collection destinations, including `/collections/men`, `/collections/new-arrivals`, `/collections/men-basketball`, `/collections/men-trail`, `/collections/women-gym-training`, and `/collections/white-sneaker`.
- **Fix:** remove `nofollow` from ordinary navigation, category, and editorial links to indexable commercial collections. Retain it only where a deliberate crawl-control policy has a documented reason; do not use it as a substitute for robots, canonical, or faceted-navigation controls.
- **Owner:** Shopify theme developer / SEO
- **Confidence:** high for the audited templates
- **Expected impact:** restores normal internal PageRank flow and stronger discovery signals to important collections.

### 5. Analytics and third-party JavaScript are broken

- **Severity:** high
- **Status:** fail
- **Evidence:** `https://analytics.gokwik.co/analytics.js` fails DNS. Rendered homepage checks captured a Snapmint null-reference error and two `MutationObserver` errors. The GoKwik DNS failure was already present in the brand's 2026-07-13 audit.
- **Fix:** remove or replace the dead GoKwik analytics endpoint; confirm whether checkout/conversion events are dropping; update or conditionally initialize Snapmint only when its target node exists; guard theme observers against missing nodes.
- **Owner:** ecommerce engineering / analytics
- **Confidence:** high
- **Expected impact:** restores measurement reliability and reduces avoidable main-thread errors.

### 6. Product and collection title templates need correction

- **Severity:** high
- **Status:** fail
- **Evidence:** the rendered PDP sample uses `STRATA-01 - DARK BEIGE/NAVY`, which omits product type, audience, and brand. Across the audited non-product set, 24 titles exceed the 561-pixel estimate and 29 exceed 60 characters. The product H1 says `Beige/Sky Lace Up Running & Gym Shoe For Men`, which also conflicts with the title's colour wording.
- **Fix:** use a Shopify product-title pattern such as `{Product} – {Type} for {Audience} | OFFLIMITS`, while keeping important terms within the pixel limit. Reconcile product colour naming between title, H1, variant data, and structured data. Shorten the 24 pixel-overflow page titles individually.
- **Owner:** SEO / merchandising
- **Confidence:** high for the sampled PDP and audited collection/page set; catalogue-scale PDP count remains not checked.
- **Expected impact:** stronger relevance and more readable search snippets.

### 7. Header and image links lack accessible names

- **Severity:** medium
- **Status:** fail
- **Evidence:** every successfully audited HTML page has internal outlinks without anchor text. Shared header links to search, account, and wishlist are empty; homepage content also contains image links without alt/anchor text. The sampled media crawl found 262 affected placements. Rendered homepage checks found nine images without an `alt` attribute and 44 with empty alt text.
- **Fix:** add accessible names (`aria-label` or visible/visually hidden text) to icon-only search, account, wishlist, and cart links. Give meaningful linked images descriptive alt text; retain `alt=""` only for genuinely decorative, unlinked images.
- **Owner:** Shopify theme developer / content
- **Confidence:** high
- **Expected impact:** better screen-reader navigation and clearer internal-link context.

### 8. Search snippets overflow on important collection pages

- **Severity:** medium
- **Status:** fail
- **Evidence:** 24 titles exceed 561 pixels. Fifteen meta descriptions exceed 985 pixels, including `/collections/high-top-shoes-for-men`, `/collections/men-gym-training`, `/collections/mens-shoes`, `/collections/women-clothing`, and `/pages/return-exchange`. `/collections/all` has no meta description.
- **Fix:** rewrite around primary intent, front-load the differentiator, and remove repeated filler such as “work, travel, and everyday wear.” Use pixel width as the deciding signal.
- **Owner:** SEO / content
- **Confidence:** high
- **Expected impact:** fewer truncated snippets and clearer category positioning.

### 9. Internal links still point through five redirects

- **Severity:** medium
- **Status:** fail
- **Evidence:**
  - `/collections/men-bestsellers` → `/collections/mens-bestsellers`
  - `/collections/men-running-gym` → `/collections/mens-running-gym-shoes`
  - `/collections/mens-footwear` → `/collections/mens-shoes`
  - `/collections/sneaker-for-men` → `/collections/mens-sneakers`
  - `/collections/uk-13-size` → `/collections/size-13-shoes`
- **Fix:** update navigation, collection cards, sitemap/page content, and any theme settings to link directly to final destinations. Keep the redirects for external/legacy traffic.
- **Owner:** Shopify administrator / theme developer
- **Confidence:** high
- **Expected impact:** removes avoidable crawl hops and small latency/link-equity loss.

### 10. Referrer policy is missing on almost every audited HTML page

- **Severity:** medium
- **Status:** fail
- **Evidence:** 83 unique successful HTML URLs lack a secure `Referrer-Policy` header. HSTS is present. CSP and X-Frame-Options are present on HTML; Screaming Frog flags only Shopify's `/checkouts/internal/preloads.js` for those two headers.
- **Fix:** set `Referrer-Policy: strict-origin-when-cross-origin` at the edge if Shopify/CDN controls allow it, then test checkout, payment, analytics, and affiliate flows.
- **Owner:** platform/security
- **Confidence:** high
- **Expected impact:** reduced referrer-data leakage and clearer browser policy.

### 11. Protocol-relative resources and unsafe `_blank` links remain site-wide

- **Severity:** medium
- **Status:** fail
- **Evidence:** 75 successful HTML pages contain protocol-relative resource references. Affected shared assets include theme CSS/JS, logo SVGs, Shopify storefront scripts, and an app stylesheet. External social/press links open with `target="_blank"` without `noopener`, including Instagram, Facebook, YouTube, X, Pinterest, ANI, ThePrint, Tribune India, and GreenHonchos.
- **Fix:** emit explicit `https://` resource URLs. Add `rel="noopener noreferrer"` to external new-tab links.
- **Owner:** Shopify theme developer
- **Confidence:** high
- **Expected impact:** security hardening and more deterministic resource loading.

### 12. Heading and category duplication issues

- **Severity:** medium
- **Status:** fail
- **Evidence:** `/pages/technology` has no H1 in crawled HTML. `/collections/black-shoes-for-men` and `/collections/black-sneakers` share the same H1 intent. Forty-four pages have no H2 and 25 have non-sequential H2 structure; multiple H2s alone are not treated as an error.
- **Fix:** add a descriptive H1 to the technology page; consolidate or clearly differentiate the two black-sneaker collections; correct heading order in shared templates without choosing heading levels for styling.
- **Owner:** SEO / content / theme developer
- **Confidence:** high for raw HTML; the technology template was not included in rendered verification.
- **Expected impact:** clearer page hierarchy and less category-intent overlap.

### 13. Thin collection/support pages need selective improvement

- **Severity:** medium
- **Status:** fail
- **Evidence:** 13 pages contain fewer than 200 words, including `/collections/men-trail` (130), `/collections/women-shorts` (101), `/pages/store-gallery` (95), and `/pages/technology` (80).
- **Fix:** add unique decision-useful copy, product selection guidance, technology proof, FAQs, and contextual child links where useful. Do not pad `/pages/contact` merely to cross a threshold.
- **Owner:** SEO / content
- **Confidence:** medium; 200 words is diagnostic, not a ranking rule.
- **Expected impact:** better intent coverage and internal discovery.

### 14. URL hygiene is inconsistent

- **Severity:** low
- **Status:** fail
- **Evidence:** the blog handle produces `/blogs/blogs/...`; seven discovered URLs use underscores; one tracked collection URL contains `srsltid` and `utm_source=chatgpt.com`; `/collections/men-shoes/` canonicalises to the no-slash form.
- **Fix:** keep tracking parameters out of internal links, standardise no-trailing-slash internal URLs, and avoid new underscore paths. Treat `/blogs/blogs/` as a migration item: change only with a complete redirect and internal-link plan.
- **Owner:** SEO / Shopify administrator
- **Confidence:** high
- **Expected impact:** cleaner crawl paths and reporting.

## All Screaming Frog issue groups — triage

Counts below combine unique successful URLs from the primary crawl and seed-only retry. The image rows come from the successful media sample. Threshold-based opportunities are diagnostic, not automatic ranking defects.

| Issue group | Unique URLs / assets | Triage |
|---|---:|---|
| Validation: HTML document over 2 MB | 26 pages | Fix — high priority |
| Pagination: URL not in anchor tag | 10 pages | Fix — high priority |
| Links: internal nofollow outlinks | 43 audited source pages / 238 placements / 40 destinations | Fix — high priority |
| Images over 100 kB | 68 of 112 sampled assets | Fix — high priority |
| Images missing size attributes | 105 sampled assets / 545 placements | Fix |
| Images missing alt attribute | 5 sampled assets; rendered homepage found 9 | Fix meaningful images |
| Page titles over 561 pixels | 24 pages | Fix |
| Page titles over 60 characters | 29 pages | Use the pixel-width list |
| Meta descriptions over 985 pixels | 15 pages | Fix |
| Meta descriptions over 155 characters | 17 pages | Use the pixel-width list |
| Meta description missing | 1 page (`/collections/all`) | Fix |
| H1 missing | 1 page (`/pages/technology`) | Fix |
| H1 duplicate | 2 collection pages | Differentiate/consolidate |
| H2 missing | 44 pages | Review template/content need |
| H2 non-sequential | 25 pages | Fix hierarchy |
| H2 multiple | 16 pages | Not a defect by itself |
| Content low-content pages | 13 pages | Improve selectively |
| Content readability difficult | 2 pages | Editorial review |
| Internal redirection (3xx) | 5 URLs | Update internal links |
| Internal client error (4xx) | 39 initial rows | Rejected as false positives: all were HTTP 429 and passed seed-only retry |
| Internal blocked by robots.txt | 123 utility/faceted URLs | Accepted in sampled Shopify patterns |
| Canonicalised | 2 URLs | Accepted: tracking parameters and trailing slash canonicalise cleanly |
| Protocol-relative resources | 75 pages | Fix shared theme/app references |
| Unsafe cross-origin links | 75-page shared pattern | Add `noopener noreferrer` |
| Missing secure Referrer-Policy | 83 pages | Fix at platform/edge |
| Missing CSP / X-Frame-Options | 1 JS resource | Low priority; HTML responses have these protections |
| Internal outlinks with no anchor text | Site-wide successful HTML pattern; 262 sampled placements | Fix shared icons and linked images |
| External no response | 1 (`analytics.gokwik.co`) | Fix — DNS failure |
| External client error (4xx) | 3 links | Manual recheck; publishers/Flipkart returned crawler `403`, not proven broken |
| Pages with high external outlinks | 1 page | Review; likely contextual/policy content |
| URL parameters / GA tracking parameters | 5 / 1 | Remove tracked URL from internal content |
| URL underscores / uppercase / over 115 chars | 7 / 1 / 1 | Low-priority hygiene |
| URL repetitive path | `/blogs/blogs/` pattern | Migration item, not an emergency |
| Page title below 30 characters / 200 pixels | 1 page | Review |
| Page title same as H1 | 2 pages | Opportunity, not inherently defective |
| Pagination non-indexable | 1 page | Review with pagination-anchor fix |

## Validated non-issues

- No confirmed internal 4xx or 5xx URLs remain after the seed-only retry.
- No redirect chains or loops were confirmed.
- HSTS is present; no HTTP or mixed-content URLs were found.
- No missing/conflicting/multiple canonical defects were found in the successful navigation set.
- The tracked query URL canonicalises to its clean collection URL; the trailing-slash collection URL canonicalises to the no-slash form.
- Rendered home, product, collection, and blog templates each had one H1, a canonical, a viewport tag, and no horizontal mobile overflow.
- Rendered JSON-LD was parseable on all four samples:
  - homepage: `OnlineStore`
  - product: `BreadcrumbList`, `Product`
  - collection: `BreadcrumbList`, `FAQPage`
  - blog: `BreadcrumbList`, `FAQPage`, `Article`

## Full-audit status

| Check | Status | Evidence / blocker | Next action |
|---|---|---|---|
| robots.txt handling | pass | 123 utility/faceted URLs blocked; sampled patterns are expected Shopify search/account/cart/checkout paths | Review only when faceted SEO requirements change |
| XML sitemap endpoints | pass | six sitemap endpoints returned `200` in the throttled retry | Keep current |
| Full sitemap URL expansion | not_checked_blocked | Shopify quota repeatedly throttled bulk expansion; final audit used navigation coverage plus seed-only sitemap checks | Run an overnight sitemap/list crawl at ≤1 URL/s |
| Internal 4xx/5xx | pass | all 39 prior 429 URLs recrawled to `200` or intentional `301`; no true 4xx/5xx | Monitor |
| Redirect chains/loops | pass | none confirmed | Keep current |
| Direct internal redirects | fail | five legacy routes linked internally | Update internal links |
| Canonicals | pass | no missing/conflicting canonicals; two intentional canonicalised variants | Keep current |
| GSC index coverage / orphans | not_checked_blocked | GSC is not connected to this workspace | Connect GSC through Composio |
| Field LCP / INP / CLS | not_checked_blocked | no PageSpeed/CrUX key or connected field provider | Run `tools/google_pagespeed.py cwv` after connection |
| Full Lighthouse lab audit | not_checked_blocked | not run in this Screaming Frog crawl | Run Lighthouse separately |
| Rendered mobile/template parity | pass | four bounded mobile template checks | Expand only if template-specific regressions are suspected |
| Structured-data parsing | pass | Screaming Frog reported no validation/parse issue group; four rendered samples parsed | Validate rich-result eligibility after schema changes |
| Full accessibility/WCAG | not_checked_blocked | only obvious rendered DOM/mobile signals were checked | Run a dedicated accessibility audit |

## Implementation order

1. **Theme performance sprint:** reduce collection HTML, fix product-card/image sizing, compress the largest image assets, and make pagination crawlable.
2. **Measurement/runtime sprint:** repair GoKwik analytics and Snapmint/theme JavaScript.
3. **SEO template sprint:** product-title pattern, collection title/meta rewrites, technology H1, duplicate category intent.
4. **Theme hygiene sprint:** accessible icon links, direct redirect targets, explicit HTTPS resources, `noopener`, referrer policy.
5. **Close blocked evidence:** overnight sitemap expansion, GSC, CrUX/PageSpeed, Lighthouse, and accessibility.

## Evidence

- Clean primary crawl and exports: `brands/offlimits/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl-final/`
- Seed-only 429 retry: `brands/offlimits/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl-final/429-recrawl/`
- Successful media/link sample: `brands/offlimits/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl/`
- Rendered verification: `brands/offlimits/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl-final/rendered-verification.json`
