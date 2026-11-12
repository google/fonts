# Purple Purse — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `purplepurse/src/`

## Source Files

The `purplepurse/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): PurplePurse-Regular-OTF.vfb, PurplePurse-Regular-TTF.vfb, PurplePurse-Regular.vfb
- **OTF** (compiled binaries, not design sources): PurplePurse-Regular.otf

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Designer

Brian J. Bonislawsky (astigma@astigmatic.com) for Astigmatic (AOETI). Website: www.astigmatic.com.

## Investigation Details

- **Checked cache**: the upstream repo cache — no cached entry.
- **GitHub search**: Searches for "Purple Purse font astigmatic" returned no relevant results.
- **Astigmatic GitHub**: The GitHub user `astigmatic` exists but has only two placeholder repos (`astigmatic/pro`, `astigmatic/project1`) — no font source repositories.
- **FONTLOG evidence**: The FONTLOG lists three VFB source files: `PurplePurse-Regular.vfb`, `PurplePurse-Regular-TTF.vfb`, and `PurplePurse-Regular-OTF.vfb`. No public repository is referenced.
