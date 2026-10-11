# Ruluko — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ruluko/src/`

## Source Files

The `ruluko/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Ruluko-Regular-OTF.vfb, Ruluko-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Ruluko-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Ruluko-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

Ana Sanfelippo, Angélica Díaz, Meme Hernández

## Investigation Details

Ruluko was designed by Ana Sanfelippo (Twitter: @anasanfelippo), Angélica Díaz (@angiecinadiaz), and Meme Hernández (@memepeca) as a typeface intended to aid those learning to read, with shapes related to handwriting styles used in Argentine schools.

Searches were conducted for:
- `Ruluko` by name on GitHub
- `Ruluko sanfelippo`
- `anasanfe` GitHub user
- `Ruluko typeface argentina`

The only repositories found matching `Ruluko` were:
- `librefonts/ruluko` — a librefonts mirror (skipped per policy)
- `google-fonts-bower/ruluko-bower` — a bower packaging repo (skipped)

No GitHub account was found for any of the three designers. The DESCRIPTION.en_us.html and FONTLOG.txt contain no upstream source repository links.
