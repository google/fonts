# Russo One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `russoone/src/`

## Source Files

The `russoone/src/` directory contains design sources in SFD (FontForge) format only, which cannot be built with gftools-builder:

- **SFD** (FontForge, not buildable with gftools-builder): RussoOne-Regular-TTF.sfd

## Buildability

Not buildable with gftools-builder. The SFD sources are in FontForge format, which is not supported by the gftools-builder pipeline. Conversion to UFO or Glyphs format would be required.

## Designer

Jovanny Lemonad

## Investigation Details

Russo One was designed by Jovanny Lemonad (lemonad@jovanny.ru). The DESCRIPTION.en_us.html and FONTLOG.txt direct contributors to contact the designer directly at `lemonad@jovanny.ru`, but contain no upstream source repository links.

Searches were conducted for:
- `RussoOne` by name on GitHub
- `Russo One lemonad`
- `Russo One font Cyrillic`
- `jovanny lemonad` GitHub search
- GitHub user `jovanny`

The GitHub user `jovanny` was found but only had one unrelated repository (`jovanny/repositorio`). Jovanny Lemonad's font work appeared to be managed through third parties: the Google Fonts engineer `alexeiva` maintained repos for two other Jovanny Lemonad fonts (Philosopher and Yeseva One) but no Russo One repository was found.

The only repositories matching `RussoOne` were:
- `librefonts/russoone` — a librefonts mirror (skipped per policy)
- `google-fonts-bower/russoone-bower` — a bower packaging repo (skipped)
