# Investigation: Forum

## Summary

- **Family name**: Forum
- **Designer**: Denis Masharov
- **Date added to Google Fonts**: 2011-07-06
- **Repository URL**: https://github.com/librefonts/forum
- **Commit**: e8efc0bceef3b98cf32f722bf637f3c110f68a37
- **Config**: none (VFB-only sources)
- **Status**: complete (no buildable sources)
- **Confidence**: HIGH

## METADATA.pb (current)

The current METADATA.pb has no `source` block. The font is categorized as DISPLAY/SERIF with subsets: menu, cyrillic, cyrillic-ext, latin, latin-ext.

## Upstream Repository

- **URL**: https://github.com/librefonts/forum (verified accessible, HTTP 200)
- **Type**: librefonts archive repo (TTX decomposition + VFB sources)
- **Single commit**: `e8efc0b` by hash3g (2014-10-17) -- "update .travis.yml"
- **Remote**: `origin` at `https://github.com/librefonts/forum`
- **Status**: clean, up to date with origin/master

### Repository Contents

The repo contains:
- **Root**: TTX decomposition files of `Forum-Regular.ttf` (split by table), plus DESCRIPTION.en_us.html, METADATA.json, OFL.txt, menusubset-forum.ff, .travis.yml
- **src/**: `Forum-Regular.vfb` (258,436 bytes), `Forum-Regular-TTF.vfb` (268,592 bytes), OTF TTX decomposition files, METADATA_comments.txt, VERSIONS.txt

### Source File Analysis

- **VFB files** (FontLab Studio binary format): These are the original design sources but are not buildable with gftools-builder or fontc.
- **No .glyphs, .ufo, .designspace, or .sfd files** exist in the repo.
- **No config.yaml** exists in the repo.
- The TTX files are decompositions of the compiled binary, not editable design sources.
- VERSIONS.txt confirms: "Forum-Regular.ttf: Version 1.000"

## google/fonts History

The font binary (`Forum-Regular.ttf`, 303,316 bytes) has been unchanged since the initial commit in google/fonts:
- **Initial commit**: `90abd17b` (2015-03-07) by Dave Crossland -- "Initial commit" -- blob hash `961dffbb`
- **Current HEAD**: Same blob hash `961dffbb` -- the binary has never been modified
- The font was originally part of the Google Web Fonts directory (dateAdded: 2011-07-06) and was migrated to the google/fonts repo in the 2015 initial import.

### Font Metadata (from TTX name table)

- Copyright: "Copyright (c) 2011, Denis Masharov"
- Version: 1.000
- Created: Thu Jun 30 08:26:00 2011
- Modified: Thu Jun 30 08:28:24 2011
- Unique ID: "DenisMasharov: Forum: 2011"

## Commit Hash Verification

The upstream repo has only a single commit (`e8efc0b`), so this is trivially the correct reference. The repo was created on 2014-10-17 as a librefonts archive containing the TTX decomposition and VFB sources of the original font. Since the google/fonts binary has never been updated, this single commit encompasses all the source material that corresponds to the font in the catalog.

## Build Configuration

No config.yaml is needed. The upstream repo contains only VFB sources (FontLab binary format), which are not compatible with gftools-builder or fontc. There are no .glyphs, .ufo, .designspace, or .sfd source files that could be used for rebuilding.

## Proposed Source Block

```
source {
  repository_url: "https://github.com/librefonts/forum"
  commit: "e8efc0bceef3b98cf32f722bf637f3c110f68a37"
}
```

No `config_yaml` field is needed since there are no buildable sources.
