---
title: Repository Map
sidebar_position: 1
---

# Repository Map

This repo is the Strique SEO AI module. It contains docs, a local audit harness, checklist assets, brand workspaces, tests, and agent guidance.

| Path | Purpose | Publishability |
| --- | --- | --- |
| `AGENTS.md` | Project contract for agent behavior, SEO agent shape, MCP policy, and verification rules. | Internal reference |
| `.agents/skills/` | Local Strique skill instruction assets. | Internal unless reviewed |
| `docs/` | Source docs for Docusaurus, checklists, workflows, schemas, and plans. | Public-safe only after review |
| `tools/seo_audit_harness.py` | Local CLI for checklist compilation, audit matrices, evidence collection, keywords, and authenticity gates. | Source code |
| `tests/` | Harness regression tests. | Source code |
| `registry/` | Context field, question, assumption, and checklist context map registries. | Source code |
| `schemas/` | Runtime JSON schemas for context intelligence artifacts. | Source code |
| `prompts/` | Prompt contracts for resolver, HITL, evaluator, strategy, content, media plans, and reporting. | Internal unless reviewed |
| `templates/` | JSON and Markdown templates for generated context artifacts. | Source code |
| `brands/` | Brand workspaces, crawls, evidence, exports, and audit outputs. | Restricted by default |
| `tmp/` | Ignored temporary reports and scratch artifacts. | Not published |

Current checklist coverage:

| Checklist | Sections | Items |
| --- | ---: | ---: |
| `docs/checklists/ai-seo-aeo-geo-checklist.md` | 23 | 133 |
| `docs/checklists/content-seo-checklist.md` | 26 | 173 |
| `docs/checklists/ecommerce-seo-checklist.md` | 23 | 169 |
| `docs/checklists/generic-on-page-seo-checklist.md` | 36 | 381 |
| `docs/checklists/local-seo-checklist.md` | 25 | 196 |
| `docs/checklists/off-page-seo-checklist.md` | 23 | 148 |
| `docs/checklists/site-architecture-seo-checklist.md` | 31 | 218 |
| **Total** | **187** | **1418** |

Do not publish `brands/` wholesale. It can contain customer context, screenshots, raw connector payloads, and evidence artifacts.
