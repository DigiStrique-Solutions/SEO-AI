---
name: google-ads-keyword-planner
description: Research keyword ideas and directional search demand with the configured Google Ads Keyword Planner MCP. Use for keyword volumes, variants, or planning; never use for campaign management or GAQL.
---

# Google Ads Keyword Planner

Use the configured hosted `google-ads` MCP only through `google_ads_generate_keyword_ideas`.

- Read `GOOGLE_ADS_PLATFORM_ID` from the environment and pass it as `platform_id`; never hardcode or log it.
- Provide seed keywords, a seed URL, or a site seed. Select the language, geographic target constants, and Google Search network from the brand’s market. For India/English research, use `languageConstants/1000`, `geoTargetConstants/2356`, and `GOOGLE_SEARCH`.
- Record the request targeting and returned ideas, volume, competition/index, bid estimates, and pagination state in the brand’s keyword provenance log. Do not record credentials, headers, connection URLs, or tokens.
- Treat volume and bid metrics as directional Keyword Planner data, not a guarantee of traffic or commercial performance.
- Stop after the keyword-ideas call. Do not call GAQL, account-reporting, campaign, asset, recommendation, or write tools exposed by the same MCP.
