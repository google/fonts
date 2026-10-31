# Rosarivo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rosarivo/src/`

## Source Files

The `rosarivo/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Rosarivo-Italic-OTF.vfb, Rosarivo-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Rosarivo-Italic-TTF.sfd, Rosarivo-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Rosarivo-Italic.otf, Rosarivo-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

GitHub was searched for "Rosarivo font" and "Rosarivo Ugerman". The `profound-labs/rosarivo-x-font` repository was confirmed to be a non-fork extended version containing only SFD sources, and was therefore excluded. The GitHub accounts `pablougerman` and `ugerman` were checked, but neither was found. The designer's domain `ugrdesign.com.ar` did not lead to any GitHub account.

## Notes

Rosarivo was released in 2011 by Pablo Ugerman of UGR Design (`www.ugrdesign.com.ar`). No public source repository with UFO or Glyphs files was found for the original typeface.
