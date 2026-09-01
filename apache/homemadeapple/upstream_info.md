# Investigation Report: Homemade Apple

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `homemadeapple/src/` |
| **Buildable** | No — no original design sources present |

The googlefontdirectory-hg monorepo (a git mirror of the original Google Code Mercurial repository) contains a `homemadeapple/src/` directory with only:

- `METADATA_comments.txt` — metadata only, not a source file

No original design sources are present. The font was contributed as a pre-compiled binary without editable source files.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Homemade Apple |
| Designer           | Font Diner |
| License            | Apache 2.0 |
| Category           | HANDWRITING / DISPLAY |
| Date Added         | 2011-01-06 |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/homemadeapple/`
- **No source block** in METADATA.pb

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 90abd17b4 | 2015-03-07 | Dave Crossland | Initial commit |
| 8e94f9c12 | 2017-08-07 | Marc Foley | hotfix-homemadeapple: v1.001 added (#776) |

The hotfix renamed `HomemadeApple.ttf` to `HomemadeApple-Regular.ttf` and updated METADATA.pb fields (filename, post_script_name, full_name, copyright) and DESCRIPTION.en_us.html.

### Cached Mirror: librefonts/homemadeapple

The librefonts mirror at `https://github.com/librefonts/homemadeapple` contains:

- **1 commit total**: `5159ae2` (2014-10-17) "update .travis.yml"
- **Files**: TTX-decomposed font tables, LICENSE.txt, COPYRIGHT.txt, DESCRIPTION.en_us.html, METADATA.json
- **src/ directory**: Contains only `VERSIONS.txt` (recording "HomemadeApple.ttf: Version 1.000") and an empty `METADATA_comments.txt`
- **No buildable sources**: No .glyphs, .ufo, .designspace, .sfd, or .vfb files anywhere

This is a legacy librefonts mirror containing TTX decompositions, not actual design sources.

### Font Diner Context

Font Diner is a commercial foundry. The font was contributed under the Apache 2.0 license. The original design sources (likely proprietary format) were never made publicly available.

## Conclusion

Homemade Apple has no buildable design sources in any known repository. Both the googlefontdirectory-hg monorepo and the librefonts mirror contain only metadata and TTX decompositions. No config.yaml can be created.

### Status: no_config_possible
### Confidence: HIGH
