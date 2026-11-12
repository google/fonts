# Manuale — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/Omnibus-Type/Manuale"
  commit: "20a5ab6a0da1c8cb56916d843e50db0ad6b6dfd3"
  config_yaml: "sources/config.yaml"
}
```

The source block was built up in two stages:
1. Simon Cozens added the `repository_url` in the "Update upstreams" commit (2023-12-14).
2. Felipe Sanches added the `commit` and `config_yaml` fields in the "[Batch 2/4] port info from fontc_crater targets list" commit (2025-03-31), sourced from fontc_crater's target.json.

## Repository Analysis

- **Repository**: https://github.com/Omnibus-Type/Manuale
- **Cached at**: `upstream_repos/fontc_crater_cache/Omnibus-Type/Manuale`
- **Default branch**: master
- **Repo status**: Clean, up to date with origin
- **Total commits**: 1 (the repo was created by force-pushing a restructured version)

The upstream repository contains only a single commit (`20a5ab6`) dated 2021-07-22. This commit was authored by Aaron Bell (aaron@sajatypeworks.com) with the message "Rebuilding static instances with autohinting." It reorganized the entire repository into the UFR (Unified Font Repository) format.

### Repository Structure

```
sources/
  config.yaml
  Manuale.glyphs
  Manuale-Italic.glyphs
fonts/
  variable/
    Manuale[wght].ttf
    Manuale-Italic[wght].ttf
  ttf/ (static instances)
  otf/ (static instances)
  webfonts/
```

### Source Files

- `sources/Manuale.glyphs` — Glyphs source for the upright
- `sources/Manuale-Italic.glyphs` — Glyphs source for the italic

## Onboarding History

### Initial Onboarding (v0.075, 2016-12-03)

The font was first added to Google Fonts in commit `3a506845` by Marc Foley as static font files (Regular, Italic, Medium, MediumItalic, Bold, BoldItalic, SemiBold, SemiBoldItalic).

### Variable Font Upgrade (v1.000, 2019-09-16)

Marc Foley upgraded the font to variable format in commit `77a8f07e` with the message "manuale: v1.000 added." The commit message referenced upstream PR #6 at commit `39e7a697efaf956d9ad4feec5ab7002abab3bce1`. This added `Manuale[wght].ttf` and `Manuale-Italic[wght].ttf` while removing the old static files.

### UFR Rebuild (v1.002, 2021-08-05)

Aaron Bell updated the font to UFR format in PR #3643, merged as commit `a9c658a2`. The PR body stated: "Font repo updated to the UFR format (https://github.com/aaronbell/Manuale). PR'd to upstream. Font files rebuilt."

This is the most recent update to the font binary files in google/fonts. The variable font files in this commit match exactly with the files at commit `20a5ab6` in the upstream repo (verified by SHA256 hash comparison):

- `Manuale[wght].ttf`: `19ea09ad2fbf321cf8f94ac3f66547bc9b2bdf3723a2f073615eaa02fe17ded6`
- `Manuale-Italic[wght].ttf`: `13eb20f22e8b6a28eba93670219cb472980e8fd006319a917316434e2ed1961a`

### Static Font Removal (2021-08-16)

Static fonts were removed in PR #3695 ("Remove static fonts for unhinted variable font families").

## Build Configuration

The upstream repo has a `config.yaml` at `sources/config.yaml` containing a valid gftools-builder configuration:

```yaml
sources:
  - Manuale.glyphs
  - Manuale-Italic.glyphs
axisOrder:
  - wght
familyName: Manuale
stat:
  Manuale[wght].ttf:
  - name: Weight
    tag: wght
    values:
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
    - name: ExtraBold
      value: 800
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  Manuale-Italic[wght].ttf:
  - name: Weight
    tag: wght
    values:
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
    - name: ExtraBold
      value: 800
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
```

The config references two `.glyphs` source files and defines STAT tables for both the upright and italic variable fonts.

## Findings

1. **Source block is complete and correct.** The repository URL, commit hash, and config_yaml path are all accurate and verified.

2. **Commit hash verified.** The upstream repo has only a single commit (`20a5ab6`), which is exactly the one referenced in METADATA.pb. The binary font files at this commit match the files in google/fonts byte-for-byte (SHA256 verified).

3. **Timeline is consistent.** The upstream commit (2021-07-22) predates the google/fonts PR #3643 merge (2021-08-05), confirming this was the commit used for the rebuild.

4. **Config.yaml is valid.** The config at `sources/config.yaml` contains proper gftools-builder configuration with source references and STAT table definitions.

5. **No corrections needed.** All metadata fields are accurate.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/Omnibus-Type/Manuale"
  commit: "20a5ab6a0da1c8cb56916d843e50db0ad6b6dfd3"
  config_yaml: "sources/config.yaml"
}
```
