# Investigation Report: Kranky

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kranky/src/` |
| **Buildable** | No — no original design sources present |

The googlefontdirectory-hg monorepo (a git mirror of the original Google Code Mercurial repository) contains a `kranky/src/` directory with only:

- `METADATA_comments.txt` — metadata only, not a source file

No original design sources are present. The font was contributed as a pre-compiled binary without editable source files.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Kranky |
| Designer           | Sideshow (Font Diner, Inc) |
| License            | Apache 2.0 |
| Category           | DISPLAY |
| Date Added         | 2011-01-06 |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/kranky/`
- **No source block** in METADATA.pb
- **Copyright**: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow. All rights reserved."
- **Description**: "a hand-crafted, fun-filled font"

### Git History in google/fonts

The font was added with the initial commit (90abd17b4, 2015-03-07). Only metadata-only changes have been made since.

### Cached Mirror: librefonts/kranky

The cached repository at `librefonts/kranky` contains only TTX-decomposed font tables (`Kranky.ttf.*`). No buildable source files (.glyphs, .ufo, .designspace, .sfd, .vfb) are present. This is a legacy librefonts mirror, not a proper upstream repository.

### Designer Context

Font Diner (DBA Sideshow) is a commercial type foundry. The font was donated to Google Fonts under the Apache 2.0 license. The original design sources (likely proprietary format) were never made publicly available.

## Conclusion

Kranky has no buildable design sources in any known repository. Neither the googlefontdirectory-hg monorepo nor the librefonts mirror contains anything beyond metadata and TTX dumps. No config.yaml can be created.

### Status: no_config_possible
### Confidence: HIGH
