# Climate Crisis - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Climate Crisis |
| Designer | Daniel Coull, Eino Korkala |
| Repository URL | https://github.com/dancoull/ClimateCrisis |
| Commit Hash | `8e3882135dddeb43f582ae88f337589dbba625f4` (updated Feb 2026) |
| Original Onboarding Commit | `e0398e2d7e84a9f08cf7ec67bb463e4e2bb35431` |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Status | Complete |
| Date Added | 2022-09-30 |

## How URL Found

The repository URL `https://github.com/dancoull/ClimateCrisis` was documented in the METADATA.pb source block from the original onboarding PR.

## How Commit Determined

### Original Onboarding (Version 1.003)

PR #5350 ("Climate Crisis: Version 1.003 added", by Rosalie Wagner, 2022-10-06) explicitly states: "Climate Crisis Version 1.003 taken from the upstream repo https://github.com/dancoull/ClimateCrisis at commit https://github.com/dancoull/ClimateCrisis/commit/e0398e2d7e84a9f08cf7ec67bb463e4e2bb35431."

Commit `e0398e2` ("Merge pull request #4 from RosaWagner/main", dated 2022-09-28) is the original onboarding commit.

### Recent Update (Version 1.007)

Commit `9eabeac10` in google/fonts ("Climate Crisis: Version 1.007 added", by Emma Marichal, 2026-02-20) updated the font to a new version, referencing upstream commit `8e38821` ("Merge pull request #9 from emmamarichal/main"). The METADATA.pb was updated to reflect this new commit hash.

The current METADATA.pb now records commit `8e38821` as the source commit, with `sources/config.yaml` as the config path and `main` as the branch.

## Config YAML Status

- **config.yaml exists in upstream**: Located at `sources/config.yaml` in the upstream repository.
- **No override config.yaml**: Not needed since the upstream has the config file.
- **METADATA.pb records**: `config_yaml: "sources/config.yaml"` and `branch: "main"`

Config.yaml at the latest commit (`8e38821`) references:
```yaml
sources:
  - ClimateCrisis.glyphs
buildOTF: False
cleanUp: true
axisOrder:
  - YEAR
familyName: "Climate Crisis"
```

The config also includes STAT table definitions and fvar instance overrides for the YEAR axis.

## Verification

- Original onboarding commit `e0398e2` verified to exist in upstream repo
- Latest commit `8e38821` verified to exist in upstream repo (tip of origin/main)
- `sources/config.yaml` confirmed present at both the original and latest commits
- `sources/ClimateCrisis.glyphs` confirmed as the source file referenced by config.yaml
- The variable font uses a custom `YEAR` axis (range 1979-2050) representing climate data

## Confidence Level

**High** - Both the original onboarding and the recent update are explicitly documented in google/fonts commit messages with upstream commit references. The config.yaml is present in the upstream repository and correctly referenced in METADATA.pb.

## Open Questions

None. The tracking data should be updated to reflect the latest commit hash `8e3882135dddeb43f582ae88f337589dbba625f4` which is now recorded in the current METADATA.pb in google/fonts.
