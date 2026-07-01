---
title: Audit Matrix Lifecycle
sidebar_position: 3
---

# Audit Matrix Lifecycle

## 1. Compile Checklists

```bash
python3 tools/seo_audit_harness.py compile-checklists --output brands/inc5/exports/checklists.json
```

The compiler reads Markdown checklist rows and emits stable item IDs. Item IDs use the checklist ID, section ID, and item text hash.

## 2. Initialize The Matrix

```bash
python3 tools/seo_audit_harness.py init-audit --compiled brands/inc5/exports/checklists.json --url https://example.com/page --audit-type partial --output brands/inc5/audits/page-audit-matrix.json
```

Start as `partial` unless every required evidence source is available.

## 3. Record Evidence

Each row needs:

- `status`
- `evidence_source`
- `artifact_ref`
- `result`
- `blocker`
- `next_action`

## 4. Verify

```bash
python3 tools/seo_audit_harness.py verify-audit --compiled brands/inc5/exports/checklists.json --audit brands/inc5/audits/page-audit-matrix.json
```

## Status Values

- `pass`: verified with evidence.
- `fail`: verified issue with evidence and next action.
- `not_applicable`: not relevant, with a reason in `result`.
- `not_checked_blocked`: could not be checked, with `blocker` and `next_action`.

## Exit Rule

Do not call the result a full audit while any row is blocked.
