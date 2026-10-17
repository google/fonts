# Playwrite NZ — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository
- **URL**: https://github.com/TypeTogether/Playwrite
- **Commit**: fbc8d9790feeba3a5d0c0b4ccdcf246d3c41526e

## Findings
The METADATA.pb contained a source block pointing to the TypeTogether/Playwrite repository with a specific commit hash. This used a different commit than most other Playwrite families.

## Status
- **Category**: WITH_SOURCE

## Recent upstream/main activity (post-investigation)

Two commits on 2026-01-21 advanced this family to v1.004:

- **2026-01-21** — Emma Marichal, commit [`51c2bf9c5`](https://github.com/google/fonts/commit/51c2bf9c5) ("Playwrite NZ: Version 1.004 added"): version bump to 1.004 via gftools-packager. Updated `PlaywriteNZ[wght].ttf` (349396 → 368940 bytes), METADATA.pb, and article. Source block fields advanced to reflect the v1.004 upstream commit.
- **2026-01-21** — Marc Foley, commit [`e6f137049`](https://github.com/google/fonts/commit/e6f137049) ("remove all subsets apart from menu"): removed 3 subsets from METADATA.pb (post-onboarding cleanup; presumably to address a fontspector or QA finding). Outside the `source { ... }` block.
