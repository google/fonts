# Playwrite NZ Basic — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository
- **URL**: https://github.com/TypeTogether/Playwrite
- **Commit**: fbc8d9790feeba3a5d0c0b4ccdcf246d3c41526e

## Findings
The METADATA.pb contained a source block pointing to the TypeTogether/Playwrite repository with a specific commit hash. This used the same newer commit as the other NZ Playwrite variants.

## Status
- **Category**: WITH_SOURCE

## Recent upstream/main activity (post-investigation)

This family was newly onboarded to google/fonts on 2026-01-21:

- **2026-01-21** — Emma Marichal, commit [`dd04af331`](https://github.com/google/fonts/commit/dd04af331) ("Playwrite NZ Basic: Version 1.004 added"): initial onboarding via gftools-packager. Created `ofl/playwritenzbasic/` with METADATA.pb, OFL.txt, the binary `PlaywriteNZBasic[wght].ttf`, and article.
- **2026-01-21** — Marc Foley, commit [`9168cb8eb`](https://github.com/google/fonts/commit/9168cb8eb) ("playwritenzbasic*: rm all subsets apart from menu"): same-day post-onboarding cleanup, removing extra subsets from METADATA.pb. Same commit also touched the sibling `ofl/playwritenzbasicguides/` family.

Source block was populated by gftools-packager in the v1.004 commit; no corrections needed.
