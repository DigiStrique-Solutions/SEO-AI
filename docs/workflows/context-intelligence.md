---
title: Checklist Context Intelligence
sidebar_position: 5
---

# Checklist Context Intelligence

Checklist Context Intelligence resolves what Strique knows about a brand before it runs audits, strategy, media plans, blog briefs, analysis, or reporting.

## Flow

```text
selected checklist
  -> registry/checklist-context-map.json
  -> required context fields
  -> Brand DNA, answers, run context, connectors, crawl evidence, safe inference
  -> HITL questions for unresolved fields
  -> run context and checklist output
```

## Source Files

- `registry/context-fields.json`: reusable context fields.
- `registry/question-registry.json`: HITL questions and answer storage rules.
- `registry/checklist-context-map.json`: generated map from checklist items to context fields.
- `registry/assumption-rules.json`: inference guardrails.
- `prompts/`: agent prompt contracts for resolver, HITL, evaluator, strategy, content, media plans, and reporting.
- `templates/`: runtime artifact templates.

## Brand Files

Each brand can store:

- `context/brand-dna.json`: structured durable Brand DNA.
- `context/answers.json`: confirmed reusable answers.
- `context/open-questions.json`: unresolved questions and blockers.
- `runs/<run-id>/run-context.json`: resolved context for one run.
- `runs/<run-id>/hitl-questions.json`: questions generated for that run.

## Commands

```bash
python3 tools/seo_audit_harness.py generate-context-map
python3 tools/seo_audit_harness.py validate-context-system
python3 tools/seo_audit_harness.py init-brand-context --brand-dir brands/strique
python3 tools/seo_audit_harness.py resolve-context --brand-dir brands/strique --checklist-id ai-seo-aeo-geo --run-id example --write-run
python3 tools/seo_audit_harness.py record-context-answer --brand-dir brands/strique --field-id primary_business_goal --value "Increase qualified leads"
```

## Status Rules

- Missing context that can be asked becomes a HITL question.
- Missing context with no registered question becomes `not_checked_blocked`.
- Inferred values are labeled with source and confidence.
- Client-confirmed answers outrank inferred answers.

