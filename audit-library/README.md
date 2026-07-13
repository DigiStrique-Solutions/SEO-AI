# Audit Library

Predefined, reusable SEO audit definitions — the "question papers" every brand is graded against.
Each audit is a pair: a **`.json`** definition (machine-readable checklist) + a **`.md`** (human-readable explainer).

These are **shared across all brands**. A brand's `audits/` folder stores only the *results* of running
these definitions against that brand's site (findings + `summary.json`), referenced by `audit_id`.

## Audits

| # | Audit ID | Title | Scope | Definition |
|---|----------|-------|-------|------------|
| 1 | `generic-on-page` | Generic On-Page SEO | per URL | [json](generic-on-page.json) · [md](generic-on-page.md) |
| 2 | `content-seo` | Content SEO | per URL | [json](content-seo.json) · [md](content-seo.md) |
| 3 | `site-architecture` | Site Architecture & Technical SEO | per site | [json](site-architecture.json) · [md](site-architecture.md) |
| 4 | `core-web-vitals` | Core Web Vitals & Performance | per URL | [json](core-web-vitals.json) · [md](core-web-vitals.md) |
| 5 | `structured-data` | Structured Data & Schema | per URL | [json](structured-data.json) · [md](structured-data.md) |
| 6 | `ai-seo-aeo-geo` | AI SEO / AEO / GEO | per site | [json](ai-seo-aeo-geo.json) · [md](ai-seo-aeo-geo.md) |

## Definition schema (JSON)

```
audit_id        stable id, referenced by brand audit results
title           human name
description      one-line purpose
applies_to      per_url | per_site
scoring         method + severity_weights (high=3, medium=2, low=1)
sections[]      section_id, title, items[]
  items[]       item_id, check, pass_criteria, severity, required_evidence[]
```

## Scoring

Weighted pass ratio per audit: `score = passed_weight / applicable_weight`, where each item contributes
its severity weight. `not_applicable` items are excluded from the denominator.

## Candidate additions (not yet built)

`serp-visibility` · `off-page-seo` · `mobile-ux` · `accessibility` · `indexation-coverage` ·
`local-seo` · `security-trust`
