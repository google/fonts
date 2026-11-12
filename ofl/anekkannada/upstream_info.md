# Anek Kannada

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Confidence**: HIGH

## Designer

Ek Type

## Source Data

| Field | Value |
|---|---|
| repository_url | https://github.com/EkType/Anek |
| commit | 34074c6b406f4112e20c7ad10254a6e954d0324b |
| config_yaml | sources/AnekKannada/builder.yaml |

## Repository URL Verification

The repository URL `https://github.com/EkType/Anek` is confirmed valid. The cached clone at `EkType/Anek` has its remote set to this URL. The copyright field in METADATA.pb also references this repository: "Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)".

The Anek repository is a monorepo containing multiple Anek font families (Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Latin, Malayalam, Odia, Tamil, Telugu), each with its own sources and builder configuration under `sources/Anek{Script}/`.

## Commit Hash Verification

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is verified:

- **Exists in repo**: Yes, it is a valid commit object
- **Commit message**: "Merge pull request #3 from yanone/main"
- **Author**: Girish Dalvi
- **Date**: 2022-02-14
- **Position**: This is the HEAD of the `main` branch (the latest and final commit in the repo)

The google/fonts onboarding commit `8781cff48` (2022-02-18) has the message: "[gftools-packager] Anek Kannada: Version 1.003 added (#4279)". The commit body explicitly states: "Anek Kannada Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b."

The timeline is consistent: upstream commit on 2022-02-14, google/fonts onboarding on 2022-02-18 (4 days later). No additional upstream commits exist after the referenced hash, confirming this is the correct onboarding commit.

## Config Verification

The builder config at `sources/AnekKannada/builder.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - "Masters/AnekKannada.designspace"
outputDir: "../../fonts/AnekKannada"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration. The source is a `.designspace` file, the output directory points to `fonts/AnekKannada` (relative to the builder.yaml location), and it builds variable TTF only. No override config.yaml exists in the google/fonts family directory.

The METADATA.pb `files` block correctly maps `fonts/AnekKannada/variable/AnekKannada[wdth,wght].ttf` to the family directory, consistent with the builder output path.

## Conclusion

All source metadata for Anek Kannada is complete and verified:
- **Repository URL**: Correct, points to the EkType/Anek monorepo
- **Commit hash**: Correct, matches the gftools-packager onboarding message and is the latest commit in the repo
- **Config path**: Correct, `sources/AnekKannada/builder.yaml` exists at the referenced commit with valid gftools-builder configuration

No changes needed. The existing source block in METADATA.pb is fully accurate.
