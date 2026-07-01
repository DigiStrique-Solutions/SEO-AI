---
title: 15. Template-Level Architecture
sidebar_position: 19
---

# 15. Template-Level Architecture

Checklist: `site-architecture-seo`

Source: `docs/checklists/site-architecture-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `site-architecture-seo.15-template-level-architecture.594b8778`

Original checklist item: Every page template supports unique title, meta description, H1, intro, canonical, schema, and internal-link modules.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Every page template supports unique title, meta description, H1, intro, canonical, schema, and internal-link modules." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

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

Item ID: `site-architecture-seo.15-template-level-architecture.0804ef52`

Original checklist item: Template defaults do not create duplicate titles or boilerplate copy across many URLs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Template defaults do not create duplicate titles or boilerplate copy across many URLs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

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

Item ID: `site-architecture-seo.15-template-level-architecture.533f398b`

Original checklist item: Templates expose crawlable links to related pages, parent hubs, and conversion paths.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Templates expose crawlable links to related pages, parent hubs, and conversion paths." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4, GA4 or PostHog.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4, GA4 or PostHog

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have analytics make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 4

Item ID: `site-architecture-seo.15-template-level-architecture.e5ecddac`

Original checklist item: Templates support breadcrumbs where hierarchy exists.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Templates support breadcrumbs where hierarchy exists." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

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

## Item 5

Item ID: `site-architecture-seo.15-template-level-architecture.48befe82`

Original checklist item: Templates do not hide main content or links behind client-only rendering.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Templates do not hide main content or links behind client-only rendering." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Rewrite the affected copy or page structure so the primary intent, answer, and next step are clear and evidence-backed.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 6

Item ID: `site-architecture-seo.15-template-level-architecture.ffd9f0c4`

Original checklist item: Templates handle empty states, out-of-stock states, removed content, and unpublished content correctly.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Templates handle empty states, out-of-stock states, removed content, and unpublished content correctly." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Rewrite the affected copy or page structure so the primary intent, answer, and next step are clear and evidence-backed.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 7

Item ID: `site-architecture-seo.15-template-level-architecture.55b276a4`

Original checklist item: Templates prevent indexable thin pages from being generated by default.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Templates prevent indexable thin pages from being generated by default." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Firecrawl, Playwright, GSC, GA4.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Firecrawl, Playwright, GSC, GA4

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
