# Benne - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Benne |
| Repository URL | https://github.com/googlefonts/Benne |
| Commit Hash | 0e13f2e4e66eb5ed0076224b113398b78109748d |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/Benne` is embedded in the font copyright string ("Copyright 2015 The Benne Project Authors (https://github.com/googlefonts/Benne)") and was documented in the METADATA.pb source block from the time of onboarding. It was also referenced in gftools-packager commit messages in google/fonts PRs #2926 and #3096.

## How the Commit Hash Was Determined

The commit hash `0e13f2e4e66eb5ed0076224b113398b78109748d` was ported from fontc_crater's target.json in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

**Historical context**: The font went through two onboarding events in google/fonts:
1. **Version 1.000** (PR #2926): gftools-packager used commit `3fed638b3bd8c6229b54d3e5007fac10645a4b53` (upstream merge of PR #1 from yanone/master)
2. **Version 1.001** (PR #3096): gftools-packager used commit `4a7cc7e94f818114bfae7e04a731da7076efa0a0` (upstream merge of PR #2 from yanone/master)

The currently recorded commit `0e13f2e` ("Put description in usual place", 2024-04-09) is the HEAD of the repo and represents 5 additional commits after the last onboarding commit `4a7cc7e`:
- `c24c2d7` Rename Benne_Source
- `f99b186` Rename Sources -> sources
- `558ab33` Use a gftools-builder config (adds sources/config.yaml)
- `d814d1c` Rebuild fonts in our normal locations
- `0e13f2e` Put description in usual place

These later commits were made by Simon Cozens to set up gftools-builder infrastructure. The recorded commit `0e13f2e` was chosen for fontc_crater because it is the first version of the repo that has `config.yaml` and a proper build setup.

## Config YAML Status

- **`sources/config.yaml` exists** at the recorded commit `0e13f2e` with content:
  ```yaml
  familyName: Benne
  sources:
    - Benne-Regular.ufo
  ```
- The config.yaml was introduced in commit `558ab33` ("Use a gftools-builder config") by Simon Cozens on 2024-04-09
- No override config.yaml exists in google/fonts

## Verification

- Commit hash `0e13f2e` exists in the upstream repo and is HEAD of master
- `sources/config.yaml` is present and valid at this commit
- The METADATA.pb source block includes explicit file mappings, branch ("master"), and config_yaml path
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/Benne`
- Full commit history verified (83 commits total)

## Confidence Level

**High** - While the recorded commit (`0e13f2e`) differs from the original onboarding commit (`4a7cc7e`), it was intentionally set to HEAD for fontc_crater compatibility. The font file at this commit (from `d814d1c` "Rebuild fonts in our normal locations") should match the currently served version. The config.yaml and build setup are verified to exist and point to valid sources.

## Open Questions

- The font binary at commit `0e13f2e` (rebuilt by Simon Cozens) should be verified to match the font currently served in google/fonts
- The original onboarding commit `4a7cc7e` (Version 1.001, Feb 2021) is the historically correct reference for what was originally pushed to google/fonts
- Benne supports Kannada script (`primary_script: "Knda"`) - this is a specialized script that may need specific QA
