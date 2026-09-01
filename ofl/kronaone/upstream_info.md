# Investigation: Krona One

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kronaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (5)

| File | Format | Notes |
|------|--------|-------|
| `KronaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KronaOne-Regular-OTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KronaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KronaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Krona'."

The DESCRIPTION.en_us.html credits "Sorkin Type Co" and mentions the source files were available from "Google Code" (http://code.google.com/p/googlefontdirectory/), which is no longer available. The FONTLOG.txt confirms the Sorkin Type Co origin with contact email `sorkineben@gmail.com`.

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kronaone` containing only TTX dumps. The googlefontdirectory-hg monorepo preserves the more complete VFB and SFD design sources that the librefonts mirror did not retain. The original Google Code hosting is defunct.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. The original Google Code hosting is defunct, and no upstream GitHub repository is known for this family.
