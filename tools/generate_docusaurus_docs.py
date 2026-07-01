#!/usr/bin/env python3
"""Generate Docusaurus docs from the current Strique SEO AI sources."""

import argparse
import csv
import importlib.util
import re
import subprocess
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
HARNESS_PATH = ROOT / "tools" / "seo_audit_harness.py"

CHECKLIST_PATHS = sorted((DOCS / "checklists").glob("*.md"))
COMMANDS = [
    "compile-checklists",
    "init-audit",
    "verify-audit",
    "summarize-audit",
    "init-authenticity",
    "verify-authenticity",
    "write-content",
    "firecrawl-scrape",
    "generate-keywords",
    "verify-keywords",
    "collect-evidence",
    "crawl-site",
    "collect-site-evidence",
    "run-site-checks",
    "resolve-google-visible-audit",
    "resolve-google-visible-audits",
    "route-evidence",
    "record-source-evidence",
    "record-evidence",
]

COMMAND_PURPOSES = {
    "compile-checklists": "Compile Markdown checklist items into stable JSON rows for audits.",
    "init-audit": "Create an audit matrix for a target URL from compiled checklists.",
    "verify-audit": "Validate audit matrix completeness, statuses, and evidence requirements.",
    "summarize-audit": "Summarize audit coverage and unresolved findings after evidence is recorded.",
    "init-authenticity": "Create a source and claim log before publishing SEO content.",
    "verify-authenticity": "Check whether a rewrite has enough source evidence and claim support.",
    "write-content": "Write publishable content only when the authenticity gate passes.",
    "firecrawl-scrape": "Collect public page evidence through Firecrawl when configured.",
    "generate-keywords": "Build or update keyword tracker rows from available demand evidence.",
    "verify-keywords": "Validate keyword tracker and keyword universe quality.",
    "collect-evidence": "Collect page-level evidence for a brand URL.",
    "crawl-site": "Crawl public site URLs into a brand workspace.",
    "collect-site-evidence": "Collect evidence across site inventory rows.",
    "run-site-checks": "Create site-level checks from crawl and evidence artifacts.",
    "resolve-google-visible-audit": "Resolve audit rows that can be checked through Google-visible evidence.",
    "resolve-google-visible-audits": "Resolve Google-visible rows across multiple audit files.",
    "route-evidence": "Map checklist items to required logical and concrete evidence sources.",
    "record-source-evidence": "Record a source-level evidence note against an audit item.",
    "record-evidence": "Record status, result, artifact, and next action for an audit item.",
}


