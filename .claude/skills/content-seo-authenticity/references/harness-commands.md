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

Use during iteration — checks source coverage + local AI-pattern risk without saving anything. Returns `ai_text_risk.score`, and `craft` **report-only** (it does not fail the command here; `write-content` is where craft blocks).

## 3. `craft-report` — editorial craft signals (read-only)

```bash
python3 tools/seo_audit_harness.py craft-report \
  --file <draft.md> \
  [--max-craft-score 20] \
  [--output <craft-report.json>]
```

Reports `defensive_hedging`, `unresolved_placeholder`, `en_em_dash` and `near_duplicate_sections`. Any one of them alone can reach 20 and block — a single `[needs source]`, a single en/em dash, or one pair of cloned sections is a hard fail.

**A craft score of 0 is not a verdict.** It measures hedging and structural cloning, nothing else. Voice, hook, narrative spine, product integration and styling payload are unmeasured and stay your judgement — see `checklists/editorial-craft.md`.

## 4. `write-content` — gated save (writes the final file)

```bash
python3 tools/seo_audit_harness.py write-content \
  --draft-file <draft.md> \
  --content-output <final.md> \
  --authenticity <authenticity.json> \
  --max-ai-detector-score 20 \
  [--max-craft-score 20] \
  [--output <write-report.json>]
```

Only writes `--content-output` when all authenticity checks pass, `ai_text_risk < 20`, **and** `craft < 20`. This is the publish step.

## 5. `zerogpt-check` — optional external detector (weak signal)

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
Step 0 (brand context + voice contract)  ->  init-authenticity  ->  (log sources)
   ->  verify-authenticity / craft-report  (loop until both pass)  ->  write-content
                     └── always: zerogpt-check (weak signal; local fallback if paywalled)
```

## Rules

- The score is a **local AI-pattern risk percentage**, not plagiarism/authorship proof.
- Never lower the score by adding errors, awkward phrasing, fake anecdotes, or unverifiable detail — fix by adding source-backed specificity.
- **Never lower `craft` by hiding the symptom.** Delete the hedge *and* the claim it was defending (cut and pivot), or resolve the source. Renaming a cloned section, or paraphrasing it just past the similarity threshold, leaves the draft exactly as repetitive as the reviewer found it.
- **Passing every gate is not the goal.** These scores detect bad writing; they cannot recognise good writing, and a draft optimized to satisfy them reads flat. Write for the reader, then check the gates.
- No secrets in commands, drafts, logs, or reports.
- For on-page *content-SEO scoring* (not authenticity), evaluate `audit-library/content-seo.json` the brand-setup Phase 4 way — see `checklists/content-seo-onpage.md`. That's a different path from these authenticity commands.
