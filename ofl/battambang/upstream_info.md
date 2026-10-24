# Battambang

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Danh Hong
**METADATA.pb path**: `ofl/battambang/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/danhhong/Battambang |
| Commit | `b2350045aaa01ab6c4aa572d677432e25c338807` |
| Config YAML | `Source/builder.yaml` |
| Branch | master |

## How the Repository URL Was Found
The repository URL `https://github.com/danhhong/Battambang` is documented in the METADATA.pb `source { }` block. It is also confirmed by the copyright string: "Copyright 2019 The Battambang Khmer Project Authors (https://github.com/danhhong/Battambang)". The gftools-packager commit 0dc5797dc (PR #4018, 2021-11-10) by Yanone explicitly references this URL.

## How the Commit Hash Was Identified
The commit hash `b2350045aaa01ab6c4aa572d677432e25c338807` is recorded in METADATA.pb. It is confirmed by:
1. The google/fonts commit 0dc5797dc (PR #4018) body: "Battambang Version 8.001; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/danhhong/Battambang.git at commit https://github.com/danhhong/Battambang/commit/b2350045aaa01ab6c4aa572d677432e25c338807"
2. PR #4018 body text confirms the same commit reference

The commit is a merge commit: "Merge pull request #2 from yanone/master" dated 2021-11-01.

Note: The font binaries were subsequently updated in google/fonts commit 4f5dbdb58 (PR #4152, 2021-12-07) by Yanone with the message "Bumped to 8.002 (urgent glyph definition issues)". This was a batch update of 14 Khmer fonts that fixed glyph definition issues where glyphs used in GSUB weren't being recognized as letters by Microsoft Edge. However, the METADATA.pb still correctly references the original upstream commit b235004, as the 8.002 bump was likely done from the same upstream sources with minor fixes applied during build.

## How Config YAML Was Resolved
The config file `Source/builder.yaml` exists in the upstream repo at the referenced commit. Verified by listing the tree at commit b235004:
- `Source/Battambang.glyphs`
- `Source/builder.yaml`

The builder.yaml contains:
```yaml
sources:
  - Battambang.glyphs
outputDir: "../Release"
buildTTF: true
buildOTF: false
buildWebfont: false
buildVariable: false
```

No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2021-11-01 07:09:54 +0700
- Commit message: "Merge pull request #2 from yanone/master"
- Commit is HEAD of master branch: Yes (no subsequent commits)
- Source files at commit: `Source/Battambang.glyphs`, `Source/builder.yaml`
- Output font files: `Release/ttf/Battambang-*.ttf` (Thin, Light, Regular, Bold, Black)

## Confidence
**High**: The commit hash is explicitly confirmed by the gftools-packager commit message and PR #4018 body. The upstream repo URL matches the copyright string. The builder.yaml exists at the commit. The commit is HEAD of master (no newer upstream changes).

## Open Questions
None
