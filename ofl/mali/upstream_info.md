# Mali — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/cadsondemak/Mali"
}
```

The source block contains only `repository_url`. There is no `commit` hash and no `config_yaml` field. An override `config.yaml` already exists in the google/fonts family directory (created in commit `5ddf312` on 2026-02-20).

## Repository Analysis

- **Repository**: https://github.com/cadsondemak/Mali
- **Owner**: cadsondemak (Cadson Demak, a Thai type foundry)
- **Default branch**: master
- **Source file**: `source/Mali-Master.glyphs` (Glyphs format)
- **Pre-compiled fonts**: `fonts/` directory contains .ttf, .eot, .woff, .woff2 files
- **config.yaml in upstream**: None — the upstream repo has no gftools-builder configuration at any commit
- **Latest upstream commit**: `7e11de1` (2020-10-27) "Update Mali-Master.glyphs"
- **Repo status**: Clean, single branch (master)

The upstream repository contains a `.glyphs` source file suitable for gftools-builder compilation, but no `config.yaml`. The repo also includes pre-compiled font binaries in the `fonts/` directory and a GitHub Pages website for specimen display.

## Onboarding History

Mali was onboarded to Google Fonts through three commits by Marc Foley:

### 1. Initial onboarding (2018-08-22)
- **google/fonts commit**: `78b2603` — "mali: v1.000 added"
- **Upstream commit referenced**: `d22db34` ("Merge pull request #7 from m4rc1e/gf-mastering — Fixed fonts to pass fontbakery and gf-glyphs-scripts")
- This was Marc Foley's PR to the upstream repo that fixed the fonts for Google Fonts compatibility

### 2. Vertical metrics fix (2018-08-24)
- **google/fonts commit**: `b74118b` — "mali: Updated fonts to avoid clipping."
- **Upstream commit referenced**: `4f4843c` ("Merge pull request #9 from m4rc1e/metrics — Updated vertical metrics to stop first line clipping")
- Marc Foley's second upstream PR that fixed vertical metrics causing first-line clipping

### 3. Unhinted fonts (2018-09-07)
- **google/fonts commit**: `fbdd512` — "mali: unhinted fonts."
- **Upstream commit referenced**: None explicitly stated
- Commit body: "In the future, we plan to release this family as an unhinted variable font."
- This commit significantly reduced file sizes (e.g., Mali-Regular.ttf went from 170744 to 112756 bytes) by removing hinting
- The source used was from upstream commit `4f4843c`, as there were no upstream changes between Aug 2018 and July 2020

### 4. Source block added (2023-12-14)
- **google/fonts commit**: `6392e4f` — "Update upstreams" by Simon Cozens
- Added `repository_url: "https://github.com/cadsondemak/Mali"` to METADATA.pb

### 5. Override config.yaml added (2026-02-20)
- **google/fonts commit**: `5ddf312` — "Add config_yaml enrichment for 82 font families"
- Created override `config.yaml` referencing `source/Mali-Master.glyphs`

## Build Configuration

- **Upstream config.yaml**: None — the upstream repo has never had a gftools-builder configuration file
- **Override config.yaml**: Already exists in the google/fonts family directory with content:
  ```yaml
  sources:
    - source/Mali-Master.glyphs
  ```
- **Source file verified**: `source/Mali-Master.glyphs` exists at upstream commit `4f4843c` (the commit used for the current fonts in google/fonts)

## Findings

1. **Missing commit hash**: The METADATA.pb source block lacks a `commit` field. The correct commit hash is `4f4843c99ad83880f530b33a2ac1d69054c236bf` — this is the last upstream commit used before the fonts were added/updated in google/fonts. The "unhinted fonts" update (2018-09-07) used the same upstream source from this commit.

2. **Override config.yaml already in place**: The override `config.yaml` was added in February 2026 and correctly references `source/Mali-Master.glyphs`. No `config_yaml` field is needed in METADATA.pb since google-fonts-sources auto-detects local overrides.

3. **Upstream has newer commits not in google/fonts**: The upstream repo has commits from 2020 (`0f0093f`, `4889e45`, `58355f7`, `7e11de1`) that modified the source file, but these were never incorporated into google/fonts. Any future update would need a separate review process.

4. **Confidence**: HIGH — The onboarding commits in google/fonts explicitly reference upstream commits `d22db34` and `4f4843c`, and the timeline is clear with no ambiguity. The last font-modifying commit (`fbdd512`) used the same upstream source from `4f4843c`.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/cadsondemak/Mali"
  commit: "4f4843c99ad83880f530b33a2ac1d69054c236bf"
}
```

Note: `config_yaml` is intentionally omitted because an override `config.yaml` already exists in the google/fonts family directory, and google-fonts-sources auto-detects it.
