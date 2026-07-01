# SEO Audit Harness Workflow

Use this workflow when a user asks for every checklist, full verification, or publish-ready content rewriting.

## Full Checklist Audits

1. Compile the selected Markdown checklists:

```bash
python3 tools/seo_audit_harness.py compile-checklists --output brands/inc5/exports/checklists.json
```

2. Create the audit matrix:

```bash
python3 tools/seo_audit_harness.py init-audit --compiled brands/inc5/exports/checklists.json --url https://example.com/page --audit-type partial --output brands/inc5/audits/page-audit-matrix.json
```

3. Fill every row in the matrix.

Use these statuses only:

- `pass`: verified with evidence.
- `fail`: verified issue with evidence and next action.
- `not_applicable`: not relevant, with a short reason in `result`.
- `not_checked_blocked`: could not be checked, with `blocker` and `next_action`.

4. Verify before summarizing:

```bash
python3 tools/seo_audit_harness.py verify-audit --compiled brands/inc5/exports/checklists.json --audit brands/inc5/audits/page-audit-matrix.json
```

Only call the result a full audit when verification passes and there are zero `not_checked_blocked` rows.

## Content Authenticity

1. Create a source log:

```bash
python3 tools/seo_audit_harness.py init-authenticity --target brands/inc5/blogs/drafts/example.md --output brands/inc5/references/example-authenticity.json
```

2. Add concrete sources such as product pages, brand DNA, GSC, GA4, Shopify data, reviews, customer notes, merchandiser notes, SERP observations, or human context.

3. Add claim rows for unsupported-sensitive language such as `best` or `top`.

4. Verify before calling a rewrite publish-ready:

```bash
python3 tools/seo_audit_harness.py verify-authenticity --authenticity brands/inc5/references/example-authenticity.json --rewrite-file brands/inc5/blogs/drafts/example.md
```

When a rewrite file is supplied, the harness also computes local `ai_text_risk`. Scores at or above `20` fail the gate. External AI detector scores can be recorded in `detector_notes`, but they are not proof of plagiarism and do not replace source evidence.

## Future Runtime Contract

When Strique runtime code exists, mirror this local harness with typed tools:

- `start_full_checklist_audit`
- `record_audit_evidence`
- `verify_audit_matrix`
- `finalize_audit`

`finalize_audit` should refuse full-audit wording unless `verify_audit_matrix` passes.
