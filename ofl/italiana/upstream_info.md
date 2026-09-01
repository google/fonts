# Investigation: Italiana

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `italiana/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (5)

| File | Format | Notes |
|------|--------|-------|
| `Italiana-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `Italiana-Regular-OTF.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `Italiana-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `Italiana-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline, which requires Glyphs, UFO, or Designspace formats.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository (2015).

The copyright states: "Copyright (c) 2011 by Santiago Orozco (hi@typemade.mx) with reserved name Italiana"

The FONTLOG.txt reveals:
- Designer: Santiago Orozco (hi@typemade.mx, www.typemade.mx, Twitter: @Typemade)
- Version 1.001 — Initial release on 11 March 2012
- The font was designed for use in newspaper and magazine headlines, inspired by Italian calligraphy masters

No GitHub repository has been identified for this font. The designer (Santiago Orozco / typemade.mx) appears to have submitted this font directly to Google Fonts. No cached upstream repository was found for this family beyond the googlefontdirectory-hg monorepo.

The font has only a regular weight (no italics or other variants). The font date_added is "2012-03-14" and has never been updated in google/fonts since the initial commit.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. No upstream GitHub repository is known. The font was contributed directly to Google Fonts by Santiago Orozco of typemade.mx.
