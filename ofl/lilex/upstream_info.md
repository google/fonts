# Investigation Report: Lilex

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Family**: Lilex
**Slug**: lilex
**Directory**: ofl/lilex

## Summary

Lilex is a monospace font family with variable weight (100-700) in both upright and italic styles. It was onboarded to Google Fonts in November 2025 via PR #9975. The METADATA.pb has a complete source block with repository URL and commit hash. However, the `config_yaml` field currently points to a path (`sources/Lilex/config.yaml`) that does not exist at the referenced commit -- the correct path at that commit was `sources/config.yaml`.

## Source Block Status

**Has source block**: Yes
**Status**: needs_correction (config_yaml path incorrect for referenced commit)

## Repository Information

- **Repository URL**: https://github.com/mishamyrt/Lilex
- **Branch**: master
- **Cached at**: upstream_repos/fontc_crater_cache/mishamyrt/Lilex
- **Repository is clean**: Yes
- **Default branch**: master

## Commit Verification

- **Referenced commit**: `50260ef98a52ee7e74617c13894505497fa8b2ea`
- **Commit date**: 2025-11-07 00:34:37 +0300
- **Commit message**: "feat(preview): improve superpowers mobile ux"
- **Commit exists in repo**: Yes

### Binary File Verification

The font binaries at the referenced commit match exactly with those in google/fonts:

| File | SHA-256 Match |
|------|--------------|
| `Lilex[wght].ttf` | Yes (`ac99facd1db106a77d662a8285d97f1f241fb1f5316a41f8ceee8279b4750d82`) |
| `Lilex-Italic[wght].ttf` | Yes (`84a80f6db4fbcdd03bde31a8561e3ba9c7f7a6673cce05d627bf5e6816abf57b`) |

### Relationship to Version Tag

The referenced commit `50260ef` is 5 commits after the `2.621` tag (`f379432`, dated 2025-11-06). The intervening commits are exclusively website/preview/documentation changes -- no font source or binary modifications. The font binaries are identical at both the tag and the referenced commit. The onboarding commit message says "Lilex: Version 2.621 added", which is consistent.

## Onboarding History

- **Google Fonts PR**: #9975 ("Lilex: Version 2.621 added")
- **PR author**: Emma Marichal (@emmamarichal)
- **PR created**: 2025-11-06
- **PR merged**: 2025-11-21
- **Onboarding commit**: `875c757` (2025-11-07)
- **Commit message body**: "Taken from the upstream repo https://github.com/mishamyrt/Lilex at commit https://github.com/mishamyrt/Lilex/commit/50260ef98a52ee7e74617c13894505497fa8b2ea."

The commit message explicitly references the upstream commit hash, and the binary files match, confirming the commit hash is correct.

## Config YAML Analysis

### Current METADATA.pb Setting

```
config_yaml: "sources/Lilex/config.yaml"
```

This path was added by PR #10248 ("Add config_yaml enrichment for 82 font families", merged 2026-02-20).

### Issue: Path Does Not Exist at Referenced Commit

At the referenced commit `50260ef`, the directory structure was:

```
sources/
  Lilex.glyphs
  Lilex-Italic.glyphs
  config.yaml          <-- config was here
  lilexgen_config.yaml
  opentype_features/
```

The `sources/Lilex/` subdirectory did not exist. The sources were restructured in commit `f9a2c20` (2025-11-12, "chore: adapt generation scripts"), which moved the files into `sources/Lilex/` and also added `sources/LilexDuo/` for a new "Duo" variant.

### Config at Referenced Commit (`sources/config.yaml`)

```yaml
sources:
  - Lilex.glyphs
  - Lilex-Italic.glyphs
outputDir: ../build
axisOrder:
  - wght
  - ital
familyName: "Lilex"
cleanUp: true
stat:
  Lilex[wght].ttf:
    - name: Weight
      tag: wght
      values:
        - name: Thin
          value: 100
        - name: ExtraLight
          value: 200
        - name: Light
          value: 300
        - name: Regular
          value: 400
          linkedValue: 700
          flags: 2
        - name: Medium
          value: 500
        - name: SemiBold
          value: 600
        - name: Bold
          value: 700
    - name: Italic
      tag: ital
      values:
        - name: Roman
          value: 0
          linkedValue: 1
          flags: 2
  Lilex-Italic[wght].ttf:
    - name: Weight
      tag: wght
      values:
        - name: Thin
          value: 100
        - name: ExtraLight
          value: 200
        - name: Light
          value: 300
        - name: Regular
          value: 400
          linkedValue: 700
          flags: 2
        - name: Medium
          value: 500
        - name: SemiBold
          value: 600
        - name: Bold
          value: 700
    - name: Italic
      tag: ital
      values:
        - name: Italic
          value: 1
```

This is a valid gftools-builder config that correctly references the `.glyphs` source files relative to the config file location.

### Config at HEAD (`sources/Lilex/config.yaml`)

The config at HEAD is nearly identical but has two differences:
1. `outputDir` changed from `../build` to `../../build/Lilex` (adjusted for the new subdirectory)
2. Added `recipeProvider: googlefonts`

## Recommended Correction

The `config_yaml` field in METADATA.pb should be corrected from `sources/Lilex/config.yaml` to `sources/config.yaml` to match the path that exists at the referenced commit `50260ef`.

**Corrected source block**:
```
source {
  repository_url: "https://github.com/mishamyrt/Lilex"
  commit: "50260ef98a52ee7e74617c13894505497fa8b2ea"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Lilex[wght].ttf"
    dest_file: "Lilex[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Lilex-Italic[wght].ttf"
    dest_file: "Lilex-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Confidence

**HIGH** -- The repository URL and commit hash are confirmed by the onboarding commit message and verified by binary file hash comparison. The config_yaml path correction is confirmed by inspecting the upstream repo's file tree at the referenced commit.
