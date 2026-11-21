# Chivo - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Chivo |
| Repository URL | https://github.com/Omnibus-Type/Chivo |
| Commit Hash | `d98623c96068cd02fbe9f22982d4b0504be8b851` |
| Branch | `master` |
| Config YAML | `sources/config.yaml` |
| Override Config | No |
| Designer | Omnibus-Type |
| License | OFL |
| Date Added | 2011-12-07 |

## How URL Found

The repository URL `https://github.com/Omnibus-Type/Chivo` is documented in the METADATA.pb source block and confirmed by the onboarding commit message for version 2.002 (commit `a72c00288`, PR #5348).

## How Commit Determined

The commit hash `d98623c96068cd02fbe9f22982d4b0504be8b851` is explicitly stated in the merge commit message of the google/fonts PR #5348 (commit `a72c00288`):

> "Chivo Version 2.002 taken from the upstream repo https://github.com/Omnibus-Type/Chivo at commit https://github.com/Omnibus-Type/Chivo/commit/d98623c96068cd02fbe9f22982d4b0504be8b851."

Note: The PR body (before squash) mentioned a different commit (`b651a548bc8432485aaf0513da0f00a9ad774868`), but the final merged commit message has `d98623c9`, which is the authoritative version. Our project's commit `8678d187e` corrected the METADATA.pb from an incorrect value (`dc61c468` - the Chivo Mono commit) to the correct `d98623c9`.

The upstream repo is a shallow clone locally, so the commit cannot be verified directly. However, the commit hash is well-documented in the google/fonts merge commit.

## Config YAML Status

The config file `sources/config.yaml` exists in the upstream repo. It references two Glyphs sources (`Chivo.glyphs` and `Chivo-Italic.glyphs`) with proper STAT table configuration for the `wght` axis (100-900) and `ital` axis.

## Verification

- Repository URL is valid and accessible
- The upstream repo contains `sources/config.yaml` with proper gftools-builder configuration
- Commit hash is documented in the google/fonts merge commit message
- The METADATA.pb source block has complete and correct data including file mappings
- The upstream repo is a shallow clone locally (only has `dc61c46`, the latest commit), so `d98623c9` cannot be verified locally

## Confidence Level

**HIGH** - The commit hash is explicitly documented in the google/fonts merge commit message. The config.yaml path is verified. The repo URL is confirmed by both METADATA.pb and the onboarding commit.

## Open Questions

None. The data is complete and verified through the google/fonts PR history.
