# Rufina — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rufina/src/`

## Source Files

The `rufina/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Rufina-Bold-OTF.vfb, Rufina-Bold.vfb, Rufina-Regular-OTF.vfb, Rufina-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Rufina-Bold-TTF.sfd, Rufina-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Rufina-Bold.otf, Rufina-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

Martin Sommaruga

## Investigation Details

The FONTLOG.txt describes two source files:
1. `Rufina-Regular-OTF.vfb` — FontLab VFB format
2. `Rufina-Regular-TTF.sfd` — FontForge SFD format

These sources were described as available from `http://code.google.com/p/googlefontdirectory/`, the old Google Fonts code repository, which is no longer accessible.

Searches were conducted for:
- `Rufina font` by name
- `estudiotrama font`
- `sommaruga typeface`
- `Rufina sommaruga typeface`
- `estudiotrama` GitHub organization/user

No GitHub user or organization named `estudiotrama` was found. The only repositories matching "Rufina" were unrelated (Discord bots, random repos) or the `librefonts/rufina` mirror (skipped per policy).
