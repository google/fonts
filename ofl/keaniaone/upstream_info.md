# Investigation: Keania One

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `keaniaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (5)

| File | Format | Notes |
|------|--------|-------|
| `KeaniaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KeaniaOne-Regular-OTF.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KeaniaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KeaniaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012, Julia Petretta (julia.petretta@googlemail.com), with Reserved Font Name 'Keania'"

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/keaniaone` containing similar legacy source files. This librefonts repository is an archival mirror.

There is no publicly known upstream GitHub repository for this Julia Petretta font.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. No upstream GitHub repository is known for this family.
