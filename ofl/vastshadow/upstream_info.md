# Vast Shadow — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Nicole Fally

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `vastshadow/src/`.

### Source Files

- **VFB (FontLab)**: VastShadow-Regular.vfb
- **SFD (FontForge)**: VastShadow-Regular-TTF.sfd
- **OTF (compiled)**: VastShadow-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

The copyright string credited Sorkin Type Co (`eben@eyebytes.com`), but despite an extensive search of the [SorkinType GitHub organization](https://github.com/SorkinType) (which has 68+ public repositories), no Vast Shadow repository was found. The SorkinType org contained Vampiro (a related display font) but not Vast Shadow. No standalone repository for Vast Shadow was identified in any public Git hosting platform. The `librefonts/vastshadow` mirror was found but excluded per policy.
