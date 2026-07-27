# Brand Knowledge — Winn Foods

> Living brand memory for Codex and Strique SEO work. Read this file before producing Winn Foods output; it overrides generic assumptions.
> Structured facts live in `brand-dna.json`. Add dated entries here and preserve history.

---

## Product & Positioning

- (2026-07-27) Winn Foods presents itself as an Indian packaged-food brand for fast, flavorful Indo-Chinese cooking at home.
- (2026-07-27) Current public catalog families observed: sauces and chutneys, dish-specific Chinese masalas / instant cooking mixes, Hakka noodles, instant soups, and combo deals.
- (2026-07-27) Lead promise observed on the homepage: **“Turn Every Meal Into Chinese Magic”** and **“Authentic Indo-Chinese Taste at Home.”**
- (2026-07-27) Core product job: help a home cook reach a recognizable restaurant- or street-style result quickly, often by stirring in a ready sauce or measured masala.
- (2026-07-27) Storefront runs on Shopify, prices in INR, promotes a first-order offer, and uses a free-shipping threshold. Treat promotional values as time-sensitive and re-check before publishing.

## Voice — How Winn Writes

- (2026-07-27) Voice is playful, high-energy, sensory, and easy to understand. It sells flavor and simplicity before technical detail.
- (2026-07-27) Common structure: appetite cue → familiar dish/result → speed/ease → usage occasions → purchase CTA.
- (2026-07-27) Use vivid but recognizable food words: **bold, spicy, tangy, fiery, rich, fresh, aromatic, street-style, restaurant-style**.
- (2026-07-27) Use short transformation lines and imperatives: **bring home**, **turn every meal**, **simply stir it in**, **elevate your noodles**.
- (2026-07-27) Product naming embraces wordplay and Indian flavor: **Mirchilli, Sirkedar, Shandar, Chattak, Peppy, Fiery, Hotshot, OMG**.
- (2026-07-27) Copy often anchors the flavor to specific dishes and occasions—momos, fried rice, noodles, soups, stir-fries, samosas, lunch, dinner, or evening snacks.
- (2026-07-27) For blogs/recipes, retain the brand's approachable kitchen-helper tone. Put the dish and craving first, explain what Winn product reduces effort, then give concrete method and serving ideas.

## Messaging Do / Don't

- **Do:** lead with a dish, craving, or meal outcome; be specific about preparation time only when the source supports it; name the exact product; include practical uses; keep sentences energetic and accessible.
- **Do:** use playful language selectively, especially in headlines and transitions, while keeping recipe steps unambiguous.
- **Do:** distinguish a product-specific clean-label or ingredient claim from a brand-wide claim.
- **Don't:** invent nutrition benefits, health outcomes, heritage, awards, manufacturing standards, customer counts, or distribution reach.
- **Don't:** call every product “healthy,” “natural,” “preservative-free,” or “MSG-free” without product-level evidence.
- **Don't:** drift into generic gourmet prose, chef jargon, or corporate FMCG language that loses the friendly home-cooking feel.
- **Don't:** reuse live promotional prices, coupons, or shipping thresholds without re-checking the storefront.

## Visual System

- (2026-07-27) Firecrawl branding extraction observed primary red `#C81E2B`, secondary red `#D32F2F`, white background, black body text, Poppins headings, Inter body copy, and rounded red purchase buttons.
- (2026-07-27) Use bold food imagery, obvious product packs, high contrast, and direct retail CTAs. Reconfirm assets/tokens against current design files before production design.
- (2026-07-27) Logo source observed: `https://winn-foods.com/cdn/shop/files/Winn-Logo-White-Png_1.png?v=1766404569&width=110`.

## Mimu — Brand Mascot

