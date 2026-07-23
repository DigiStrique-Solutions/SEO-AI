# Strique technical SEO crawl - Screaming Frog

**Target:** https://www.strique.io  
**Run date:** 2026-07-23  
**Run ID:** `20260723T111541Z-screamingfrog-technical`  
**Status:** Partial technical audit - complete Screaming Frog spider crawl plus bounded rendered verification; CWV, GSC index coverage, full JavaScript rendering, and a full accessibility audit were not run.

## Summary

Screaming Frog crawled **121 internal URLs**, including **49 HTML URLs**: **38 indexable pages** and **11 query-string contact variants correctly canonicalised to `/contact`**. Every internal URL returned `200 OK`. The crawl found **no internal 4xx/5xx URLs, redirect chains, redirect loops, missing page titles, missing H1s, or conflicting canonicals**.

The most consequential defects are oversized images, missing intrinsic image dimensions, site-wide missing security headers, and a site-wide logo link with no accessible anchor name. Snippet-length and content-depth issues affect a smaller set of pages.

## Priority findings

### 1. Homepage serves a 10.78 MB PNG

- **Severity:** high
- **Evidence:** `/ad%20examples/ad-8.png` is 10,779,000 bytes and is referenced twice from the homepage. Four other images exceed 100 kB: `/images/inc5-case-study.png` (843,489 bytes), three `/images/product/*.jpg` files (371,937-407,790 bytes).
- **Fix:** replace the 10.78 MB PNG with an appropriately sized AVIF/WebP asset; compress and resize all five assets; provide `srcset`/`sizes`; lazy-load below-the-fold images; remove the duplicate homepage reference if it is not intentional.
- **Owner:** frontend/design
- **Confidence:** high
- **Expected impact:** lower transfer size and likely LCP improvement, especially on mobile.

### 2. Fifteen image assets lack intrinsic dimensions across 169 placements

- **Severity:** high
- **Evidence:** Screaming Frog exported 169 affected image placements. Shared footer images account for most occurrences, so one template fix has site-wide reach.
- **Fix:** add correct `width` and `height` attributes or an equivalent stable `aspect-ratio` for every affected image component. Start with shared footer assets and the product/customer imagery.
- **Owner:** frontend
- **Confidence:** high
- **Expected impact:** lower layout-shift risk.

### 3. HSTS, CSP, and X-Frame-Options are absent site-wide

- **Severity:** medium
- **Evidence:** all 121 crawled internal responses were flagged for missing `Strict-Transport-Security`, `Content-Security-Policy`, and `X-Frame-Options`.
- **Fix:** set HSTS at the CDN/edge after confirming every subdomain is HTTPS-ready; deploy a tested CSP and include `frame-ancestors`; add `X-Frame-Options: SAMEORIGIN` as a compatibility fallback where appropriate.
- **Owner:** platform/security
- **Confidence:** high for header absence; medium for the final policy values, which require application testing.
- **Expected impact:** security hardening; indirect trust and risk reduction rather than a direct ranking gain.

### 4. Header logo link has no accessible name

- **Severity:** medium
- **Evidence:** Screaming Frog flagged internal outlinks without anchor text on all 49 HTML URLs; the export contains 48 instances of the navigation link to `/` with blank anchor and image alt text.
- **Fix:** give the home link an accessible name such as `aria-label="Strique home"` or meaningful logo alt text. Do not rely on a visually empty SVG.
- **Owner:** frontend
- **Confidence:** high
- **Expected impact:** better keyboard/screen-reader navigation and clearer link context.

### 5. Five images have empty alt text; at least one appears meaningful

- **Severity:** medium
- **Evidence:** empty alt text was found on the Strique logomark, ISO footer logo, footer glow, ISO ring, and the homepage ad creative. The ad creative is also the 10.78 MB image.
- **Fix:** keep `alt=""` only for genuinely decorative assets. Add concise functional/descriptive alt text to the linked brand mark, certification mark, and ad creative when they convey information.
- **Owner:** frontend/content
- **Confidence:** medium because decorative intent is a design decision.

### 6. Search snippets are likely to truncate on six important pages

- **Severity:** medium
- **Evidence:** titles exceed the 561-pixel estimate on `/product` (625 px) and `/trust-center` (606 px). Meta descriptions exceed the 985-pixel estimate on `/customers/powerlook`, `/customers/inc5`, `/product`, and `/solutions/b2b-saas`; five pages exceed 155 characters.
- **Fix:** rewrite the two titles and four pixel-overflow descriptions around the primary intent and front-load the differentiator. Pixel width is the deciding signal; character thresholds are advisory.
- **Owner:** SEO/content
- **Confidence:** high

### 7. Eight indexable landing/hub pages contain fewer than 200 words

- **Severity:** medium
- **Evidence:** `/contact` (88), `/vs` (103), `/integrations` (135), `/for` (143), `/customers` (181), `/solutions` (182), `/integrations/hubspot` (182), and `/integrations/google-ads` (180).
- **Fix:** strengthen the hub and integration pages with unique decision-useful copy, proof, FAQs, and links to child pages. Do not pad `/contact` merely to cross an arbitrary threshold.
- **Owner:** SEO/content
- **Confidence:** medium; Screaming Frog's 200-word threshold is diagnostic, not a ranking rule.

