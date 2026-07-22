# Alumni Sans SC

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: needs_correction
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alumnisanssc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alumni |
| Commit | `44a7998fa2bfa1b3e119983cdc565dd7f0f03bda` |
| Config YAML | `sources/config.yml` (INCORRECT for SC variant -- see below) |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/alumni` was set in the METADATA.pb since the original onboarding commit `521d1cdf` by Simon Cozens on 2024-05-27. The google/fonts commit message explicitly states: "Taken from the upstream repo https://github.com/googlefonts/alumni at commit https://github.com/googlefonts/alumni/commit/44a7998fa2bfa1b3e119983cdc565dd7f0f03bda." The repo is verified and cached at `googlefonts/alumni`.

This repository is shared with the non-SC "Alumni Sans" family (`ofl/alumnisans/`), which uses the same repo URL and commit hash.

## How the Commit Hash Was Identified

The commit hash `44a7998fa2bfa1b3e119983cdc565dd7f0f03bda` was recorded in the onboarding commit message and in the METADATA.pb source block since the initial onboarding (PR #7768, merged 2024-06-19). The commit exists in the upstream repo and is the HEAD (and only) commit on the master branch, authored by Viviana Monsalve on 2021-12-18 with message "one blank line added to the OFL."

The commit hash is correct -- it represents the state of the upstream repo from which the SC fonts were built.

## How Config YAML Was Resolved

**The `config_yaml: "sources/config.yml"` field is INCORRECT for the Alumni Sans SC family.**

The upstream `sources/config.yml` at the referenced commit defines:
- `familyName: "Alumni Sans"` (NOT "Alumni Sans SC")
- Output files: `AlumniSans[wght].ttf` and `AlumniSans-Italic[wght].ttf` (NOT AlumniSansSC)
- Sources: `AlumniSans.glyphs` and `AlumniSans-Italic.glyphs`

This config correctly builds the non-SC "Alumni Sans" family, but does NOT produce the "Alumni Sans SC" variant.

The `config_yaml` field was added by the "Batch 1/4" commit (`19cdcec5`, 2025-03-31) which ported data from fontc_crater's targets.json. The fontc_crater targets list has this config_yaml for the alumni repo, but it is only valid for building the non-SC "Alumni Sans" family. The same config_yaml was applied to the SC variant in error.

### How the SC Fonts Were Actually Built

PR #7768 includes a comment from Simon Cozens stating: "This is a serious PR, but it is also a test of the **small caps builder** and the `gftools-packager --build-from-source` option."

This confirms the AlumniSansSC binaries were generated using gftools-packager's `--build-from-source` flag with its built-in small caps builder feature. The small caps builder takes the regular Alumni Sans sources (which contain `.sc` glyphs and `smcp`/`c2sc` OpenType features) and produces a separate "Small Caps" font family where the small caps glyphs replace the default lowercase forms.

### Incorrect source_file Paths

The METADATA.pb source block references:
- `source_file: "fonts/variable/AlumniSansSC[wght].ttf"`
- `source_file: "fonts/variable/AlumniSansSC-Italic[wght].ttf"`

These file paths **do not exist** in the upstream repository at the referenced commit (or at any commit). The upstream repo only contains `fonts/variable/AlumniSans[wght].ttf` and `fonts/variable/AlumniSans-Italic[wght].ttf`. The SC binaries were built at packaging time by gftools-packager, not pulled from pre-existing files in the upstream repo.

## Issues Found

1. **`config_yaml` is incorrect**: `sources/config.yml` builds "Alumni Sans", not "Alumni Sans SC". This config cannot be used to reproduce the SC fonts. The SC fonts require a separate build configuration that invokes the small caps builder.

2. **`source_file` paths are invalid**: The referenced paths (`fonts/variable/AlumniSansSC[wght].ttf` and `AlumniSansSC-Italic[wght].ttf`) do not exist in the upstream repository. The fonts were built from source at packaging time, not copied from pre-built binaries.

3. **No override config.yaml exists** in the google/fonts family directory to build the SC variant.

## Conclusion

The repository URL and commit hash are correct -- the SC fonts were built from the same upstream sources as the non-SC "Alumni Sans" at commit `44a7998`. However, the current METADATA.pb has two problems:

1. The `config_yaml: "sources/config.yml"` field (added by the Batch 1/4 commit) is incorrect for this family. That config only builds the non-SC variant. It should either be removed or replaced with a config that produces the SC variant.

2. The `source_file` paths reference files that do not exist in the upstream repo.

To properly fix this, an override `config.yaml` would need to be created in the google/fonts family directory that uses gftools-builder's small caps builder to produce `AlumniSansSC[wght].ttf` and `AlumniSansSC-Italic[wght].ttf` from the upstream `.glyphs` sources. The `config_yaml` field would then be removed from METADATA.pb (since google-fonts-sources auto-detects local overrides).

This family needs correction. The status is **needs_correction** due to the incorrect config_yaml and invalid source_file paths.
