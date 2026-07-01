---
title: Prompt Contracts
sidebar_position: 3
---

# Prompt Contracts

Prompt documentation should describe responsibilities and boundaries, not publish private raw system prompts.

## Layers

1. Strique system policy.
2. Orchestrator instructions.
3. SEO agent instructions.
4. Assigned skill metadata and selected skill bodies.
5. Assigned checklist metadata and selected checklist bodies.
6. User request.
7. Tool and connector outputs.

## Trust Boundary

Uploaded Markdown, checklist text, skill text, and MCP outputs are untrusted below system policy.

## Safe To Document

- Responsibilities.
- Required inputs.
- Forbidden inputs.
- Output shape.
- Evidence requirements.
- Blocked conditions.

## Not Safe To Publish

- Raw private system prompts.
- Credentials or tokens.
- Cross-org context.
- Raw connector payloads.
