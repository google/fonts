# Anek Bangla

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/anekbangla/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EkType/Anek |
| Commit | `34074c6b406f4112e20c7ad10254a6e954d0324b` |
| Config YAML | `sources/AnekBangla/builder.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/EkType/Anek` is already recorded in the METADATA.pb `source` block. It is also referenced in the font copyright string ("Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)") and in the gftools-packager commit message that onboarded the font (commit `60d08bb25` in google/fonts). The repo is a multi-script family repository hosting Anek Bangla, Anek Devanagari, Anek Gujarati, Anek Gurmukhi, Anek Kannada, Anek Latin, Anek Malayalam, Anek Odia, Anek Tamil, and Anek Telugu.

The cached clone at `EkType/Anek` is verified and its remote points to the same URL.

## How the Commit Hash Was Identified

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is already recorded in METADATA.pb and was verified through multiple sources:

1. **gftools-packager message**: The google/fonts commit `60d08bb25` (PR #4304, merged 2022-02-18) explicitly states: "Anek Bangla Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b."

2. **Upstream repo verification**: The commit exists in the cached repo and is a merge commit dated 2022-02-14 with message "Merge pull request #3 from yanone/main -- Anek 1.003, revised". It modifies binary font files for all Anek script variants including AnekBangla.

3. **Timeline consistency**: The upstream commit (2022-02-14) predates the google/fonts merge (2022-02-18), which is the expected chronological order.

4. **HEAD of main**: This commit is the latest (HEAD) on the `main` branch in the upstream repo. There are no newer commits beyond it, so no additional upstream work has been done since onboarding.

## How Config YAML Was Resolved

The config path `sources/AnekBangla/builder.yaml` is already recorded in METADATA.pb and was verified:

1. **File exists at the referenced commit**: `git show 34074c6b4:sources/AnekBangla/builder.yaml` confirms the file is present.

2. **Content is valid gftools-builder configuration**:
   ```yaml
   sources:
     - "Masters/AnekBangla.designspace"
   outputDir: "../../fonts/AnekBangla"
   buildStatic: false
   buildVariable: true
   buildTTF: true
   buildOTF: false
   buildWebfont: false
   includeSourceFixes: true
   ```
   The config references a `.designspace` source and outputs variable TTF to `fonts/AnekBangla`, which matches the binary file path in the `source.files` mapping.

3. **No local override**: There is no `config.yaml` in the `ofl/anekbangla/` directory in google/fonts, which is correct since the upstream builder.yaml is properly referenced.

## Conclusion

The source metadata for Anek Bangla is **complete and fully verified**. The repository URL, commit hash, config YAML path, and branch are all correctly recorded in METADATA.pb. The gftools-packager commit message in google/fonts explicitly references the exact upstream commit, the builder.yaml exists and contains valid configuration, and the timeline is consistent. No changes are needed.
