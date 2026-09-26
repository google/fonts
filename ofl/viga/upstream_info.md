# Viga — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Fontstage

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `viga/src/`.

### Source Files

- **VFB (FontLab)**: Viga-Regular-OTF.vfb
- **SFD (FontForge)**: Viga-Regular-TTF.sfd
- **OTF (compiled)**: Viga-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

The font was created by Fontstage (`info@fontstage.com`). Searches were conducted on GitHub for "Viga font", "Fontstage", and related terms, but no dedicated font source repository was identified. The `fontstage.com` website was inaccessible. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.
