# Phase 2: Source Inventory

## Goal

Document what exists in the repo so the Docusaurus site describes real assets instead of imaginary runtime pieces.

This phase creates the map. It does not deeply explain every command or checklist item yet.

## Current Inputs

Verified source areas:

- `AGENTS.md`
- `tools/seo_audit_harness.py`
- `tests/test_seo_audit_harness.py`
- `docs/workflows/`
- `docs/checklists/`
- `docs/schemas/`
- `docs/mcp-requirements-generic-on-page-seo.md`
- `.agents/skills/content-seo-authenticity/SKILL.md`
- `brands/` workspaces, exports, references, crawls, and evidence artifacts

Checklist scale:

- `ai-seo-aeo-geo-checklist.md`: 23 sections, 133 items
- `content-seo-checklist.md`: 26 sections, 173 items
- `ecommerce-seo-checklist.md`: 23 sections, 169 items
- `generic-on-page-seo-checklist.md`: 36 sections, 381 items
- `local-seo-checklist.md`: 25 sections, 196 items
- `off-page-seo-checklist.md`: 23 sections, 148 items
- `site-architecture-seo-checklist.md`: 31 sections, 218 items
- Total: 187 sections, 1,418 checklist items

## Assumptions

- Inventory pages should distinguish implemented files from planned runtime contracts.
- Brand workspaces should be documented as examples and data structures, not fully published evidence archives.
- Any generated inventory should be reviewable Markdown, not hidden magic.

## Implementation Steps

1. Create the docs taxonomy.
   - Define where each existing source type belongs in Docusaurus.
   - Proposed groups:
     - `docs/start/`
     - `docs/harness/`
     - `docs/workflows/`
     - `docs/checklists/`
     - `docs/checklist-encyclopedia/`
     - `docs/agents/`
     - `docs/skills/`
     - `docs/tools-and-connectors/`
     - `docs/schemas/`
     - `docs/brand-workspaces/`
     - `docs/implementation-plan/`

2. Create a repository map.
   - Explain each top-level directory.
   - Mark whether each directory is source, docs, brand evidence, test coverage, or generated output.
   - Call out that `brands/` can contain customer or brand-specific artifacts and should not be blindly published.

3. Create a source inventory page.
   - List current workflow docs.
   - List current checklist docs.
   - List current schema files.
   - List the local skill.
   - List the harness and tests.
   - List brand workspace types without exposing every artifact path.

4. Create an implementation status page.
   - Separate these buckets:
     - Built now
     - Documented contract
     - Planned runtime integration
     - External connector category
     - Brand evidence artifact
   - Example: `tools/seo_audit_harness.py` is built now.
   - Example: `orchestrator -> run_sub_agent(...) -> seo_agent` is documented contract.
   - Example: GSC, GA4, Shopify, HubSpot, Firecrawl, and GBP are connector categories unless concrete callable wrappers exist in this repo.

5. Create a privacy and publishability classification.
   - Public-safe docs:
     - generic workflows
     - checklists
     - schema descriptions
     - harness command reference
   - Internal-only docs:
     - agent prompt contracts
     - connector policy details
     - brand workspace operating procedures
   - Restricted artifacts:
     - raw evidence payloads
     - crawl screenshots
     - customer notes
     - raw connector responses
     - credentials or tokens

6. Add source-of-truth references.
   - Every inventory entry should point to the file or folder that proves it exists.
   - Use relative repo paths in docs.
   - If an item is planned, label it as planned and link to the contract section.

## Deliverables

- Repository map page.
- Source inventory page.
- Implementation status page.
- Publishability classification page.
- Sidebar entries for the inventory pages.

## Verification

Run:

```bash
rg --files
rg --files docs .agents tools tests
npm run docs:build
```

Exit criteria:

- Every current source category is represented.
- Planned items are not described as implemented.
- Restricted artifacts are not linked from public navigation.
- Docusaurus build succeeds.

## Risks

- The repo has many brand evidence files, so a naive inventory can become noisy.
- Connectors can be over-described if the docs do not distinguish categories from concrete implementations.
- A future reader may confuse local harness behavior with Strique production runtime behavior unless the status page is explicit.

## Deferred

- Auto-generated inventory script.
- Full artifact catalog for every brand evidence file.
- Runtime architecture diagrams beyond the basic source map.
