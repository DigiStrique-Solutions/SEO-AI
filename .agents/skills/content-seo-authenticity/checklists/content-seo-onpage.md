# Checklist — Content SEO On-Page

Load this when the task is to assess or improve a page's **on-page content quality** (intent match, depth, structure, links).

## Do NOT duplicate — the scored checklist is shared

The canonical content-SEO checklist lives in the shared audit library:

- Definition: `audit-library/content-seo.json` (`audit_id: content-seo`, `applies_to: per_url`)
- Explainer: `audit-library/content-seo.md`

Run it the way `brand-setup` Phase 4 does (`.claude/skills/brand-setup/references/04-audits.md`) — evaluate the definition, don't re-list items here:

1. Load the definition from `audit-library/content-seo.json`.
2. Evaluate every item → `status` (`pass` | `fail` | `not_applicable`) with a `result` string, `next_action`, and one `evidence_ref`.
3. Write the **result** under `brands/<brand_id>/audits/content-seo.json` — `{schema_version, brand_id, audit_id, target_url, run_date, score, counts, rows[]}`; row = `item_id, section_id, status, result, next_action, evidence_ref`.
4. Score: weighted pass ratio, severity weights high=3 / medium=2 / low=1; `not_applicable` excluded from the denominator.

Its sections/items (purpose-intent, depth-quality, e-e-a-t) are the source of truth. Store only the **result** by `audit_id`, per the audit-library contract — never copy the definition into the brand.

## What this skill adds on top of the audit

The audit scores *whether* the page earns the ranking. When producing or rewriting copy, also return, per target page:

- [ ] **Search intent** — informational / commercial / navigational / transactional / mixed.
- [ ] **Primary keyword** + the closest matching current page (cannibalization check).
- [ ] **Title & meta** recommendation (only if a change is needed).
- [ ] **H1 / H2** fixes (only if needed).
- [ ] **Missing sections / answer gaps** vs. the intent and competitor coverage.
- [ ] **Internal links** to add, remove, or relabel (`>= 2` relevant contextual links).
- [ ] **Structured-data opportunity** (defer schema validity to the `structured-data` audit).
- [ ] **Claims requiring source support** → hand to `authenticity-gate.md` before writing them.

Every content edit that makes a factual claim must pass `authenticity-gate.md`; every rewrite must pass `ai-pattern-review.md`.
