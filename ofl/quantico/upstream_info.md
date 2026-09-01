# Quantico — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `quantico/src/`

## Source Files

The `quantico/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Quantico-Bold-OTF.vfb, Quantico-BoldItalic-OTF.vfb, Quantico-Italic-OTF.vfb, Quantico-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Quantico-Bold-TTF.sfd, Quantico-BoldItalic-TTF.sfd, Quantico-Italic-TTF.sfd, Quantico-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Quantico-Bold.otf, Quantico-BoldItalic.otf, Quantico-Italic.otf, Quantico-Regular.otf

## Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

## Investigation Details

The following searches were performed:

- Searched GitHub for "quantico font" repositories — no relevant font source repositories were found.
- Checked the `MadType` GitHub account — it exists but has no public repositories.
- Checked the `mattdesmond` GitHub account — found `mattdesmond/fonts`, which is a personal mirror of google/fonts with only TTF binaries in the `ofl/quantico/` subdirectory, not a source repository.
- Searched for dedicated Quantico repos by Matthew Desmond — none found.
- Reviewed the FONTLOG.txt, which references `http://www.madtype.com` as documentation and `mattdesmond@gmail.com` as contact, but no GitHub repository was linked.

No canonical upstream repository with font source files was found.

## Notes

- Designer: Matthew Desmond (MADType)
- The FONTLOG lists only a single initial release in December 2011, with no modern build pipeline references
- The `madtype.com` website was not investigated as GitHub search was the primary method used
