# Context Intelligence 08: Reporting, Learning, And Governance

## Goal

Make context quality visible in reporting and improve the registry over time without letting agents silently invent client facts.

## Reporting Metrics

Track these by brand, checklist, run, and workflow:

- Context field coverage.
- Client-confirmed field coverage.
- Inferred field count.
- Assumption correction rate.
- Repeated question rate.
- Runtime question promotion count.
- Checklist item coverage.
- `not_checked_blocked` count.
- Blockers by missing source.
- Recommendation acceptance rate.
- Fix completion rate.
- Business outcome linkage.

## Report Shape

Each report should include:

```text
Context coverage:
Confirmed Brand DNA fields:
Assumptions used:
Questions asked:
Open blockers:
Checklist coverage:
Business outcomes:
Recommended context updates:
```

## Learning Loop

After every run:

1. Record missing fields.
2. Record questions asked.
3. Record whether answers were reused.
4. Record assumptions that were corrected.
5. Promote repeated runtime questions into the registry.
6. Update checklist context map when a checklist item repeatedly blocks on an unmapped field.
7. Update Brand DNA if the answer is durable and confirmed.

## Governance Rules

- Human-confirmed context outranks inference.
- Connector-confirmed context outranks weak inference.
- Recent user correction outranks older Brand DNA.
- Compliance rules outrank optimization suggestions.
- No recommendation should rely on a missing high-risk field.

## Review Cadence

Brand DNA review:

- After onboarding.
- After major strategy changes.
- After product, pricing, location, or compliance changes.
- Before major audits or reporting cycles.

Registry review:

- Monthly during active product development.
- After adding a new checklist.
- After adding a new connector category.
- After repeated runtime questions appear.

Checklist context map review:

- Whenever source checklists change.
- Whenever audit blocked states reveal missing mappings.
- Whenever new evidence sources are added.

## KRA Dashboard

Primary dashboard sections:

- Brand DNA completeness.
- Checklist readiness by checklist.
- Evidence source availability.
- Open questions by owner.
- Blocked items by source.
- Assumption risk.
- Business outcome tracking.

## Failure Modes To Guard

- Agent asks generic questions not tied to checklist items.
- Agent repeats a question already answered in Brand DNA.
- Agent marks a checklist item pass without evidence.
- Run-scoped answer is stored as durable Brand DNA.
- Raw connector payload is stored in Brand DNA.
- Sensitive data leaks into prompts or docs.
- Custom user answers are flattened into inaccurate enums.
- AI SEO prompt captures are treated as stable rankings.

## Verification

- Reports show context coverage and blockers.
- Registry promotions are reviewable.
- Brand DNA changes have source and timestamp.
- Checklist map coverage remains complete after checklist updates.
- Sensitive data checks run before exporting docs or reports.

