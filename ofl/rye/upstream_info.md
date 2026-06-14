# Rye — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rye/src/`

## Source Files

The `rye/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Rye-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Rye-Regular-OTF.sfd, Rye-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Rye-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Designer

Nicole Fally (Sorkin Type Co)

## Investigation Details

Rye was published under a Sorkin Type Co copyright, with the email `eben@eyebytes.com` (Eben Sorkin). The DESCRIPTION.en_us.html states that source files are available from `http://code.google.com/p/googlefontdirectory/` (the old Google Fonts code repository, now defunct), and directs contributors to contact `sorkineben@gmail.com`.

Searches were conducted for:
- `Rye font` by name on GitHub
- `Rye sorkintype`
- `Rye eben sorkin`
- `Rye font western`
- SorkinType GitHub organization repos (full list examined)
- `googlefonts/Rye` and `SorkinType/Rye` repos

The SorkinType GitHub organization hosts many Sorkin Type Co fonts, but Rye was not among them. The organization's repository list was examined in full and no Rye repository was present. No repository named `Rye` was found under either `googlefonts` or `SorkinType` namespaces.

The original sources for Rye appear to exist only in the defunct Google Code repository.
