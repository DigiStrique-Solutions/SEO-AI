---
title: SEO Agent Contract
sidebar_position: 2
---

# SEO Agent Contract

## The SEO Agent Receives

- Current org, user, conversation, brand, website, and connected platform context.
- Product marketing context when available.
- Skill metadata for assigned SEO skills.
- Checklist metadata for assigned SEO checklists.
- MCP tool metadata for configured tools.

## The SEO Agent Must Not Receive

- Raw credentials.
- Cross-org context.
- Skills or checklists outside the active assignment.
- Raw system prompts from other Strique agents.

## Blog Writing Route

When the user asks to write a blog, the SEO agent must not freewrite publish-ready copy. It must:

- Resolve brand, website, keyword, audience, and checklist context.
- Initialize or load the authenticity log for the target draft.
- Record concrete sources with `record-authenticity-source`.
- Create or read the content brief.
- Draft the Markdown blog package with the required frontmatter and body sections.
- Run `write-blog`.
- Return the final content path when `write-blog` passes, or exact blockers when it fails.

If concrete evidence is missing, return a blocked draft or source request instead of publish-ready copy.

## Output Shape

SEO outputs should include summary, top findings, evidence, priority fixes, implementation notes, expected impact, and open questions.
