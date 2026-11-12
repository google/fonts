# Roboto — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/roboto-classic
- **Commit**: `91d5d3e5b81efa04a77925cc609fdcdd7ee663d1`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
Designed by Christian Robertson, ParaType, and Font Bureau. A variable sans-serif with width (75–100) and weight (100–900) axes, available in upright and italic styles. One of Google Fonts' most widely used typefaces. Covers a broad range of subsets including Cyrillic, Greek, Latin, Vietnamese, Math, and Symbols. An archive URL pointing to a versioned release zip is also present in the source block.

## Recent upstream/main activity (post-investigation)

- **2026-01-27** — Aaron Bell, commit [`6183fc0d2`](https://github.com/google/fonts/commit/6183fc0d2) ("Roboto 3.015 update"): advanced the source block from v3.011 → v3.015. METADATA.pb changes:
  - `commit`: `b3ab25297a96373a8053db2d6fbf94b3ce61a8ac` → `91d5d3e5b81efa04a77925cc609fdcdd7ee663d1`
  - `archive_url`: `.../v3.011/Roboto_v3.011.zip` → `.../v3.015/Roboto_v3.015.zip`

  Both binaries (`Roboto[wdth,wght].ttf` and `Roboto-Italic[wdth,wght].ttf`) were updated. The recorded `91d5d3e5b...` is what the existing investigation captured; this appendix simply records the chronology of how it got there.
