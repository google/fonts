# Pirata One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/pirataone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.vfb** (FontLab, proprietary): PirataOne-Regular-OTF.vfb
- **.sfd** (FontForge): PirataOne-Regular-TTF.sfd
- **Compiled binary** (not a design source): PirataOne-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are VFB (FontLab, proprietary) and SFD (FontForge) format files. Neither format is buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

Designer: Rodrigo Fuenzalida, Nicolas Massi. Script: Latin. Category: DISPLAY.

No source block was found in METADATA.pb. No canonical upstream GitHub repository was identified.

## Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. Sources exist as VFB/SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.
