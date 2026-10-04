# Yesteryear — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `yesteryear/src/`.

### Source Files

- **VFB (FontLab)**: Yesteryear-Regular-OTF.vfb, Yesteryear-Regular-TTF.vfb, Yesteryear-Regular.vfb
- **OTF (compiled)**: Yesteryear-Regular.otf

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

## Investigation Details

Yesteryear was designed by Brian J. Bonislawsky (DBA Astigmatic / AOETI). The FONTLOG explicitly listed three VFB source files: `Yesteryear-Regular-OTF.vfb`, `Yesteryear-Regular-TTF.vfb`, and `Yesteryear-Regular.vfb`. No GitHub repository was found under `astigmatic/yesteryear` or by searching for "yesteryear font" or "astigmatic font". Astigmatic does not appear to have a GitHub presence for their fonts.