def load_harness():
    spec = importlib.util.spec_from_file_location("seo_audit_harness", HARNESS_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def mdx_escape(text):
    return (
        text.replace("\\", "\\\\")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
    )


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def title_from_slug(slug):
    return " ".join(part.capitalize() for part in slug.replace("-", " ").split())


def repo_path(path):
    path = Path(path)
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def checklist_name(path):
    return path.stem.replace("-checklist", "")


def has_term(text, term):
    if re.fullmatch(r"[a-z0-9]+", term):
        return re.search(rf"\b{re.escape(term)}\b", text) is not None
    return term in text


def has_any(text, terms):
    return any(has_term(text, term) for term in terms)


def parse_required_sources(text):
    tokens = re.findall(r"`([^`]+)`", text)
    if tokens:
        return [token.strip().rstrip(".") for token in tokens if token.strip()]
    return [part.strip().rstrip(".") for part in text.split(",") if part.strip()]


def command_help(command):
    result = subprocess.run(
        ["python3", str(HARNESS_PATH), command, "--help"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def list_files(pattern):
    return sorted(str(path.relative_to(ROOT)) for path in ROOT.glob(pattern))


def infer_topics(text, checklist_id):
    lower = text.lower()
    topics = []
    primary_topics = {
        "ai-seo-aeo-geo": "AI answer visibility",
        "content-seo": "content quality and trust",
        "ecommerce-seo": "ecommerce eligibility",
        "generic-on-page-seo": "search intent and relevance",
        "local-seo": "local visibility",
        "off-page-seo": "off-page authority",
        "site-architecture-seo": "internal links and architecture",
    }
    checks = [
        ("crawlability and indexing", ("crawl", "index", "robots", "sitemap", "canonical", "noindex", "redirect", "status code")),
        ("search intent and relevance", ("intent", "query", "keyword", "audience", "purpose", "topic", "serp")),
        ("metadata and snippets", ("title", "meta description", "snippet", "h1", "heading", "schema", "structured data")),
        ("content quality and trust", ("helpful", "evidence", "author", "expert", "trust", "review", "claim", "original", "fresh")),
        ("internal links and architecture", ("internal link", "navigation", "breadcrumb", "taxonomy", "orphan", "depth", "hub")),
        ("page experience", ("mobile", "core web vitals", "lcp", "cls", "inp", "speed", "accessibility", "render")),
        ("ecommerce eligibility", ("product", "price", "availability", "variant", "shipping", "return", "merchant", "feed", "collection")),
        ("local visibility", ("local", "gbp", "maps", "address", "phone", "hours", "category", "review")),
        ("off-page authority", ("backlink", "mention", "citation", "partner", "pr", "directory", "referral")),
        ("AI answer visibility", ("ai", "prompt", "citation", "answer engine", "chatgpt", "perplexity", "copilot", "gemini")),
        ("measurement", ("gsc", "ga4", "analytics", "conversion", "traffic", "report", "performance")),
        ("policy and risk", ("spam", "manual action", "policy", "ymyl", "compliance", "security", "risk")),
    ]
    for topic, needles in checks:
        if has_any(lower, needles):
            topics.append(topic)
    primary_topic = primary_topics.get(checklist_id)
    if primary_topic and primary_topic not in topics:
        topics.insert(0, primary_topic)
    if not topics:
        topics.append("SEO quality")
    return topics


def owner_for_item(text, checklist_id):
    lower = text.lower()
    if checklist_id == "ecommerce-seo" or has_any(lower, ("product", "price", "availability", "feed", "merchant", "variant", "shipping", "return", "returns")):
        return "merchandising, marketing, or engineering"
    if has_any(lower, ("schema", "canonical", "robots", "sitemap", "javascript", "render", "speed", "core web vitals", "redirect", "status code")):
        return "engineering"
    if has_any(lower, ("ga4", "analytics", "gsc", "report", "tracking", "conversion", "event")):
        return "analytics"
    if has_any(lower, ("gbp", "maps", "hours", "address", "phone", "local profile", "review", "reviews")):
        return "local ops or admin"
    if checklist_id == "off-page-seo" or has_any(lower, ("backlink", "partner", "pr", "citation", "directory", "mention")):
        return "marketing or partnerships"
    return "content or marketing"


def evidence_for_item(item):
    lower = item["item_text"].lower()
    checklist_id = item["checklist_id"]
    sources = []
    required = item.get("required_evidence", "")
    if required:
        sources.extend(parse_required_sources(required))
    if has_any(lower, ("crawl", "canonical", "title", "meta", "heading", "link", "links", "image", "images", "schema")):
        sources.extend(["Firecrawl", "Playwright"])
    if has_any(lower, ("index", "query", "traffic", "click", "impression", "sitemap", "search appearance")):
        sources.append("GSC")
    if has_any(lower, ("conversion", "engagement", "revenue", "lead", "session")):
        sources.append("GA4 or PostHog")
    if has_any(lower, ("speed", "core web vitals", "lcp", "cls", "inp", "mobile")):
        sources.extend(["Lighthouse", "PageSpeed", "CrUX", "Playwright"])
    if checklist_id == "ecommerce-seo" or has_any(lower, ("product", "price", "availability", "merchant", "feed", "shipping", "return", "returns", "variant")):
        sources.extend(["Shopify or CMS", "GMC", "Firecrawl", "Playwright"])
    if checklist_id == "local-seo" or has_any(lower, ("local", "gbp", "maps", "hours", "address", "phone", "review", "reviews")):
        sources.extend(["GBP", "Google Maps", "GSC", "GA4"])
    if checklist_id == "off-page-seo" or has_any(lower, ("backlink", "mention", "citation", "directory", "partner", "review", "reviews")):
        sources.extend(["GSC Links", "Bing Webmaster Tools", "manual SERP", "Firecrawl"])
    if checklist_id == "ai-seo-aeo-geo" or has_any(lower, ("ai", "prompt", "citation", "answer engine", "chatgpt", "perplexity", "copilot", "gemini")):
        sources.extend(["saved prompt set", "manual AI SERP", "GSC", "Firecrawl"])
    if not sources:
        sources.extend(["Firecrawl", "Playwright", "GSC", "human context when needed"])
    deduped = []
    for source in sources:
        if source and source not in deduped:
            deduped.append(source)
    return deduped


def impact_for_item(item):
    topics = infer_topics(item["item_text"], item["checklist_id"])
    impact_map = {
        "crawlability and indexing": "Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.",
        "search intent and relevance": "Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.",
        "metadata and snippets": "Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries.",
        "content quality and trust": "Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions.",
        "internal links and architecture": "Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.",
        "page experience": "Mobile rendering, accessibility, and performance influence user success and can affect search quality signals, crawl efficiency, and conversion quality.",
        "ecommerce eligibility": "Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.",
        "local visibility": "Local SEO depends on accurate entity, location, category, review, and profile data. Inconsistency can weaken relevance, prominence, and customer trust.",
        "off-page authority": "External mentions, links, reviews, and citations help establish reputation and discovery beyond the site. Risky patterns can create spam or compliance exposure.",
        "AI answer visibility": "Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.",
        "measurement": "SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.",
        "policy and risk": "Policy, spam, and compliance issues can block visibility or create legal and reputation risk. This check catches issues before optimization work amplifies them.",
        "SEO quality": "This check supports SEO quality by making the page easier to understand, verify, prioritize, or improve.",
    }
    return " ".join(impact_map.get(topic, impact_map["SEO quality"]) for topic in topics[:2])


def meaning_for_item(item):
    text = item["item_text"].rstrip(".")
    return (
        "Confirm whether the audited scope satisfies this requirement: "
        f"\"{mdx_escape(text)}.\" In practice, this means the reviewer needs concrete evidence, not a general impression."
    )


def verification_steps(item, sources):
    lower = item["item_text"].lower()
    steps = [
        "Identify the exact URL, template, brand workspace, connector account, or page group in scope.",
        f"Collect evidence from: {', '.join(sources)}.",
    ]
    if has_any(lower, ("render", "mobile", "javascript", "hidden", "schema", "link", "links", "image", "images", "navigation")):
        steps.append("Use browser-rendered evidence before claiming the item is absent or broken.")
    if has_any(lower, ("gsc", "query", "index", "click", "impression", "sitemap")):
        steps.append("Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.")
    if has_any(lower, ("ga4", "conversion", "revenue", "lead", "engagement")):
        steps.append("Use analytics data only when the property, date range, and conversion definitions are known.")
    if has_any(lower, ("product", "price", "availability", "merchant", "feed", "shipping", "return", "returns", "variant")):
        steps.append("Compare visible page content, structured data, and feed or platform values for consistency.")
    if has_any(lower, ("ai", "prompt", "citation", "answer engine")):
        steps.append("Record prompt wording, platform, location, date, account state, cited URLs, and answer summary.")
    steps.append("Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.")
    return steps


def common_fix(item, owner):
    lower = item["item_text"].lower()
    if has_any(lower, ("product", "price", "availability", "variant", "shipping", "return", "returns", "merchant", "feed")):
        return "Fix the product source of truth, page template, schema, or feed mapping so product data is complete and consistent."
    if has_any(lower, ("canonical", "robots", "sitemap", "redirect", "status code", "schema", "javascript", "render")):
        return "Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks."
    if has_any(lower, ("title", "meta description", "heading", "h1", "content", "answer", "intent", "keyword")):
        return "Rewrite the affected copy or page structure so the primary intent, answer, and next step are clear and evidence-backed."
    if has_any(lower, ("internal link", "navigation", "breadcrumb", "taxonomy", "orphan")):
        return "Adjust navigation, breadcrumbs, contextual links, or taxonomy so priority pages are reachable and clearly related."
    if has_any(lower, ("gbp", "maps", "local", "hours", "address", "phone", "review", "reviews")):
        return "Update the business profile, location page, local schema, citations, or review workflow, then verify the live surface."
    if has_any(lower, ("backlink", "mention", "citation", "partner", "directory", "pr")):
        return "Prioritize legitimate relationship, PR, citation, or partner updates and avoid manipulative link tactics."
    if has_any(lower, ("ga4", "analytics", "gsc", "report", "tracking")):
        return "Fix the data source, property scoping, export, tagging, or report definition before using the metric for decisions."
    return f"Have {owner} make the smallest change that satisfies the evidence requirement, then rerun the check."


def render_item_entry(index, item):
    sources = evidence_for_item(item)
    owner = owner_for_item(item["item_text"], item["checklist_id"])
    steps = "\n".join(f"{step_index}. {mdx_escape(step)}" for step_index, step in enumerate(verification_steps(item, sources), 1))
    source_text = ", ".join(mdx_escape(source) for source in sources)
    return f"""
## Item {index}

Item ID: `{item["item_id"]}`

Original checklist item: {mdx_escape(item["item_text"])}

### What It Means

{meaning_for_item(item)}

### Why It Affects SEO

{impact_for_item(item)}

### How To Verify

{steps}

### Evidence Sources

{source_text}

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

{mdx_escape(common_fix(item, owner))}

### Owner

{mdx_escape(owner)}

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.
""".strip()


def generate_start_docs(checklists):
    checklist_rows = []
    total_sections = 0
    total_items = 0
    for checklist in checklists:
        checklist_rows.append(
            f"| `{repo_path(checklist['path'])}` | {len(checklist['sections'])} | {len(checklist['items'])} |"
        )
        total_sections += len(checklist["sections"])
        total_items += len(checklist["items"])

    write(
        DOCS / "start" / "repository-map.md",
        f"""---
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
| `brands/` | Brand workspaces, crawls, evidence, exports, and audit outputs. | Restricted by default |
| `tmp/` | Ignored temporary reports and scratch artifacts. | Not published |

Current checklist coverage:

| Checklist | Sections | Items |
| --- | ---: | ---: |
{chr(10).join(checklist_rows)}
| **Total** | **{total_sections}** | **{total_items}** |

Do not publish `brands/` wholesale. It can contain customer context, screenshots, raw connector payloads, and evidence artifacts.
""",
    )

    workflow_files = "\n".join(f"- `{path}`" for path in list_files("docs/workflows/*.md"))
    checklist_files = "\n".join(f"- `{path}`" for path in list_files("docs/checklists/*.md"))
    schema_files = "\n".join(f"- `{path}`" for path in list_files("docs/schemas/*.json"))
    skill_files = "\n".join(f"- `{path}`" for path in list_files(".agents/skills/*/SKILL.md"))
    write(
        DOCS / "start" / "source-inventory.md",
        f"""---
title: Source Inventory
sidebar_position: 2
---

# Source Inventory

The docs should describe these sources as they exist today.

## Built Source

- `tools/seo_audit_harness.py`
- `tests/test_seo_audit_harness.py`

## Workflow Docs

{workflow_files}

## Checklist Docs

{checklist_files}

## Schemas

{schema_files}

## Local Skills

{skill_files or "- No local skills found."}

## Brand Workspace Examples

- `brands/_template/`
- `brands/strique/`
- `brands/inc5/`
- `brands/kaya-clinic/`
- `brands/crimzon/`
- `brands/digimaze/`

Brand workspaces are examples of the data shape, not public docs content by default.
""",
    )

    write(
        DOCS / "start" / "implementation-status.md",
        """---
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
""",
    )

    write(
        DOCS / "start" / "publishability-classification.md",
        """---
title: Publishability Classification
sidebar_position: 4
---

# Publishability Classification

## Public-Safe After Review

- Generic workflow docs.
- Generic checklist docs.
- Harness command reference.
- Schema descriptions.
- High-level connector category docs.
- Checklist encyclopedia entries that do not include customer evidence.

## Internal Only

- Agent prompt contracts.
- MCP policy details.
- Skill loading policy.
- Brand workspace operating procedures.
- Implementation status for planned runtime contracts.

## Restricted By Default

- `brands/*/references/evidence/`
- `brands/*/references/crawls/`
- Raw connector responses.
- Screenshots from audits.
- Customer, sales, support, or CRM notes.
- Credentials, tokens, API keys, and private account IDs.

## Rule

Publish generic methods, contracts, and examples. Do not publish raw brand evidence unless it has explicit review and approval.
""",
    )


def generate_harness_docs():
    command_sections = []
    for index, command in enumerate(COMMANDS, 1):
        help_text = command_help(command)
        command_sections.append(
            f"""## {command}

Purpose: {COMMAND_PURPOSES[command]}

```text
{help_text}
```
"""
        )

    write(
        DOCS / "harness" / "overview.md",
        """---
title: Harness Overview
sidebar_position: 1
---

# Harness Overview

`tools/seo_audit_harness.py` is the local CLI for Strique SEO audit work. It turns Markdown checklists into stable audit rows, collects evidence, verifies audit coverage, records source-backed content authenticity, and keeps brand workspace outputs in predictable files.

## Core Flows

1. Compile Markdown checklists.
2. Initialize an audit matrix.
3. Collect or attach evidence.
4. Record `pass`, `fail`, `not_applicable`, or `not_checked_blocked`.
5. Verify before summarizing.
6. Generate tasks or content only after the relevant gate passes.

## Full Audit Rule

A full audit is only complete when every relevant row is `pass`, `fail`, or `not_applicable`. If any row is `not_checked_blocked`, call it a partial audit and name the missing access, data, or tool.

## Content Authenticity Rule

Publish-ready content needs concrete source evidence. AI detector scores are weak editorial signals and never replace source-backed claims.
""",
    )

    write(
        DOCS / "harness" / "command-reference.md",
        f"""---
title: Command Reference
sidebar_position: 2
---

# Command Reference

These command sections are generated from the current CLI help. The harness file is the source of truth.

{chr(10).join(command_sections)}
""",
    )

    write(
        DOCS / "harness" / "audit-matrix-lifecycle.md",
        """---
title: Audit Matrix Lifecycle
sidebar_position: 3
---

# Audit Matrix Lifecycle

## 1. Compile Checklists

```bash
python3 tools/seo_audit_harness.py compile-checklists --output brands/inc5/exports/checklists.json
```

The compiler reads Markdown checklist rows and emits stable item IDs. Item IDs use the checklist ID, section ID, and item text hash.

## 2. Initialize The Matrix

```bash
python3 tools/seo_audit_harness.py init-audit --compiled brands/inc5/exports/checklists.json --url https://example.com/page --audit-type partial --output brands/inc5/audits/page-audit-matrix.json
```

Start as `partial` unless every required evidence source is available.

## 3. Record Evidence

Each row needs:

- `status`
- `evidence_source`
- `artifact_ref`
- `result`
- `blocker`
- `next_action`

## 4. Verify

```bash
python3 tools/seo_audit_harness.py verify-audit --compiled brands/inc5/exports/checklists.json --audit brands/inc5/audits/page-audit-matrix.json
```

## Status Values

- `pass`: verified with evidence.
- `fail`: verified issue with evidence and next action.
- `not_applicable`: not relevant, with a reason in `result`.
- `not_checked_blocked`: could not be checked, with `blocker` and `next_action`.

## Exit Rule

Do not call the result a full audit while any row is blocked.
""",
    )

    write(
        DOCS / "harness" / "content-authenticity-lifecycle.md",
        """---
title: Content Authenticity Lifecycle
sidebar_position: 4
---

# Content Authenticity Lifecycle

Use this flow before publishing customer-facing SEO content.

## 1. Initialize The Source Log

```bash
python3 tools/seo_audit_harness.py init-authenticity --target brands/inc5/blogs/drafts/example.md --output brands/inc5/references/example-authenticity.json
```

## 2. Add Concrete Sources

Useful source types include:

- product pages
- brand DNA
- GSC
- GA4
- Shopify
- Merchant Center
- reviews
- customer notes
- merchandiser notes
- SERP observations
- competitor pages
- human context

## 3. Gate Sensitive Claims

Claims such as `best`, `top`, `leading`, superiority, customer proof, performance claims, and comparisons need source evidence.

## 4. Verify Or Write

```bash
python3 tools/seo_audit_harness.py verify-authenticity --authenticity brands/inc5/references/example-authenticity.json --rewrite-file brands/inc5/blogs/drafts/example.md
```

Use `write-content` when the output file should be written only after the gate passes.

## Detector Notes

Record AI detector output only as weak editorial signal in `detector_notes`. Do not treat it as plagiarism proof or authorship proof.
""",
    )

    write(
        DOCS / "harness" / "evidence-collection.md",
        """---
title: Evidence Collection
sidebar_position: 5
---

# Evidence Collection

Evidence should be specific enough to support an audit row.

## Public Crawl Evidence

- Firecrawl markdown, HTML, raw HTML, links, images, and screenshots.
- Public HTTP status, canonical, robots, sitemap, and headers.

## Rendered Browser Evidence

- Playwright DOM checks.
- Desktop and mobile screenshots.
- JavaScript-rendered content.
- Hidden content and interactive states.
- Accessibility tree when relevant.

## Performance Evidence

- Lighthouse lab data.
- PageSpeed Insights.
- CrUX field data when available.

## Connected Platform Evidence

- GSC for queries, pages, indexing, sitemaps, search appearance, and links.
- GA4 or PostHog for traffic, engagement, conversions, funnels, and revenue.
- Shopify or CMS for product, page, template, and source-of-truth data.
- GMC for product feed, shipping, returns, availability, and merchant listing diagnostics.
- GBP and Maps for local profile, reviews, photos, categories, services, and hours.

If access is missing, mark the exact item as `not_checked_blocked`.
""",
    )

    write(
        DOCS / "harness" / "keyword-workflow.md",
        """---
title: Keyword Workflow
sidebar_position: 6
---

# Keyword Workflow

The harness tracks keyword evidence in brand workspaces.

## Files

- `keywords/keywords.csv`: prioritized working keyword list.
- `exports/keyword-universe.csv`: larger deduped keyword universe.
- `references/keyword-research-summary.json`: summary counts, blockers, and source notes.

## Fields

The tracker captures keyword, intent, page type, target URL, volume, difficulty, priority, source, status, and notes.

## Commands

Use `generate-keywords` to create or update keyword rows from available demand inputs. Use `verify-keywords` to check quality, coverage, and blockers.

Do not invent demand. If Keyword Planner, GSC, or other demand evidence is missing, record the blocker.
""",
    )

    write(
        DOCS / "harness" / "brand-workspace-paths.md",
        """---
title: Brand Workspace Paths
sidebar_position: 7
---

# Brand Workspace Paths

Each folder under `brands/` is one brand workspace.

| Path | Use |
| --- | --- |
| `brand-dna.md` | Stable brand context for SEO work. |
| `keywords/keywords.csv` | Prioritized keyword tracker. |
| `audits/audits.csv` | Audit findings and follow-ups. |
| `tasks/tasks.csv` | Tasks created from audits and content work. |
| `references/` | Crawl notes, source URLs, screenshots, exports, and evidence. |
| `references/evidence/<run-id>/` | Evidence artifacts collected for a run. |
| `references/crawls/<run-id>/` | Crawl artifacts collected for a run. |
| `exports/` | Shareable or importable outputs. |

Keep raw connector payloads and private evidence out of public docs.
""",
    )


def generate_agent_skill_connector_docs():
    write(
        DOCS / "agents" / "architecture.md",
        """---
title: Agent Architecture
sidebar_position: 1
---

# Agent Architecture

The Strique Orchestrator is the user-facing control plane. The SEO agent is a specialist invoked by the orchestrator, not a standalone chatbot.

```text
user request
  -> Strique Orchestrator
  -> run_sub_agent(agent_id="seo_agent", input=...)
  -> SEO specialist agent
  -> scoped skills, checklists, tools, brand context
  -> actionable Strique output
```

This repo currently documents the contract and local harness. Production runtime code should mirror Strique's existing ai-server pattern when added.
""",
    )

    write(
        DOCS / "agents" / "seo-agent-contract.md",
        """---
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

## Output Shape

SEO outputs should include summary, top findings, evidence, priority fixes, implementation notes, expected impact, and open questions.
""",
    )

    write(
        DOCS / "agents" / "prompt-contracts.md",
        """---
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
""",
    )

    write(
        DOCS / "agents" / "output-contract.md",
        """---
title: Output Contract
sidebar_position: 4
---

# Output Contract

SEO agent outputs should be actionable Strique work.

## Standard Shape

- Summary
- Top findings
- Evidence
- Priority fixes
- Implementation notes
- Expected impact
- Open questions

## Audit Fields

- Severity: `critical`, `high`, `medium`, `low`
- Evidence: URL, metric, crawl result, Search Console row, analytics row, or rendered-page observation
- Fix: concrete action
- Owner: content, engineering, marketing, analytics, admin, merchandising, local ops, or legal/compliance
- Confidence: high, medium, or low

If evidence is missing, say what is missing and do not invent it.
""",
    )

    write(
        DOCS / "skills" / "overview.md",
        """---
title: Skills Overview
sidebar_position: 1
---

# Skills Overview

Skills teach the agent how to think and execute. Checklists define what must be checked.

## Rules

- Keep third-party skills as Markdown instruction assets.
- Preserve skill frontmatter and version metadata.
- Load product marketing context before other SEO or content skills when available.
- Load full skill bodies only when the SEO agent decides the skill is relevant.
- Scope skill access by allowed directories or allowed IDs.
- Do not expose every skill to every agent.
""",
    )

    write(
        DOCS / "skills" / "content-seo-authenticity.md",
        """---
title: Content SEO Authenticity Skill
sidebar_position: 2
---

# Content SEO Authenticity Skill

Source file: `.agents/skills/content-seo-authenticity/SKILL.md`

Use this skill for SEO content that must be source-backed, brand-voice aligned, less likely to trigger detector concerns, and publish-ready.

## Non-Negotiables

- AI detector scores are weak editorial signals.
- Do not invent sources, proof, product details, rankings, reviews, or expert claims.
- Publish-ready content needs concrete evidence in the authenticity log.
- Unsupported `best`, `top`, superiority, comparison, and performance claims need source-backed claim rows.

## Output Shape

- Verdict
- Target URL
- Primary keyword
- Intent
- Evidence used
- Content SEO findings
- Authenticity risks
- Recommended edits
- Detector notes
- Next action
""",
    )

    write(
        DOCS / "tools-and-connectors" / "overview.md",
        """---
title: Tools And Connectors
sidebar_position: 1
---

# Tools And Connectors

Connectors provide evidence. They do not override Strique policy, user permissions, or audit verification rules.

| Category | SEO Evidence |
| --- | --- |
| Google Search Console | Queries, pages, indexing, sitemaps, search appearance, links, crawl stats. |
| Google Analytics | Landing page sessions, engagement, conversions, revenue, lead quality. |
| Shopify | Products, variants, collections, redirects, themes, feeds, metafields. |
| HubSpot or CRM | Lead quality, funnel context, customer fit, lifecycle stage. |
| Firecrawl | Public crawl, rendered extraction, metadata, links, images, screenshots. |
| Google Business Profile | Local profile data, reviews, photos, services, categories, performance. |
| Google Merchant Center | Feed health, products, prices, availability, shipping, returns, diagnostics. |
| Bing Webmaster Tools | Bing search performance, backlinks, crawl and index data. |
| Keyword Planner | Directional demand and keyword variants. |
| PostHog | Product behavior, funnels, events, and conversion paths. |

When access is missing, mark affected audit rows as `not_checked_blocked`.
""",
    )

    write(
        DOCS / "tools-and-connectors" / "mcp-policy.md",
        """---
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
""",
    )

    write(
        DOCS / "tools-and-connectors" / "evidence-sources.md",
        """---
title: Evidence Sources
sidebar_position: 3
---

# Evidence Sources

## Public Evidence

- Firecrawl
- Public HTTP
- Playwright
- Lighthouse
- PageSpeed
- CrUX
- Manual SERP review

## Connected Evidence

- GSC
- GA4
- Shopify
- GMC
- GBP
- Bing Webmaster Tools
- Keyword Planner
- PostHog
- CRM

## Human Context

Use human context for product facts, legal constraints, sales objections, support themes, merchandising notes, and editorial judgment. Label it clearly in the evidence row.
""",
    )


def generate_schema_and_brand_docs():
    write(
        DOCS / "schemas" / "overview.md",
        """---
title: Schemas Overview
sidebar_position: 1
---

# Schemas Overview

The repo contains JSON schemas for audit matrices and content authenticity logs.

## Files

- `docs/schemas/audit-matrix.schema.json`
- `docs/schemas/content-authenticity.schema.json`

Use these schemas to validate generated artifacts before claiming an audit or content gate has passed.
""",
    )

    write(
        DOCS / "brand-workspaces" / "overview.md",
        """---
title: Brand Workspaces
sidebar_position: 1
---

# Brand Workspaces

Each folder under `brands/` is one brand workspace. Use `brands/_template/` when starting a new brand.

## Standard Files

- `brand-dna.md`
- `keywords/keywords.csv`
- `audits/audits.csv`
- `tasks/tasks.csv`
- `docs/`
- `references/`
- `blogs/briefs/`
- `blogs/drafts/`
- `blogs/published/`
- `images/source/`
- `images/generated/`
- `exports/`

## Rules

- Keep trackers as CSV for Sheets and Git review.
- Keep raw connector payloads out of Brand DNA.
- Keep evidence close to the audit or task that depends on it.
- Do not store secrets, credentials, private customer data, or raw MCP tokens.
""",
    )


def generate_qa_docs():
    write(
        DOCS / "start" / "reader-paths.md",
        """---
title: Reader Paths
sidebar_position: 5
---

# Reader Paths

## I Need To Run A Full Audit

1. Read [Harness Overview](../harness/overview.md).
2. Follow [Audit Matrix Lifecycle](../harness/audit-matrix-lifecycle.md).
3. Use the [Checklist Encyclopedia](../checklist-encyclopedia/overview.md).
4. Verify before summarizing.

## I Need To Rewrite Content Safely

1. Read [Content Authenticity Lifecycle](../harness/content-authenticity-lifecycle.md).
2. Use the [Content SEO Authenticity Skill](../skills/content-seo-authenticity.md).
3. Record sources and claims before publishing.

## I Need To Understand A Checklist Item

1. Open [Checklist Encyclopedia](../checklist-encyclopedia/overview.md).
2. Choose the checklist and section.
3. Use the item ID when recording audit evidence.

## I Need To Add A Connector

1. Read [Tools And Connectors](../tools-and-connectors/overview.md).
2. Read [MCP Policy](../tools-and-connectors/mcp-policy.md).
3. Document scoping, blocked states, and high-risk actions before use.

## I Need To Add A Brand Workspace

1. Read [Brand Workspaces](../brand-workspaces/overview.md).
2. Start from `brands/_template/`.
3. Keep restricted evidence out of public docs.
""",
    )

    write(
        DOCS / "start" / "glossary.md",
        """---
title: Glossary
sidebar_position: 6
---

# Glossary

| Term | Meaning |
| --- | --- |
| Audit matrix | JSON rows representing every checklist item that must be checked. |
| Blocked row | An audit row marked `not_checked_blocked` because evidence or access is missing. |
| Brand DNA | Stable brand context used for SEO, audits, content, and image generation. |
| Checklist | Markdown source that defines what must be checked. |
| Connector | Scoped integration that provides evidence from an external platform. |
| Evidence source | Tool, connector, artifact, or human context used to support an audit row. |
| Full audit | Audit where every relevant row is `pass`, `fail`, or `not_applicable`. |
| MCP | Tool connection layer used for scoped external evidence and actions. |
| Skill | Markdown instruction asset that teaches the SEO agent how to think or execute. |
| Source log | Content authenticity artifact that records sources and claims before publishing. |
| Strique Orchestrator | User-facing control plane that invokes specialist agents. |
""",
    )

    write(
        DOCS / "start" / "release-checklist.md",
        """---
title: Release Checklist
sidebar_position: 7
---

# Release Checklist

## Required Checks

```bash
test -f AGENTS.md
sed -n '1,220p' AGENTS.md
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
```

## Privacy Checks

```bash
rg -i "api[_-]?key|secret|token|password|credential" docs .agents
rg -i "raw connector|customer data|private payload" docs
```

## Local URL Check

Before reporting a preview URL:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN
curl -I http://localhost:<port>/
```

## Release Notes Template

- What changed.
- Verification commands and results.
- Known gaps.
- Restricted artifacts excluded.
- Deployment target.
""",
    )


def generate_checklist_encyclopedia(harness):
    checklists = [harness.parse_checklist(path) for path in CHECKLIST_PATHS]
    base = DOCS / "checklist-encyclopedia"
    rows = []

    overview_rows = []
    for checklist in checklists:
        checklist_dir = base / checklist["checklist_id"]
        grouped = defaultdict(list)
        for item in checklist["items"]:
            grouped[item["section_id"]].append(item)

        section_links = []
        for section_index, section in enumerate(checklist["sections"], 1):
            section_id = section["section_id"]
            items = grouped.get(section_id, [])
            if not items:
                continue
            section_links.append(
                f"- [{mdx_escape(section['section_title'])}](./{section_id}.md): {len(items)} items"
            )
            entries = []
            for item_index, item in enumerate(items, 1):
                entries.append(render_item_entry(item_index, item))
                rows.append(
                    {
                        "checklist": checklist["checklist_id"],
                        "section": section_id,
                        "item_id": item["item_id"],
                        "item_text": item["item_text"],
                        "doc_path": str((checklist_dir / f"{section_id}.md").relative_to(ROOT)),
                        "status": "generated",
                    }
                )

            write(
                checklist_dir / f"{section_id}.md",
                f"""---
title: {mdx_escape(section['section_title'])}
sidebar_position: {section_index + 1}
---

# {mdx_escape(section['section_title'])}

Checklist: `{checklist["checklist_id"]}`

Source: `{repo_path(checklist["path"])}`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

{(chr(10) + chr(10)).join(entries)}
""",
            )

        overview_rows.append(
            f"| [{mdx_escape(checklist['title'])}](./{checklist['checklist_id']}/) | {len(checklist['sections'])} | {len(checklist['items'])} |"
        )

        write(
            checklist_dir / "index.md",
            f"""---
title: {mdx_escape(checklist['title'])}
sidebar_position: 1
---

# {mdx_escape(checklist['title'])}

Source: `{repo_path(checklist["path"])}`

Sections: {len(checklist["sections"])}

Items: {len(checklist["items"])}

## Sections

{chr(10).join(section_links)}
""",
        )

    write(
        base / "overview.md",
        f"""---
title: Checklist Encyclopedia
sidebar_position: 1
---

# Checklist Encyclopedia

The encyclopedia expands each checklist item into meaning, SEO impact, verification steps, evidence sources, pass criteria, fail criteria, common fix, owner, and blocked-state guidance.

| Checklist | Sections | Items |
| --- | ---: | ---: |
{chr(10).join(overview_rows)}

## Coverage

- Checklists: {len(checklists)}
- Sections: {sum(len(checklist["sections"]) for checklist in checklists)}
- Items: {sum(len(checklist["items"]) for checklist in checklists)}
- Entry status: generated first pass

Use the original checklist Markdown as the source of truth. Use these expanded docs to explain and execute each row.
""",
    )

    with open(base / "coverage-manifest.csv", "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["checklist", "section", "item_id", "item_text", "doc_path", "status"],
        )
        writer.writeheader()
        writer.writerows(rows)

    write(
        base / "coverage-summary.md",
        f"""---
title: Coverage Summary
sidebar_position: 2
---

# Coverage Summary

Generated checklist encyclopedia coverage:

- Checklists: {len(checklists)}
- Sections with items: {len(set((row["checklist"], row["section"]) for row in rows))}
- Items: {len(rows)}
- Manifest: `docs/checklist-encyclopedia/coverage-manifest.csv`

Every source checklist item currently has a generated encyclopedia entry. Review status should move from `generated` to `reviewed` as editors tighten the explanations.
""",
    )
    return checklists, rows


def validate_coverage(checklists, rows):
    source_count = sum(len(checklist["items"]) for checklist in checklists)
    if source_count != len(rows):
        raise SystemExit(f"coverage mismatch: source={source_count} generated={len(rows)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    harness = load_harness()
    checklists, rows = generate_checklist_encyclopedia(harness)
    validate_coverage(checklists, rows)
    if not args.validate_only:
        generate_start_docs(checklists)
        generate_harness_docs()
        generate_agent_skill_connector_docs()
        generate_schema_and_brand_docs()
        generate_qa_docs()
    print(f"generated {len(rows)} checklist encyclopedia entries")


if __name__ == "__main__":
    main()
