# Salsa — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `salsa/src/`

## Source Files

The `salsa/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Salsa-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Salsa-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Salsa-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

- **Designer**: John Vargas Beltrán (john.vargasbeltran@gmail.com)

## Investigation Details

The following searches and checks were performed:

- Searched GitHub for `Salsa font John Vargas` — no results
- Searched GitHub for `Salsa Vargas Colombian script` — no relevant results
- Checked `repos/googlefonts/SalsaFont` and `repos/googlefonts/Salsa` — not found
- Checked `repos/jvb/Salsa` and `repos/jvargasbeltran/Salsa` — not found
