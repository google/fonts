# Martel — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/typeoff/martel"
  commit: "ae74b972c6870d296e1a2693c91006beba8c4801"
}
```

An override `config.yaml` also exists in the google/fonts family directory with:
```yaml
buildVariable: false
sources:
  - Martel Source Files/Martel 20150421.glyphs
```

No `config_yaml` field is set in METADATA.pb, as the override is auto-detected.

## Repository Analysis

- **Repository**: https://github.com/typeoff/martel (accessible, HTTP 200)
- **Default branch**: master
- **Designer**: Dan Reynolds
- **Description**: Martel is a Devanagari + Latin serif family with 7 weights (UltraLight to Heavy). The Latin glyphs are based on Merriweather.
- **License**: OFL

### Repository Structure (at HEAD)

```
LICENSE.md
README.md
Martel Font Files/
  OTFs/
  TTFs with ttfautohints/
  TTFs without hints/
Martel Source Files/
  Martel 20150421.glyphs
  Martel-Bold.ufo/
  Martel-Light.ufo/
  Martel-Regular.ufo/
```

The repository contains .glyphs sources and .ufo exports, which are gftools-builder compatible. No `config.yaml` exists in the upstream repo.

### Key Commits

| Commit | Date | Description |
|--------|------|-------------|
| `76c161e` | 2015-03-06 | Version 1.001 — TTFs match google/fonts binaries |
| `3a986ff` | 2015-04-21 | Version 1.002 — first commit, updated fonts/sources/license |
| `ae74b97` | 2015-04-21 | Version 1.002 — second commit, added DemiBold/UltraLight unhinted TTFs |
| `573551a` | (latest) | ReadMe update (no font changes) |

## Onboarding History

The font was added to google/fonts in commit `fc4d5c7d6` on 2015-04-20 with the message "Adding Martel". This commit added all 7 weight TTFs plus DESCRIPTION, METADATA.json, and OFL.txt.

**Critical finding**: The binary TTF files added in that commit are **identical** (byte-for-byte confirmed) to the files at upstream commit `76c161e` (Version 1.001, dated 2015-03-06), specifically from the `Martel Font Files/TTFs with ttfautohints/` directory.

File size comparison (all 7 weights match exactly):

| File | google/fonts | upstream @ 76c161e (v1.001) | upstream @ ae74b97 (v1.002) |
|------|-------------|---------------------------|---------------------------|
| Martel-Bold.ttf | 170,240 | 170,240 | 179,040 |
| Martel-DemiBold.ttf | 170,100 | 170,100 | 196,036 |
| Martel-ExtraBold.ttf | 170,900 | 170,900 | 173,196 |
| Martel-Heavy.ttf | 164,364 | 164,364 | 169,452 |
| Martel-Light.ttf | 170,540 | 170,540 | 184,052 |
| Martel-Regular.ttf | 170,196 | 170,196 | 185,204 |
| Martel-UltraLight.ttf | 168,700 | 168,700 | 183,028 |

The font files have never been updated in google/fonts since the original onboarding.

### Timeline

- 2015-03-06: Version 1.001 committed upstream (`76c161e`)
- 2015-04-20: Martel onboarded to google/fonts (`fc4d5c7d6`) using v1.001 binaries
- 2015-04-21: Version 1.002 committed upstream (`3a986ff`, `ae74b97`) — never onboarded
- 2024-03-04: Simon Cozens added `repository_url` to METADATA.pb in "Update upstreams" commit (`c891a9b85`)
- 2025-10-30: Felipe Sanches added commit hash `ae74b97` and override config.yaml (`2e7beb83a`) — **incorrectly referencing v1.002 instead of v1.001**

## Build Configuration

The upstream repo has no `config.yaml`. An override was created in google/fonts at `ofl/martel/config.yaml` referencing:
```yaml
buildVariable: false
sources:
  - Martel Source Files/Martel 20150421.glyphs
```

**Issue**: This references the v1.002 .glyphs file (`Martel 20150421.glyphs`), which only exists at commits `3a986ff` and later. At the correct commit `76c161e` (v1.001), the .glyphs file was named `Martel 20150306.glyphs`.

## Findings

### Issues Identified

1. **Wrong commit hash**: The current source block references `ae74b972c6870d296e1a2693c91006beba8c4801` (v1.002), but the actual binaries in google/fonts are from commit `76c161e71bc7c8c9304b4b6c468e9dd2ddc34661` (v1.001). This was confirmed by byte-for-byte comparison of the Regular TTF and exact file size matches across all 7 weights.

2. **Wrong source path in override config.yaml**: The override config references `Martel 20150421.glyphs` (the v1.002 filename), but at the correct commit (v1.001 / `76c161e`), the file was named `Martel 20150306.glyphs`.

3. **Upstream has newer unreleased version**: Version 1.002 (commits `3a986ff` and `ae74b97`) exists upstream with significantly larger font files (re-hinted with updated ttfautohint), updated copyright info, and a renamed .glyphs source. This version was never incorporated into Google Fonts and would need separate QA review.

### Root Cause

The error in commit `2e7beb83a` appears to have been caused by referencing the latest tagged version ("Version 1.002") in the upstream repo without verifying that the binary files actually match. The commit message itself says "sources info for Martel v1.002" — the investigator assumed the latest version was what had been onboarded, but the actual onboarding predated v1.002 by about a month.

## Recommended Source Block

The commit hash and override config must be corrected:

### METADATA.pb source block:
```
source {
  repository_url: "https://github.com/typeoff/martel"
  commit: "76c161e71bc7c8c9304b4b6c468e9dd2ddc34661"
}
```

### Override config.yaml:
```yaml
buildVariable: false
sources:
  - Martel Source Files/Martel 20150306.glyphs
```

**Confidence**: HIGH — Binary comparison confirms the correct commit with 100% certainty.
