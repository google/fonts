# Rum Raisin — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rumraisin/src/`

## Source Files

The `rumraisin/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): RumRaisin-Regular-OTF.vfb, RumRaisin-Regular-TTF.vfb, RumRaisin-Regular.vfb
- **OTF** (compiled binaries, not design sources): RumRaisin-Regular.otf

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Designer

Astigmatic (Brian J. Bonislawsky)

## Investigation Details

Rum Raisin was designed by Brian J. Bonislawsky DBA Astigmatic (AOETI). The DESCRIPTION.en_us.html and FONTLOG.txt direct contributors to contact `astigma@astigmatic.com`, but contain no upstream source repository links.

Searches were conducted for:
- `RumRaisin` by name on GitHub
- `astigmatic fonts`
- `astigmatic AOETI typeface`
- `Rum Raisin astigmatic`
- GitHub user `astigmatic`

The GitHub user `astigmatic` was found but only had two unrelated repositories (`astigmatic/pro`, `astigmatic/project1`). No font source repositories were associated with this account.

The only font repository associated with Astigmatic found via GitHub search was `googlefonts/SacramentoFont`.

The only repositories matching `RumRaisin` were:
- `librefonts/rumraisin` — a librefonts mirror (skipped per policy)
- Unrelated repositories (image processing, gaming projects)
