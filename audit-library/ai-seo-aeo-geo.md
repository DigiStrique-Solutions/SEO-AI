# AI SEO / AEO / GEO — Audit Definition

**ID:** `ai-seo-aeo-geo` · **Scope:** per site · **Pairs with:** [ai-seo-aeo-geo.json](ai-seo-aeo-geo.json)

## What it checks
How well AI answer engines (ChatGPT, Perplexity, Google AI Overviews) understand and cite the brand.

| Section | Items |
|---------|-------|
| Answer-ability | Direct, concise answers · AI-friendly structures (FAQs, definitions, lists, tables) |
| Entity & Authority | Consistent entity definition · credible citations (given and earned) |
| AI Visibility | AI crawler access + llms.txt · brand mentioned in AI answers for target queries |

## Why it matters
Search is shifting from "ten blue links" to synthesized answers. If AI engines can't cleanly extract and attribute your content, you lose visibility even when you rank in classic search. **AEO** = answer engine optimization; **GEO** = generative engine optimization.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**.

## Output
- `audits/ai-seo-aeo-geo.json` — findings rows.
- Rolled into `audits/summary.json`.

## Needs
`ai-mentions` requires manual/LLM checks against priority prompts; those rows are `blocked` until that evidence is supplied.
