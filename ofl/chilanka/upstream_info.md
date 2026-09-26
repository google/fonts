# Chilanka - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Chilanka |
| Designer | SMC, Santhosh Thottingal |
| License | OFL |
| Date Added | 2019-06-10 |
| Repository URL | https://github.com/smc/Chilanka |
| Commit | `4688e5c6fcfb5ccf8fc9f28dedaa15b2eacbe8e9` |
| Branch | master |
| Config YAML | Override in google/fonts family directory |
| Status | complete |

## How URL Found

The repository URL `https://github.com/smc/Chilanka` is documented in the METADATA.pb source block on google/fonts main. It was set during the gftools-packager onboarding in PR #6144.

## How Commit Determined

The commit history shows an interesting correction:

1. **Original packager reference**: PR #6144 by vv-monsalve (Viviana Monsalve) onboarded Chilanka Version 1.600 on 2023-08-24. The gftools-packager commit message referenced upstream commit `bbc2c94ae7af008975c81e509911b609444b3902`.

2. **Commit not found**: The commit `bbc2c94` no longer exists in the upstream repository (likely force-pushed away or from a different branch that was deleted).

3. **Corrected to `4688e5c6`**: In commit `733c2866` (2025-11-21), the hash was updated from `bbc2c94` to `4688e5c6fcfb5ccf8fc9f28dedaa15b2eacbe8e9`. This commit (2023-03-11) is "Update version - 1.6" by Santhosh Thottingal, which updated the VERSION file and fontinfo.plist to version 1.6.

4. **Rationale**: `4688e5c6` is the last commit on master that is part of the v1.600 release. Subsequent commits (`cd1aee0`, etc., from 2023-09-29) post-date the onboarding and include changes like "Remove unwanted files from repo" and "Remove dotted circle for rendering".

## Config YAML Status

**Override config.yaml exists** in the google/fonts family directory at `google/fonts/ofl/chilanka/config.yaml`:

```yaml
buildVariable: false
sources:
  - sources/Chilanka-Regular.ufo
```

The upstream repository does NOT have a config.yaml file. The override was created as part of the sources documentation effort (commit `ea80eba11`, 2025-11-21). The upstream sources are in UFO format (`sources/Chilanka-Regular.ufo`), which is compatible with gftools-builder.

Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Repository URL verified: accessible at https://github.com/smc/Chilanka
- Commit `4688e5c6` verified: exists in the upstream repo, authored 2023-03-11 by Santhosh Thottingal
- Source block on main includes: repository_url, commit, files mappings, and branch
- Override config.yaml present at `ofl/chilanka/config.yaml`
- UFO sources confirmed at `sources/Chilanka-Regular.ufo` in upstream

## Confidence Level

**HIGH** - The commit `4688e5c6` is the version bump commit for v1.600, which aligns with the onboarded version. The original `bbc2c94` commit is no longer accessible but was likely from the same release cycle. The override config.yaml correctly points to the UFO source.

## Open Questions

- The original commit `bbc2c94ae7af008975c81e509911b609444b3902` referenced by gftools-packager no longer exists in the upstream repo. This may have been from a force-push or a different branch. The replacement commit `4688e5c6` is a reasonable proxy as it is the version bump for v1.600.
