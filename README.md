# Strique SEO AI

Repo-local SEO agent materials for Strique: checklists, prompts, brand workspaces, content authenticity gates, and the Python SEO audit harness.

## Codex Setup

1. Clone the repo and open the folder in Codex.
2. Ask Codex to read `AGENTS.md`.
3. Install dependencies and run checks:

```bash
npm install
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
python3 tools/seo_audit_harness.py --help
```

## Optional Environment

Copy `.env.example` to `.env` locally and fill values outside Git:

```bash
FIRECRAWL_API_KEY=
GOOGLE_API_KEY=
```

Do not commit `.env`.

## Docs

```bash
npm run docs:start
```

## Publish Check

Before pushing, run:

```bash
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
rg -l --hidden -g '!.git' -g '!node_modules' -e 'sk-proj-[A-Za-z0-9_-]{20,}' -e 'gho_[A-Za-z0-9]{20,}' -e 'ghp_[A-Za-z0-9]{20,}' -e 'AIza[0-9A-Za-z_-]{35}' -e 'FIRECRAWL_API_KEY\s*=' -e 'GOOGLE_API_KEY\s*=' .
```

Generated crawl and evidence artifacts are ignored by default. Keep only reviewed summaries, briefs, drafts, and reusable source files in Git.
