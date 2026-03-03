# Chocolate Classical Sans - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Chocolate Classical Sans |
| Repository URL | https://github.com/MoonlitOwen/ChocolateSans |
| Commit Hash | `624ecb8064d34258383bcbb08521f9fa2af00124` |
| Branch | `main` |
| Config YAML | `source/config.yaml` |
| Override Config | No |
| Designer | Moonlit Owen |
| License | OFL |
| Date Added | 2024-05-14 |

## How URL Found

The repository URL has evolved. The original onboarding (commit `9351e1c8d`, 2024-05-14) used `https://github.com/aaronbell/ChocolateSans`, which was Aaron Bell's fork. The METADATA.pb was later updated to point to the canonical repository `https://github.com/MoonlitOwen/ChocolateSans`, which is the maintainer's repository.

## How Commit Determined

The commit hash `624ecb8064d34258383bcbb08521f9fa2af00124` corresponds to a commit from 2025-06-08 in the upstream repo by NightFurySL2001, with the message (in Chinese) "Upload built fonts". This is NOT the original onboarding commit.

### History of font binary updates in google/fonts:

1. **2024-05-14** - Original onboarding (v1.001) from `aaronbell/ChocolateSans` at commit `ce0c3c54`
2. **2024-05-15** - Font and metadata update
3. **2024-12-06** - Font binary update
4. **2025-05-16** - Update to v1.197
5. **2025-05-20** - Update to v1.005 per Night's request
6. **2025-05-27** - Replace with version using existing metrics
7. **2025-06-09** - Latest font binary update (commit `968ef1ed4`)

The commit `624ecb80` in the upstream repo is from 2025-06-08, one day before the latest google/fonts font binary update on 2025-06-09. This confirms the commit was used for the latest font binary update.

Our project's commit `82613a55f` updated the METADATA.pb to reflect this current commit hash (from `0446a76d` to `624ecb80`) and corrected the config_yaml path (from `sources/project.yaml` to `sources/config.yaml`). A subsequent commit further corrected the path to `source/config.yaml` (without trailing 's').

## Config YAML Status

The config file `source/config.yaml` exists in the upstream repo at the referenced commit. Note the directory is `source/` (singular), not `sources/` (plural). The config references `temp/ChocolateClassicalSans-Regular.ufo` as the source, sets the family name, and specifies version 1.005.

## Verification

- Repository URL `https://github.com/MoonlitOwen/ChocolateSans` is valid and accessible
- Commit `624ecb80` exists in the upstream repo on the `main` branch
- `source/config.yaml` exists at that commit
- The commit is on the `main` branch, matching METADATA.pb `branch: "main"`
- The font binary from this commit was the basis for the latest update in google/fonts (2025-06-09)
- The METADATA.pb source block includes correct file mappings

## Confidence Level

**HIGH** - The commit hash is verified in the upstream repo and corresponds to the font binary update timeline in google/fonts. The config.yaml path is verified.

## Open Questions

None. The data is complete and verified.
