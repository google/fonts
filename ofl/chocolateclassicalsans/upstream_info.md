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


## Source-metadata correction (2026-06-02) — override config from the committed .ufoz (KNOWN-INCOMPLETE)

**Model**: Claude Opus 4.8

fontc_crater reported `missing source 'temp/ChocolateClassicalSans-Regular.ufo'`: the upstream `source/config.yaml` declares `temp/ChocolateClassicalSans-Regular.ufo`, which the repo's build.sh produces at build time by extracting the committed `source/ChocolateClassicalSans-Regular.ufoz` and then `.gitignore`s. fontc_crater never runs build.sh, so the source appears absent.

An override `config.yaml` was added in this family directory that declares the committed `source/ChocolateClassicalSans-Regular.ufoz` (a zipped UFO) directly, with the path relative to the repository root.

Dependencies:
- **fontmake** already reads `.ufoz`. The fontc / fontc_crater path additionally needs **[googlefonts/fontc#2028](https://github.com/googlefonts/fontc/pull/2028)** (ufo2fontir reads `.ufoz`) and **[googlefonts/gftools#1192](https://github.com/googlefonts/gftools/pull/1192)** (gftools.builder recognises `.ufoz`).

### ⚠ Still-unaddressed issue: the Font Creator post-processing is not applied

The committed `.ufoz` is a **raw Font Creator 15 export**. The upstream build does not build it directly — it first runs `source/fcp_ufo_process.py` on the extracted UFO, which:
- strips a UTF-8 BOM from the UFO's XML files,
- repairs `fontinfo.plist` (adds the missing `encodingID` after `platformID`),
- corrects invalid `features.fea` data,
- sets `useTypoMetrics`, the version number, and fixes localized name records, and
- adds the `public.openTypeMeta` and `BASE` tables.

Several of these are **parse-breaking defects** (BOM, malformed plist/fea), so building directly from the raw `.ufoz` will likely **fail**, and even if it builds it will **differ substantially** from the shipped binary (missing the meta/BASE tables, the metric and version overrides, and the name fixes). This override therefore only addresses the *target-discovery* (`missing source`) failure; it is **not** a reproducible build.

A complete fix requires an **upstream PR** that commits the processed UFO (the output of `fcp_ufo_process.py`, conventionally under `sources/generated/`) and points the config at it.
