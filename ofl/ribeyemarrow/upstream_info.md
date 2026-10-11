# Ribeye Marrow — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ribeyemarrow/src/`

## Source Files

The `ribeyemarrow/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): RibeyeMarrow-Regular-OTF.vfb, RibeyeMarrow-Regular-TTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): RibeyeMarrow-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): RibeyeMarrow-Regular.otf
- **Other**: RibeyeMarrow.ai

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

The same search effort as for Ribeye was applied. Brian J. Bonislawsky of Astigmatic is the designer of both Ribeye and Ribeye Marrow. The GitHub accounts `ASTIGMATIC`, `astigmatic`, and `AOETI` were checked, with no repository found for Ribeye Marrow. No public source repository was identified for any Astigmatic fonts.

## Notes

Ribeye Marrow is a companion font to Ribeye, also by Brian J. Bonislawsky of Astigmatic, released in 2011. No public source repository was found.
