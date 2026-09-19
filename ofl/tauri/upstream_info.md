# Tauri — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `tauri/src/`.

### Source Files

- **VFB (FontLab)**: Tauri-Regular.vfb
- **SFD (FontForge)**: Tauri-Regular-OTF.sfd, Tauri-Regular-TTF.sfd
- **OTF (compiled)**: Tauri-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

- GitHub search: "Tauri font typeface" — no results
- GitHub search: "Tauri sorkin font" — no results
- github.com/EbenSorkin — no Tauri repository present
- github.com/sorkintype — organization not found
- github.com/googlefonts/tauri — not found
