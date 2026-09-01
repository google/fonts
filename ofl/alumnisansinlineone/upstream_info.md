# Alumni Sans Inline One

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alumnisansinlineone/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alumni-sans-inline |
| Commit | `81ea544e0ce487475c75df9545cd3df946c7ba26` |
| Config YAML | `sources/config.yml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/alumni-sans-inline` is recorded in the METADATA.pb `source` block. It was also referenced in the original onboarding commit message in google/fonts (`d2ed457c9`, PR #4331, 2022-02-25), which explicitly states the fonts were "taken from the upstream repo https://github.com/googlefonts/alumni-sans-inline". The copyright strings in METADATA.pb also reference this repository. The upstream repo is cached at `googlefonts/alumni-sans-inline` and its remote URL matches.

## How the Commit Hash Was Identified

The commit hash `81ea544e0ce487475c75df9545cd3df946c7ba26` is recorded in the METADATA.pb `source` block. It was explicitly referenced in the onboarding commit message (google/fonts commit `d2ed457c9`, PR #4331): "at commit https://github.com/googlefonts/alumni-sans-inline/commit/81ea544e0ce487475c75df9545cd3df946c7ba26".

Verification confirms this is correct:
- The upstream repo has only a single commit (`81ea544`), so there is no ambiguity.
- The binary TTF files in google/fonts are byte-identical (matching MD5 hashes) to those at this commit in the upstream repo:
  - `AlumniSansInlineOne-Regular.ttf`: `abc90e65e2f85dda81124fa349d12f95`
  - `AlumniSansInlineOne-Italic.ttf`: `ac82364c08ebed38f107259b968f840a`
- The onboarding date (2022-02-25) and commit date (2022-02-24) are consistent.

## How Config YAML Was Resolved

The config file `sources/config.yml` exists at the referenced commit in the upstream repo. It contains a valid gftools-builder configuration:

```yaml
sources:
  - AlumniSansInline.glyphs
  - AlumniSansInline-Italic.glyphs
familyName: "Alumni Sans Inline One"
buildVariable: false
```

The `config_yaml: "sources/config.yml"` field in METADATA.pb correctly points to this file. No override config.yaml exists in the google/fonts family directory.

## Conclusion

This family's source metadata is fully complete and verified. The upstream repository has a single commit which matches the referenced hash. Binary files are byte-identical between google/fonts and the upstream repo. The config.yml is present in the upstream repo at the documented path. No changes are needed.
