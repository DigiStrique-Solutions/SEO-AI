# Phase 2 — Keyword Research

**Goal:** Build the `keywords/` folder: `universe.csv`, `keywords.csv`, `clusters.json`, `research-summary.json`.
**Tools:** `keyword_planner` (Google Ads demand), `gsc` (real query/impression data).
**Depends on:** `brand-dna.json` (uses business_description, target_audience, competitors as seeds).

## Steps

1. **Seed** from brand-dna: product terms, category terms, competitor-alternative terms.
2. **Pull demand** via `google_ads_generate_keyword_ideas` only (geo = target_country). Pass `platform_id` from `GOOGLE_ADS_PLATFORM_ID`; never use other Google Ads MCP tools. Capture keyword text, average monthly searches, competition/index, bid estimates, targeting, and any pagination token. **Log** → `logs/keywords/activity.jsonl` (`api_call`) + raw in `raw/`, excluding credentials.
3. **Pull GSC** query/page performance for the property (if connected). Log it (may be `partial` if the property has little data).
4. **Build `universe.csv`** — raw superset, 12 cols: `keyword,intent,page_type,target_url,volume,difficulty,priority,sources,gsc_clicks,gsc_impressions,gsc_position,status`. `difficulty` = numeric 0-100 (not "MEDIUM 65").
5. **Build `keywords.csv`** — curated/prioritized working set, 8 cols: `keyword,intent,page_type,target_url,volume,difficulty,priority,status`.
6. **Build `clusters.json`** — topic clusters → member keywords + target page (`pillar` flag; `target_url: null` when each keyword maps to its own page, e.g. competitor comparisons).
7. **Build `research-summary.json`** — counts, date_range, sources, gsc_property, `default_source`, `difficulty_scale`.

## Optimization rules (do not bloat the CSVs)

- **No derived columns** (e.g. `gsc_ctr` = clicks/impressions — compute on read).
- **No constant columns** — put run-wide constants (source, country) in `research-summary.json`.
- **No restating** volume/difficulty in a `notes` column.

## Checklist items

| id | check | severity | fail action |
|----|-------|:--------:|-------------|
| `p2.demand-pull` | Keyword Planner returned ≥ 1 row | high | continue with GSC/seeds only; log error; note in summary.blockers |
| `p2.universe` | `universe.csv` written, header valid, ≥ 1 row | high | BLOCK Phase 4 content-seo intent checks |
| `p2.keywords` | `keywords.csv` curated subset written | medium | continue |
| `p2.clusters` | `clusters.json` ≥ 1 cluster, valid JSON | medium | continue; audits still run |
| `p2.gsc` | GSC pull attempted | low | if not connected, set gsc_* blank, note in summary |
| `p2.summary` | `research-summary.json` valid, counts match files | medium | fix counts |

## Failure handling

- Keyword Planner unavailable → fall back to GSC queries + brand-dna seeds; set `summary.blockers += ["keyword_planner_unavailable"]`; continue (soft fail).
- GSC not connected → leave `gsc_*` columns blank, record in `research-summary.json.blockers`; continue.

**Next:** Phase 3 → `references/03-blogs.md`.
