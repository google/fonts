# Investigation Report: Edu QLD Beginner

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Edu QLD Beginner |
| **Designer** | Tina Anderson, Corey Anderson |
| **Category** | Handwriting |
| **Date Added** | 2022-06-22 |
| **Repository URL** | https://github.com/MezMerrit/AU-School-Handwriting-Fonts |
| **Commit** | `0dbdee65c92d10e24e5d634719054f4f96b69133` |
| **Config YAML** | `QLD-School-Fonts/sources/config.yaml` |
| **Status** | needs_correction |
| **Confidence** | HIGH |

## Source Block Status

The METADATA.pb already contains a `source {}` block. The `config_yaml` path is correct (`QLD-School-Fonts/sources/config.yaml`), but the **commit hash is wrong**. The current value is:

```
commit: "1dd726bde8004743529cbeaab84ce993caf98f78"
```

This is the commit from the v1.002 update (PR #4824, "Passed Beginners to singular for consistency"), but the current font binary was updated to v1.003 in PR #4831, which used upstream commit `0dbdee6`. The correct commit should be:

```
commit: "0dbdee65c92d10e24e5d634719054f4f96b69133"
```

## Upstream Repository

- **Repository**: https://github.com/MezMerrit/AU-School-Handwriting-Fonts
- **Cached at**: `MezMerrit/AU-School-Handwriting-Fonts`
- **Status**: Clean, up to date with origin

This is a monorepo containing all five Australian school handwriting font families.

## Source Files

At commit `0dbdee6`, the QLD directory contains:
- `QLD-School-Fonts/sources/EduQLDBeginner.glyphs` -- Glyphs source file
- `QLD-School-Fonts/sources/config.yaml` -- gftools-builder config
- `QLD-School-Fonts/sources/CustomFilterSet.plist`
- `QLD-School-Fonts/fonts/variable/EduQLDBeginner[wght].ttf` -- Pre-built variable font

Source format: **.glyphs** (Glyphs app format), variable font with `wght` axis (400-700).

The config.yaml at this commit contains:
```yaml
sources:
    - EduQLDBeginner.glyphs
axisOrder:
    - wght
buildOTF: False
familyName: Edu QLD Beginner
```

## Commit Verification

The commit currently in METADATA.pb (`1dd726bde8004743529cbeaab84ce993caf98f78`, "Passed Beginners to singular for consistency", 2022-06-22) is **not the correct commit** for the current binary.

### Version History in google/fonts

1. **v1.002** -- PR #4824 (`9950d882`, 2022-06-22): QLD Beginner was onboarded separately from the other families at v1.002. This PR used upstream commit `1dd726b`.
2. **v1.003** -- PR #4831 (`536d37fd9`, 2022-06-23): All five families updated together from upstream commit `0dbdee6` ("Corrected vertical metrics") -- **CURRENT**

Note: QLD Beginner was NOT part of the initial v1.001 bulk onboarding. It was added later at v1.002 in a separate PR (#4824), then updated to v1.003 along with all other families.

### How the Wrong Commit Was Set

The PR #4831 (v1.003 update) originally set the correct commit `0dbdee6` in the source block. The April 2024 "Merge upstream.yaml into METADATA.pb" commit (`66f91f10f`) confirmed it still had `0dbdee6`. However, a "sources info" commit (`a2ec62f78`, 2025-09-18) incorrectly changed the commit from `0dbdee6` to `1dd726b` (referencing the earlier v1.002 PR #4824 instead of the current v1.003 PR #4831).

### Post-onboarding Upstream Changes

After commit `0dbdee6`, the upstream repo has only had README updates and file cleanup. No source font files were modified.

## Issues Found

1. **WRONG commit hash**: The METADATA.pb commit field points to `1dd726b` (v1.002 onboarding) instead of `0dbdee6` (v1.003 update, which is the current binary).

## Recommended Fix

Change the `commit` field in the METADATA.pb source block from:
```
commit: "1dd726bde8004743529cbeaab84ce993caf98f78"
```
to:
```
commit: "0dbdee65c92d10e24e5d634719054f4f96b69133"
```

No other changes needed -- the repository_url, config_yaml, files, and branch are all correct.
