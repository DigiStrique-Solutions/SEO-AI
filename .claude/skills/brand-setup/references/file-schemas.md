# File Schemas & Tool Map

Load this when you need the exact shape of an output file or the tool for a capability.
Canonical reference implementation: `brands/sample_brand/`.

## Tool map (capability → actual tool, via Composio)

| Capability | Tool id | Notes |
|-----------|---------|-------|
| public_crawl | `firecrawl` | v1 crawl/render/extract/screenshot |
| rendered_browser | `playwright` | precision / auth / exact DOM (fallback) |
| search_console | `gsc` | performance, indexing, sitemaps, URL inspection |
| keyword_demand | `keyword_planner` | Google Ads demand + variants |
| performance_lab | `lighthouse`, `pagespeed` | lab CWV diagnostics |
| performance_field | `crux` | field CWV (real-user) |
| analytics | `posthog` | brand uses PostHog, **not GA4** |

Do NOT use Firecrawl as a CWV source. Do NOT add paid SERP DBs (DataForSEO/Semrush/Ahrefs/SerpAPI) to v1.

## brand-dna.json (flat; one top-level `updated_at`)
```
schema_version, brand_id, updated_at,
brand_name, website_url, logo{description,icon_url},
business_description, business_model,
brand_colors{...}, brand_aesthetic,
brand_voice{description,voice_patterns[]}, brand_values[],
target_audience{primary[],roles[],secondary_verticals[]},
competitors[]{name,what_it_does,website,how_it_competes},
competitor_alternative_categories[],
primary_business_goal, primary_conversion, site_type,
measurement_and_connected_sources[], open_questions[]
```

## keywords/
- **universe.csv** (12): `keyword,intent,page_type,target_url,volume,difficulty,priority,sources,gsc_clicks,gsc_impressions,gsc_position,status`
- **keywords.csv** (8): `keyword,intent,page_type,target_url,volume,difficulty,priority,status`
- **clusters.json**: `{schema_version,brand_id,updated_at,clusters[]{cluster_id,name,intent,page_type,target_url,pillar,keywords[],notes}}`
- **research-summary.json**: `{schema_version,brand_id,brand_name,website_url,generated_at,target_country,language,date_range,default_source,difficulty_scale,counts{},sources{},gsc_property,gsc_available_properties[],blockers[]}`

## blogs/
- **summary.md**: index table + coverage notes.
- **references/<slug>.md**: frontmatter `title,slug,url,status,published_date,category,primary_keyword,fetched_at` + summary + key points + Notes.

## audits/
- **<audit_id>.json**: `{schema_version,brand_id,audit_id,audit_ref,target_url,run_date,score,counts{items,pass,fail,not_applicable},rows[]{item_id,section_id,status,result,next_action,evidence_ref}}`
- **summary.json**: `{schema_version,brand_id,run_date,target_url,overall_score,totals{},audits[]{audit_id,title,score,items,pass,fail,not_applicable,file},top_fixes[]{audit_id,item_id,severity,action}}`
- **summary.md**: score table + top fixes.

## logs/  → see `05-logs-and-failures.md`.

## brand.json (manifest, Phase 5)
```
schema_version, brand_id, display_name, status, primary_domain, domains[],
locale, market, created_at, updated_at,
pointers{brand_dna,keywords,blogs,audits,logs},
counts{audits,blogs,keywords}
```

## Scoring (audits)
`score = passed_weight / applicable_weight`, weights high=3/medium=2/low=1, `not_applicable` excluded.
