# Investigation Report: Crafty Girls

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `apache/craftygirls/src/` |
| **Buildable** | No — no original design sources available |

The font is referenced in the **googlefontdirectory-hg** monorepo (the git mirror of the original Google Code Mercurial repository that hosted Google Fonts from 2010–2013). However, the `src/` directory contains only a TTX-processed TTF and metadata comments — not original design sources. The original .vfb design files were never published.

### Files in googlefontdirectory-hg `src/`

- `CraftyGirls-TTX.ttf` — TTX round-tripped binary (not a design source)
- `METADATA_comments.txt`

## Summary

Crafty Girls is a handwriting font designed by Crystal Kluge for Font Diner, Inc (DBA Tart Workshop). It was added to Google Fonts on 2011-01-06 and last updated via PR #770 in August 2017. The font was produced by a commercial foundry and delivered as a compiled binary. No original design sources (.glyphs, .ufo, .vfb) are known to exist in any public repository.

## Key Facts

| Field | Value |
|-------|-------|
| Designer | Tart Workshop (Crystal Kluge) |
| License | Apache 2.0 |
| Date Added | 2011-01-06 |
| Font Version | 1.001 |
| Source Types | TTX only (no design sources) |
| Confidence | HIGH |

## Investigation Details

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 98e7670 | 2017-08-07 | Marc Foley | hotfix-craftygirls: v1.001 added (#770) |
| 64d3e3a | earlier | (batch) | Remove duplicate files |
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

PR #770 (merged 2017-08-07) renamed the font file from CraftyGirls.ttf to CraftyGirls-Regular.ttf and updated metadata. The PR body was empty.

### librefonts/craftygirls Mirror

The `librefonts/craftygirls` GitHub repo is an automated TTX dump, not an upstream source. It contains decompiled table dumps (`CraftyGirls-TTX.ttf.*.ttx`) which cannot be used to rebuild the font. Single commit by hash3g: "update .travis.yml".

### Search for Original Sources

- **fontdiner/fonts** on GitHub exists but is empty (LICENSE + README only)
- No `googlefonts/craftygirls` repository exists
- Font Diner / Tart Workshop is a commercial foundry; the original design sources (.vfb) were never published
