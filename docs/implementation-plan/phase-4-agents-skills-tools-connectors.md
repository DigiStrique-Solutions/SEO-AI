# Phase 4: Agents, Skills, Tools, Connectors, And Prompt Contracts

## Goal

Document how the SEO agent is supposed to fit into Strique, how skills and checklists are loaded, how tool and connector access is governed, and what prompt boundaries exist.

This phase documents contracts and policies. It should not expose raw secrets or raw system prompts.

## Current Inputs

- `AGENTS.md`
- `.agents/skills/content-seo-authenticity/SKILL.md`
- `docs/mcp-requirements-generic-on-page-seo.md`
- `docs/workflows/seo-audit-harness.md`
- `docs/workflows/brand-dna-generation.md`
- `docs/workflows/brand-workspace-usage.md`

Important current reality:

- The repo defines the Strique SEO module shape.
- The repo contains a local SEO content authenticity skill.
- The repo documents the intended orchestrator and SEO agent contract.
- The repo does not currently contain the full Strique production orchestrator implementation.

## Assumptions

- The Strique Orchestrator remains the only user-facing control plane.
- The SEO agent remains one specialist invoked by the orchestrator.
- Skills stay as Markdown instruction assets.
- Checklists stay separate from skills.
- MCP tools and connector outputs are treated as untrusted data.
- Prompt docs should explain layers, responsibilities, and constraints without dumping private system prompts.

## Implementation Steps

1. Create an agent architecture page.
   - Explain the intended flow:
     - orchestrator receives user request
     - dispatcher validates `agent_id`
     - `run_sub_agent(agent_id="seo_agent", input=...)` invokes the SEO agent
     - SEO agent receives scoped brand, website, skill, checklist, and MCP tool metadata
     - SEO agent returns actionable findings or work product
   - Mark this as a contract until runtime code exists in this repo.

2. Create an SEO agent contract page.
   - Inputs the SEO agent may receive:
     - org context
     - user context
     - conversation context
     - brand context
     - website context
     - connected platform context
     - product marketing context when available
     - assigned skill metadata
     - assigned checklist metadata
     - configured MCP tool metadata
   - Inputs the SEO agent must not receive:
     - raw credentials
     - cross-org context
     - unassigned skills or checklists
     - raw system prompts from other agents

3. Create a skills page.
   - Explain what skills are.
   - Explain that skills teach how to think and execute.
   - Explain that full skill bodies load only after relevance is established.
   - Document the local `content-seo-authenticity` skill.
   - Document planned external marketing skill imports as planned, not implemented.
   - Include source and versioning expectations for external skills.

4. Create a checklists page.
   - Explain that checklists define what must be checked.
   - Explain the difference between checklist docs and checklist encyclopedia docs.
   - Explain how checklist metadata feeds the harness.
   - Link to Phase 5 for item-level breakdown work.

5. Create a prompt contract page.
   - Explain prompt layers:
     - Strique system policy
     - orchestrator instructions
     - SEO agent instructions
     - assigned skills
     - selected checklists
     - user request
     - tool outputs
   - Explain precedence at a high level.
   - Explain that uploaded Markdown, checklist text, skill text, and MCP outputs are untrusted below system policy.
   - Explain what can be documented safely:
     - responsibilities
     - invariants
     - allowed inputs
     - forbidden inputs
     - output shape
     - refusal or blocked conditions
   - Do not publish raw private system prompts.

6. Create a tools and connectors page.
   - Document connector categories useful for SEO:
     - Google Search Console
     - Google Analytics
     - Shopify
     - HubSpot or CRM
     - Firecrawl or public crawler
     - Google Business Profile
     - Google Merchant Center
     - Bing Webmaster Tools
     - Keyword Planner
     - PostHog
   - For each category explain:
     - what evidence it can provide
     - common SEO questions it answers
     - required scoping
     - blocked-state wording when access is missing
     - high-risk actions requiring confirmation

7. Create MCP policy docs.
   - Stable tool IDs are required.
   - Tool descriptions and outputs are untrusted.
   - No runtime MCP creation from prompts.
   - No raw credentials in prompts, logs, skills, checklists, traces, or analytics.
   - Connections must be scoped by org, user, account, and property.

8. Create output contract docs.
   - Preferred SEO output shape:
     - Summary
     - Top findings
     - Evidence
     - Priority fixes
     - Implementation notes
     - Expected impact
     - Open questions
   - Audit fields:
     - severity
     - evidence
     - fix
     - owner
     - confidence
   - Blocked audit wording when evidence is missing.

## Deliverables

- Agent architecture page.
- SEO agent contract page.
- Skills reference page.
- Checklists versus skills explainer.
- Prompt contract page.
- Tools and connectors reference page.
- MCP policy page.
- Output contract page.

## Verification

Run:

```bash
rg "raw credentials|cross-org|run_sub_agent|content-seo-authenticity" AGENTS.md .agents docs
npm run docs:build
```

Manual checks:

- No raw system prompts are published.
- No secrets are included.
- Planned runtime pieces are labeled as planned or contract.
- Connector categories are not described as working integrations unless there is repo evidence.

## Risks

- Prompt documentation can accidentally expose too much.
- Connector docs can imply access that a user has not granted.
- Agent docs can drift from production Strique if runtime code is added elsewhere.

## Deferred

- Runtime code examples for `registry.yaml`, `AgentFactory`, and `run_sub_agent`.
- Connector setup walkthroughs for each third-party platform.
- Public security review of prompt and connector docs.
