# Quattrocento Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `quattrocentosans/src/`

## Source Files

The `quattrocentosans/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): QuattrocentoSans-Bold-OTF.vfb, QuattrocentoSans-Bold-TTF.vfb, QuattrocentoSans-Bold.vfb, QuattrocentoSans-BoldItalic-OTF.vfb, QuattrocentoSans-BoldItalic-TTF.vfb, QuattrocentoSans-BoldItalic.vfb, QuattrocentoSans-Italic-OTF.vfb, QuattrocentoSans-Italic-TTF.vfb, QuattrocentoSans-Italic.vfb, QuattrocentoSans-Regular-OTF.vfb, QuattrocentoSans-Regular-TTF.vfb, QuattrocentoSans-Regular.vfb
- **OTF** (compiled binaries, not design sources): QuattrocentoSans-Bold.otf, QuattrocentoSans-BoldItalic.otf, QuattrocentoSans-Italic.otf, QuattrocentoSans-Regular.otf

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Investigation Details

The following searches were performed:

- Searched GitHub for "quattrocento sans font" and "QuattrocentoSans" repositories.
- Checked the `impallari` GitHub account — Pablo Impallari has 26 public repositories, but none for Quattrocento Sans. (Same investigation as Quattrocento above.)
- Searched for repos with "QuattrocentoSans" in the name — found only `librefonts/quattrocentosans` (a librefonts mirror — skipped per policy) and `google-fonts-bower/quattrocentosans-bower` (a Bower packaging mirror).
- Checked the `OpenMandrivaAssociation/texlive-quattrocento` repo found in search — this is a LaTeX package, not a font source repository.

No canonical upstream repository with font source files was found.

## Notes

- Designer: Pablo Impallari (Impallari Type), with contributions from Brenda Gallo, Rodrigo Fuenzalida, and kerning by Igino Marini
- Quattrocento Sans is the companion sans-serif to Quattrocento
- Same situation as Quattrocento: Impallari's GitHub account does not include a source repository for this family
