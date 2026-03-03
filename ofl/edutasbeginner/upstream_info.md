# Investigation Report: Edu TAS Beginner

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Edu TAS Beginner |
| **Designer** | Tina Anderson, Corey Anderson |
| **Category** | Handwriting |
| **Date Added** | 2022-06-10 |
| **Repository URL** | https://github.com/MezMerrit/AU-School-Handwriting-Fonts |
| **Commit** | `0dbdee65c92d10e24e5d634719054f4f96b69133` |
| **Config YAML** | `TAS-School-Fonts/sources/config.yaml` |
| **Status** | needs_correction |
| **Confidence** | HIGH |

## Source Block Status

The METADATA.pb already contains a `source {}` block. The `config_yaml` path is correct (`TAS-School-Fonts/sources/config.yaml`), but the **commit hash is wrong**. The current value is:

```
commit: "055799b858017157b6138e59833ab5b1a8947bbd"
```

This is the commit from the v1.001 initial onboarding (PR #4765, "Update emails"), but the current font binary was updated through v1.002 (PR #4823) and then to v1.003 (PR #4831), which used upstream commit `0dbdee6`. The correct commit should be:

```
commit: "0dbdee65c92d10e24e5d634719054f4f96b69133"
```

## Upstream Repository

- **Repository**: https://github.com/MezMerrit/AU-School-Handwriting-Fonts
- **Cached at**: `MezMerrit/AU-School-Handwriting-Fonts`
- **Status**: Clean, up to date with origin

This is a monorepo containing all five Australian school handwriting font families.

## Source Files

At commit `0dbdee6`, the TAS directory contains:
- `TAS-School-Fonts/sources/EduTASBeginner.glyphs` -- Glyphs source file
- `TAS-School-Fonts/sources/config.yaml` -- gftools-builder config
- `TAS-School-Fonts/sources/CustomFilterSet.plist`
- `TAS-School-Fonts/fonts/variable/EduTASBeginner[wght].ttf` -- Pre-built variable font

Source format: **.glyphs** (Glyphs app format), variable font with `wght` axis (400-700).

The config.yaml at this commit contains:
```yaml
sources:
    - EduTASBeginner.glyphs
axisOrder:
    - wght
buildOTF: False
familyName: Edu TAS Beginner
```

## Commit Verification

The commit currently in METADATA.pb (`055799b858017157b6138e59833ab5b1a8947bbd`, "Update emails", 2022-06-10) is **not the correct commit** for the current binary.

### Version History in google/fonts

1. **v1.001** -- PR #4765 (`64b1a836`, 2022-06-15): Initial onboarding from upstream commit `055799b` ("Update emails")
2. **v1.002** -- PR #4823 (`506584e13`, 2022-06-22): Bulk update of all 5 families from upstream commit `8a71f27` ("Merge branch 'main'"). Note: TAS Beginner was actually updated twice in this PR -- first from `8a71f27`, then from `80ca0a0` ("Corrected TAS UPM").
3. **v1.003** -- PR #4831 (`536d37fd9`, 2022-06-23): Final update of all 5 families from upstream commit `0dbdee6` ("Corrected vertical metrics") -- **CURRENT**

### How the Wrong Commit Was Set

The PR #4831 (v1.003 update) originally set the correct commit `0dbdee6` in the source block. The April 2024 "Merge upstream.yaml into METADATA.pb" commit confirmed it still had `0dbdee6`. However, a "sources info" commit (`265283482`, 2025-09-18) incorrectly changed the commit from `0dbdee6` to `055799b` (referencing the v1.001 initial onboarding PR #4765 instead of the current v1.003 PR #4831).

### Post-onboarding Upstream Changes

After commit `0dbdee6`, the upstream repo has only had README updates and file cleanup. No source font files were modified.

## Issues Found

1. **WRONG commit hash**: The METADATA.pb commit field points to `055799b` (v1.001 initial onboarding) instead of `0dbdee6` (v1.003 update, which is the current binary). This is two versions behind.

## Recommended Fix

Change the `commit` field in the METADATA.pb source block from:
```
commit: "055799b858017157b6138e59833ab5b1a8947bbd"
```
to:
```
commit: "0dbdee65c92d10e24e5d634719054f4f96b69133"
```

No other changes needed -- the repository_url, config_yaml, files, and branch are all correct.
