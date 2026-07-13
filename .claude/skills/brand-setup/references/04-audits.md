# Phase 4 — SEO Audits

**Goal:** Run the predefined audits against the brand and write `audits/*.json` + `summary.json` + `summary.md`.
**Definitions:** `audit-library/` (shared "question papers", referenced by `audit_id` — do NOT copy them into the brand).
**Tools per audit:** crawl (`firecrawl`/`playwright`), `gsc`, `crux`+`pagespeed`+`lighthouse` (CWV), `posthog`.
**Depends on:** Phase 1 (site), Phase 2 (keywords for content-seo intent).

## Default audit set (6)

`generic-on-page` · `content-seo` · `site-architecture` · `core-web-vitals` · `structured-data` · `ai-seo-aeo-geo`
(Optional adds listed in `audit-library/README.md`.)

## Steps

1. **Gather evidence once** — full site crawl + GSC + CWV pull. **Log** each to its `logs/<category>/` and reference those raw files as the audit's `evidence_inputs`. Log the audit run itself → `logs/audits/activity.jsonl` (`audit_run`) + raw site-checks in `raw/`.
2. **For each audit_id**, load its definition from `audit-library/<id>.json`. Evaluate every item → `status` (`pass`|`fail`|`not_applicable`) with a `result` string, `next_action`, and one `evidence_ref`.
3. **Write `audits/<id>.json`** — `{schema_version, brand_id, audit_id, audit_ref, target_url, run_date, score, counts, rows[]}`. Row = `item_id, section_id, status, result, next_action, evidence_ref`.
4. **Score** each audit: weighted pass ratio, severity weights high=3/medium=2/low=1; `not_applicable` excluded from the denominator.
5. **Write `summary.json`** — overall_score (avg of audit scores), totals, per-audit rows, and `top_fixes[]` (ranked high→low severity).
6. **Write `summary.md`** — human report: score table + top fixes with impact.

## Evidence gating

If a required provider for an item is not connected, set that item `status: not_applicable` (or `blocked`), put the reason in `result`, and add a `next_action`. Do NOT mark it `pass`. Example: CWV items are n/a until CrUX/PageSpeed is connected.

## Checklist items

| id | check | severity | fail action |
|----|-------|:--------:|-------------|
| `p4.evidence` | Site crawl evidence gathered | high | BLOCK — audits need crawl data |
| `p4.per-audit` | Each of the 6 audits produced a valid findings file | high | log which audit failed; still write summary for the rest |
| `p4.counts` | Each file's `counts` == its row status tallies | medium | recompute before summary |
| `p4.summary` | `summary.json` totals == sum of files; score == avg | high | fix before reporting |
| `p4.summary-md` | `summary.md` written with top_fixes | low | continue |

## Failure handling

- A whole audit errors → mark `p4.per-audit` partial, log it, exclude it from `summary.json`, note it in `summary.md` (don't fake a score).
- Provider missing → items become `not_applicable`, not `fail`. Record needed connections in `top_fixes`/summary so the user can wire them.

**Next:** Phase 5 (finalize) — verify all, write `brand.json`, report to user.
