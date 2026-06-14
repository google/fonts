# Chivo Mono - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Chivo Mono |
| Repository URL | https://github.com/Omnibus-Type/Chivo |
| Commit Hash | `dc61c468d79781eb5183426e88e844af16cdc3e5` |
| Branch | `master` |
| Config YAML | `sources/configmono.yaml` |
| Override Config | No |
| Designer | Omnibus-Type |
| License | OFL |
| Date Added | 2022-11-03 |

## How URL Found

The repository URL `https://github.com/Omnibus-Type/Chivo` is the same repository used for both Chivo and Chivo Mono families. It is documented in the METADATA.pb source block and confirmed by both the google/fonts merge commit and PR #5539.

## How Commit Determined

The commit hash `dc61c468d79781eb5183426e88e844af16cdc3e5` is explicitly stated in both the google/fonts merge commit (commit `5b62bc464`, PR #5539) and the PR body:

> "Chivo Mono Version 1.008 taken from the upstream repo https://github.com/Omnibus-Type/Chivo at commit https://github.com/Omnibus-Type/Chivo/commit/dc61c468d79781eb5183426e88e844af16cdc3e5."

This commit is verified to exist in the local clone as it is the HEAD of the master branch (the most recent commit in the repo). The commit message is "Merge pull request #5 from emmamarichal/master".

Note: This same commit (`dc61c46`) was also the latest commit in the repo, so both Chivo and Chivo Mono source from the same repository but at different commits.

## Config YAML Status

The config file `sources/configmono.yaml` exists in the upstream repo. It was initially incorrectly set to `sources/config.yaml` in METADATA.pb (which is the Chivo non-mono config). Our project's commit `5f125d9e6` corrected it to `sources/configmono.yaml`.

The config references `ChivoMono.glyphs` and `ChivoMono-Italic.glyphs` with proper STAT table configuration for `wght` (100-900) and `ital` axes.

## Verification

- Repository URL is valid and accessible
- Commit `dc61c46` exists in the local clone as HEAD of master
- `sources/configmono.yaml` exists and contains correct gftools-builder configuration for Chivo Mono
- The METADATA.pb source block has complete and correct data including file mappings
- Both the PR body and the merge commit message confirm the same commit hash

## Confidence Level

**HIGH** - All data is fully verified. The commit hash is confirmed by both the PR and merge commit, and it can be verified locally as it is the HEAD of the upstream repo.

## Open Questions

None. The data is complete and verified.
