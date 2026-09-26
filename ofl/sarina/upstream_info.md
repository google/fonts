# Sarina — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sarina/src/`

## Source Files

The `sarina/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Sarina-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Sarina-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Sarina-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

- **Designer**: James Grieshaber
- **Publisher**: Sorkin Type Co (www.sorkintype.com, eben@eyebytes.com)

## Investigation Details

The following searches and checks were performed:

- Searched GitHub for `Sarina font sorkintype` — no results
- Searched GitHub for `Sarina font display` — no relevant results
- Checked `repos/sorkintype/Sarina` and `repos/sorkintype/sarina` — not found
- Checked `repos/googlefonts/SarinaFont` and `repos/googlefonts/Sarina` — not found
