# Borel

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Rosalie Wagner
**METADATA.pb path**: `ofl/borel/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/RosaWagner/Borel |
| Commit | `68b8266ec6b70c4753b46753c8b103d2ee50b7c8` |
| Config YAML | `Borel/sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/RosaWagner/Borel` was present from the initial font onboarding. The earliest gftools-packager commit `f5e738c9c` (2023-07-07) by Rosalie Wagner herself references this URL: "Borel Version 1.004 taken from the upstream repo https://github.com/RosaWagner/Borel". This also matches the copyright string in the font files.

## How the Commit Hash Was Identified

The current commit hash `68b8266ec6b70c4753b46753c8b103d2ee50b7c8` corresponds to the latest font update (Version 1.008), added in google/fonts commit `8c949834a` by Marc Foley (2025-10-22) via PR #9926. The commit message states: "Taken from the upstream repo https://github.com/RosaWagner/Borel at commit https://github.com/RosaWagner/Borel/commit/68b8266ec6b70c4753b46753c8b103d2ee50b7c8."

The `config_yaml` field was added in a subsequent commit `5b7605895` by Felipe Sanches ("sources info for Borel: Version 1.008 (PR #9926)", 2025-10-22).

The Borel font has been through multiple updates:

1. **v1.004** (2023-07-07, PR #6513): commit `f6e1e35c95b7af91a6be7294e5e9a2b38858b8bb`
2. **v1.005** (2023-10-10, PR #6846): commit `dd3d42ca23056f23889e31cde0af0081da3d847d`
3. **v1.008** (2025-10-22, PR #9926): commit `68b8266ec6b70c4753b46753c8b103d2ee50b7c8` (current)

The recorded commit `68b8266` is verified in the upstream repo with message "Fixed spacing of t and few kerning pairs".

## How Config YAML Was Resolved

The config file `Borel/sources/config.yaml` exists in the upstream repository at the recorded commit. Note the nested directory structure -- the repo has a `Borel/` subdirectory containing the font project. Contents:

```yaml
sources:
  - Borel.glyphs
familyName: "Borel"
buildOTF: true
buildVariable: false
buildWebfont: true
autohintOTF: true
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit message: "Fixed spacing of t and few kerning pairs"
- Source files at commit: `Borel/sources/Borel.glyphs`, `Borel/sources/config.yaml`
- Config.yaml present: Yes at `Borel/sources/config.yaml`
- No override config.yaml in google/fonts family directory
- Font update history traced through 3 versions with consistent upstream references

## Confidence

**High**: The repository URL has been consistent across all three font versions and is confirmed by the designer (Rosalie Wagner) herself, who authored the initial onboarding commits. The commit hash is well-documented in both the google/fonts commit message and the PR. The config.yaml is present and valid. All data is fully corroborated.

## Open Questions

None. All source data is well-documented and verified.
