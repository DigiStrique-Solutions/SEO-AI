---
title: 26. Measurement And Validation
sidebar_position: 30
---

# 26. Measurement And Validation

Checklist: `site-architecture-seo`

Source: `docs/checklists/site-architecture-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `site-architecture-seo.26-measurement-and-validation.4db9751f`

Original checklist item: Crawl before and after architecture changes.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Crawl before and after architecture changes." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 2

Item ID: `site-architecture-seo.26-measurement-and-validation.5dcea4ac`

Original checklist item: Track number of indexable pages by section and template.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track number of indexable pages by section and template." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 3

Item ID: `site-architecture-seo.26-measurement-and-validation.eacd5881`

Original checklist item: Track orphan pages and click depth.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track orphan pages and click depth." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Adjust navigation, breadcrumbs, contextual links, or taxonomy so priority pages are reachable and clearly related.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 4

Item ID: `site-architecture-seo.26-measurement-and-validation.7d00b684`

Original checklist item: Track internal links to priority pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track internal links to priority pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Adjust navigation, breadcrumbs, contextual links, or taxonomy so priority pages are reachable and clearly related.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 5

Item ID: `site-architecture-seo.26-measurement-and-validation.6b6ec793`

Original checklist item: Track GSC impressions, clicks, CTR, and position by page group.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track GSC impressions, clicks, CTR, and position by page group." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the data source, property scoping, export, tagging, or report definition before using the metric for decisions.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 6

Item ID: `site-architecture-seo.26-measurement-and-validation.ae72f07c`

Original checklist item: Track GA4 organic landing page engagement and conversion by section.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track GA4 organic landing page engagement and conversion by section." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS, GA4 or PostHog.
3. Use analytics data only when the property, date range, and conversion definitions are known.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS, GA4 or PostHog

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the data source, property scoping, export, tagging, or report definition before using the metric for decisions.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 7

Item ID: `site-architecture-seo.26-measurement-and-validation.ed4e6385`

Original checklist item: Track sitemap submitted, discovered, indexed, and excluded counts.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track sitemap submitted, discovered, indexed, and excluded counts." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 8

Item ID: `site-architecture-seo.26-measurement-and-validation.1facd998`

Original checklist item: Track crawl errors, redirect chains, soft 404s, and server errors.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Track crawl errors, redirect chains, soft 404s, and server errors." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 9

Item ID: `site-architecture-seo.26-measurement-and-validation.9428776f`

Original checklist item: Validate navigation and key paths on desktop and mobile.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Validate navigation and key paths on desktop and mobile." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Mobile rendering, accessibility, and performance influence user success and can affect search quality signals, crawl efficiency, and conversion quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS, Lighthouse, PageSpeed, CrUX.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS, Lighthouse, PageSpeed, CrUX

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Adjust navigation, breadcrumbs, contextual links, or taxonomy so priority pages are reachable and clearly related.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 10

Item ID: `site-architecture-seo.26-measurement-and-validation.404d4323`

Original checklist item: Validate a sample of templates, not just one page.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Validate a sample of templates, not just one page." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.
