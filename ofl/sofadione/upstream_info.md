# Sofadi One -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sofadione/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `SofadiOne-Regular-OTF.vfb` (VFB, proprietary)
- `SofadiOne-Regular-TTF.vfb` (VFB, proprietary)
- `SofadiOne-Regular.vfb` (VFB, proprietary)

## Designer

Botjo Nikoltchev

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. Searches for "sofadi one", "sofadione", and repositories by Botjo Nikoltchev returned only:

- **librefonts/sofadione** — a librefonts mirror (excluded per policy).
- **google-fonts-bower/sofadione-bower** — a deprecated bower packaging mirror.

No repository owned by Botjo Nikoltchev containing UFO or Glyphs sources was found.
