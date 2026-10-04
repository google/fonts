# Text Me One — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `textmeone/src/`.

### Source Files

- **VFB (FontLab)**: TextMeOne-Regular-OTF.vfb, TextMeOne-Regular.vfb
- **SFD (FontForge)**: TextMeOne-Regular-TTF.sfd
- **OTF (compiled)**: TextMeOne-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

- GitHub search: "Julia Petretta Text Me One font" — no results
- github.com/googlefonts/TextMeOne — not found
