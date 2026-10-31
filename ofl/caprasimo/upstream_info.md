# Caprasimo - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Caprasimo |
| **Designer** | The DocRepair Project, Phaedra Charles, Flavia Zimbardi |
| **Repository URL** | https://github.com/docrepair-fonts/caprasimo-fonts |
| **Commit** | `9f11e8fd4e8a4bdf069612a275a40103c5337ccf` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Date Added** | 2023-06-14 |
| **License** | OFL |
| **Status** | Complete |

## How URL Was Found

The repository URL is recorded in METADATA.pb and was added by gftools-packager when the font was first onboarded. The copyright string in the font file also references `https://github.com/docrepair-fonts/caprasimo-fonts`.

## How Commit Was Determined

The commit hash `9f11e8fd4e8a4bdf069612a275a40103c5337ccf` was recorded by gftools-packager in the original onboarding commit (`9b3a6ff0c` in google/fonts):

> [gftools-packager] Caprasimo: Version 1.001 added
> Caprasimo Version 1.001 taken from the upstream repo https://github.com/docrepair-fonts/caprasimo-fonts at commit https://github.com/docrepair-fonts/caprasimo-fonts/commit/9f11e8fd4e8a4bdf069612a275a40103c5337ccf.

This commit is the HEAD of the `main` branch at the time of onboarding (2023-06-14). The commit message is "Renamed macron#1 to legacymacron, gave it macron outlines" by Yanone.

## Config YAML Status

The file `sources/config.yaml` exists at the recorded commit and contains:

```yaml
buildOTF: false
buildVariable: false
buildWebfont: false
familyName: Caprasimo
outputDir: ../fonts
sources:
  - Caprasimo-Regular.designspace
```

This is a valid gftools-builder configuration. No override config.yaml exists in the google/fonts family directory.

## Verification

- **Commit exists in upstream repo**: Yes, verified
- **Binary match**: The TTF file `Caprasimo-Regular.ttf` at the recorded commit matches the one in google/fonts (SHA-256: `786ab84ee787d40df55be78cb4361e485a1c6687195cbcccf3538cb5e46ced90`)
- **config.yaml present at commit**: Yes, at `sources/config.yaml`
- **Onboarding author**: Yanone (post@yanone.de)

## Confidence Level

**HIGH** - The gftools-packager commit message explicitly references this exact commit hash. The binary files match between the upstream repo and google/fonts. The config.yaml is present at the recorded path. All data is consistent and verified.

## Open Questions

None. This family is fully documented and verified.
