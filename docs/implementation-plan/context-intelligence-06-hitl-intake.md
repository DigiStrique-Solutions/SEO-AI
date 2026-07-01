# Context Intelligence 06: HITL Intake Experience

## Goal

Give Strique a human-in-the-loop intake flow that asks only the questions needed for the current work, stores answers once, and reuses those answers across future work.

## Question Format

Every HITL question should present:

- A short question.
- Recommended option first.
- Two alternate options.
- Custom answer path.
- A short reason available in details.

Example:

```text
Question: What is the primary business goal for this audit?

Recommended: Increase qualified leads
Option 2: Increase ecommerce sales
Option 3: Improve brand visibility
Option 4: Write your own answer
```

## Question Batching

Batch questions by impact:

1. Scope blockers.
2. Compliance or YMYL blockers.
3. Prioritization blockers.
4. Measurement blockers.
5. Content quality blockers.

Ask no more than the product UX can handle cleanly in one step. The runtime can continue with non-blocking assumptions only when the field allows it.

## Answer Storage

After user answer:

```json
{
  "question_id": "primary_business_goal",
  "field_id": "primary_business_goal",
  "answer": "Increase qualified leads",
  "normalized_value": ["increase qualified leads"],
  "store_scope": "brand",
  "source_type": "client_confirmed",
  "confidence": "high",
  "applies_to": ["audits", "strategy", "content", "reporting"]
}
```

## Durable Versus Run-Scoped

Store in Brand DNA:

- Business model.
- Target audience.
- Priority markets.
- Competitors.
- Approved claims.
- Restricted claims.
- Compliance rules.
- Conversion definitions.
- Measurement source preferences.

Store in run context:

- This audit URL.
- This blog topic.
- This report date range.
- This media plan budget.
- This one-time campaign goal.
- This temporary priority query set.

## HITL States

- `answered`: user supplied answer.
- `skipped`: user skipped non-blocking question.
- `auto_resolved`: resolver found answer before user replied.
- `blocked`: answer required and unavailable.
- `promoted`: answer saved into Brand DNA.
- `run_only`: answer saved only to run context.

## Agent Behavior

The agent should explain why a question matters only when helpful. Main UI should stay terse.

Example detail:

```text
This determines whether the audit prioritizes leads, revenue, rankings, content quality, support deflection, or reputation.
```

## Review And Correction

Users must be able to correct prior answers. Corrections should:

- Update the stored field.
- Record previous value.
- Mark dependent assumptions for review.
- Trigger re-evaluation for affected checklist items if needed.

## Verification

- Questions always map to fields.
- Client-confirmed answers are reused.
- Run-scoped answers do not pollute Brand DNA.
- Corrected answers update downstream context.
- Skipped required questions create blocked states.

