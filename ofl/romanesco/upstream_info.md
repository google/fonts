# Romanesco — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `romanesco/src/`

## Source Files

The `romanesco/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Romanesco-Regular-OTF.vfb, Romanesco-Regular-TTF.vfb, Romanesco-Regular.vfb
- **OTF** (compiled binaries, not design sources): Romanesco-Regular.otf

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Investigation Details

GitHub was searched for "Romanesco font Astigmatic" and related terms. The designer is Brian J. Bonislawsky of Astigmatic. No repository was found under any known Astigmatic-related GitHub account (`ASTIGMATIC`, `astigmatic`, `AOETI`).

## Notes

Romanesco is a handwriting-style typeface released in 2012 by Brian J. Bonislawsky (Astigmatic). Like the other Astigmatic fonts investigated in this batch, no public source repository was found on GitHub.
