# Investigation: Karla Tamil Upright

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `karlatamilupright/src/` |
| **Buildable** | No — legacy formats only (.vfb) with VOLT pipeline |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (6)

| File | Format | Notes |
|------|--------|-------|
| `KarlaUpright-MM.vfb` | FontLab VFB (Multiple Master) | Proprietary format, not buildable with gftools |
| `InVOLT_ImportProject_1to272.vtp` | VOLT project | Microsoft VOLT table data |
| `KarlaUpright-Bold-InVOLT.ttf` | TrueType binary | Post-VOLT processing, not a design source |
| `KarlaUpright-Bold-PreVOLT.ttf` | TrueType binary | Pre-VOLT processing, not a design source |
| `KarlaUpright-Regular-InVOLT.ttf` | TrueType binary | Post-VOLT processing, not a design source |
| `KarlaUpright-Regular-PreVOLT.ttf` | TrueType binary | Pre-VOLT processing, not a design source |

The source directory contains a VFB Multiple Master file (the original design source) alongside TTF binaries at various stages of the Microsoft VOLT processing pipeline. The VFB file is proprietary FontLab format, not compatible with gftools-builder.

Both Karla Tamil families (Inclined and Upright) were created by Jonathan Pinhorn in 2011-2012 for Tamil script support and share a similar source structure.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository, which predates the source metadata tracking system.

The copyright notice reads: "Copyright (c) 2011-2012, Jonathan Pinhorn (jonpinhorn.typedesign@gmail.com), with Reserved Font Names 'Karla'"

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/karlatamilupright` containing similar TTX/VFB source files. This librefonts repository is an archival mirror, not the original design source repository.

The upstream source repository for Jonathan Pinhorn's Karla Tamil fonts is not publicly known.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy VFB Multiple Master format with a VOLT-based OpenType layout pipeline. These are not buildable with gftools-builder. No upstream GitHub repository is known for this family.
