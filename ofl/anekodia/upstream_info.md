# Anek Odia

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Ek Type
- **Primary Script**: Oriya (Odia)

## Source Data

| Field            | Value |
|------------------|-------|
| `repository_url` | `https://github.com/EkType/Anek` |
| `commit`         | `34074c6b406f4112e20c7ad10254a6e954d0324b` |
| `config_yaml`    | `sources/AnekOdia/builder.yaml` |
| `branch`         | `main` |

## How URL Found

The repository URL `https://github.com/EkType/Anek` is documented in the METADATA.pb `source {}` block and confirmed by the copyright string in the font metadata: `Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)`. The cached clone at `EkType/Anek` has its remote set to the same URL.

The Anek repository is a multi-script project containing sources for multiple Anek family variants (Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Latin, Malayalam, Odia, Tamil, Telugu). Each variant has its own subdirectory under `sources/`.

## How Commit Identified

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` was identified from the gftools-packager commit message in google/fonts:

- **First onboarding** (PR #4282, commit `4e91b538`, 2022-02-10): Used commit `634384abf35544275862ae22c7da44cc9c916caa` (2022-02-09, "Merge pull request #2 from yanone/main").
- **Second onboarding** (PR #4307, commit `059d40ca`, 2022-02-18): Updated to commit `34074c6b406f4112e20c7ad10254a6e954d0324b` (2022-02-14, "Merge pull request #3 from yanone/main").

The second commit (`34074c6`) is the latest in the upstream repo and is the HEAD of the `main` branch. It includes changes made between the two onboardings: "Reinstated original designspace files", "Added uni25CC (dotted circle)", and "Fresh binaries". The timeline is consistent: the upstream commit (2022-02-14) predates the google/fonts merge (2022-02-18).

This is also the very last commit in the repository -- no further upstream work has occurred since.

## How Config Resolved

The file `sources/AnekOdia/builder.yaml` exists at commit `34074c6` and contains a valid gftools-builder configuration:

```yaml
sources:
  - "Masters/AnekOdia.designspace"
outputDir: "../../fonts/AnekOdia"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

The builder references `Masters/AnekOdia.designspace`, which is a valid designspace file containing 9 UFO masters across weight (100-800) and width (75-125) axes. No override `config.yaml` exists in the google/fonts family directory; the `config_yaml` field in METADATA.pb correctly points to the upstream file.

The `config_yaml` field was added to METADATA.pb in commit `294f26b4` (2025-09-24, "sources info for Anek Odia: Version 1.003 (#4307)") by @felipesanches.

## Conclusion

The source metadata for Anek Odia is **complete and correct**. The repository URL, commit hash, and config_yaml path are all verified:

- The repository URL matches the copyright string and the cached clone remote.
- The commit hash `34074c6` corresponds to the final gftools-packager onboarding (PR #4307) and is explicitly referenced in the google/fonts commit body. The timeline is consistent.
- The builder config at `sources/AnekOdia/builder.yaml` is present at the referenced commit and contains valid gftools-builder configuration pointing to the correct designspace and UFO sources.

No changes needed.
