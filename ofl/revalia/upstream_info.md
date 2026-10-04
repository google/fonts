# Revalia — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `revalia/src/`

## Source Files

The `revalia/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Revalia-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Revalia-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Revalia-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

GitHub was searched for "Revalia font", "Revalia Estonian font", and the designer names "Johan Kallas" and "Mihkel Virkus". The GitHub accounts `johankallas`, `JohanKallas`, and `mihkelvirkus` were checked directly via the API, but none contained a Revalia repository. No other repositories were found for this font.

## Notes

The font was released in 2011 by Johan Kallas (`johankallas@gmail.com`) and Mihkel Virkus (`mihkelvirkus@gmail.com`). The FONTLOG.txt did not contain any URLs pointing to a public source repository. No public source repository was identified.
