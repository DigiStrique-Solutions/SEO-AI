# Brand DNA Generation Workflow

Use this workflow when creating or refreshing a brand's `brand-dna.md`.

## Inputs

- Brand name.
- Website URL.
- Existing customer, sales, or product context if available.
- Connected Firecrawl or website crawl tool.

## Crawl Scope

Use Firecrawl to collect evidence from:

- Homepage.
- About page.
- Top navigation pages.
- Product, service, collection, or category pages.
- Blog, guide, case study, or resource pages that explain positioning.
- Contact, store, clinic, location, or support pages when relevant.
- Visible brand, press, policy, or trust pages.

Keep the crawl focused. Do not collect the whole site unless the brand is small enough that the crawl stays practical.

## Fill Rules

- Fill `brand-dna.md` only from observed website evidence or user-provided context.
- Mark inferred values in `Evidence Sources` or `Open Questions`.
- Do not invent competitors, target audiences, values, colors, or tone.
- Do not paste raw Firecrawl payloads into Brand DNA.
- Store short crawl notes, source URLs, screenshots, or exports in `references/`.
- Put original logos and source imagery in `images/source/`.
- Put AI-generated images only in `images/generated/`.

## Brand DNA Fields

- Name.
- Website URL.
- Logo.
- Business Description.
- Brand Colors.
- Brand Aesthetic.
- Brand Values.
- Tone of Voice.
- Competitors.
- Target Audience.
- Evidence Sources.
- Open Questions.

## Output

After filling the file, produce a short summary:

```text
Brand DNA updated:
- Sources reviewed:
- Strong evidence:
- Inferred fields:
- Open questions:
```

Do not claim the Brand DNA is final if important fields are inferred or missing.
