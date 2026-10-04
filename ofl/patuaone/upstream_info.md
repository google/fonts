# Patua One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/patuaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.vfb** (FontLab, proprietary): PatuaOne-Regular-OTF.vfb
- **.sfd** (FontForge): PatuaOne-Regular-TTF.sfd
- **Compiled binary** (not a design source): PatuaOne-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are VFB (FontLab, proprietary) and SFD (FontForge) format files. Neither format is buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

The METADATA.pb listed the designer as LatinoType with copyright held by LatinoType Limitada (info@latinotype.com), dated 2011.

The DESCRIPTION.en_us.html described Patua One as a slab serif text type designed for use in small sizes with low contrast and strong serifs. No upstream repository link was present.

No FONTLOG.txt file was found in the google/fonts ofl/patuaone/ directory.

Web searches were conducted for a LatinoType GitHub organization, for "latinotype/patua" or related repository names, and for any public upstream source for Patua One. No results were found. LatinoType does not appear to maintain a public GitHub presence for their font sources.

## Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. LatinoType does not appear to maintain a public GitHub repository for Patua One. Sources exist as VFB/SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.
