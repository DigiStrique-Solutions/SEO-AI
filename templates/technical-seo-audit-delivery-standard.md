# Technical SEO Audit Delivery Standard

## Purpose

Use this standard for every brand technical-data request and technical SEO audit. It preserves the issue-register format in the approved reference workbook while keeping every result brand-specific and evidence-backed.

Reference workbook: `Off-Limits - Technical SEO Audit` (Google Sheets ID `1SBWFRNwe66iL6vS4P_lA48x6zEG4ckk0QX8NzJxqC8g`). The workbook is a format reference only; do not reuse its URLs, recommendations, statuses, or findings for another brand.

## Required inputs and provenance

| Source | Use for | Required handling |
| --- | --- | --- |
| Screaming Frog | Crawlability, status codes, canonicals, metadata, headings, content, images, internal links, URLs, sitemap, robots, rendering | Keep/export the raw crawl data and record the crawl configuration, date, crawl scope, and source path. |
| Google Search Console | Organic clicks, impressions, CTR, positions, query/page opportunities, index coverage, Core Web Vitals | Compare the latest 6–12 months with the equivalent preceding period where access permits. State search type, device/country filters, and dates. |
| GA4 | Organic users, sessions, engagement, landing pages, conversions, revenue | Filter to Organic Search and record property, attribution/report configuration, filters, and dates. |

Before analysis, load the target brand's `context.md` and `knowledge.md`. Log every external run under `brands/<brand_id>/logs/<category>/activity.jsonl`, with raw source payloads in `raw/`.

## Deliverable format

Create one Google Sheets technical-audit workbook per brand/run. Use separate, plainly named tabs by issue type rather than combining unrelated actions in one generic sheet. Freeze row 1 and columns A:B when they hold the identifier and URL. Preserve the approved tab style: a serial number, the live URL/evidence, current state, recommended state/fix, and implementation tracking.

### Standard tab schemas

Use the smallest schema that captures the evidence. Add columns only when the issue needs them.

| Issue tab | Required columns |
| --- | --- |
| URL Structure Optimization | `Sr. no.` · `Current Website URL Structure` · `Content Type` · `Status Code` · `Status` · `Indexability` · `Suggested Website URL Structure` · `Current Canonical Link` · `Suggested Canonical Link` · `Implementation Status` |
| Meta Tags / H1 Tags Missing | `Sr. no.` · `Address` · `Current Meta Title` · `Length` · `Suggested Meta Title` · `Length` · `Current Meta Description` · `Length` · `Suggested Meta Description` · `Length` · `Current H1 Tag` · `Length` · `Suggested H1 Tag` · `Length` · `Implementation Status` |
| Duplicate Meta Title | `Sr. no.` · `Address` · `Indexability` · `Meta Title` · `Title Length` · `Suggested Meta Title` · `Title Length` · `Implementation Status` |
| Duplicate Meta Description | `Sr. no.` · `Address` · `Indexability` · `Meta Description` · `Meta Description Length` · `Suggested Meta Description` · `Meta Description Length` · `Implementation Status` |
| Canonical Tags Missing | `Sr. no.` · `Address` · `Indexability Status` · `Recommended Canonical Tag` · `Implementation Status` |
| Redirection Errors (3xx) | `Sr. no.` · `Address` · `Content Type` · `Status Code` · `Status` · `Indexability` · `Indexability Status` · `Redirect URL` · `Comments` · `Implementation Status` |
| Broken Links (4xx) | `Sr. no.` · `Address` · `Content Type` · `Status Code` · `Status` · `Indexability` · `Indexability Status` · `Redirect URL` · `Implementation Status` |
| Image Compression (Over 100 KB) | `Sr. no.` · `Address` · `Content Type` · `Size (Bytes)` · `Size (KB)` · `Indexability` · `Suggestions` |

Add distinct tabs where evidence exists for: redirect chains/loops, server errors, robots/noindex, duplicate or thin content, missing or duplicate headings, image alt/broken-image issues, internal-linking/crawl depth, XML sitemap, hreflang, schema, JavaScript rendering, mobile, GSC performance and indexing, Core Web Vitals, GA4 organic landing pages, GA4 conversions, and cross-platform opportunities.

### Consolidated priority register

Include a `Priority Action Plan` tab using this exact column order:

`Category` · `Issue` · `Data Source` · `Affected URLs` · `Current Data` · `SEO Impact` · `Priority` · `Recommended Fix`

For each finding, include a severity (`Critical`, `High`, `Medium`, or `Low`), source/date, quantification, URL count/list or an attached URL-level tab, concrete owner-ready fix, and confidence. Prioritize by expected SEO impact × affected URL count × implementation effort. Use `not_checked_blocked` where a data source or rendered verification is unavailable—never infer a pass.

### Executive summary

Add a concise summary tab or linked companion Google Doc covering:

1. Technical health and the most consequential crawl/indexation issues.
2. Organic performance: clicks, impressions, CTR, position, traffic, and engagement trends.
3. Five to ten highest-impact opportunities and clearly marked quick wins.
4. Cross-platform findings connecting crawl data with GSC and GA4 outcomes.
5. A sequenced plan: Immediate (0–30 days), Short term (30–60 days), and Medium term (60–90 days).

## Interpretation rules

- Treat a Screaming Frog status as crawler evidence, not proof of live-user behavior; validate meaningful 4xx/5xx/429 findings where feasible.
- Separate GSC and GA4 metrics; explain material clicks-versus-sessions differences instead of merging them.
- Label CrUX/field and Lighthouse/lab Core Web Vitals separately.
- Do not make generic recommendations. Tie each fix to the affected URLs, source evidence, and expected result.
- Suggested metadata and canonicals require manual relevance checks before implementation; do not fabricate keywords, commercial claims, or canonical targets.
- `Implementation Status` is tracking only. Use values such as `Not started`, `In progress`, `Blocked`, `Ready for QA`, `Done`, and `Not applicable`; do not mark `Done` without post-release verification.
