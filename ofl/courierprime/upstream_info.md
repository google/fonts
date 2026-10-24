# Courier Prime

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Alan Dague-Greene
**METADATA.pb path**: `ofl/courierprime/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/quoteunquoteapps/CourierPrime |
| Commit | `7fd585a2dd4c1612c79b3308e300923d1c13df93` |
| Config YAML | Override config.yaml in google/fonts |
| Branch | (default) |

## How the Repository URL Was Found

The repository URL `https://github.com/quoteunquoteapps/CourierPrime` was added to the METADATA.pb source block by Simon Cozens in commit `cd5db6b6e` ("Update upstreams", 2023-12-14). The URL matches the copyright string in the font files: "Copyright 2015 The Courier Prime Project Authors (https://github.com/quoteunquoteapps/CourierPrime)."

## How the Commit Hash Was Identified

The commit hash `7fd585a2dd4c1612c79b3308e300923d1c13df93` is HEAD of the upstream repository. This is a merge commit ("Merge pull request #7 from vv-monsalve/master") dated 2019-12-05, the same day the font was added to Google Fonts via the Font Bakery Dashboard create commit `cc9ce5318` (2019-12-05). The TTF files at this commit in the upstream repo are byte-identical to those in google/fonts, confirming this is the correct onboarding commit.

The commit hash was added to METADATA.pb in the pending PR branch `felipesanches/sources_info_2026-02-25` (commit `4fd9e2392`, "Add source metadata to 125 METADATA.pb files"), not yet merged to google/fonts main.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. An override `config.yaml` exists in the google/fonts family directory (`ofl/courierprime/config.yaml`), referencing the Glyphs sources:
```yaml
sources:
  - sources/Courier Prime.glyphs
  - sources/Courier Prime Italic.glyphs
```

The upstream repo has `.glyphs` source files at `sources/Courier Prime.glyphs` and `sources/Courier Prime Italic.glyphs`. Since an override config exists locally, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (HEAD)
- Commit date: 2019-12-05 14:38:47 -0600
- Commit message: "Merge pull request #7 from vv-monsalve/master"
- Font files match: Yes (TTFs are byte-identical between upstream and google/fonts)
- Source files at commit: `sources/Courier Prime.glyphs`, `sources/Courier Prime Italic.glyphs`
- Override config.yaml: Present in `ofl/courierprime/config.yaml`

## Confidence

**High**: The repository URL is confirmed by the copyright string. The commit hash matches HEAD, which was created on the same day as the google/fonts onboarding. TTF files are byte-identical between upstream and google/fonts. The override config.yaml references the correct source files.

## Open Questions

None. This family is fully documented and verified.
