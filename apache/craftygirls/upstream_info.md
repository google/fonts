# Investigation Report: Crafty Girls

## Summary

Crafty Girls is a handwriting font designed by Crystal Kluge for Font Diner, Inc (DBA Tart Workshop). It was added to Google Fonts on 2011-01-06 and last updated via PR #770 in August 2017. There is no dedicated upstream repository beyond the `librefonts/craftygirls` automated mirror, which contains only TTX dumps and decompiled source files. No original design sources (.glyphs, .ufo, .designspace) or config.yaml exist. The font was produced by Font Diner and delivered as a compiled binary.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Crafty Girls |
| Designer           | Tart Workshop (Crystal Kluge) |
| License            | Apache 2.0 |
| Category           | HANDWRITING |
| Date Added         | 2011-01-06 |
| Repository URL     | None (no proper upstream repo) |
| Commit Hash        | N/A |
| Config YAML        | None |
| Source Types        | TTX only (librefonts mirror) |
| Font Version        | 1.001 |
| Status             | no_upstream_repo |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/craftygirls/`
- **Files**: CraftyGirls-Regular.ttf, DESCRIPTION.en_us.html, LICENSE.txt, METADATA.pb
- **No source block** in METADATA.pb
- **Font version**: Version 1.001 (from name table: "1.001;DINR;CraftyGirls-Regular")
- **Copyright**: "Copyright (c) 2010 by Font Diner, Inc DBA Tart Workshop. All rights reserved."
- **Vendor**: Font Diner, Inc DBA Tart Workshop
- **Designer credit**: Crystal Kluge

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 98e7670 | 2017-08-07 | Marc Foley | hotfix-craftygirls: v1.001 added (#770) |
| 64d3e3a | earlier | (batch) | Remove duplicate files |
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

PR #770 (merged 2017-08-07 by Marc Foley) renamed the font file from CraftyGirls.ttf to CraftyGirls-Regular.ttf and updated metadata. The PR body was empty.

### Cached Mirror: librefonts/craftygirls

- **Path**: upstream_repos/fontc_crater_cache/librefonts/craftygirls
- **URL**: https://github.com/librefonts/craftygirls
- **Content**: TTX dumps of the binary font, plus src/ directory with more TTX files and metadata
- **Source type**: TTX only (decompiled from binary, not original design sources)
- **Single commit** by hash3g (undated): "update .travis.yml"
- **Versions file**: Lists Version 1.000

The librefonts mirror is an automated TTX dump. The src/ directory contains CraftyGirls-TTX.ttf.*.ttx files (decompiled table dumps). These are NOT original design sources and cannot be used to rebuild the font with gftools-builder.

### Search for Upstream Repository

- **No googlefonts/craftygirls** or **googlefonts/crafty-girls** repository exists
- **fontdiner/fonts** exists on GitHub but is empty (only LICENSE and README.md)
- **No other upstream repository** was found for this font
- Font Diner / Tart Workshop is a commercial foundry; the font was contributed under Apache 2.0 but the original design sources (.vfb or similar) were likely never published

### Config.yaml Assessment

No config.yaml exists anywhere. The only available source format is TTX (decompiled binary tables), which is not compatible with gftools-builder. The original design sources (likely FontLab .vfb format given the era and foundry) were never published.

## Conclusion

Crafty Girls has no proper upstream repository. The librefonts/craftygirls mirror contains only TTX dumps and should not be used as a repository_url. The font was produced by Font Diner and delivered as a compiled binary to Google Fonts. No original design sources or build configuration exist.

### Recommended METADATA.pb Source Block

No source block can be added. There is no upstream repository containing original design sources.

### Status: no_upstream_repo
### Confidence: HIGH

There is no proper upstream repository for this font. The font was created by Font Diner (a commercial foundry) and the original design files were never published to a public repository.
