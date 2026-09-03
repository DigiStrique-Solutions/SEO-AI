# Google Ads Keyword Planner MCP

The runtime uses a configured hosted `google-ads` MCP. For SEO work, use exactly one read-only tool: `google_ads_generate_keyword_ideas`. Do not use the other tools that the hosted server may advertise. `tools/google_ads_keyword_planner_mcp.py` remains an optional local fallback for environments without the hosted connection.

## Required setup

1. Create or use a Google Ads **manager account**. In its [API Center](https://ads.google.com/aw/apicenter), obtain a developer token. A developer token is required for every API call; its access level determines whether production accounts can be queried.
2. Create an OAuth 2.0 client in a Google Cloud project, then authorize a Google user who has access to the intended Google Ads account with the `https://www.googleapis.com/auth/adwords` scope. Store the resulting refresh token. The tool refreshes access tokens automatically; do not place an ephemeral access token in configuration.
3. Record the target Google Ads customer ID (10 digits, no hyphens). If the target account is managed through an MCC, also set that manager account ID as `GOOGLE_ADS_LOGIN_CUSTOMER_ID`.
4. Copy `.mcp.google-ads.example.json` into your local Codex MCP configuration and replace the blank values. Keep real values in local configuration or environment variables only; never commit them.
5. Restart/reconnect Codex so it starts the stdio server. The tool will then be available as `google_ads_generate_keyword_ideas`.

## Required variables

| Variable | Required | Purpose |
| --- | --- | --- |
| `GOOGLE_ADS_PLATFORM_ID` | Yes | Strique platform/account-scope identifier. Each call must pass the same value. |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Yes | Google Ads API developer token from the manager account API Center. |
| `GOOGLE_ADS_CLIENT_ID` | Yes | OAuth 2.0 client ID from Google Cloud. |
| `GOOGLE_ADS_CLIENT_SECRET` | Yes | OAuth 2.0 client secret. |
| `GOOGLE_ADS_REFRESH_TOKEN` | Yes | Long-lived OAuth refresh token issued with the Google Ads scope. |
| `GOOGLE_ADS_ACCESS_TOKEN` | Temporary test only | A short-lived bearer token; provide at process launch and never save it to `.env`. It bypasses refresh-token exchange. |
| `GOOGLE_ADS_CUSTOMER_ID` | Yes | Google Ads client account ID used for Keyword Planner. |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Only for MCC | Manager account ID that has access to the client account. |
| `GOOGLE_ADS_API_VERSION` | No | Defaults to `v25`; update it only when Google sunsets the version. |

## Demo request

```json
{
  "platform_id": "your-platform-id",
  "seed_keywords": ["ai marketing"],
  "language_id": "1000",
  "geo_target_ids": [2356],
  "network": "GOOGLE_SEARCH",
  "page_size": 100
}
```

This targets English in India (`2356`). The response includes Google-provided keyword ideas, historical metrics such as average monthly searches and competition, plus any pagination token.

To request a specific historical period, add `year_month_range` with `start` and `end` values. For example, `{"start":{"year":2025,"month":"APRIL"},"end":{"year":2025,"month":"AUGUST"}}` requests the Apr–Aug 2025 series returned by Google Ads.

## References

Google documents the [developer-token requirement](https://developers.google.com/google-ads/api/docs/api-policy/developer-token), [OAuth requirements](https://developers.google.com/google-ads/api/docs/oauth/overview), and [GenerateKeywordIdeas request structure](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas).
