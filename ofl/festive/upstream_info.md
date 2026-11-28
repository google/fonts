# Investigation Report: Festive

## Family Details

- **Family name**: Festive
- **Designer**: Robert Leuschke
- **License**: OFL
- **Category**: HANDWRITING, DISPLAY
- **Date added**: 2021-04-23
- **Google Fonts path**: ofl/festive

## Source Repository

- **Repository URL**: https://github.com/googlefonts/festive
- **Branch**: master
- **Status**: Active, owned by googlefonts organization

## Onboarding History

### PR and Commit

- **PR**: [google/fonts#3314](https://github.com/google/fonts/pull/3314) - "Festive: Version 1.101; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (vv-monsalve)
- **Merged by**: Marc Foley (m4rc1e)
- **Merged on**: 2021-04-26
- **google/fonts commit**: `7d43ecce95de59077ba3031103badf5c76a8cf34`

### Commit Hash Analysis

Three different commit hashes appear in the history:

1. **`6781f7e31a50b299859242ff94fc6f3d00fc2a55`** — Referenced in the PR #3314 body as the gftools-packager source. Dated 2021-04-14, message: "new fonts without 'Pro' particle". Binary SHA256: `92256ebc96ecf066aed125179613894ed381d9ebe8fa11321fd3bd2a76c8a4d7` — does NOT match google/fonts.

2. **`bd9351113997057606ffc2ef98ccca9f2c968eb0`** — Referenced in the google/fonts commit message body. Dated 2021-04-23, message: "one single space". Binary SHA256: `34940d4e68ffdbaee80e25d9ac8ef956eb0f4965c804d067041373ddca6a9ec8` — MATCHES google/fonts.

3. **`5a37931ba2af0e7eb487e7c04f800e9006618bc7`** — Currently in METADATA.pb, sourced from fontc_crater targets.json. Dated 2023-12-07, message: "Personalize for this repo". Binary SHA256: `34940d4e68ffdbaee80e25d9ac8ef956eb0f4965c804d067041373ddca6a9ec8` — matches google/fonts (same binary as bd93511).

### Correct Onboarding Commit

**`bd9351113997057606ffc2ef98ccca9f2c968eb0`** is the correct onboarding commit.

The PR body mentions commit `6781f7e` (Apr 14, 2021), but between that commit and the merge date (Apr 26, 2021), 14 additional commits were made upstream including diacritics fixes, dingbats additions, spacing/kerning fixes, and caret additions. The binary at `bd93511` (Apr 23, 2021) is an exact match to the file that was ultimately onboarded.

The current METADATA.pb commit `5a37931` (Dec 7, 2023) is the tip of the master branch — a "Personalize for this repo" commit that applied googlefonts template files without modifying any source or binary font files. While the binary is identical at both `bd93511` and `5a37931`, the correct reference should be the actual onboarding commit `bd93511`, not a later template commit.

### Commits After Onboarding (bd93511..5a37931)

5 commits, all template/documentation changes (no source or font modifications):
- `2389740` - GF distributed font proof added
- `88a07cd` - Deleting old CI action
- `059be14` - Adding template files
- `eb8c570` - Proofs moved to local-proofs folder
- `5a37931` - Personalize for this repo

## Build Configuration

- **Config file**: `sources/config.yml` (exists at both `bd93511` and `5a37931`)
- **Config contents**:
  ```yaml
  sources:
    - Festive-Pro.glyphs
  familyName: "Festive"
  buildVariable: false
  # autohintTTF: false
  ```
- **Source file**: `sources/Festive-Pro.glyphs` (Glyphs format)
- **Build type**: Static only (buildVariable: false)

## Binary Verification

| File | google/fonts SHA256 | Upstream (bd93511) SHA256 | Match |
|------|---------------------|--------------------------|-------|
| Festive-Regular.ttf | 34940d4e68ffdbaee80e25d9ac8ef956eb0f4965c804d067041373ddca6a9ec8 | 34940d4e68ffdbaee80e25d9ac8ef956eb0f4965c804d067041373ddca6a9ec8 | YES |

File size: 1,326,792 bytes (identical).

## Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/festive"
  commit: "5a37931ba2af0e7eb487e7c04f800e9006618bc7"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Festive-Regular.ttf"
    dest_file: "Festive-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Issues Found

### Commit hash should reference the onboarding commit

The METADATA.pb currently references `5a37931` (the latest commit / template personalization from Dec 2023), but the actual onboarding commit is `bd9351113997057606ffc2ef98ccca9f2c968eb0` (Apr 23, 2021). While the font binary and source files are identical at both commits, the commit hash should reference the original onboarding point for accuracy.

**Recommended correction**: Change commit from `5a37931ba2af0e7eb487e7c04f800e9006618bc7` to `bd9351113997057606ffc2ef98ccca9f2c968eb0`.

**Note**: This is a minor issue since the binary/source files are unchanged. The current METADATA.pb is functionally correct — the config.yml and sources exist at the referenced commit and produce the same output. However, for historical accuracy, the onboarding commit is preferred.

## Summary

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/festive |
| Commit (correct) | bd9351113997057606ffc2ef98ccca9f2c968eb0 |
| Commit (current METADATA.pb) | 5a37931ba2af0e7eb487e7c04f800e9006618bc7 |
| Branch | master |
| Config | sources/config.yml |
| Source format | Glyphs (.glyphs) |
| Binary match | YES |
| Override config needed | No |
| Status | needs_correction (commit hash) |
| Confidence | HIGH |
