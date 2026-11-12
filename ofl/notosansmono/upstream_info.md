# Noto Sans Mono — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/latin-greek-cyrillic
- **Commit**: `N/A` (no commit hash recorded in METADATA.pb)
- **Status**: present

## What Was Done
The existing source metadata was reviewed. A `source` block was present pointing to the notofonts/latin-greek-cyrillic GitHub repository with an associated archive release at NotoSansMono-v2.014. No specific commit hash was recorded.

## Notes
- Designer: Google
- Script: Latin, Greek, Cyrillic
- Category: SANS_SERIF (MONOSPACE classification)
- Variable axes: wdth (62.5–100), wght (100–900)
- Monospaced variant of Noto Sans; covers an extensive range of Latin, Cyrillic, and Greek script languages.

## Commit Added (HIGH confidence)

Commit `9b7310b8f99fcd2583c49606e6aefca13a391350` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2023-09-30). This is the most reliable method.
