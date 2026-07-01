# Phase 6: QA, Navigation, And Release

## Goal

Make the Docusaurus docs reliable enough to use: navigation is coherent, builds pass, links work, private artifacts stay private, and readers can find the right workflow without already knowing the repo.

This phase is release hardening, not new content expansion.

## Current Inputs

Expected completed inputs from earlier phases:

- Docusaurus app and sidebar from Phase 1.
- Repository inventory from Phase 2.
- Harness docs from Phase 3.
- Agent, skill, prompt, tool, and connector docs from Phase 4.
- Checklist encyclopedia from Phase 5.

Existing repo checks:

- Docs-only verification from `AGENTS.md`.
- Harness unit tests in `tests/test_seo_audit_harness.py`.

## Assumptions

- The first release can be internal.
- Public release needs an additional privacy and security pass.
- Build reliability matters more than visual polish.
- No deployment target is assumed yet.

## Implementation Steps

1. Finalize navigation.
   - Make the sidebar task-based, not file-tree-based.
   - Recommended order:
     - Start Here
     - How The SEO Module Works
     - Run The Harness
     - Full Checklist Audits
     - Content Authenticity
     - Evidence Sources
     - Agents And Skills
     - Tools And Connectors
     - Checklist Encyclopedia
     - Schemas
     - Brand Workspaces
     - Implementation Plan
   - Keep deep generated checklist pages nested below their checklist.

2. Add a glossary.
   - Include:
     - audit matrix
     - blocked row
     - brand DNA
     - checklist
     - connector
     - evidence source
     - Firecrawl
     - full audit
     - GSC
     - MCP
     - Playwright
     - skill
     - source log
     - Strique Orchestrator
   - Keep definitions short and linked to deeper docs.

3. Add reader paths.
   - "I need to run a full audit."
   - "I need to document a connector."
   - "I need to understand a checklist item."
   - "I need to rewrite content safely."
   - "I need to add a new brand workspace."
   - Each path should link to the fewest needed pages.

4. Add diagrams only where useful.
   - Harness lifecycle.
   - SEO agent invocation contract.
   - Evidence flow from connector to audit matrix.
   - Skill and checklist loading boundary.
   - Use Mermaid for diagrams.
   - Avoid decorative diagrams.

5. Run docs build checks.
   - Docusaurus build must pass.
   - Broken links must be fixed or intentionally excluded.
   - Markdown frontmatter must be valid.
   - Generated checklist docs must not break routes.

6. Run repo checks.
   - Docs-only instruction check:
     - `test -f AGENTS.md`
     - `sed -n '1,220p' AGENTS.md`
   - Harness regression check:
     - `python3 -m unittest tests/test_seo_audit_harness.py`
   - Optional command smoke checks:
     - `python3 tools/seo_audit_harness.py --help`
     - `python3 tools/seo_audit_harness.py compile-checklists --help`

7. Privacy review.
   - Search for likely secrets and private payloads.
   - Search for raw connector data linked from docs.
   - Ensure brand evidence folders are not exposed through sidebar or public build.
   - Confirm prompt docs describe contracts, not raw private prompts.

8. Release notes.
   - Summarize what the docs cover.
   - List known gaps.
   - List blocked areas requiring runtime code, connector access, or policy decisions.
   - Include verification commands and results.

9. Local preview.
   - Start docs preview only when useful.
   - Verify the local URL before reporting it:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN
curl -I http://localhost:<port>/
```

10. Decide deployment target.
   - Internal only:
     - local build artifact or internal static hosting
   - Team docs:
     - private GitHub Pages, Vercel, Netlify, or internal docs host
   - Public docs:
     - requires privacy, security, brand, and legal review first

## Deliverables

- Final sidebar and docs navigation.
- Glossary.
- Reader path pages.
- Mermaid diagrams where they clarify real flows.
- QA checklist.
- Release notes.
- Verified docs build.

## Verification

Run:

```bash
test -f AGENTS.md
sed -n '1,220p' AGENTS.md
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
```

Privacy spot checks:

```bash
rg -i "api[_-]?key|secret|token|password|credential" docs .agents
rg -i "raw connector|customer data|private payload" docs
```

Exit criteria:

- Build passes.
- Harness tests pass.
- Main reader paths are easy to follow.
- Private artifacts are not exposed.
- Known gaps are listed.
- Local URL is verified before being reported, if a server is started.

## Risks

- Broken links can appear late after generated checklist docs are added.
- Public deployment can expose more than intended if `brands/` artifacts are copied into the build.
- Navigation can become too deep because the checklist encyclopedia is large.

## Deferred

- Public deployment.
- Hosted search.
- Versioned docs.
- Visual design polish.
- Automated doc screenshots.
