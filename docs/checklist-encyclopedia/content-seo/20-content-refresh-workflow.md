---
title: 20. Content Refresh Workflow
sidebar_position: 25
---

# 20. Content Refresh Workflow

Checklist: `content-seo`

Source: `docs/checklists/content-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `content-seo.20-content-refresh-workflow.1f9e7861`

Original checklist item: Pull current queries and top pages from GSC.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Pull current queries and top pages from GSC." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP

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

## Item 2

Item ID: `content-seo.20-content-refresh-workflow.12818461`

Original checklist item: Pull organic landing page engagement and conversions from GA4.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Pull organic landing page engagement and conversions from GA4." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, GA4 or PostHog.
3. Use analytics data only when the property, date range, and conversion definitions are known.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, GA4 or PostHog

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

## Item 3

Item ID: `content-seo.20-content-refresh-workflow.ce390ed8`

Original checklist item: Crawl the page for current title, headings, copy, links, schema, media, and indexability.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Crawl the page for current title, headings, copy, links, schema, media, and indexability." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright

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

Item ID: `content-seo.20-content-refresh-workflow.97cd21ad`

Original checklist item: Compare the page against current SERP intent and result formats.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Compare the page against current SERP intent and result formats." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP

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

## Item 5

Item ID: `content-seo.20-content-refresh-workflow.7e20463f`

Original checklist item: Identify content gaps, factual issues, stale assets, weak links, and conversion gaps.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Identify content gaps, factual issues, stale assets, weak links, and conversion gaps." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright, GA4 or PostHog.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright, GA4 or PostHog

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Rewrite the affected copy or page structure so the primary intent, answer, and next step are clear and evidence-backed.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 6

Item ID: `content-seo.20-content-refresh-workflow.bf2fae36`

Original checklist item: Update only what improves usefulness, trust, or business fit.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Update only what improves usefulness, trust, or business fit." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP

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

Item ID: `content-seo.20-content-refresh-workflow.d803d811`

Original checklist item: Validate rendered content, schema, links, and metadata after publishing.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Validate rendered content, schema, links, and metadata after publishing." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP, Playwright

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

Item ID: `content-seo.20-content-refresh-workflow.cb2fc1eb`

Original checklist item: Monitor GSC and GA4 after the refresh.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Monitor GSC and GA4 after the refresh." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, GA4, Firecrawl, CMS/code, Human/context, Manual/free SERP

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
