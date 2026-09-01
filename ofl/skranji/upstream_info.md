# Skranji -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `skranji/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Skranji-Bold-TTF.vfb` (VFB, proprietary)
- `Skranji-Regular-TTF.vfb` (VFB, proprietary)

## Designer

Neapolitan / Font Diner, Inc.

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. Searches for "skranji", "fontdiner", and "neapolitan font" returned only:

- **librefonts/skranji** — a librefonts mirror (excluded per policy).
- **google-fonts-bower/skranji-bower** — a deprecated bower packaging mirror.

No repository owned by Font Diner / Neapolitan containing UFO or Glyphs sources was found.
