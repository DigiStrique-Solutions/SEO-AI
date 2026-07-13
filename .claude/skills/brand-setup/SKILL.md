---
name: brand-setup
description: Use when onboarding or building a brand's SEO workspace — crawling the site to extract brand DNA, researching keywords, fetching existing blogs, running SEO audits, and assembling the brands/<brand_id>/ folder (brand-dna.json, knowledge.md, keywords/, blogs/, audits/, logs/). Trigger on "add a brand", "set up / onboard a brand", "create brand info", "build the brand workspace", or "run brand setup". Mirrors the structure of brands/sample_brand.
---

# Brand Setup

Build a complete, provenance-tracked SEO workspace for one brand, phase by phase, exactly like `brands/sample_brand/`.

## Golden rules

1. **Respect the dependency graph — parallelize the rest.** Only Phase 1 is foundational. After it, independent branches fan out to parallel subagents (see Execution Model). Don't serialize work that has no dependency.
2. **Progressive disclosure — do NOT read every reference up front.** Read only the phase reference you (or a subagent) are about to execute. Each phase names the one file to load — which makes each phase a clean, self-contained subagent task.
3. **Log everything.** Every fetch/pull/run gets an event in `brands/<brand_id>/logs/<category>/activity.jsonl` plus its raw payload in `raw/`. See `references/05-logs-and-failures.md`.
4. **The orchestrator owns the checklist.** `brands/<brand_id>/tasks/brand-setup.checklist.json` is written only by the orchestrator, which merges the structured status each subagent returns. Subagents never write it (avoids concurrent-write races).
5. **On any failure, follow the failure protocol** in `references/05-logs-and-failures.md` — never silently skip a check.

## Inputs required

- `brand_id` (kebab-case folder name, e.g. `acme-co`)
- `website_url` (e.g. `https://www.acme.com`)
- Optional: `target_country` (default `United States`), primary seed keywords.

## Tools available (via Composio)

`firecrawl` (public crawl/render) · `playwright` (precision browser) · `gsc` (Search Console) ·
`keyword_planner` (Google Ads) · `lighthouse` + `pagespeed` (lab CWV) · `crux` (field CWV) · `posthog` (analytics).
Full mapping: `references/file-schemas.md`.

## Phases (the task checklist)

> At each phase, first read its reference file, then execute, then tick the checklist and write logs.

- [ ] **Phase 0 — Init.** Create `brands/<brand_id>/` skeleton + `tasks/brand-setup.checklist.json` + empty `logs/` categories. (See `references/05-logs-and-failures.md` for the checklist file shape.)
- [ ] **Phase 1 — Crawl & Brand DNA.** → read `references/01-crawl-brand-dna.md`. Crawl the site → write `brand-dna.json` + `knowledge.md`.
- [ ] **Phase 2 — Keyword Research.** → read `references/02-keyword-research.md`. Pull demand + GSC → write `keywords/` (universe.csv, keywords.csv, clusters.json, research-summary.json).
- [ ] **Phase 3 — Existing Blogs.** → read `references/03-blogs.md`. Discover + fetch up to 20 posts → write `blogs/summary.md` + `blogs/references/`.
- [ ] **Phase 4 — SEO Audits.** → read `references/04-audits.md`. Run the `audit-library/` audits → write `audits/*.json` + `summary.json` + `summary.md`.
- [ ] **Phase 5 — Finalize.** Verify all files valid, checklist complete, failures triaged. Write the top-level `brand.json` manifest.

## Output layout (target)

```
brands/<brand_id>/
├── brand.json                 # manifest (Phase 5)
├── brand-dna.json             # Phase 1
├── knowledge.md               # Phase 1
├── keywords/                  # Phase 2
├── blogs/                     # Phase 3
├── audits/                    # Phase 4
├── logs/                      # all phases (provenance)
└── tasks/brand-setup.checklist.json
```

## Definition of done

All phases `done`; every output file schema-valid; `audits/summary.json` present; any `failed` checklist item has a logged reason and a `next_action`. Then report the summary to the user (overall audit score + any blockers).
