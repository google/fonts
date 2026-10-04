# Playwrite NZ Guides — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository
- **URL**: https://github.com/TypeTogether/Playwrite
- **Commit**: fbc8d9790feeba3a5d0c0b4ccdcf246d3c41526e

## Findings
The METADATA.pb contained a source block pointing to the TypeTogether/Playwrite repository with a specific commit hash. This was the guides variant of the Playwrite New Zealand family.

## Status
- **Category**: WITH_SOURCE

## Recent upstream/main activity (post-investigation)

Two commits on 2026-01-21 advanced this family to v1.004:

- **2026-01-21** — Emma Marichal, commit [`ba7373c4b`](https://github.com/google/fonts/commit/ba7373c4b) ("Playwrite NZ Guides: Version 1.004 added"): version bump to 1.004 via gftools-packager. Updated `PlaywriteNZGuides-Regular.ttf` (368516 → 387680 bytes), METADATA.pb, article. Source block fields advanced.
- **2026-01-21** — Marc Foley, commit [`55aec06a9`](https://github.com/google/fonts/commit/55aec06a9) ("Remove all subsets apart from menu"): removed 3 subsets from METADATA.pb (post-onboarding cleanup). Outside the `source { ... }` block.
