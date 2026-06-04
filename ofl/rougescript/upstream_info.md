# Rouge Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rougescript/src/`

## Source Files

The `rougescript/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): RougeScript-Regular-OTF.vfb, RougeScript-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): RougeScript-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): RougeScript-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

GitHub was searched for "Rouge Script font", "RougeScript font", and "Rouge Script Typesenses". The designer is Sabrina Mariela Lopez of Typesenses (`typesenses@live.com.ar`). No GitHub account for Typesenses or Sabrina Lopez was found. No repository was identified for this font.

## Notes

Rouge Script was released in 2011 by Sabrina Mariela Lopez of Typesenses, an Argentine type studio. No public source repository was found on GitHub or other code hosting platforms.
