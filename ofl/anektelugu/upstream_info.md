# Anek Telugu

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Ek Type

## Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | https://github.com/EkType/Anek                          |
| commit           | 34074c6b406f4112e20c7ad10254a6e954d0324b                 |
| config_yaml      | sources/AnekTelugu/builder.yaml                          |
| branch           | main                                                     |
| date_added       | 2022-02-16                                               |

## How URL Found

The repository URL `https://github.com/EkType/Anek` is already recorded in METADATA.pb. It is also confirmed by the copyright string in the font metadata: "Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)". The cached clone at `EkType/Anek` has its remote set to the same URL. The repository is a multi-script superfamily containing sources for Anek Telugu along with other Anek script variants.

## How Commit Identified

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is recorded in the METADATA.pb source block. It was verified against the onboarding commit in google/fonts:

- google/fonts commit `2d216f8bd` (2022-02-18) by Yanone with message: "[gftools-packager] Anek Telugu: Version 1.003 added (#4284)"
- The commit body explicitly states: "Anek Telugu Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b"

The upstream commit `34074c6b4` (2022-02-14) is a merge commit by Girish Dalvi: "Merge pull request #3 from yanone/main — Anek 1.003, revised". This commit is the HEAD of the upstream repository, meaning no additional changes have been made since onboarding. The timeline is consistent: the upstream commit (Feb 14, 2022) predates the google/fonts onboarding commit (Feb 18, 2022) by 4 days.

## How Config Resolved

The config file `sources/AnekTelugu/builder.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - "Masters/AnekTelugu.designspace"
outputDir: "../../fonts/AnekTelugu"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

The source is a designspace-based project with 9 UFO masters (3 widths x 3 weights) located at `sources/AnekTelugu/Masters/`. No local override config.yaml exists in the google/fonts family directory.

## Conclusion

All source metadata for Anek Telugu is complete and verified:

- **Repository URL**: Confirmed via METADATA.pb, copyright string, and onboarding commit message
- **Commit hash**: Confirmed via gftools-packager onboarding message in PR #4284; is HEAD of upstream repo with no subsequent changes
- **Config path**: `sources/AnekTelugu/builder.yaml` exists at the referenced commit with valid gftools-builder configuration
- **Confidence**: HIGH -- all three fields are explicitly documented in the onboarding commit and independently verifiable
