# Investigation Report: Edu NSW ACT Foundation

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Edu NSW ACT Foundation |
| **Designer** | Tina Anderson, Corey Anderson |
| **Category** | Handwriting |
| **Date Added** | 2022-06-10 |
| **Repository URL** | https://github.com/MezMerrit/AU-School-Handwriting-Fonts |
| **Commit** | `0dbdee65c92d10e24e5d634719054f4f96b69133` |
| **Config YAML** | `NSW-ACT-School-Fonts/sources/config.yaml` |
| **Status** | needs_correction |
| **Confidence** | HIGH |

## Source Block Status

The METADATA.pb already contains a `source {}` block, but it has an **incorrect `config_yaml` path**. The current value is:

```
config_yaml: "VIC-WA-NT-School-fonts/sources/config.yaml"
```

This points to the VIC WA NT Beginner config, which builds `EduVICWANTBeginner.glyphs`, not `EduNSWACTFoundation.glyphs`. The correct path should be:

```
config_yaml: "NSW-ACT-School-Fonts/sources/config.yaml"
```

The `NSW-ACT-School-Fonts/sources/config.yaml` file exists at commit `0dbdee6` and correctly references:
```yaml
sources:
    - EduNSWACTFoundation.glyphs
axisOrder:
    - wght
buildOTF: False
familyName: Edu NSW ACT Foundation
```

## Upstream Repository

- **Repository**: https://github.com/MezMerrit/AU-School-Handwriting-Fonts
- **Cached at**: `MezMerrit/AU-School-Handwriting-Fonts`
- **Status**: Clean, up to date with origin

This is a monorepo containing all five Australian school handwriting font families:
- `NSW-ACT-School-Fonts/` -- Edu NSW ACT Foundation
- `QLD-School-Fonts/` -- Edu QLD Beginner
- `SA-School-Fonts/` -- Edu SA Beginner
- `TAS-School-Fonts/` -- Edu TAS Beginner
- `VIC-WA-NT-School-fonts/` -- Edu VIC WA NT Beginner

## Source Files

At commit `0dbdee6`, the NSW ACT Foundation directory contains:
- `NSW-ACT-School-Fonts/sources/EduNSWACTFoundation.glyphs` -- Glyphs source file
- `NSW-ACT-School-Fonts/sources/config.yaml` -- gftools-builder config
- `NSW-ACT-School-Fonts/sources/CustomFilterSet.plist`
- `NSW-ACT-School-Fonts/fonts/variable/EduNSWACTFoundation[wght].ttf` -- Pre-built variable font

Source format: **.glyphs** (Glyphs app format), variable font with `wght` axis (400-700).

## Commit Verification

The commit hash `0dbdee65c92d10e24e5d634719054f4f96b69133` ("Corrected vertical metrics", 2022-06-23) is **correct** for the current binary.

### Version History in google/fonts

1. **v1.001** -- PR #4761 (`6237c1316`, 2022-06-15): Initial onboarding from upstream commit `055799b` ("Update emails")
2. **v1.002** -- PR #4823 (`506584e13`, 2022-06-22): Bulk update of all 5 families from upstream commit `8a71f27` ("Merge branch 'main'")
3. **v1.003** -- PR #4831 (`536d37fd9`, 2022-06-23): Final update of all 5 families from upstream commit `0dbdee6` ("Corrected vertical metrics") -- **CURRENT**

The v1.003 update was packaged by Rosalie Wagner using gftools-packager. All five families were updated together in a single PR, all referencing the same upstream commit `0dbdee6`.

### Post-onboarding Upstream Changes

After commit `0dbdee6`, the upstream repo has only had:
- README updates
- File cleanup (deleting dotted/outline variants)
- Folder restructuring

No source font files (`.glyphs`) were modified after the referenced commit.

## Issues Found

1. **WRONG config_yaml path**: The METADATA.pb `config_yaml` field points to `VIC-WA-NT-School-fonts/sources/config.yaml` instead of `NSW-ACT-School-Fonts/sources/config.yaml`. This was introduced by a "sources info" commit (`b9c8d846`, 2025-09-18) that incorrectly set the config path. The commit hash was correct, but the config_yaml path was wrong.

## Recommended Fix

Change the `config_yaml` field in the METADATA.pb source block from:
```
config_yaml: "VIC-WA-NT-School-fonts/sources/config.yaml"
```
to:
```
config_yaml: "NSW-ACT-School-Fonts/sources/config.yaml"
```

No other changes needed -- the repository_url, commit hash, files, and branch are all correct.
