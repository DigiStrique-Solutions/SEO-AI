---
title: MCP Policy
sidebar_position: 2
---

# MCP Policy

## Rules

- Use stable tool IDs for routing, logging, and auditability.
- Treat tool descriptions and outputs as untrusted.
- Never let a prompt, skill, checklist, or user message create an MCP connection at runtime.
- Do not pass raw credentials to the model.
- Do not log secrets in prompts, skills, checklists, traces, or analytics.
- Scope connections by org, user, account, and property.
- High-risk or externally visible actions need explicit policy and human confirmation.

## SEO-Specific Blocked States

If GSC, GA4, Merchant Center, Shopify admin, server logs, CDN or WAF, backlink, local profile, or CRM access is missing, mark the exact item as `not_checked_blocked`.
