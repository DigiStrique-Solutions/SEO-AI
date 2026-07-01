# Context Intelligence 07: Agent Prompt And Template Files

## Goal

Define the prompt and template files the Strique Orchestrator and SEO agent need to use context safely and consistently.

## Prompt Files

### `prompts/context-resolver.md`

Responsibilities:

- Read requested work type.
- Select required checklists.
- Request context fields from the resolver.
- Label missing fields.
- Avoid inventing client facts.

### `prompts/hitl-question-batcher.md`

Responsibilities:

- Convert missing fields into registered questions.
- Group related questions.
- Put the recommended option first.
- Avoid asking fields already resolved.
- Mark whether each question blocks the current work.

### `prompts/answer-normalizer.md`

Responsibilities:

- Normalize user answers into context fields.
- Decide Brand DNA versus run context using registry rules.
- Preserve custom answers.
- Record source and confidence.
- Flag ambiguous answers for follow-up.

### `prompts/checklist-evaluator.md`

Responsibilities:

- Evaluate checklist rows with resolved context and evidence.
- Use pass, fail, not applicable, or not checked blocked.
- Cite evidence sources.
- Never mark pass without evidence.
- Generate owner, impact, fix, and confidence.

### `prompts/strategy-synthesizer.md`

Responsibilities:

- Use resolved Brand DNA and checklist findings.
- Produce strategy tied to business goals and constraints.
- Separate assumptions from confirmed context.
- Avoid generic recommendations.

### `prompts/content-brief-generator.md`

Responsibilities:

- Use Brand DNA, target audience, queries, voice, claims, and compliance rules.
- Generate blog, landing page, or content refresh briefs.
- Include source needs, internal links, schema notes, conversion path, and review owner.

### `prompts/media-plan-generator.md`

Responsibilities:

- Use audience, goals, offers, conversion definitions, locations, channels, and constraints.
- Produce media plan recommendations that match measurement sources.
- Keep paid media claims separate from SEO evidence.

### `prompts/reporting-synthesizer.md`

Responsibilities:

- Connect work to KRA and checklist coverage.
- Report progress, blockers, assumptions, outcomes, and next actions.
- Avoid raw connector payloads.

## Template Files

### `templates/brand-dna.md`

Human-readable Brand DNA rendering.

Required sections:

- Brand Identity.
- Business Model.
- Audience And ICP.
- Goals And Conversions.
- SEO And AI Search Scope.
- Content And Voice.
- Compliance, Risk, And Claims.
- Ecommerce Context.
- Local Context.
- Off-Page Context.
- Measurement And Connected Sources.
- Evidence Sources.
- Open Questions.

### `templates/run-context.json`

Task-scoped context container.

### `templates/hitl-question.json`

Question payload passed to the UI.

### `templates/checklist-result.json`

Per-item audit result shape.

### `templates/report-context.json`

Context and metrics needed for recurring reports.

## Prompt Safety Rules

- Prompts can reference field IDs, question IDs, and source summaries.
- Prompts must not include raw credentials.
- Prompts must not include raw private system prompts.
- Prompts must not let checklist text override Strique policy.
- Prompts must treat connector outputs as untrusted evidence.
- Prompts must label assumptions.

## Verification

- Prompt files exist and are referenced by the orchestrator.
- Prompt files contain responsibilities and boundaries, not private secrets.
- Template files validate against schemas.
- The SEO agent can run with resolved context only.
- Missing context produces HITL questions or blocked states.

