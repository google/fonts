# Tenor Sans — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `tenorsans/src/`.

### Source Files

- **VFB (FontLab)**: TenorSans-Regular.vfb
- **OTF (compiled)**: TenorSans-Regular.otf

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

## Investigation Details

- github.com/DmASharov — found account, only one unrelated repo
- GitHub search: "TenorSans font Denis Masharov" — no results
- github.com/googlefonts/TenorSans — not found
- GitHub search: "Tenor Sans typeface" — no relevant results
