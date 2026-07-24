# Phase 3 — Existing Blogs

**Goal:** Discover and record the brand's already-published blogs (max 20): `blogs/summary.md` + `blogs/references/<slug>.md`.
**Tools:** `firecrawl` / `web` fetch.
**Depends on:** Phase 1 (website_url). Uses Phase 2 clusters for gap analysis (optional).

## Steps

1. **Locate the blog index** (try `/blog`, `/blogs`, `/resources`, `/insights`, sitemap). If none exists, this phase is a no-op — record 0 posts and continue.
2. **Discover posts** — list up to 20 (title, url, date, category). **Log** → `logs/blogs/activity.jsonl` (`fetch`) + raw index in `raw/`.
3. **Fetch each post** for: title, meta_description, published_date, category, primary_keyword, 3-5 key points, 2-sentence summary, and `voice_notes` (below). Log the batch fetch.
4. **Write one `references/<slug>.md` per post** — frontmatter (`title, slug, url, status: published, published_date, category, primary_keyword, fetched_at`) + summary + key points + `voice_notes` + a `Notes` section left open.
5. **Write `blogs/summary.md`** — index table (title, date, category, primary keyword, live link, reference link) + coverage notes (categories in use; topic gaps vs `keywords/clusters.json`).

## Storage rule

Store **summaries + metadata + links**, NOT full scraped article bodies (avoids republishing prose). Filenames = URL slug so a reference traces back to its post.

## `voice_notes` — the brand's voice corpus

These posts are the only record of how the brand *actually writes*, and the storage rule means the prose itself doesn't survive. Capture the style as **observations** instead — metadata, not prose, so the no-republish rule still holds:

```yaml
voice_notes:
  person: "second person, speaks directly to the reader"
  cadence: "short declaratives mixed with one long scene-setting sentence"
  opening_move: "opens on a concrete situation (a wet commute), not a definition"
  product_intro: "products arrive mid-section as the answer to a question already asked"
  vocabulary: "Tribe, push limits; names real tech (Athlite, Wiktech)"
  register: "gutsy, motivational; no luxury framing"
```

Record what you observe, not what `brand-dna.json` claims — a mismatch between the two is itself a finding worth noting. Keep it to a few lines per post; this is a style signal, not a summary.

Downstream, `content-seo-authenticity` reads these when building the voice contract (`references/brand-voice-contract.md`). Without them the writer has only `brand_voice.description` to go on, which is abstract enough that every brand ends up sounding the same.

## Checklist items

| id | check | severity | fail action |
|----|-------|:--------:|-------------|
| `p3.index` | Blog index located OR confirmed absent | medium | if absent, record 0 posts, continue |
| `p3.discovery` | Posts listed (≤ 20) with url + date | medium | continue with whatever was found |
| `p3.references` | One reference file per discovered post | medium | log per-post fetch failures; keep the rest |
| `p3.voice_notes` | `voice_notes` captured per reference | medium | if a post can't be read, leave the field out and note it; never invent a voice observation |
| `p3.summary` | `summary.md` index written, links resolve | low | continue |

## Failure handling

- Individual post fetch fails → skip that post, log `status:error` with its url, keep going. Note skipped count in `summary.md` coverage notes (no silent truncation).
- Cap at 20; if more exist, record the cap + total in `summary.md`.

**Next:** Phase 4 → `references/04-audits.md`.
