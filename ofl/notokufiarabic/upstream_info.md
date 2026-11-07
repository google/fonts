# Noto Kufi Arabic — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/arabic
- **Commit**: `N/A` (no commit field recorded)
- **Status**: Source block present

## What Was Done
The existing source metadata was reviewed. The source block contained a repository_url pointing to the notofonts/arabic GitHub repository and an archive_url to the NotoKufiArabic v2.109 release, but no commit hash was recorded.

## Notes
- **Designer**: Google
- **Script**: Arabic (Kufic style)
- **Category**: SANS_SERIF
- Part of the Google Noto project at github.com/notofonts/arabic. Covers Arabic script in a Kufi style with variable weight (wght 100–900). Supports a wide range of Arabic-script languages.

## Commit Added (HIGH confidence)

Commit `652edd9688496f88c4cf41706c892fe10f9f3c92` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2024-02-12). This is the most reliable method.
