# Caramel - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Caramel |
| **Designer** | Robert Leuschke |
| **Repository URL** | https://github.com/googlefonts/caramel |
| **Commit** | `87aff25878217835c9d22342d60678d4dcf8be75` |
| **Branch** | master |
| **Config YAML** | `sources/config.yml` |
| **Date Added** | 2021-08-06 |
| **License** | OFL |
| **Status** | Complete |

## How URL Was Found

The repository URL `https://github.com/googlefonts/caramel` is recorded in METADATA.pb and was referenced by gftools-packager in the onboarding commit. The copyright string also references this URL.

## How Commit Was Determined

Multiple commits were referenced during the onboarding process:

1. **PR body reference**: PR #3672 body references commit `bd1d693ea8d578604a2ea2411672984619938faa` ("round coordinates font", 2021-08-02). This was the state when the packager PR was first created.

2. **Merge commit reference**: The merge commit message (`8a905ba70` in google/fonts) references commit `497341c437891ac272f8b3ac68b721f07031f3d3` ("dot removed", 2021-08-06). This is one commit after `bd1d693e`.

3. **Current METADATA.pb**: Points to `87aff25878217835c9d22342d60678d4dcf8be75` ("Nhung added to Contributors", 2021-08-06). This is one commit after `497341c4`.

**Binary verification**: The TTF file `Caramel-Regular.ttf` is identical across all three commits (SHA-256: `36a460f8418d5f9710da43404776fc914fe11ff5ec649e9c8bcb670c602b92be`), matching the file in google/fonts. The font binary was produced at `bd1d693e` and the subsequent two commits were metadata-only changes (removing a dot from DESCRIPTION.en_us.html, and updating CONTRIBUTORS.txt).

The METADATA.pb commit `87aff258` represents the tip of the master branch at the time of onboarding, which is the convention when no further font changes follow.

## Config YAML Status

The file `sources/config.yml` (note: `.yml` extension, not `.yaml`) exists at the recorded commit and contains:

```yaml
sources:
  - CaramelPro.glyphs
familyName: "Caramel"
buildVariable: false
autohintTTF: false
```

This config was identical at all three candidate commits. No override config.yaml exists in the google/fonts family directory.

## Verification

- **Commit exists in upstream repo**: Yes, verified
- **Binary match**: The TTF file matches between upstream (at all 3 candidate commits) and google/fonts
- **config.yml present at commit**: Yes, at `sources/config.yml`
- **Onboarding author**: Viviana Monsalve (PR #3672)

## Confidence Level

**HIGH** - While there were 3 different commit references during onboarding, all produce identical font binaries. The current METADATA.pb commit (`87aff258`) points to the latest commit before the PR was merged, which is a reasonable choice. All data is verified.

## Open Questions

None. This family is fully documented and verified.
