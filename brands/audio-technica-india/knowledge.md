# Audio-Technica India — working knowledge

## Verified scope

- Primary site: `https://audio-technica.co.in/`.
- Public content shows product/category paths for wireless and wired headphones, microphones, turntables and commercial audio.
- The public site uses INR pricing and India-facing contact details; use India as the provisional market until confirmed.

## Verified data sources (2026-09-07)

- **Google Search Console:** active connection; `https://audio-technica.co.in/` returned `siteOwner` permission and live Search Analytics rows.
- **GA4:** active connection; account **Audio-Technica (India)**, property `properties/496800712`; a standard report returned data. The property timezone is `Asia/Calcutta` and currency is INR.
- **Public crawl:** Firecrawl can render and extract public pages.

## Blocked sources

- **Keyword Planner:** `GOOGLE_ADS_PLATFORM_ID` is not set, so no Keyword Planner request may be made.
- **PageSpeed / CrUX:** `GOOGLE_API_KEY` is not exposed to this runtime; lab and field CWV checks are blocked.
- **Local Lighthouse MCP:** no Lighthouse capability was available in the current tool set.

## Content and measurement rules

- Treat prices, promotion labels and product availability as volatile; refresh the source before publishing.
- Use GA4 and GSC as the preferred evidence sources for performance and search-demand work.
- Do not claim a Core Web Vitals result without separately labelled lab/field evidence.
- The public `/blog/` URL rendered as a page with no post index at the time checked; re-check sitemap/CMS access before treating the site as blog-free.
