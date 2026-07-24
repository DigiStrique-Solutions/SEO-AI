# Relivo — Existing Blog Inventory

**Status (2026-07-21):** No pre-existing blog or article surface found on go-mcp-server.vercel.app (landing + `/doc` only). Nothing to import.

## Authored posts

| Slug | Status | Gates (ai / craft / zerogpt) | Voice contract |
|------|--------|------------------------------|----------------|
| [publish-the-task-event-server-pattern](published/publish-the-task-event-server-pattern.md) | gate-passed (not yet placed on a live URL) | 5.41 / 0.0 / 0.0 human | [voice-contract-event-server.md](voice-contract-event-server.md) |

Drafts land in `blogs/drafts/` and, once gated (ai-text-risk under 20 + craft under 20 + zerogpt note) via `write-content`, are written to `blogs/published/`. References for any imported posts would live in `blogs/references/`.

**Content home open question:** Relivo has no `/blog` route yet. Confirm where authored posts should be published (e.g. a new `/blog` on the docs site, dev.to/Medium cross-post, or the repo). Tracked in `brand-dna.json → open_questions`.
