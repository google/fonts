# Investigation Report: Exile

## Family Overview

- **Family name**: Exile
- **Designer**: Bartlomiej Rozga
- **License**: OFL
- **Category**: Display
- **Date added**: 2025-03-17
- **Fonts**: Exile-Regular.ttf (single weight, Regular 400)
- **Subsets**: latin, latin-ext, menu
- **Description**: A display stencil font inspired by music and the iconic logo of The Rolling Stones

## Source Repository

- **Repository URL**: https://github.com/rozgatype/Exile
- **Status**: Valid and accessible
- **Owner**: rozgatype (Bartlomiej Rozga)

## Source Block in METADATA.pb

The METADATA.pb already contains a complete `source {}` block:

```
source {
  repository_url: "https://github.com/rozgatype/Exile"
  commit: "b5c737683dcc95f1e749e2189fc242c4a2b31e97"
  config_yaml: "Source/config.yaml"
  files {
    source_file: "OFL.txt.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Exile-Regular.ttf"
    dest_file: "Exile-Regular.ttf"
  }
  files {
    source_file: "Documentation/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "Documentation/exile_1.jpg"
    dest_file: "article/exile_1.jpg"
  }
  files {
    source_file: "Documentation/exile_2.jpg"
    dest_file: "article/exile_2.jpg"
  }
  files {
    source_file: "Documentation/exile_3.jpg"
    dest_file: "article/exile_3.jpg"
  }
  files {
    source_file: "Documentation/exile_4.jpg"
    dest_file: "article/exile_4.jpg"
  }
  files {
    source_file: "Documentation/exile_5.jpg"
    dest_file: "article/exile_5.jpg"
  }
  branch: "main"
}
```

## Onboarding History

### Google Fonts Timeline

1. **2022-11-14**: Issue [#5548](https://github.com/google/fonts/issues/5548) opened by `rozgatype` requesting addition of Exile
2. **2025-03-31**: Commit `7e71908` - "Exile: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" by Yanone via gftools-packager. Commit body states: "Taken from the upstream repo https://github.com/rozgatype/Exile at commit b5c737683dcc95f1e749e2189fc242c4a2b31e97"
3. **2025-04-01**: Commit `06dfed7` - "Smaller image files sizes" (optimized article images)
4. **2025-04-09**: PR [#9281](https://github.com/google/fonts/pull/9281) merged by Marc Foley (`m4rc1e`). PR was authored by Yanone (`yanone`). PR body references resolving issue #5548

### Upstream Repository Timeline

- **2022-11-14**: Initial font upload by rozgatype (commits `1ae79eb` through `957d878`)
- **2024-06-28**: Font issues fixed and Zdotaccent correction (commits `88dfb73`, `bb4205e`)
- **2025-02-19**: Major preparation work by Yanone via PR #2 in upstream repo:
  - Re-exported corrupted FontLab file
  - Renamed glyphs to Glyphs.app naming scheme
  - Added copyright and license
  - Updated v-metrics, fixed caron, deleted .notdef
  - Set fsType
  - Improved Ldot/ldot
  - Deleted old fonts, added latest binary
  - Created ARTICLE.en_us.html
- **2025-03-06**: PR #2 merged (commit `b5c7376` = the referenced commit hash)

## Commit Hash Verification

- **Referenced commit**: `b5c737683dcc95f1e749e2189fc242c4a2b31e97`
- **Commit date**: 2025-03-06 (merge of PR #2 from yanone/main)
- **Current HEAD of origin/main**: `b5c737683dcc95f1e749e2189fc242c4a2b31e97` (same)
- **Verification**: The commit hash is confirmed correct. It is the HEAD of the upstream `main` branch. No additional commits have been made since. The onboarding commit in google/fonts (2025-03-31) explicitly references this commit, and it predates the google/fonts merge date (2025-04-09).
- **Confidence**: HIGH

## Config Verification

- **config.yaml location**: `Source/config.yaml` in upstream repo
- **Verified at referenced commit**: Yes, file exists at `b5c7376:Source/config.yaml`
- **Contents**:
  ```yaml
  sources:
  - Source-Glyphs/Exile.glyphs
  buildStatic: true
  buildTTF: true
  buildOTF: false
  buildWebfont: false
  ```
- **Override config in google/fonts**: None (not needed; upstream has config.yaml)

## Source Files

- **Primary source**: `Source/Source-Glyphs/Exile.glyphs` (.glyphs format, Glyphs.app v3337, format v3)
- **Original source**: `Source/Source-Fontlab/Exile.vfc` (FontLab source, also present)
- **Legacy sources**: `Source/Old/` directory contains older versions
- **Binary output**: `fonts/ttf/Exile-Regular.ttf`

## Summary

| Field | Value |
|---|---|
| Repository URL | https://github.com/rozgatype/Exile |
| Commit | b5c737683dcc95f1e749e2189fc242c4a2b31e97 |
| Config | Source/config.yaml (in upstream) |
| Status | complete |
| Confidence | HIGH |

This family's source metadata is fully complete. The METADATA.pb already contains a correct and verified `source {}` block with the proper repository URL, commit hash, config.yaml path, file mappings, and branch. No action needed.