- (2026-07-27) Mimu is Winn Foods' panda mascot. Official campaign artwork shows a black-and-white panda wearing a gold chain with a large `MIMU` pendant against Winn's red stage backdrop.
- (2026-07-27) A first-party post dated 2025-12-16 used Mimu in Winn's `Hello I am MIMU` / `Souper Tasty` reel campaign.
- (2026-07-27) First-party July 2026 posts place Mimu alongside the Winn soup range and use the character to celebrate Winn's arrival at six D-Mart stores in Chhattisgarh.
- (2026-07-27) The live homepage uses `winn_mimu_banner_v1.1.jpg` with alt text `Winn Foods Mimu Banner`; the banner links directly to `/collections/soup-range`.
- (2026-07-27) Winn's site search returns zero results for `Mimu`, and the mapped site has no dedicated Mimu biography or article. The proposed Mimu blog should become the canonical indexable character introduction and receive a link from the homepage banner or nearby copy.
- (2026-07-27) No reviewed first-party source provides an approved origin story, age, place of origin, dialogue style, or full character biography. Do not invent these details; request a brand character guide before expanding Mimu's lore.
- Evidence: `logs/content/raw/20260727T084900Z-mimu-first-party-social-evidence.json` and `logs/content/raw/20260727T085500Z-mimu-website-evidence.json`.

## SEO & Content Operating Rules

- (2026-07-27) Existing recipe content is stored in `blogs/references/`; consult it before planning a new recipe to avoid dish and keyword duplication.
- (2026-07-27) First-party product and recipe pages are authoritative for ingredients, preparation, use cases, and claims. Secondary press may provide corporate context but must not override the site.
- (2026-07-27) The storefront includes `/agents.md` and Universal Commerce Protocol discovery, indicating agent-commerce support. Preserve this as a technical capability, not a consumer-facing brand claim unless relevant.
- (2026-07-27) Shopify is confirmed.
- (2026-07-27) Google Search Console is connected through Composio for `sc-domain:winn-foods.com` with `siteRestrictedUser` permission. Use it for query/page performance and sitemap evidence, but do not treat Search Analytics as complete indexation coverage.
- (2026-07-27) Google Analytics 4 is connected through Composio for Winn Foods property `properties/533748438` (INR, Asia/Calcutta). Confirm key-event and ecommerce definitions before interpreting outcomes.
- (2026-07-27) GSC data contains unrelated gambling queries and `/food-services/` traffic; GA4 also exposes legacy/anomalous paths such as `/wp-login.php`, apparel collections, and malformed product paths. Treat aggregate totals as contaminated until compromise, historical migration, and indexing-spam causes are investigated.
- (2026-07-27) PageSpeed/CrUX and Lighthouse could not run during setup, so no field or lab performance claim is approved.

## Evidence & Provenance

- Foundational crawl: `run_id=winn-foods-setup-20260727`, `logs/web_data/raw/20260727T072346Z-brand-dna-crawl.json`.
- Homepage visual identity: `logs/web_data/raw/20260727T072449Z-homepage-branding.json`.
- Secondary company/category context: `logs/web_data/raw/20260727T072437Z-market-context-search.json`.
- Connected GSC and GA4 evidence: `logs/audits/raw/20260727T073600Z-connected-data-evidence.json`.
- Full audit findings: `audits/summary.json` and `audits/summary.md`.

## Open Questions / Approval Needed

- Legal parent and approved corporate history after reported 2026 Adinova rebrand.
- Product-level substantiation for nutrition, ingredient, and clean-label claims.
- Priority geographies, retail channels, and customer segments.
- Approved competitor set and differentiation.
- GA4 conversion-event, key-event, and ecommerce KPI definitions.
- Root cause and remediation owner for unrelated gambling queries and anomalous/legacy URLs.
- Canonical design files, packaging assets, and high-resolution logo.

## Change Log

- **2026-07-27** — Added first-party Mimu mascot facts and character guardrails from three Winn Foods social posts.
- **2026-07-27** — Workspace initialized from a 35-page Firecrawl crawl, homepage branding extraction, and external category/company search.
