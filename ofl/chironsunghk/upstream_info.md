# Chiron Sung HK - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Chiron Sung HK |
| Repository URL | https://github.com/chiron-fonts/chiron-sung-hk |
| Commit Hash | `65b752caf7698f9e773991fda674152c4bce21fb` |
| Branch | `source` |
| Config YAML | `scripts/config.yaml` |
| Override Config | No |
| Designer | Tamcy |
| License | OFL |
| Date Added | 2025-05-17 |

## How URL Found

The repository URL `https://github.com/chiron-fonts/chiron-sung-hk` was set in the original METADATA.pb when the family was onboarded (commit `83ae20a53`). The onboarding commit message mentions a source fork `https://github.com/aaronbell/chiron-sung-hk`, but the METADATA.pb and copyright string both point to the canonical `chiron-fonts` organization repo.

## How Commit Determined

The commit hash `65b752caf7698f9e773991fda674152c4bce21fb` is explicitly stated in the onboarding commit message in google/fonts (commit `83ae20a53`):

> "Taken from https://github.com/aaronbell/chiron-sung-hk (source fork) at commit 65b752caf7698f9e773991fda674152c4bce21fb."

The commit was verified to exist in the upstream repo on the `remotes/origin/source` branch. The commit message is "Implementing GF version" by Aaron (2025-05-17), which created the Google Fonts build configuration and compiled variable fonts.

Note: The commit hash was not in the original METADATA.pb on main. It was added by our project's PR (commit `4fd9e2392` on branch `sources_info_2026-02-25`), not yet merged.

## Config YAML Status

The config file `scripts/config.yaml` exists at commit `65b752caf7698f9e773991fda674152c4bce21fb` on the `source` branch. It was created as part of the same commit that implemented the Google Fonts build system. The config references two designspace sources (ChironSungHK.designspace and ChironSungHK-Italic.designspace) and includes proper STAT table definitions.

## Verification

- Repository URL is valid and accessible
- Commit `65b752c` exists in the upstream repo on `remotes/origin/source` branch
- The commit is correctly on the `source` branch, matching METADATA.pb `branch: "source"`
- `scripts/config.yaml` exists at that commit with proper gftools-builder configuration
- Font files built from this commit match what was onboarded to google/fonts

## Confidence Level

**HIGH** - All data is fully verified. The commit hash is explicitly documented in the onboarding commit message and verified against the upstream repository.

## Open Questions

None. The data is complete and verified.
