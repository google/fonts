# Anek Malayalam

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Ek Type

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/EkType/Anek |
| commit           | 34074c6b406f4112e20c7ad10254a6e954d0324b |
| config_yaml      | sources/AnekMalayalam/builder.yaml |
| branch           | main |

## How URL Found

The repository URL `https://github.com/EkType/Anek` is already present in METADATA.pb (line 30) and also appears in the font copyright string: `Copyright 2021 The Anek Project Authors (https://github.com/EkType/Anek)`. The URL is confirmed valid. This is a multi-script font family with all scripts (Anek Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Latin, Malayalam, Odia, Tamil, Telugu) sharing a single upstream repository.

## How Commit Identified

The commit `34074c6b4` is recorded in METADATA.pb and was set by the `sources info` commit `bc9912ec5` in google/fonts. The onboarding was done via PR [#4281](https://github.com/google/fonts/pull/4281) by yanone (Yanone), merged on 2022-02-18 by RosaWagner.

The PR body initially referenced an earlier commit `634384abf` (2022-02-09), but yanone posted an update comment on 2022-02-16 updating the reference to `34074c6b4` (2022-02-14), which is a merge of PR #3 from yanone's fork containing fresh binaries and a dotted circle addition (uni25CC). The final packager commit in google/fonts correctly records the updated hash.

The upstream commit `34074c6b4` is also HEAD of the `main` branch -- no further commits have been made to the upstream repo since onboarding. This confirms the commit hash is correct and up-to-date.

Timeline:
- 2022-02-14: Upstream commit `34074c6b4` (Merge PR #3, "Anek 1.003, revised")
- 2022-02-16: yanone updated PR #4281 to reference the new commit
- 2022-02-18: PR #4281 merged into google/fonts

## How Config Resolved

The file `sources/AnekMalayalam/builder.yaml` exists at commit `34074c6b4` in the upstream repo. Its contents:

```yaml
sources:
  - "Masters/AnekMalayalam.designspace"
outputDir: "../../fonts/AnekMalayalam"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration referencing the `.designspace` source file. No override config.yaml exists in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly points to this file.

## Conclusion

All source metadata for Anek Malayalam is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. The commit hash matches the one used for onboarding (confirmed via PR #4281 history), and the builder.yaml exists at the referenced commit with valid gftools-builder configuration. No changes are needed.
