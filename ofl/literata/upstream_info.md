# Literata — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The current source block in `ofl/literata/METADATA.pb` is:

```
source {
  repository_url: "https://github.com/googlefonts/literata"
  commit: "0c2761b727a1b3a7cffd313c37f0f5163dfc7a63"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Literata[opsz,wght].ttf"
    dest_file: "Literata[opsz,wght].ttf"
  }
  files {
    source_file: "fonts/variable/Literata-Italic[opsz,wght].ttf"
    dest_file: "Literata-Italic[opsz,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

- **Repository URL**: https://github.com/googlefonts/literata (verified accessible, HTTP 200)
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/literata/`
- **Repo status**: Clean, up to date with origin, on branch `main`
- **Remote**: `https://github.com/googlefonts/literata` (fetch/push)
- **Branches**: `main` (only branch)
- **Tags**: `3.103`
- **Total commits**: 1 (single initial commit containing the entire project)

The upstream repo contained a single commit (`0c2761b`, dated 2023-05-19) titled "Built fonts 3.103". This commit was the initial commit populating the repository with the full project — sources, built fonts (variable, static, webfonts), documentation, and historical source versions (v2.0, v2.1, v3.0, v3.021).

### Source Files

The repository contained the following source files at the referenced commit:

- `sources/Literata.glyphs` (~9.4 MB)
- `sources/Literata-Italic.glyphs` (~9.0 MB)
- `sources/config.yaml` (gftools-builder configuration)

Additionally, historical source versions were preserved in subdirectories:
- `sources/v_2.0/` — Glyphs sources for v2.0
- `sources/v_2.1/` — Glyphs sources for v2.1 with build scripts
- `sources/v_3.0/` — Glyphs sources for v3.0
- `sources/v_3.021/` — Designspace/UFO sources for v3.021 with build scripts

### Config.yaml

The `sources/config.yaml` file was a complete gftools-builder configuration:

- **Sources**: `Literata.glyphs`, `Literata-Italic.glyphs`
- **buildOTF**: false
- **buildStatic**: true
- **axisOrder**: opsz, wght, ital
- **familyName**: "Literata"
- **stat**: Full STAT table configuration for both upright and italic variable fonts, defining optical size values (7pt, 12pt, 36pt, 72pt) and weight values (ExtraLight through Black)

## Onboarding History

Literata had multiple updates in google/fonts:

1. **2018-12-06** — `62dc5cc`: Initial addition as "literata: v2.100 added (VF with wght axis)" (PR #1781). Taken from the upstream repo at release tag `v2.100`. Added static Roman and Italic TTFs with `wght` axis only.

2. **2019-04-15** — `145ce9d`: METADATA.pb updated (PR #2029).

3. **2019-08-12** — `9253a514`: Renamed files related to VFs (PR #2216).

4. **2019-12-20** — `2f7e976a`: "literata: v3.002 added" (PR #2580). Major update taken from upstream repo at tagged release `3.002`. Added variable fonts with `opsz` and `wght` axes, plus extensive static font instances for multiple optical sizes (7pt, 12pt, 36pt, 72pt). This introduced the optical size axis.

5. **2020-01-07** — `5d627545`: Source keys removed from METADATA.pb (PR #2585). This was a bulk operation across many families.

6. **Various** — Language metadata updates and rollbacks (PRs #4160, #4677, #4706).

7. **2022-07-06** — `70b0fc8a`: Static fonts removed for unhinted variable font families (PR #3695).

8. **2023-05-19** — `c8018e98`: **Current version** — "[gftools-packager] Literata: Version 3.103;gftools[0.9.29] added". This was the last update to the font binaries, by Rosalie Wagner. The commit message explicitly referenced upstream commit `0c2761b727a1b3a7cffd313c37f0f5163dfc7a63`. This added the initial source block with `repository_url` and `commit` fields. Merged via PR #6283 on 2023-05-24.

9. **2024-04-03** — `66f91f1`: Simon Cozens merged upstream.yaml data into METADATA.pb, adding the `files { }` mappings and `branch: "main"`.

10. **2025-03-31** — `4ad8ac68`: Batch operation by Felipe Sanches ported `config_yaml: "sources/config.yaml"` from fontc_crater targets list.

## Build Configuration

- **config.yaml location**: `sources/config.yaml` in the upstream repo
- **Config exists at referenced commit**: Verified (blob `a2129c8` at commit `0c2761b`)
- **Config type**: gftools-builder YAML format
- **Source format**: Glyphs (.glyphs) files
- **Override config.yaml in google/fonts**: Not present (not needed — upstream config exists)
- **METADATA.pb config_yaml field**: Set to `sources/config.yaml` (correct)

## Findings

**Commit hash verification**: The commit hash `0c2761b727a1b3a7cffd313c37f0f5163dfc7a63` in METADATA.pb was verified as correct through multiple lines of evidence:

1. The gftools-packager commit message (`c8018e98`) explicitly referenced this commit
2. PR #6283 body confirmed the same commit hash
3. The upstream repo has only one commit (`0c2761b`), tagged `3.103`
4. SHA-256 hashes of both `Literata[opsz,wght].ttf` and `Literata-Italic[opsz,wght].ttf` matched exactly between google/fonts and the upstream repo at this commit
5. File sizes matched exactly (955,132 bytes for upright, 902,728 bytes for italic)
6. The commit date in upstream (2023-05-19 14:57:27) closely preceded the gftools-packager commit date (2023-05-19 15:06:57), consistent with automated packaging

**Repository structure note**: The upstream repo was created with a single initial commit containing the entire project history as archived subdirectories. This is unusual — most upstream repos have an incremental commit history. However, the single commit contains all necessary source files and build configuration.

**Designer**: Literata was designed by TypeTogether, originally created for Google Play Books.

**Source block completeness**: The source block is fully complete with repository_url, commit hash, file mappings, branch, and config_yaml. No corrections needed.

**Confidence**: HIGH — All data points are consistent and verified through binary file comparison.

## Recommended Source Block

The current source block is correct and complete. No changes recommended:

```
source {
  repository_url: "https://github.com/googlefonts/literata"
  commit: "0c2761b727a1b3a7cffd313c37f0f5163dfc7a63"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Literata[opsz,wght].ttf"
    dest_file: "Literata[opsz,wght].ttf"
  }
  files {
    source_file: "fonts/variable/Literata-Italic[opsz,wght].ttf"
    dest_file: "Literata-Italic[opsz,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
