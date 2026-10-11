# Wallpoet — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Lars Berggren

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `wallpoet/src/`.

### Source Files

- **VFB (FontLab)**: wallpoet.vfb
- **SFD (FontForge)**: Wallpoet-Regular-TTF.sfd
- **EPS glyph drawings**: 242 files in wallpoet_eps/

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

The font was created by Lars Berggren (`punktlars@gmail.com`). Searches were conducted on GitHub for "Wallpoet", "Lars Berggren", and related terms, but no dedicated font source repository was identified. The `librefonts/wallpoet` mirror was found but excluded per policy. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.
