---
title: 25. Architecture Governance
sidebar_position: 29
---

# 25. Architecture Governance

Checklist: `site-architecture-seo`

Source: `docs/checklists/site-architecture-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `site-architecture-seo.25-architecture-governance.665ae76e`

Original checklist item: New page creation has rules for parent section, URL pattern, template, canonical, indexability, sitemap inclusion, and internal links.

### What It Means

Confirm whether the audited scope satisfies this requirement: "New page creation has rules for parent section, URL pattern, template, canonical, indexability, sitemap inclusion, and internal links." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl, Playwright.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl, Playwright

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

## Item 2

Item ID: `site-architecture-seo.25-architecture-governance.0d28200b`

Original checklist item: New categories, tags, filters, and collections require approval or documented criteria before becoming indexable.

### What It Means

Confirm whether the audited scope satisfies this requirement: "New categories, tags, filters, and collections require approval or documented criteria before becoming indexable." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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

Item ID: `site-architecture-seo.25-architecture-governance.91713d91`

Original checklist item: Redirect rules are owned and reviewed before URL changes launch.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Redirect rules are owned and reviewed before URL changes launch." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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

## Item 4

Item ID: `site-architecture-seo.25-architecture-governance.16c8853e`

Original checklist item: Navigation changes have an owner and a before/after validation plan.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Navigation changes have an owner and a before/after validation plan." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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

Item ID: `site-architecture-seo.25-architecture-governance.2556efe7`

Original checklist item: Page deletion has a decision path: update, consolidate, redirect, noindex, 404, or 410.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Page deletion has a decision path: update, consolidate, redirect, noindex, 404, or 410." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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

## Item 6

Item ID: `site-architecture-seo.25-architecture-governance.fc181fe1`

Original checklist item: Architecture changes are tracked with date, owner, rationale, affected URLs, and expected impact.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Architecture changes are tracked with date, owner, rationale, affected URLs, and expected impact." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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

## Item 7

Item ID: `site-architecture-seo.25-architecture-governance.0993509e`

Original checklist item: GSC and GA4 annotations or equivalent release notes are kept for major architecture changes.

### What It Means

Confirm whether the audited scope satisfies this requirement: "GSC and GA4 annotations or equivalent release notes are kept for major architecture changes." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Human/context, GSC, GA4, Firecrawl.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Human/context, GSC, GA4, Firecrawl

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
