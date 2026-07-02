# Sansita One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sansitaone/src/`

## Source Files

The `sansitaone/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): SansitaOne-TTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): SansitaOne-TTF.sfd

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

- **Designer**: Omnibus-Type (omnibus.type@gmail.com / www.omnibus-type.com)

## Investigation Details

The following searches and checks were performed:

- Checked `repos/Omnibus-Type/SansitaOne` — not found
- Checked `repos/googlefonts/SansitaOne` — not found
- Searched GitHub for `Sansita One font` — no relevant results
- Searched GitHub for `SansitaOne font OFL` — no relevant results
- Listed all `Omnibus-Type` user repositories — no SansitaOne repository present

The `Omnibus-Type` user repositories included a `Sansita` repo (for the 2016 family) and a `Sansita-Swashed` repo, but no dedicated Sansita One repository. Sansita One is an earlier, distinct display font from 2011.
