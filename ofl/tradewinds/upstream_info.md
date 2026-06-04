# Trade Winds — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Sideshow (Font Diner, Inc.)

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `tradewinds/src/`.

### Source Files

- **VFB (FontLab)**: TradeWinds-Regular-TTF.vfb

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

## Investigation Details

Trade Winds was designed by Font Diner, Inc. (DBA Sideshow). The GitHub account `fontdiner` was found and examined. It contained two repositories:
- `fontdiner/fonts` — contained only a README and LICENSE, no font sources
- `fontdiner/fontdinerswanky` — contained TTF binary and OFL.txt for Fontdiner Swanky, no source files

No repository for Trade Winds was found under the `fontdiner` GitHub account.

Additional searches on GitHub using queries for "Trade Winds font Sideshow", "Trade Winds fontdiner", and related terms returned no relevant results.

The Font Diner website (fontdiner.com) was not investigated further as it is a commercial foundry website unlikely to host open source font source files.

Trade Winds was produced by a commercial foundry (Font Diner / Sideshow) and the sources are not publicly hosted. The font was released under OFL but no editable source files are publicly available.
