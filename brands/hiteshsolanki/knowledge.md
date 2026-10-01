# Hitesh Solanki — brand knowledge

This is a crawl-only workspace, seeded from the live public site on 2026-10-01. Do not infer analytics, target geography, competitors, or conversion results. Provenance run: `hiteshsolanki-crawl-20261001` in [web data activity](logs/web_data/activity.jsonl).

## Site and positioning

- Personal portfolio for Hitesh Solanki, a software engineer and AI builder. The site features projects, professional experience, technical writing, and a resume. Source: `logs/web_data/raw/2026-10-01T13-15-08-555Z-crawl.json`.
- The [contact page](https://hiteshsolanki.com/contact) invites discussions about roles, freelance work, and collaboration. Source: `logs/web_data/raw/2026-10-01T13-15-08-555Z-sample-0.json`.
- The [blogs page](https://hiteshsolanki.com/blogs) links to four Medium articles; the crawl found no on-domain blog article page among the 20 fetched pages. Source: `logs/web_data/raw/2026-10-01T13-15-08-555Z-crawl.json`.

## Crawl carry-outs

- The 20-page crawl reached its configured limit: 19 HTML pages and one resume PDF, all HTTP 200. It is not full coverage of the 50 sitemap entries. Source: `logs/web_data/raw/2026-10-01T13-15-08-555Z-crawl.json`.
- All 19 crawled HTML pages expose Open Graph URL and image metadata on `master.d2p4p6tfmpfvri.amplifyapp.com`. Source: `logs/web_data/raw/2026-10-01T13-15-08-555Z-crawl.json`.
- `robots.txt` points its Host and Sitemap directives at that staging host; all 50 sitemap `<loc>` entries also use it. Sources: `logs/web_data/raw/2026-10-01T13-15-08-555Z-robots.json`, `logs/web_data/raw/2026-10-01T13-15-08-555Z-sitemap.json`.
- Three production-equivalent sitemap paths outside the crawl were spot checked and returned HTTP 200: `/contact`, `/projects/relivo`, and `/projects/ai-story-planner`. This does not verify the remaining paths. Sources: `logs/web_data/raw/2026-10-01T13-15-08-555Z-sample-0.json`, `-sample-1.json`, `-sample-2.json`.
- Browser navigation and local direct HTTP access timed out. Canonicals, structured data, mobile rendering, accessibility, and live search indexing were not verified. Sources: `logs/web_data/raw/2026-10-01T13-15-08-555Z-playwright-error.json`, `-curl-error.json`.

## Voice and evidence rules

Use first-person, direct, technical language only when writing as the portfolio owner. Ground claims in the site or user-provided materials. Do not treat project descriptions as independently verified product performance.
