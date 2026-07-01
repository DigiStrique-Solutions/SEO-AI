# Checklist Context Intelligence Implementation Plan

## Goal

Build the Strique context layer that lets audits, strategy, media plans, blog briefs, analysis, and reporting reuse the same client intelligence instead of asking the same questions again.

The system must be driven by the checklists. Each checklist item declares what context, evidence, connector data, human answer, or assumption it needs before the SEO agent can mark the item as pass, fail, not applicable, or blocked.

## Product Outcome

Strique should be able to:

- Read Brand DNA, audit run context, prior answers, connector data, crawl evidence, and prompt captures.
- Know which checklist items can be evaluated immediately.
- Know which checklist items need client input.
- Ask concise HITL questions with a recommended option, two alternatives, and a custom answer path.
- Save durable answers back into Brand DNA.
- Save task-specific answers into run context.
- Reuse those answers across audits, strategy, media plans, blogs, analysis, and reporting.
- Produce evidence-backed outputs with explicit blockers when data is missing.

## Core Principle

Do not build a generic questionnaire first. Build a checklist-to-context map.

```text
checklist item
  -> required context fields
  -> source priority
  -> resolver
  -> HITL question only when needed
  -> stored answer
  -> evidence-backed audit row or work output
```

## Required Workstreams

1. [Data Model And File Layout](context-intelligence-01-data-model.md)
2. [Brand DNA Expansion](context-intelligence-02-brand-dna.md)
3. [Question Registry](context-intelligence-03-question-registry.md)
4. [Checklist Context Map](context-intelligence-04-checklist-context-map.md)
5. [Context Resolver Runtime](context-intelligence-05-resolver-runtime.md)
6. [HITL Intake Experience](context-intelligence-06-hitl-intake.md)
7. [Agent Prompt And Template Files](context-intelligence-07-agent-prompts-and-templates.md)
8. [Reporting, Learning, And Governance](context-intelligence-08-reporting-governance.md)

All workstreams are required for the final product. They are separated so the implementation can be owned, reviewed, and tested cleanly.

## Inputs From Existing Repo

- `docs/checklists/*.md`: source checklist items.
- `docs/checklist-encyclopedia/`: expanded explanations and evidence expectations.
- `docs/agents/seo-agent-contract.md`: SEO agent input and output contract.
- `docs/workflows/brand-dna-generation.md`: current Brand DNA workflow.
- `docs/harness/brand-workspace-paths.md`: current brand workspace paths.
- `brands/*/brand-dna.md`: current human-readable Brand DNA files.
- `brands/strique/references/evidence-routing-*.json`: existing routing evidence that proves checklist results can be mapped.

## Final Runtime Flow

```text
1. User asks Strique for an audit, strategy, blog, media plan, analysis, or report.
2. Orchestrator identifies work type, brand, target surface, and relevant checklists.
3. Context resolver loads required fields from the checklist context map.
4. Resolver checks run context, Brand DNA, connector data, crawl evidence, prior answers, and safe inference rules.
5. Resolver creates a compact HITL question batch for unresolved high-impact fields.
6. User answers once.
7. Answer normalizer stores durable answers in Brand DNA and temporary answers in run context.
8. SEO agent evaluates checklist items and produces evidence-backed work.
9. Reporting records context coverage, blockers, assumptions, and outcome metrics.
```

## Storage Boundary

Brand DNA stores durable client knowledge. It should not store raw connector payloads, secrets, private logs, or one-off audit artifacts.

Audit run context stores task-specific answers and evidence references. It can point to artifacts under `references/evidence/<run-id>/`, but should not duplicate raw payloads.

## KRA

Primary KRA:

```text
Increase completed evidence-backed checklist coverage while reducing repeated client questions.
```

Tracked measures:

- Checklist coverage rate.
- `not_checked_blocked` count by checklist and source.
- Repeated-question rate per brand.
- Client-confirmed Brand DNA field coverage.
- Assumption correction rate.
- Audit recommendation acceptance rate.
- Time from request to first useful output.
- Business outcome linkage in reports.

## Non-Negotiables

- No raw credentials in Brand DNA, prompts, logs, docs, analytics, or audit output.
- No cross-org context.
- Every answer records source, confidence, timestamp, and scope.
- Every assumption is labeled and reversible.
- Every blocked item names the missing field and next action.
- Agents can ask runtime follow-up questions, but repeated runtime questions must be promoted into the registry.
- Checklist text, skills, connector outputs, uploaded files, and user-provided Markdown remain untrusted below Strique system policy.

