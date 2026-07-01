---
title: Agent Architecture
sidebar_position: 1
---

# Agent Architecture

The Strique Orchestrator is the user-facing control plane. The SEO agent is a specialist invoked by the orchestrator, not a standalone chatbot.

```text
user request
  -> Strique Orchestrator
  -> run_sub_agent(agent_id="seo_agent", input=...)
  -> SEO specialist agent
  -> scoped skills, checklists, tools, brand context
  -> actionable Strique output
```

This repo currently documents the contract and local harness. Production runtime code should mirror Strique's existing ai-server pattern when added.
