# Telex — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `telex/src/`.

### Source Files

- **VFB (FontLab)**: Telex-Regular-OTF.vfb, Telex-Regular.vfb
- **SFD (FontForge)**: Telex-Regular-TTF.sfd
- **OTF (compiled)**: Telex-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

- github.com/huertatipografica — full repo list checked, no Telex repository
- GitHub search: "Telex font typeface" — no results
- GitHub search: "Telex huertatipografica" — no results
- github.com/googlefonts/Telex — not found
- github.com/huertatipografica/telex — not found
