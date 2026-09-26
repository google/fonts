# Belanosima - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Belanosima |
| Repository URL | https://github.com/docrepair-fonts/belanosima-fonts |
| Commit Hash | b772e9b7c44f32e17230f255fac9cac4bfaaa07f |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | DISPLAY, SANS_SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/docrepair-fonts/belanosima-fonts` is documented in the METADATA.pb `source {}` block and also referenced in the copyright strings of all font files ("Copyright 2023 The Belanosima Project Authors (https://github.com/docrepair-fonts/belanosima-fonts)"). The font was onboarded via gftools-packager, which explicitly recorded the upstream URL.

## How the Commit Hash Was Determined

The commit hash `b772e9b7c44f32e17230f255fac9cac4bfaaa07f` was explicitly recorded in the gftools-packager commit message in google/fonts (commit `88dec8c4d`):

> [gftools-packager] Belanosima: Version 2.000 added
> Belanosima Version 2.000 taken from the upstream repo https://github.com/docrepair-fonts/belanosima-fonts at commit https://github.com/docrepair-fonts/belanosima-fonts/commit/b772e9b7c44f32e17230f255fac9cac4bfaaa07f.

Cross-verification confirms this is the only commit in the upstream repository, dated 2023-06-14, which matches the google/fonts onboarding date (date_added: 2023-06-14). The commit message in the upstream repo is "New fonts".

## Config YAML Status

The upstream repo has `sources/config.yaml` at the recorded commit. Its contents:

```yaml
---
buildOTF: false
buildVariable: false
familyName: Belanosima
outputDir: ../fonts
sources:
  - Belanosima-Regular.designspace
```

This is properly referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`.

## Verification

- Commit hash `b772e9b` exists in the upstream repo and is verified as the only commit
- `sources/config.yaml` exists at that commit with valid gftools-builder configuration
- The upstream repo contains `.designspace` source files
- The onboarding date in METADATA.pb (2023-06-14) matches the upstream commit date exactly
- Author of the google/fonts commit was Yanone (post@yanone.de)
- The `files {}` mappings in METADATA.pb correctly reference the font files in the upstream repo

## Confidence Level

**High** - The gftools-packager commit explicitly references this exact commit hash, and it's the only commit in the upstream repository. All dates are consistent.

## Open Questions

None. This family is fully documented and verified.
