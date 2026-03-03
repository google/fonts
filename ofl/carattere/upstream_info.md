# Carattere - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Carattere |
| **Designer** | Robert Leuschke |
| **Repository URL** | https://github.com/googlefonts/carattere |
| **Commit** | `18fbebe0c73ec82068be167eb3e63a795bd814ac` |
| **Branch** | master |
| **Config YAML** | `sources/config.yml` |
| **Date Added** | 2021-08-26 |
| **License** | OFL |
| **Status** | Complete |

## How URL Was Found

The repository URL `https://github.com/googlefonts/carattere` is recorded in METADATA.pb and was referenced by gftools-packager in the onboarding commit. The copyright string also references this URL.

## How Commit Was Determined

The commit `18fbebe0c73ec82068be167eb3e63a795bd814ac` was explicitly referenced by gftools-packager in:

1. **Merge commit** in google/fonts (`08c5eb1bd`):
   > Carattere Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/carattere at commit https://github.com/googlefonts/carattere/commit/18fbebe0c73ec82068be167eb3e63a795bd814ac.

2. **PR #3766 body** also references the same commit.

The commit is titled "v1.010 fonts added" (2021-08-18) by Viviana Monsalve, and is the HEAD of the master branch. It includes updated font binaries and a source change.

## Config YAML Status

The file `sources/config.yml` exists at the recorded commit and contains:

```yaml
sources:
  - Carattere.glyphs
familyName: "Carettere"
buildVariable: false
# autohintTTF: false
```

**NOTE**: There is a typo in the `familyName` field: "Carettere" instead of "Carattere" (extra 't'). This typo has been present since the config file was first added (commit `203fbfc`) and remains in the current HEAD. Despite this typo, the font was successfully built and onboarded, suggesting gftools-builder may have used the family name from the source file rather than the config.

No override config.yaml exists in the google/fonts family directory.

## Verification

- **Commit exists in upstream repo**: Yes, verified (it is the HEAD commit of master)
- **Binary match**: The TTF file `Carattere-Regular.ttf` at the recorded commit matches the one in google/fonts (SHA-256: `2ee075b50a75aeaea0d976d916b535fbcd423a684e97fe8536fd8f9efe905ae6`)
- **config.yml present at commit**: Yes, at `sources/config.yml` (with familyName typo)
- **Onboarding author**: Viviana Monsalve (PR #3766)

## Confidence Level

**HIGH** - The gftools-packager commit message in both the merge commit and PR body reference this exact commit hash. The binary files match. All three sources (merge commit, PR body, METADATA.pb) are consistent.

## Open Questions

1. **familyName typo in config.yml**: The `familyName` in `sources/config.yml` is "Carettere" (with an extra 't') instead of "Carattere". This should ideally be fixed in the upstream repo, but since the font has already been successfully built and onboarded, it may not be blocking. The typo may cause issues if fonts are rebuilt from source in the future using this config file.
