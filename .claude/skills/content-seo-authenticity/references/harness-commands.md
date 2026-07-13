# Reference — Harness Commands (content authenticity)

The **main task is the harness run**: generate/rewrite the draft, then gate it through these discrete commands.
Each step is a separate tool — call only the ones the current task needs, in order. Don't run the whole harness.

All paths are examples. The gate threshold is `< 20` (a score `>= 20` blocks publish-ready output).

## 1. `init-authenticity` — start the log (once per target)

```bash
python3 tools/seo_audit_harness.py init-authenticity \
  --target <target> \
  [--output <authenticity.json>]
```

Creates the authenticity log. Then add every source you use to it (`source_id`, `source_type`, `source_ref`, extracted facts) — see `checklists/authenticity-gate.md` for allowed `source_type` values.

## 2. `verify-authenticity` — read-only gate (no file written)

```bash
python3 tools/seo_audit_harness.py verify-authenticity \
  --authenticity <authenticity.json> \
  --rewrite-file <draft.md> \
  --max-ai-detector-score 20 \
  [--output <verify-report.json>]
```

Use during iteration — checks source coverage + local AI-pattern risk without saving anything. Returns `ai_text_risk.score`.

## 3. `write-content` — gated save (writes the final file)

```bash
python3 tools/seo_audit_harness.py write-content \
  --draft-file <draft.md> \
  --content-output <final.md> \
  --authenticity <authenticity.json> \
  --max-ai-detector-score 20 \
  [--output <write-report.json>]
```

Only writes `--content-output` when all authenticity checks pass **and** the score is `< 20`. This is the publish step.

## 4. `zerogpt-check` — optional external detector (weak signal)

```bash
python3 tools/seo_audit_harness.py zerogpt-check \
  (--content-file <draft.md> | --text "<inline>") \
  [--authenticity <authenticity.json>]   # appends a detector_note in place \
  [--max-ai-detector-score 20] \
  [--output <zerogpt-report.json>]
```

Records an external detector result in `detector_notes`. Never treat it as proof of authorship — it's a weak editorial signal only.

## Typical order

```text
init-authenticity  ->  (log sources)  ->  verify-authenticity  (loop until pass)  ->  write-content
                                                     └── always: zerogpt-check (weak signal; local fallback if paywalled)
```

## Rules

- The score is a **local AI-pattern risk percentage**, not plagiarism/authorship proof.
- Never lower the score by adding errors, awkward phrasing, fake anecdotes, or unverifiable detail — fix by adding source-backed specificity.
- No secrets in commands, drafts, logs, or reports.
- For on-page *content-SEO scoring* (not authenticity), evaluate `audit-library/content-seo.json` the brand-setup Phase 4 way — see `checklists/content-seo-onpage.md`. That's a different path from these authenticity commands.
