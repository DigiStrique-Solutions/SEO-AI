# Phase 3: Harness Documentation

## Goal

Document the SEO audit harness end to end: what each command does, what files it reads and writes, what evidence it expects, and how it prevents false full-audit claims.

This phase turns `tools/seo_audit_harness.py` and its tests into usable operator documentation.

## Current Inputs

Harness file:

- `tools/seo_audit_harness.py`

Test file:

- `tests/test_seo_audit_harness.py`

Existing workflow doc:

- `docs/workflows/seo-audit-harness.md`

Verified command surface:

- `compile-checklists`
- `init-audit`
- `verify-audit`
- `summarize-audit`
- `init-authenticity`
- `verify-authenticity`
- `write-content`
- `firecrawl-scrape`
- `generate-keywords`
- `verify-keywords`
- `collect-evidence`
- `crawl-site`
- `collect-site-evidence`
- `run-site-checks`
- `resolve-google-visible-audit`
- `resolve-google-visible-audits`
- `route-evidence`
- `record-source-evidence`
- `record-evidence`

## Assumptions

- The CLI is the source of truth for local docs.
- Tests are evidence for expected behavior.
- Documentation should avoid promising production Strique runtime behavior until that runtime exists in this repo.
- Environment variables such as `FIRECRAWL_API_KEY` and `GOOGLE_API_KEY` can be named, but values must never be printed or committed.

## Implementation Steps

1. Create a harness overview.
   - Explain why the harness exists.
   - Explain full checklist audit mode.
   - Explain content authenticity mode.
   - Explain keyword and evidence collection flows.
   - Show the relationship between checklists, compiled JSON, audit matrix, evidence artifacts, summaries, and tasks.

2. Create a command reference.
   - One section per command.
   - For each command document:
     - purpose
     - required arguments
     - optional arguments
     - input files
     - output files
     - common examples
     - failure modes
     - when to use it
   - Pull flags from `python3 tools/seo_audit_harness.py <command> --help`, not from memory.

3. Document audit matrix lifecycle.
   - Compile checklist Markdown.
   - Initialize audit matrix.
   - Fill rows.
   - Record evidence.
   - Verify matrix.
   - Summarize only after verification.
   - Explain status values:
     - `pass`
     - `fail`
     - `not_applicable`
     - `not_checked_blocked`
   - Make the rule explicit: a full audit cannot have blocked rows.

4. Document content authenticity lifecycle.
   - Initialize source log.
   - Add concrete sources.
   - Add claim rows for sensitive claims.
   - Verify authenticity.
   - Use `write-content` only when the gate passes.
   - Explain AI detector notes as weak editorial signals, not proof.

5. Document evidence collection.
   - Explain public HTTP checks.
   - Explain Firecrawl scrape artifacts.
   - Explain Playwright artifacts.
   - Explain Lighthouse, PageSpeed, and CrUX artifacts.
   - Explain GSC, Keyword Planner, GA4, PostHog, Shopify, and manual evidence as source categories.
   - Mark unavailable connectors as blocked, not failed.

6. Document keyword workflow.
   - Explain `keywords/keywords.csv`.
   - Explain keyword universe exports.
   - Explain demand sources, GSC joins, priorities, and status fields.
   - Explain `generate-keywords` and `verify-keywords`.

7. Document brand workspace paths used by the harness.
   - `brand-dna.md`
   - `keywords/keywords.csv`
   - `audits/audits.csv`
   - `tasks/tasks.csv`
   - `references/`
   - `exports/`
   - `references/evidence/<run-id>/`
   - `references/crawls/<run-id>/`

8. Add examples.
   - Use `brands/_template/` or sanitized examples.
   - Avoid hardcoding real private customer evidence.
   - Prefer command snippets that can be pasted into a local terminal.

9. Link tests to behavior.
   - Cite test coverage for stable item IDs.
   - Cite validation tests for missing rows, pass without evidence, blocked rows, and full audit blocked-row failures.
   - Do not turn tests into user docs, but use them to know what claims are safe.

## Deliverables

- Harness overview page.
- Harness command reference page.
- Audit matrix lifecycle page.
- Content authenticity lifecycle page.
- Evidence collection page.
- Keyword workflow page.
- Brand workspace path reference.

## Verification

Run:

```bash
python3 tools/seo_audit_harness.py --help
python3 tools/seo_audit_harness.py compile-checklists --help
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
```

Exit criteria:

- Every current harness command is documented.
- Every command example uses real flags.
- Full audit gating is explained clearly.
- Content authenticity gating is explained clearly.
- Docusaurus build succeeds.

## Risks

- The harness is a single large Python file, so docs can drift if commands change.
- Some commands depend on optional external APIs or browser tooling.
- It is easy to over-document internals that an operator does not need.

## Deferred

- Auto-generated command docs from argparse.
- Runtime tool wrappers for production Strique.
- Rich screenshots of evidence artifacts.
