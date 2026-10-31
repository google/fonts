# Volkhov — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Cyreal

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `volkhov/src/`.

### Source Files

- **VFB (FontLab)**: Volkhov-Bold-OTF.vfb, Volkhov-Bold-TTF.vfb, Volkhov-Bold.vfb, Volkhov-BoldItalic-OTF.vfb, Volkhov-BoldItalic-TTF.vfb, Volkhov-BoldItalic.vfb, Volkhov-Italic-OTF.vfb, Volkhov-Italic-TTF.vfb, Volkhov-Italic.vfb, Volkhov-Regular-OTF.vfb, Volkhov-Regular-TTF.vfb, Volkhov-Regular.vfb
- **SFD (FontForge)**: Volkhov-BoldItalic-TTF.sfd, Volkhov-Italic-TTF.sfd
- **OTF (compiled)**: Volkhov-Bold-OTF.otf, Volkhov-BoldItalic-OTF.otf, Volkhov-Italic-OTF.otf, Volkhov-Regular-OTF.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

The [cyrealtype GitHub organization](https://github.com/cyrealtype) was identified as the correct maintainer (linked from `www.cyreal.org`). A `cyrealtype/Volkhov` repository exists on GitHub but contains only a single `README.md` file with no font source files. The repository appears to be a placeholder that was never populated with source files. The older `cyrealtype/Cyrealfonts` archive also did not contain Volkhov source files. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.
