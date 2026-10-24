# Investigation: IM Fell Double Pica

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `imfelldoublepica/src/` |
| **Buildable** | No — no original design sources available |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (1)

| File | Format | Notes |
|------|--------|-------|
| `METADATA_comments.txt` | Metadata | Not a design source |

The `src/` directory contains only a metadata comments file. There are no original design sources (no VFB, SFD, Glyphs, or UFO files). The font cannot be rebuilt from these files.

## Investigation

The METADATA.pb at `ofl/imfelldoublepica/METADATA.pb` contains no source block. The font was added to google/fonts in the initial commit (`90abd17b4f97671435798b6147b698aa9087612f`, dated 2015-03-07) by Dave Crossland, along with all other IM Fell variants. This predates the practice of tracking upstream repository information.

The git log for `ofl/imfelldoublepica/` shows:
- `49cd93129` — "imfelldoublepica: rename fonts and regenerate METADATA.pb" (renamed `IMFeDPit28P.ttf` to `IMFELLDoublePica-Italic.ttf` and `IMFeDPrm28P.ttf` to `IMFELLDoublePica-Regular.ttf`)
- `90abd17b4` — "Initial commit"

None of these commits reference an upstream repository URL or commit hash.

The font was designed by Igino Marini (iginomarini.com). The copyright string reads: "Copyright 2007 Igino Marini (www.iginomarini.com mail@iginomarini.com)".

A repository `https://github.com/librefonts/imfelldoublepica` exists in the local cache. This repo has a single commit (`35b0c6ea`, "update .travis.yml", 2014-10-17) and contains only TTX-disassembled font data (no VFB or other editable source files, only `src/METADATA_comments.txt` and `src/VERSIONS.txt`). The font version documented is 3.00. This librefonts repository is an archival mirror of the compiled TTF, not the original design source.

Igino Marini does not appear to have a public GitHub repository for the IM Fell fonts; the actual sources were originally provided from his personal website (www.iginomarini.com).

No Google Fonts config.yaml override exists in `ofl/imfelldoublepica/` in google/fonts.

## Conclusion

Neither the googlefontdirectory-hg monorepo nor the librefonts mirror contain original design sources for this family — only metadata and TTX dumps of prebuilt binaries. The actual designer (Igino Marini) does not maintain a public repository. The font cannot be rebuilt from available sources.
