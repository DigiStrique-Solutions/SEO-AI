# Structured Data & Schema — Audit Definition

**ID:** `structured-data` · **Scope:** per URL · **Pairs with:** [structured-data.json](structured-data.json)

## What it checks
Schema.org coverage and validity.

| Section | Items |
|---------|-------|
| Coverage | Organization + WebSite schema · BreadcrumbList · correct content type (Article/Product/FAQ) |
| Validity & Eligibility | No validation errors · eligible for rich results |

## Why it matters
Structured data does double duty in 2026: it powers **rich results** in Google *and* gives **AI answer engines** clean, machine-readable facts to cite. Weak schema hurts both classic SEO and AEO/GEO.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**.

## Output
- `audits/structured-data.json` — findings rows with detected types.
- Rolled into `audits/summary.json`.

## Related
Feeds the `ai-seo-aeo-geo` audit — clean entity schema improves `entity-clarity` there.
