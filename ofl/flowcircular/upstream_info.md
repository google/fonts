# Flow Circular

**Date investigated**: 2026-02-27
**Status**: missing_commit
**Designer**: Dan Ross
**METADATA.pb path**: `ofl/flowcircular/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/HYPD/flow-typeface |
| Commit | `44f3478408936f5240cbc4fb3f7b4ed19d22822e` |
| Config YAML | `Circular/sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/HYPD/flow-typeface` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by:
- The copyright string in the font files: "Copyright 2020 The Flow Project Authors (https://github.com/HYPD/flow-typeface)"
- The gftools-packager commit message in google/fonts PR #3957, which explicitly references this URL
- The DESCRIPTION.en_us.html file, which links to `github.com/HYPD/flow-typeface`

## How the Commit Hash Was Identified

The commit hash `44f3478408936f5240cbc4fb3f7b4ed19d22822e` was identified from the gftools-packager onboarding commit in google/fonts. The onboarding commit `4eafa0895` (PR #3957, 2021-10-22, by Rosalie Wagner) states: "Flow Circular Version 1.101; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/HYPD/flow-typeface at commit https://github.com/HYPD/flow-typeface/commit/44f3478408936f5240cbc4fb3f7b4ed19d22822e."

This commit (`44f3478`) is the HEAD of the upstream repository's main branch. It is a merge commit with the message "Merge pull request #1 from RosaWagner/main - Ready for GF", dated 2021-10-21. This is the most recent (and final) commit in the upstream repository; no further commits have been made since.

**Binary verification**: The TTF file in google/fonts (`ofl/flowcircular/FlowCircular-Regular.ttf`) has an identical SHA-256 hash to the file at `Circular/fonts/ttf/FlowCircular-Regular.ttf` in the upstream repo at this commit, confirming the match.

## Build Configuration

The upstream repository contains a valid `config.yaml` at `Circular/sources/config.yaml`:
```yaml
sources:
    - FlowCircular.glyphs
buildVariable: False
```

This is a gftools-builder configuration that builds from `FlowCircular.glyphs` as a static (non-variable) font. The repository also includes a `build.sh` script that runs `gftools builder Circular/sources/config.yaml` (along with the other two Flow families).

The METADATA.pb correctly references this config path in the `config_yaml` field.

## Relationship to Other Flow Families

Flow Circular shares the `HYPD/flow-typeface` repository with Flow Block and Flow Rounded. The repository is organized with separate directories for each variant:
- `Block/` - Flow Block sources and fonts
- `Circular/` - Flow Circular sources and fonts
- `Rounded/` - Flow Rounded sources and fonts

All three families were onboarded simultaneously in google/fonts PR #3957 on 2021-10-22, all from the same upstream commit `44f3478`.

## Timeline

- **2021-10-21**: Upstream commit `44f3478` (merge of PR #1 from RosaWagner, "Ready for GF")
- **2021-10-22**: All three Flow families onboarded to google/fonts by Rosalie Wagner in PR #3957 (commit `4eafa0895`)
- **2026-02-20**: config_yaml field added to METADATA.pb (commit `5ddf312e6`)

## Issues Found

**Missing commit hash in METADATA.pb**: The METADATA.pb for Flow Circular on upstream/main is missing the `commit` field in the source block. The sibling family Flow Block already has this commit hash recorded (`44f3478408936f5240cbc4fb3f7b4ed19d22822e`), but it was not added for Flow Circular. The commit hash should be added to complete the source metadata.

All other fields (repository_url, config_yaml, branch, file mappings) are present and correct.
