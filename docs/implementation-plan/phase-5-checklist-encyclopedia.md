# Phase 5: Checklist Encyclopedia

## Goal

Break down every checklist item into an explanation that tells a reader what the item means, why it affects SEO, how to verify it, what evidence proves it, who owns the fix, and what to do next.

This is the largest phase.

## Current Inputs

Current checklist scope:

- `docs/checklists/ai-seo-aeo-geo-checklist.md`: 23 sections, 133 items
- `docs/checklists/content-seo-checklist.md`: 26 sections, 173 items
- `docs/checklists/ecommerce-seo-checklist.md`: 23 sections, 169 items
- `docs/checklists/generic-on-page-seo-checklist.md`: 36 sections, 381 items
- `docs/checklists/local-seo-checklist.md`: 25 sections, 196 items
- `docs/checklists/off-page-seo-checklist.md`: 23 sections, 148 items
- `docs/checklists/site-architecture-seo-checklist.md`: 31 sections, 218 items

Total:

- 187 sections
- 1,418 checklist items

## Assumptions

- The original checklist Markdown remains the source of truth.
- Item IDs should follow the harness stable ID behavior.
- The encyclopedia can be generated in a first pass, then edited.
- Not every item needs a long essay. Most need a practical, repeatable explanation.
- The docs should explain SEO effects without inventing ranking guarantees.

## Recommended Entry Template

Each checklist item gets this shape:

```md
## <Item Title>

Checklist: <checklist name>
Section: <section name>
Item: <original checklist item text>

### What It Means
Plain-language explanation of the check.

### Why It Affects SEO
How it can affect crawling, indexing, relevance, snippets, AI visibility, user trust, conversion, local visibility, product eligibility, or measurement.

### How To Verify
Specific checks to run manually or with the harness.

### Evidence Sources
Expected evidence, such as Firecrawl, Playwright, GSC, GA4, GBP, GMC, Shopify, Lighthouse, PageSpeed, CrUX, logs, CMS/code, manual SERP, or human context.

### Pass Criteria
What a verified pass looks like.

### Fail Criteria
What a verified fail looks like.

### Common Fix
The smallest concrete fix direction.

### Owner
Content, engineering, marketing, analytics, admin, merchandising, local ops, or legal/compliance.

### Notes
Assumptions, edge cases, and blocked-state guidance.
```

## Implementation Steps

1. Decide file layout.
   - Keep original checklists in `docs/checklists/`.
   - Add expanded docs under `docs/checklist-encyclopedia/`.
   - Use one folder per checklist:
     - `ai-seo-aeo-geo/`
     - `content-seo/`
     - `ecommerce-seo/`
     - `generic-on-page-seo/`
     - `local-seo/`
     - `off-page-seo/`
     - `site-architecture-seo/`

2. Generate a first pass from checklist Markdown.
   - Parse headings and `- [ ]` rows.
   - Preserve source checklist name, section name, and item text.
   - Create stable slugs from item text and section.
   - Include the template sections with practical initial copy.
   - Add a review marker for generated entries.
   - Use the harness parser if possible instead of writing a second parser.

3. Create checklist overview pages.
   - For each checklist, document:
     - purpose
     - best-fit use cases
     - evidence source legend
     - severity model
     - section map
     - blocked-source guidance
   - Link every section to its expanded item entries.

4. Prioritize manual review order.
   - First pass:
     - generic on-page SEO
     - content SEO
     - site architecture
   - Second pass:
     - ecommerce SEO
     - AI SEO, AEO, and GEO
   - Third pass:
     - local SEO
     - off-page SEO
   - Reason: the first pass covers the most common audits and the biggest checklist by item count.

5. Expand item explanations.
   - Keep each entry actionable.
   - Avoid generic SEO advice.
   - Include concrete verification paths.
   - Include blocked-state language where external access is required.
   - Include owner and likely fix direction.
   - Label assumptions when evidence requirements vary by platform.

6. Add cross-links.
   - Link items to harness command docs.
   - Link items to evidence source docs.
   - Link items to relevant workflow docs.
   - Link content authenticity items to the local skill docs.
   - Link ecommerce items to product feed, schema, and merchant evidence docs.

7. Add coverage tracking.
   - Track generated, reviewed, and blocked states per item.
   - A lightweight CSV or JSON manifest is enough.
   - Fields:
     - checklist
     - section
     - item_id
     - item_text
     - doc_path
     - status
     - reviewer
     - notes
   - Avoid adding a database.

8. Add validation.
   - Count checklist source items.
   - Count encyclopedia entries.
   - Fail if source item count and doc entry count differ.
   - Fail if any generated entry is missing required headings.
   - Keep the validation as a small script only if manual review becomes unreliable.

## Deliverables

- `docs/checklist-encyclopedia/` folder.
- One overview page per checklist.
- Expanded item pages or section pages covering all 1,418 checklist items.
- Coverage manifest.
- Validation command or documented manual verification.
- Sidebar entries for checklist encyclopedia docs.

## Verification

Run:

```bash
for f in docs/checklists/*.md; do
  printf '%s sections=' "$f"
  rg -c '^## ' "$f"
  printf '%s items=' "$f"
  rg -c '^- \[ \]' "$f"
done
npm run docs:build
```

When validation exists, also run it.

Exit criteria:

- Every source checklist item has an encyclopedia entry.
- Every entry includes what it means, why it affects SEO, how to verify, evidence sources, pass criteria, fail criteria, common fix, and owner.
- Generated entries are clearly marked until reviewed.
- Docusaurus build succeeds.

## Risks

- 1,418 entries can create repetitive docs if the first pass is not reviewed.
- Some items require connector access, so docs must explain blocked-state handling.
- SEO impact explanations can drift into ranking guarantees if not worded carefully.
- One page per item may create too many files. Section-level pages with anchors may be easier to maintain.

## Deferred

- Fully custom checklist UI.
- Search filters by evidence source, owner, and severity.
- Auto-sync from checklist Markdown on every build.
- External citation refresh for every research link.
