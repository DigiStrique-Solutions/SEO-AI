# Phase 1 — Crawl & Brand DNA

**Goal:** Crawl the brand's site and produce `brand-dna.json` + `knowledge.md`.
**Tools:** `firecrawl` (primary), `playwright` (fallback for JS-heavy/auth pages).
**Depends on:** Phase 0 skeleton exists.

## Steps

1. **Crawl the key pages.** With Firecrawl, fetch: `/`, `/product`, `/about`, `/pricing`, `/solutions`, `/customers`, `/integrations`, `/security`, `/contact`, plus any linked nav pages (depth 1, render on).
2. **Log the crawl** → `logs/web_data/activity.jsonl` (action `crawl`) + raw payload in `logs/web_data/raw/<ts>-brand-dna-crawl.json`.
3. **Extract each field** below from the crawl. Write descriptions in the brand's own language; never invent facts — if unknown, put the field in `open_questions` instead.
4. **Write `brand-dna.json`** (flat top-level fields, one `updated_at`, `schema_version`). Schema → `file-schemas.md`.
5. **Write `knowledge.md`** — free-form living memory seeded from the crawl (positioning, messaging do/don't, measurement/tooling notes, proof, key pages, open questions).

## Checklist items (write to tasks checklist)

| id | check | severity | fail action |
|----|-------|:--------:|-------------|
| `p1.crawl-ok` | Site crawl returned ≥ 1 page, HTTP 200 | high | BLOCK — cannot proceed without site content |
| `p1.brand-name` | `brand_name` + `website_url` resolved | high | BLOCK |
| `p1.core-fields` | business_description, business_model, target_audience, brand_voice filled | medium | continue; unknowns → open_questions |
| `p1.competitors` | ≥ 2 competitors with name/what/website/how | medium | continue; note gap in open_questions |
| `p1.dna-valid` | `brand-dna.json` parses and matches schema | high | BLOCK — fix before Phase 2 |
| `p1.knowledge` | `knowledge.md` written with seeded sections | low | continue |

## Fields to capture (brand-dna.json)

`brand_name, website_url, logo, business_description, business_model, brand_colors, brand_aesthetic, brand_voice (+voice_patterns), brand_values, target_audience (primary/roles/secondary_verticals), competitors[] (name, what_it_does, website, how_it_competes), competitor_alternative_categories, primary_business_goal, primary_conversion, site_type, measurement_and_connected_sources, open_questions`

## Failure handling

- If Firecrawl fails or returns thin content → retry once with `playwright`. If still empty, mark `p1.crawl-ok` failed, log `status:error`, and STOP (hard dependency). Report to user.
- Missing individual fields are NOT failures — route them to `open_questions` and continue.

**Next:** Phase 2 → `references/02-keyword-research.md`.
