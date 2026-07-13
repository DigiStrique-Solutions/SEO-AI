# Blog Article Completeness Checklist

Updated: 2026-07-09

Use this checklist when briefing, drafting, validating, or publishing a blog article. It sits on top of the content SEO checklist and turns the HubSpot-style blog anatomy into explicit pass or fail checks.

## Evidence Source Legend

- `Markdown`: draft frontmatter and body.
- `Authenticity log`: source and claim evidence recorded before publishing.
- `Brief`: content brief, SERP notes, keyword intent, and FAQ requirement.
- `Playwright`: rendered post-publish verification for live pages.
- `Human/context`: editorial judgment, product facts, customer notes, and expert review.

## 1. Frontmatter And SERP Promise

Evidence sources: `Markdown`, `Brief`, `Authenticity log`.

- [ ] The draft has `title`, `meta_description`, `slug`, `primary_keyword`, and `intent` frontmatter.
- [ ] The title, H1, meta description, and slug make the same promise.
- [ ] The slug is lowercase, hyphenated, readable, and stable.
- [ ] The primary keyword in frontmatter matches the requested blog keyword.
- [ ] The meta description is specific, honest, and not stuffed with keywords.

## 2. Trust And Editorial Identity

Evidence sources: `Markdown`, `Human/context`.

- [ ] The draft has `author` frontmatter.
- [ ] The draft has `updated_at` frontmatter.
- [ ] The update date reflects a meaningful content state, not fake freshness.
- [ ] Expert, reviewer, or editor context is included when the topic requires trust.

## 3. Above-The-Fold Usefulness

Evidence sources: `Markdown`, `Brief`.

- [ ] The body has exactly one H1.
- [ ] The opening section answers the main query without generic setup.
- [ ] The draft includes `## TLDR` or `## Quick Answer` near the top.
- [ ] The draft avoids broad filler before the useful answer.

## 4. Structure And Navigation

Evidence sources: `Markdown`.

- [ ] H2 and H3 headings form a logical outline.
- [ ] A `## Table of Contents` section with anchor links exists when the article has four or more H2 sections.
- [ ] The table of contents links match real sections.
- [ ] Long sections are broken with lists, examples, tables, or short paragraphs.
- [ ] Paragraphs stay readable on mobile.

## 5. Media And Explanation Assets

Evidence sources: `Markdown`, `Human/context`.

- [ ] The draft has `hero_image` frontmatter.
- [ ] The draft has `hero_image_alt` frontmatter.
- [ ] Images, tables, video, screenshots, or examples help the reader understand the topic.
- [ ] Informative images have useful alt text.
- [ ] Media claims are backed by source evidence when they show products, results, rankings, or comparisons.

## 6. Source Evidence And Claims

Evidence sources: `Authenticity log`, `Markdown`.

- [ ] The authenticity log has at least one concrete source.
- [ ] Product, ranking, comparison, price, performance, comfort, material, and customer claims are backed by source evidence.
- [ ] `best`, `top`, `leading`, and superiority claims have explicit claim records.
- [ ] External citations point to useful sources when public evidence is needed.
- [ ] Missing evidence is labeled as a blocker, not smoothed over in copy.

## 7. Internal Discovery

Evidence sources: `Markdown`, `Brief`, `Playwright`.

- [ ] The article links to at least one relevant internal page.
- [ ] Internal links use descriptive anchor text.
- [ ] The article links to relevant parent, child, sibling, product, offer, or support pages.
- [ ] The article includes a `## Related Reading` section with useful links.
- [ ] Related links are topical, not random archive filler.

## 8. Conversion Path

Evidence sources: `Markdown`, `Brief`, `Human/context`.

- [ ] The draft has `cta` frontmatter.
- [ ] The article includes a `## Next Step` section.
- [ ] The CTA or lead magnet fits the reader stage and article intent.
- [ ] The CTA does not interrupt before the article earns the ask.

## 9. FAQ Decision

Evidence sources: `Brief`, `Markdown`.

- [ ] A `## FAQ` section exists when the brief, SERP notes, or People Also Ask research says FAQ is useful.
- [ ] FAQ answers are short, source-backed, and not duplicated from the main body.
- [ ] FAQ is skipped when it would only add filler.

## 10. Schema And Publishing Metadata

Evidence sources: `Markdown`, `Playwright`.

- [ ] The draft has `article_schema: true` frontmatter.
- [ ] The draft has `breadcrumb_schema: true` frontmatter.
- [ ] Article schema fields match visible title, author, update date, and hero image.
- [ ] Breadcrumb schema matches visible breadcrumb hierarchy after publishing.
- [ ] Post-publish rendered checks use `collect-site-evidence` and `run-site-checks`.
