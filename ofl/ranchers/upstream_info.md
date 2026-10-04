# Ranchers — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ranchers/src/`

## Source Files

The `ranchers/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Ranchers-Regular-OTF.vfb, Ranchers-Regular-TTF.vfb, Ranchers-Regular.vfb
- **OTF** (compiled binaries, not design sources): Ranchers-Regular.otf
- **Other**: EXT_BLOAT

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Investigation Details

GitHub was searched for "Ranchers" and "Ranchers Impallari Gallo". The `impallari` GitHub account was examined (listing all public repositories) but did not include a Ranchers repository. The project website `www.impallari.com` was referenced in the FONTLOG but is no longer functional. The `googlefonts` organization was also checked with no result.

## Notes

The font was released in 2012 by Pablo Impallari and Brenda Gallo. It appears that the Ranchers source files were never published on GitHub; the original project appears to have been hosted on the impallari.com website which is no longer available.
