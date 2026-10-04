# Sail — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sail/src/`

## Source Files

The `sail/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Sail-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Sail-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Sail-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

- **Designer**: Miguel Hernandez
- **Publisher**: LatinoType Limitada (luciano@latinotype.com)

## Investigation Details

The following searches and checks were performed:

- Searched GitHub for `Sail font latinotype display` — no results
- Searched GitHub for `Sail font display Google` — no relevant results
- Checked `repos/Latinotype/Sail` — not found
- Checked `repos/googlefonts/SailFont` and `repos/googlefonts/Sail` — not found
- Checked LatinoType GitHub organization repos — no Sail repository found
