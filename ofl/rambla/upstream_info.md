# Rambla — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rambla/src/`

## Source Files

The `rambla/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Rambla-Bold-OTF.vfb, Rambla-Bold.vfb, Rambla-BoldItalic-OTF.vfb, Rambla-BoldItalic.vfb, Rambla-Regular-Italic-OTF.vfb, Rambla-Regular-Italic.vfb, Rambla-Regular-OTF.vfb, Rambla-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Rambla-Bold-TTF.sfd, Rambla-BoldItalic-TTF.sfd, Rambla-Regular-Italic-TTF.sfd, Rambla-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Rambla-Bold.otf, Rambla-BoldItalic.otf, Rambla-Regular-Italic.otf, Rambla-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

GitHub was searched for the font name "Rambla" and the designer name "Martin Sommaruga" / "Estudio Trama". The `flokk/font-rambla` repository was examined but contained only CSS and WOFF files, making it unsuitable as a source reference. The FONTLOG.txt referenced `http://code.google.com/p/googlefontdirectory/` (the old Google Font Directory project), which is no longer active. No other repositories were identified.

## Notes

The font's copyright year is 2011–2012, predating widespread use of GitHub for font source hosting. The designer appears to be from Argentina (email: `martin@estudiotrama.com`). No public Git repository with UFO or Glyphs sources was found.
