# Wellfleet — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `wellfleet/src/`.

### Source Files

- **VFB (FontLab)**: Wellfleet-Regular.vfb
- **SFD (FontForge)**: Wellfleet-Regular-TTF.sfd
- **OTF (compiled)**: Wellfleet-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

Wellfleet was designed by Riccardo De Franceschi and mastered by Eben Sorkin (Sorkin Type Co). The FONTLOG confirmed that the font was "Mastered from Fontlab VBF to TTF" — meaning the original source files were in FontLab VFB format. No GitHub repository was found for this font under any of the expected namespaces (`sorkintype/wellfleet`, `googlefonts/wellfleet`, or by searching for Riccardo De Franceschi). The DESCRIPTION.en_us.html referenced Google Code (`code.google.com/p/googlefontdirectory/`) as the source location, which has been decommissioned.
