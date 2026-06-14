# Wendy One — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `wendyone/src/`.

### Source Files

- **VFB (FontLab)**: WendyOne-Regular-OTF.vfb
- **SFD (FontForge)**: WendyOne-Regular-TTF.sfd
- **OTF (compiled)**: WendyOne-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

Wendy One was designed by Alejandro Inler in collaboration with Julieta Ulanovsky. Searches on GitHub for repositories by `alejandroinler`, combinations of "wendy one font", "wendy font inler", and "wendy font julieta" returned no results. No GitHub account for Alejandro Inler was found. The font's DESCRIPTION mentioned it was "developed by Alejandro Inler in conjunction with Julieta Ulanovsky" but contained no URL to a source repository.
