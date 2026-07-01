# Brand Workspace Usage

Each folder in `brands/` is one brand workspace. Use `brands/_template/` when starting a new brand.

## Folder Map

```text
brand-dna.md
context/
keywords/keywords.csv
audits/audits.csv
tasks/tasks.csv
docs/
references/
runs/
blogs/briefs/
blogs/drafts/
blogs/published/
images/source/
images/generated/
exports/
```

## How To Use It

- `brand-dna.md`: stable brand context for SEO work, content briefs, audits, and image generation.
- `context/`: structured Brand DNA, reusable answers, assumptions, and open questions.
- `keywords/keywords.csv`: keyword targets, intent, page type, target URL, priority, source, and status.
- `audits/audits.csv`: findings from checklists, crawls, GSC, GA4, Firecrawl, and manual review.
- `tasks/tasks.csv`: work items created from audits, briefs, and implementation follow-ups.
- `docs/`: brand-specific SEO docs, strategy notes, standards, and planning docs.
- `references/`: crawl notes, source URLs, screenshots, exports, competitor notes, and evidence.
- `runs/`: task-specific resolved context, HITL questions, and run outputs.
- `blogs/briefs/`: content briefs before drafting.
- `blogs/drafts/`: draft content.
- `blogs/published/`: final published copy or published URL notes.
- `images/source/`: original brand images, logos, and source screenshots.
- `images/generated/`: AI-generated assets.
- `exports/`: shareable outputs for clients, stakeholders, or imports into other tools.

## Rules

- Keep trackers as CSV so they can be imported into Sheets and reviewed in Git.
- Keep raw connector payloads out of Brand DNA.
- Store durable answers in `context/brand-dna.json`; store one-run answers in `runs/<run-id>/run-context.json`.
- Keep evidence close to the task or audit that depends on it.
- Do not store secrets, credentials, private customer data, or raw MCP tokens.
- If a field is unknown, leave it blank or add it to `Open Questions`.
