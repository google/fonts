# Passion One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/passionone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.vfb** (FontLab, proprietary): PassionOne-Regular-OTF.vfb, PassionOne-Bold-OTF.vfb, PassionOne-Black-OTF.vfb
- **.sfd** (FontForge): PassionOne-Regular-TTF.sfd, PassionOne-Bold-SFD.sfd, PassionOne-Black-SFD.sfd
- **Compiled binaries** (not design sources): PassionOne-Regular.otf, PassionOne-Bold.otf, PassionOne-Black.otf
- **Metadata**: METADATA_comments.txt

The design sources are VFB (FontLab, proprietary) and SFD (FontForge) format files. Neither format is buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

The METADATA.pb listed the designer as Fontstage with copyright held by Fontstage (info@fontstage.com), dated 2011.

The FONTLOG.txt identified:
- Designer: Ernesto "Passion" Garcia Cabral (Fontstage)
- Source files: `Passion-Regular-OTF.vfb` (FontLab OTF source) and `Passion-Regular-TTF.sfd` (Fontforge SFD TTF source)
- Initial release: 5 December 2011

Web searches were conducted for Fontstage on GitHub, for a "Passion One" font repository, and for any organization or user matching the Fontstage foundry. No public GitHub repository was found beyond the legacy googlefontdirectory-hg archive.

The DESCRIPTION.en_us.html contained no upstream repository link.

## Conclusion

No canonical upstream GitHub repository was found beyond the legacy googlefontdirectory-hg archive. Sources exist as VFB/SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.
