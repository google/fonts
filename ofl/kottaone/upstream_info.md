# Investigation: Kotta One

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kottaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (4)

| File | Format | Notes |
|------|--------|-------|
| `KottaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KottaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KottaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012 by Ania Kruk (hello@aniakruk.com), with Reserved Font Name 'Kotta'"

The DESCRIPTION.en_us.html describes Kotta One as "a new and unusual text typeface that mixes the characteristics of an italic with legibility of a roman."

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kottaone` containing only TTX dumps of the binary font — no VFB or SFD sources. The googlefontdirectory-hg monorepo preserves the more complete VFB and SFD design sources that the librefonts mirror did not retain.

No upstream GitHub repository for Ania Kruk or Kotta One was found.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. The librefonts mirror only preserved TTX dumps, making the googlefontdirectory-hg sources the more complete record. No upstream GitHub repository is known for this family.
