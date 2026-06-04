# Anek Gujarati

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Confidence**: HIGH

## Designer

Ek Type

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| Repository URL   | https://github.com/EkType/Anek                                    |
| Commit           | 34074c6b406f4112e20c7ad10254a6e954d0324b                           |
| Config           | sources/AnekGujarati/builder.yaml                                  |
| Branch           | main                                                               |

## Repository URL Verification

The repository URL `https://github.com/EkType/Anek` is already present in METADATA.pb and matches the copyright string in the font metadata: `Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)`. The cached repo at `EkType/Anek` confirms the remote is valid.

## Commit Verification

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` exists in the cached repo. It is a merge commit by Girish Dalvi dated 2022-02-14, merging PR #3 from yanone/main. The commit message is "Merge pull request #3 from yanone/main" and it includes fresh binaries and the addition of dotted circle (uni25CC) glyphs, along with reinstated designspace files.

This commit is confirmed as the correct onboarding commit. The google/fonts commit `d3ec55769` (PR #4306, dated 2022-02-18) explicitly states: "Anek Gujarati Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b". The commit was added via gftools-packager just 4 days after the upstream commit, consistent with a direct onboarding.

Notably, this commit (`34074c6`) is also the HEAD of the repository -- no further upstream work has been done after the onboarding.

## Config Verification

The builder config at `sources/AnekGujarati/builder.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - "Masters/AnekGujarati.designspace"
outputDir: "../../fonts/AnekGujarati"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

The designspace source file `sources/AnekGujarati/Masters/AnekGujarati.designspace` also exists at this commit, confirming the build configuration is valid. The font supports two axes (wdth and wght), consistent with the METADATA.pb axes definition.

No override `config.yaml` exists in the google/fonts family directory.

## Conclusion

All source metadata is complete and correct. The repository URL, commit hash, and config_yaml path in METADATA.pb are all verified and accurate. The Anek project is a multi-script super-family maintained by Ek Type, with Anek Gujarati being one of its script-specific variants. The source block also correctly maps the binary font file and license from the upstream repo structure. No changes needed.
