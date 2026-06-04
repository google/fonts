# Anek Tamil

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Confidence**: HIGH
- **Designer**: Ek Type

## Source Data

| Field | Value |
|---|---|
| repository_url | https://github.com/EkType/Anek |
| commit | 34074c6b406f4112e20c7ad10254a6e954d0324b |
| config_yaml | sources/AnekTamil/builder.yaml |
| branch | main |

## How URL Found

The repository URL `https://github.com/EkType/Anek` is recorded in the METADATA.pb `source {}` block and confirmed by the copyright string in the font metadata: "Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)". The cached repo at `EkType/Anek` has its remote set to the same URL.

## How Commit Identified

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is explicitly stated in the google/fonts commit `33962261d` (2022-02-18), which used gftools-packager:

> Anek Tamil Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b.

**Cross-verification**: The binary font blob hash in the upstream repo at this commit (`8d73854...`) matches exactly the blob hash committed to google/fonts in commit `33962261d`. The upstream commit is a merge of PR #3 from yanone/main ("Anek 1.003, revised"), dated 2022-02-14, four days before the google/fonts packager commit on 2022-02-18. This commit is also HEAD of the upstream repo -- no additional commits have been made since.

The onboarding was done by Yanone (post@yanone.de), who also contributed the upstream changes via PR #3.

## How Config Resolved

The file `sources/AnekTamil/builder.yaml` exists at the referenced commit and contains a valid gftools-builder configuration:

```yaml
sources:
  - "Masters/AnekTamil.designspace"
outputDir: "../../fonts/AnekTamil"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

The source is a `.designspace` file with variable font output. No override config.yaml is present in the google/fonts family directory.

## Conclusion

All source metadata for Anek Tamil is complete and verified. The repository URL, commit hash, and config_yaml path are all correct and consistent. The binary font at the referenced commit matches exactly what was committed to google/fonts. No changes needed.