### 8. Heading hierarchy skips levels on eight pages

- **Severity:** low
- **Evidence:** `/customers`, `/for`, `/solutions`, `/integrations`, `/for/founders`, `/for/cmos`, `/for/marketing-managers`, and `/vs` are flagged as non-sequential. `/contact` has no H2.
- **Fix:** make the heading outline descend logically without choosing heading levels for styling. Add a useful H2 on `/contact` only if the page structure warrants one.
- **Owner:** frontend/content
- **Confidence:** high

### 9. Two case-study H1s are unusually long

- **Severity:** low
- **Evidence:** `/customers/powerlook` has a 76-character H1 and `/customers/inc5` has a 73-character H1.
- **Fix:** shorten only if scanability improves; there is no hard SEO character limit for H1s.
- **Owner:** content
- **Confidence:** high that the threshold was exceeded; low that it materially harms SEO.

## All Screaming Frog issue groups

| Issue group | SF priority | URLs | Triage |
|---|---:|---:|---|
| Images: Missing Alt Text | Low | 5 | Review; some are decorative, some likely meaningful |
| Images: Missing Size Attributes | Low | 15 assets / 169 placements | Fix |
| Links: Internal Outlinks With No Anchor Text | Low | 49 | Fix shared logo link |
| H2: Duplicate | Low | 16 | Template similarity; review, not inherently defective |
| Security: Missing HSTS Header | Low | 121 | Fix at edge |
| H2: Missing | Low | 1 | Low-priority review |
| Response Codes: External Client Error (4xx) | Low | 1 | Recheck; OpenAI returned 403 to crawler |
| Security: Missing Content-Security-Policy Header | Low | 121 | Fix with tested policy |
| Meta Description: Over 985 Pixels | Low | 4 | Fix |
| Canonicals: Canonicalised | High | 11 | Accepted: contact parameters correctly canonicalise |
| Images: Over 100 kB | Medium | 5 | Fix urgently |
| Page Titles: Below 30 Characters | Medium | 5 | Mostly legal/comparison pages; review |
| H2: Non-Sequential | Low | 8 | Fix |
| Page Titles: Over 561 Pixels | Medium | 2 | Fix |
| Content: Low Content Pages | Medium | 8 | Improve selectively |
| Page Titles: Below 200 Pixels | Medium | 1 | `/terms`; optional |
| URL: Parameters | Low | 11 | Accepted; intentional contact state |
| Meta Description: Over 155 Characters | Low | 5 | Use pixel-width list for fixes |
| Page Titles: Over 60 Characters | Medium | 2 | Use pixel-width list for fixes |
| Content: Readability Difficult | Low | 2 | `/trust-center`, `/security`; editorial review |
| H2: Multiple | Low | 32 | Not an error when hierarchy is logical |
| Security: Missing X-Frame-Options Header | Low | 121 | Fix or cover with CSP `frame-ancestors` |
| Links: Pages With High External Outlinks | Low | 2 | `/privacy-policy`, `/trust-center`; expected context |
| H1: Over 70 Characters | Low | 2 | Optional shortening |

## Validated non-issues

- All 121 internal URLs returned `200 OK`.
- No internal redirects, redirect chains, redirect loops, or internal 4xx/5xx responses were found.
- All 38 indexable HTML pages have a title, meta description, H1, and canonical.
- The 11 query-string contact URLs canonicalise to `https://www.strique.io/contact`; they are not duplicate indexable pages.
- A rendered mobile check of `/`, `/product`, `/contact`, and `/trust-center` found one H1, a canonical, a viewport tag, no horizontal overflow, and no console errors/warnings on each page.
- Structured data is client-injected. The rendered homepage exposed parseable `Organization`, `WebSite`, `SoftwareApplication`, and `FAQPage` JSON-LD. `/product` exposed `Organization`, `WebSite`, and `SoftwareApplication`; the other two checked templates exposed `Organization` and `WebSite`.

## Blocked / not checked

- **Core Web Vitals:** not checked; Screaming Frog PageSpeed integration was not configured. Run PageSpeed/CrUX separately and keep lab and field results distinct.
- **Full rendered crawl:** not checked; only four representative templates were rendered. JavaScript-only issues across all 49 HTML URLs remain unverified.
- **Full accessibility:** not checked; the rendered checks covered only obvious DOM signals and mobile overflow, not WCAG conformance.
- **GSC index coverage and orphan detection:** not checked in this run.
- **Sitemap membership:** the crawl export did not contain sitemap membership data, so sitemap coverage is unverified.

## Evidence

- Raw crawl database and exports: `brands/sample_brand/logs/audits/raw/2026-07-23-screamingfrog-technical-crawl/`
- Screaming Frog issue overview: `issues_overview_report.csv`
- Per-issue URL exports: `issues_reports/`
- Rendered verification: `rendered-verification.json`

