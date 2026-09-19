# 42dot Sans

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: 42dot
**METADATA.pb path**: `ofl/42dotsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/42dot/42dot-Sans |
| Commit | `d23e87fe44d5b4f5afaa9dca9d5926d7c414d625` |
| Config YAML | sources/config_variable.yaml |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/42dot/42dot-Sans` was already present in the METADATA.pb source block. It is also referenced in the font's copyright string within METADATA.pb: `"Copyright 2024 The 42dot Sans Project Authors (https://github.com/42dot/42dot-Sans)."` The original onboarding commit (`d60948acd`) in google/fonts explicitly states: "Taken from the upstream repo https://github.com/42dot/42dot-Sans". The upstream repo is cached locally and confirmed accessible.

## How the Commit Hash Was Identified

The commit hash `d23e87fe44d5b4f5afaa9dca9d5926d7c414d625` is directly referenced in the original google/fonts onboarding commit (`d60948acd`, dated 2024-12-23). The onboarding commit message reads:

> Taken from the upstream repo https://github.com/42dot/42dot-Sans at commit https://github.com/42dot/42dot-Sans/commit/d23e87fe44d5b4f5afaa9dca9d5926d7c414d625

The upstream commit is dated 2024-12-23 05:50:28 (PST), and the google/fonts onboarding commit is dated 2024-12-23 05:51:32 (PST) -- just one minute later. This tight timing strongly confirms that `d23e87fe` was the exact commit used for onboarding.

The upstream commit (by Aaron at sajatypeworks.com) is titled "Adding some metadata" and updated font binary files and fontinfo metadata. It was the most recent commit in the upstream repo at the time of onboarding.

The source block (commit hash, config_yaml, branch) was added to METADATA.pb later by Felipe Sanches in commit `da0442cc` (2025-03-31), referencing PR #8772.

## How Config YAML Was Resolved

The config file `sources/config_variable.yaml` exists at the referenced commit `d23e87fe`. Its contents are:

```yaml
sources:
  - 42dotSans.designspace
familyName: 42dot Sans
autohintTTF: False
buildOTF: False
buildStatic: False
buildVariable: True
buildWebfont: False
removeOutlineOverlaps: False
```

This configuration builds a variable font from `42dotSans.designspace`, which aligns with the single variable font file `42dotSans[wght].ttf` found in google/fonts. No override config.yaml exists in the google/fonts family directory.

## Notable History

The font underwent a rename in google/fonts: commit `db2611132` (2025-04-30) renamed it from "42dotSans" to "AstaSans" (moving files from `ofl/42dotsans/` to `ofl/astasans/`). This corresponded to upstream commit `52c07071` ("name update 42dot Sans -> Asta Sans", 2025-04-22). However, this was subsequently reverted -- commit `572407623` (2025-05-02) re-added the `ofl/42dotsans/` directory from the main branch, restoring the original "42dot Sans" family. As a result, both `ofl/42dotsans/` and `ofl/astasans/` may coexist in the repository, but `42dotsans` is the canonical directory.

## Conclusion

The source metadata for 42dot Sans is **complete** with **HIGH confidence**. The commit hash is explicitly documented in the original onboarding commit message and the timestamps align precisely (1-minute gap). The config file exists at the specified path in the upstream repo at the referenced commit. All three key fields (repository_url, commit, config_yaml) are correct and verified.
