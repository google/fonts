# Bahianita

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Omnibus-Type
**METADATA.pb path**: `ofl/bahianita/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Bahiana |
| Commit | `e96af6905aadd095bf2568c44fc643c1b2c412d4` (from PR #1669) |
| **Config YAML** | Override in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The upstream repository URL was identified from:
1. The copyright string in METADATA.pb: "Copyright 2018 The Bahianita Project Authors (https://github.com/Omnibus-Type/Bahiana/tree/master/Bahianita)"
2. The google/fonts commit body `747c13d4` (2019-06-12): "Taken from the upstream repo https://github.com/Omnibus-Type/Bahiana"
3. PR #1669 body explicitly states: "Taken from the upstream repo https://github.com/Omnibus-Type/Bahiana"

**Note**: Bahianita shares the same upstream repository as Bahiana (`Omnibus-Type/Bahiana`). The Bahianita sources live in the `Bahianita/` subdirectory within that repo.

## How the Commit Hash Was Identified

PR #1669 explicitly references the onboarding commit: "at commit https://github.com/Omnibus-Type/Bahiana/commit/e96af6905aadd095bf2568c44fc643c1b2c412d4"

This commit is dated 2018-08-07 with the message "Fixed bad glyph names and vertical metrics". The PR was merged on 2019-06-12.

**Important discrepancy**: The tracking file (`gfonts_library_sources.json`) currently lists commit `0efedac55f05ea7f6b277b2d63424984e53d005d` (the HEAD of the repo), but this is incorrect. Two commits happened after the PR-referenced commit `e96af69`:
- `927d451` (2019-03-05) "Updating text info" — modified the Glyphs source (appVersion, copyright year change)
- `0efedac` (2019-03-12) "Update README.md"

The PR was explicitly created referencing `e96af69`, not HEAD. The source file `.glyphs` was modified between `e96af69` and `0efedac`, so the correct commit for the onboarded binaries is `e96af69`.

Also note: the METADATA.pb currently has NO source block at all. The repository_url and commit are only tracked in `gfonts_library_sources.json`, not in METADATA.pb.

## How Config YAML Was Resolved

No config.yaml or builder.yaml exists in the upstream repository. No override config.yaml exists in the google/fonts family directory. The source files at the onboarding commit are `Bahianita/sources/Bahianita.glyphs` and `Bahianita/sources/Bahianita.ufo`.

An override config.yaml needs to be created in the google/fonts family directory referencing `Bahianita/sources/Bahianita.glyphs`.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2018-08-07 14:03:43 +0100
- Commit message: "Fixed bad glyph names and vertical metrics"
- Source files at commit: `Bahianita/sources/Bahianita.glyphs`, `Bahianita/sources/Bahianita.ufo`, `Bahianita/sources/Backup/` (containing older versions)

## Confidence

**High**: PR #1669 explicitly references commit `e96af69`. The commit exists in the upstream repo and pre-dates the PR merge. The PR was merged on 2019-06-12 in google/fonts, and the referenced commit is from 2018-08-07. While two later commits exist in the repo, the PR explicitly named this commit as the source.

**Note**: The tracking file should be corrected from `0efedac` to `e96af69`.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Bahianita/sources/Bahianita.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The METADATA.pb has no source block — a PR to google/fonts is needed to add `source { repository_url, commit, branch }`.
2. An override config.yaml needs to be created. The source path would be `Bahianita/sources/Bahianita.glyphs` (relative to repo root).
3. The tracking file commit should be corrected from `0efedac` (HEAD) to `e96af69` (the commit actually referenced in PR #1669).
