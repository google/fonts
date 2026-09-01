# Flow Block

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Dan Ross
**METADATA.pb path**: `ofl/flowblock/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/HYPD/flow-typeface |
| Commit | `44f3478408936f5240cbc4fb3f7b4ed19d22822e` |
| Config YAML | `Block/sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/HYPD/flow-typeface` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by:
- The copyright string in the font files: "Copyright 2020 The Flow Project Authors (https://github.com/HYPD/flow-typeface)"
- The gftools-packager commit message in google/fonts PR #3957, which explicitly references this URL
- The DESCRIPTION.en_us.html file, which links to `github.com/HYPD/flow-typeface`

## How the Commit Hash Was Identified

The commit hash `44f3478408936f5240cbc4fb3f7b4ed19d22822e` was identified from the gftools-packager onboarding commit in google/fonts. The onboarding commit `4eafa0895` (PR #3957, 2021-10-22, by Rosalie Wagner) states: "Flow Block Version 1.101; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/HYPD/flow-typeface at commit https://github.com/HYPD/flow-typeface/commit/44f3478408936f5240cbc4fb3f7b4ed19d22822e."

This commit (`44f3478`) is the HEAD of the upstream repository's main branch. It is a merge commit with the message "Merge pull request #1 from RosaWagner/main - Ready for GF", dated 2021-10-21. This is the most recent (and final) commit in the upstream repository; no further commits have been made since.

**Binary verification**: The TTF file in google/fonts (`ofl/flowblock/FlowBlock-Regular.ttf`) has an identical SHA-256 hash to the file at `Block/fonts/ttf/FlowBlock-Regular.ttf` in the upstream repo at this commit, confirming the match.

The METADATA.pb already contained this commit hash, having been set by a prior enrichment commit (`6d43afe79`, 2025-09-18).

## Build Configuration

The upstream repository contains a valid `config.yaml` at `Block/sources/config.yaml`:
```yaml
sources:
    - FlowBlock.glyphs
buildVariable: False
```

This is a gftools-builder configuration that builds from `FlowBlock.glyphs` as a static (non-variable) font. The repository also includes a `build.sh` script that runs `gftools builder Block/sources/config.yaml` (along with the other two Flow families).

The METADATA.pb correctly references this config path in the `config_yaml` field.

## Relationship to Other Flow Families

Flow Block shares the `HYPD/flow-typeface` repository with Flow Circular and Flow Rounded. The repository is organized with separate directories for each variant:
- `Block/` - Flow Block sources and fonts
- `Circular/` - Flow Circular sources and fonts
- `Rounded/` - Flow Rounded sources and fonts

All three families were onboarded simultaneously in google/fonts PR #3957 on 2021-10-22, all from the same upstream commit `44f3478`.

## Timeline

- **2021-10-21**: Upstream commit `44f3478` (merge of PR #1 from RosaWagner, "Ready for GF")
- **2021-10-22**: All three Flow families onboarded to google/fonts by Rosalie Wagner in PR #3957 (commit `4eafa0895`)
- **2025-09-18**: Commit hash added to METADATA.pb source block (commit `6d43afe79`)

## Issues Found

None. The METADATA.pb on upstream/main has the correct repository URL, commit hash, config_yaml path, and branch. The source block is complete with file mappings. No further action needed.
