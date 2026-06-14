# Ribeye — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ribeye/src/`

## Source Files

The `ribeye/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Ribeye-Regular-OTF.vfb, Ribeye-Regular-TTF.vfb
- **OTF** (compiled binaries, not design sources): Ribeye-Regular.otf
- **Other**: RibeyeMarrow.ai

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Investigation Details

GitHub was searched for "Ribeye font Astigmatic" and related terms. The designer is Brian J. Bonislawsky of Astigmatic (AOETI — Astigmatic One Eye Typographic Institute). The GitHub accounts `ASTIGMATIC`, `astigmatic`, and `AOETI` were checked directly, but none contained a Ribeye repository. Only placeholder repositories were found under those accounts. A broader search for "Ribeye Astigmatic" returned no results.

## Notes

Brian J. Bonislawsky of Astigmatic has designed numerous fonts available on Google Fonts. None of them appear to have public source repositories on GitHub, suggesting the source files have not been made publicly available. The font was released in 2011.
