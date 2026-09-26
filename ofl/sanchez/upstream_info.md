# Sanchez — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sanchez/src/`

## Source Files

The `sanchez/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Sanchez-Italic-OTF.vfb, Sanchez-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Sanchez-Italic-TTF.sfd, Sanchez-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Sanchez-Italic.otf, Sanchez-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

- **Designer**: Daniel Hernandez
- **Publisher**: LatinoType (luciano@latinotype.com)

## Investigation Details

The following searches and checks were performed:

- Searched GitHub for `Sanchez slab serif font` — no relevant results
- Searched GitHub for `Sanchez font LatinoType` — no relevant results
- Checked `repos/Latinotype/Sanchez` — not found
- Checked `repos/LatinoType/Sanchez` — not found
- Checked `repos/googlefonts/SanchezFont` — not found
- Checked LatinoType GitHub organization repos — no Sanchez repository found
