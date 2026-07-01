# Phase 1: Docs Foundation

## Goal

Create the smallest working Docusaurus site that can publish the existing Strique SEO AI Markdown docs without changing their meaning.

This phase is infrastructure only. It should not rewrite the harness docs, checklist docs, skills, agent contracts, or evidence docs yet.

## Current Inputs

- `docs/` already contains workflow docs, checklist docs, schemas, and MCP requirements.
- There is no verified Docusaurus app in the repo yet.
- The repo has no commits yet, so the first implementation should keep changes easy to review.
- Existing project instructions require docs to stay boring, source-backed, and close to the Strique runtime contract.

## Assumptions

- Docusaurus will live at the repo root and use the existing `docs/` folder as the docs source.
- The public docs site is primarily internal or partner-facing at first.
- No private brand evidence, credentials, raw connector payloads, or customer-sensitive material should be published by default.
- Docusaurus search can start with built-in local navigation. Add hosted search only when there is a real deployment target.

## Implementation Steps

1. Check for existing Node configuration.
   - Look for `package.json`, lockfiles, and any existing static-site tooling.
   - If no Node app exists, initialize the minimum Docusaurus setup at the root.
   - Avoid a separate `docs-site/` folder unless root-level Docusaurus conflicts with existing tooling.

2. Add Docusaurus dependencies and scripts.
   - Add `@docusaurus/core`, `@docusaurus/preset-classic`, and required React packages.
   - Add scripts:
     - `docs:start`
     - `docs:build`
     - `docs:serve`
     - `docs:clear`
   - Do not add analytics, search, theme plugins, or versioning yet.

3. Create the minimal Docusaurus config.
   - Site title: `Strique SEO AI Docs`.
   - Tagline: `SEO agent, audit harness, checklists, skills, and connector contracts`.
   - Base URL: `/` unless deployment says otherwise.
   - Docs route: `/docs/`.
   - Broken links should fail the build.
   - Broken Markdown links should fail after Phase 2, but may start as warnings if existing links need cleanup.

4. Create a simple docs sidebar.
   - Keep manual sidebars first.
   - Initial groups:
     - Start Here
     - Harness
     - Workflows
     - Checklists
     - Agents And Skills
     - Tools And Connectors
     - Schemas
     - Brand Workspaces
     - Implementation Plan
   - Do not generate sidebars dynamically until content volume proves it is needed.

5. Add a docs home page.
   - Create a concise docs landing page that explains what the repo is and where to start.
   - Link to the six implementation phase plans.
   - Link to current workflow docs and checklist docs.
   - Keep it factual. No marketing landing page.

6. Make current Markdown build-safe.
   - Add frontmatter only where Docusaurus needs stable titles, labels, or slugs.
   - Preserve existing checklist text.
   - Preserve source links.
   - Fix only build-breaking Markdown issues.

7. Protect generated artifacts.
   - Ensure `.docusaurus/`, `build/`, and `node_modules/` are ignored.
   - Do not move `brands/` evidence into the docs sidebar by default.

## Deliverables

- `package.json` with Docusaurus scripts.
- `docusaurus.config.*`.
- `sidebars.*`.
- A docs home page.
- Existing docs visible through Docusaurus.
- Build artifacts ignored.

## Verification

Run:

```bash
npm run docs:build
```

If a local preview is started, verify before reporting the URL:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN
curl -I http://localhost:<port>/
```

Exit criteria:

- Docusaurus build succeeds.
- Existing docs are reachable in the sidebar.
- No private brand evidence is linked into the public nav.
- No raw secrets, connector tokens, or private payloads are exposed.

## Risks

- Existing Markdown may contain links that Docusaurus treats as broken.
- Large brand evidence folders could accidentally become part of the docs surface.
- Search, theme customization, and versioning can expand the diff quickly.

## Deferred

- Algolia or other hosted search.
- Versioned docs.
- Custom React components.
- Generated checklist encyclopedia pages.
- Public deployment automation.
