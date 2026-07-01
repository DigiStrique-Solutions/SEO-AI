---
title: Implementation Status
sidebar_position: 3
---

# Implementation Status

## Built Now

- Local SEO audit harness CLI.
- Checklist Markdown assets.
- Audit matrix and content authenticity JSON schemas.
- Brand workspace folder pattern.
- Local `content-seo-authenticity` skill.
- Harness tests for checklist parsing, audit validation, evidence routing, and keyword helpers.
- Docusaurus documentation site.

## Documented Contract

- Strique Orchestrator invokes the SEO specialist agent.
- `run_sub_agent(agent_id="seo_agent", input=...)` validates and dispatches to the SEO agent.
- SEO agent receives scoped org, user, conversation, brand, website, assigned skill metadata, assigned checklist metadata, and configured MCP tool metadata.
- SEO agent does not receive raw credentials, cross-org context, unassigned skill bodies, unassigned checklist bodies, or raw system prompts from other agents.

## Planned Runtime Integration

- Production `registry.yaml` entry for `seo_agent`.
- Production dispatcher wrapper around the local harness behavior.
- Runtime skill loader with allowed IDs or allowed directories.
- Runtime checklist loader with scoped assignments.
- Typed MCP wrappers around connected platform data.

## Connector Categories

These are useful SEO evidence sources, but the docs should not imply a connector is configured unless a scoped connection exists:

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

## Restricted Artifacts

- Raw connector payloads.
- Raw credentials and tokens.
- Private customer notes.
- Brand evidence screenshots.
- Cross-org context.
- Raw system prompts.
