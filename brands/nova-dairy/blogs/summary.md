# Nova Dairy — Existing Editorial Coverage

Nova Dairy's current editorial hub is the [Nutrition Centre](https://steragro.com/nutrition-centre/). It links six published recipe pages. The legacy [`/blog/`](https://steragro.com/blog/) route currently returns “No Results Found,” so cached legacy blog URLs were not included as live published posts.

| Title | Date | Category | Primary keyword | Live link | Reference |
|---|---|---|---|---|---|
| Stuffed Paneer Paratha | 2026-02-23 | Recipes | stuffed paneer paratha | [View](https://steragro.com/recipes/stuffed-paneer-paratha/) | [Metadata](references/stuffed-paneer-paratha.md) |
| Pav Bhaji | 2026-02-23 | Recipes | pav bhaji | [View](https://steragro.com/recipes/pav-bhaji/) | [Metadata](references/pav-bhaji.md) |
| Moong Dal Halwa | 2026-02-23 | Recipes | moong dal halwa | [View](https://steragro.com/recipes/moong-dal-halwa/) | [Metadata](references/moong-dal-halwa.md) |
| Overnight Strawberry Oats | 2026-02-23 | Recipes | overnight strawberry oats | [View](https://steragro.com/recipes/overnight-strawberry-oats/) | [Metadata](references/overnight-strawberry-oats.md) |
| Paneer Butter Masala | 2026-02-23 | Recipes | paneer butter masala | [View](https://steragro.com/recipes/paneer-butter-masala/) | [Metadata](references/paneer-butter-masala.md) |
| Gajar Ka Halwa | 2026-02-23 | Recipes | gajar ka halwa | [View](https://steragro.com/recipes/gajar-ka-halwa/) | [Metadata](references/gajar-ka-halwa.md) |

## Coverage notes

- Discovered and fetched: 6 of 6 posts exposed by the live Nutrition Centre and `recipes-sitemap.xml`; below the 20-post cap.
- The site does not expose an on-page category label on these recipe pages. `Recipes` is inferred from the `/recipes/` content type and the Nutrition Centre's “Family-Favourite Recipes” grouping.
- Current coverage clusters around paneer meals (2), ghee-and-milk desserts (2), a butter-led street-food meal (1), and a milk/creamer breakfast (1).
- The retired `/blog/` surface and search-engine-cached legacy posts were excluded because the current blog index returns “No Results Found” and Firecrawl's current site map exposes no legacy `/blog/<slug>` pages.
- Topic-gap comparison against `keywords/clusters.json` was not run because that Phase 2 file was not present at fetch time. Revisit when keyword clusters are available.
- No individual post fetches failed.

## Provenance

- Run ID: `nova-dairy-blogs-20260804`
- Discovery: `../logs/blogs/raw/20260804T074900Z-editorial-url-map.json`
- Batch fetch: `../logs/blogs/raw/20260804T075100Z-recipe-batch-fetch.json`
