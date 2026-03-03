# Mate — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The source block in `ofl/mate/METADATA.pb` is already fully populated:

```
source {
  repository_url: "https://github.com/etunni/mate"
  commit: "2ea8febc952610379af663b1651411493d34beea"
  config_yaml: "sources/mate.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/mate/ttf/Mate-Regular.ttf"
    dest_file: "Mate-Regular.ttf"
  }
  files {
    source_file: "fonts/mate/ttf/Mate-Italic.ttf"
    dest_file: "Mate-Italic.ttf"
  }
  branch: "master"
}
```

## Repository Analysis

**Repository**: https://github.com/etunni/mate
**Owner**: Eduardo Tunni (etunni)
**Branch**: master (only branch)
**Accessible**: Yes (HTTP 200)

The upstream repository was set up by Emma Marichal (emmamarichal) via PR #1 to the owner's repo, merged on 2023-02-24 by Eduardo Rodriguez Tunni. The repository has exactly one commit — the merge commit `2ea8febc952610379af663b1651411493d34beea`.

### Repository Structure

```
AUTHOR.txt
CONTRIBUTORS.txt
OFL.txt
README.md
requirements.txt
documentation/
  image1.png, image2.png, image3.png
fonts/
  mate/
    otf/   Mate-Regular.otf, Mate-Italic.otf
    ttf/   Mate-Regular.ttf, Mate-Italic.ttf
    webfonts/ Mate-Regular.woff2, Mate-Italic.woff2
  matesc/
    otf/   MateSC-Regular.otf
    ttf/   MateSC-Regular.ttf
    webfonts/ MateSC-Regular.woff2
sources/
  Mate.glyphs
  Mate-Italic.glyphs
  MateSC.glyphs
  mate.yaml
  matesc.yaml
```

The repo contains sources and pre-built binaries for both Mate and Mate SC font families. The sources are `.glyphs` files (GlyphsApp format).

### Cached Repo Status

The cached clone at `fontc_crater_cache/etunni/mate/` was clean (no local modifications, up to date with origin).

## Onboarding History

### Original Addition

The Mate font was originally added to Google Fonts in the initial commit (`90abd17b4`, 2015-03-07).

### Update via gftools-packager

The font was updated via PR #5930 on google/fonts:
- **PR title**: "Mate: Version 1.003; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.24] added"
- **Author**: Emma Marichal (emmamarichal)
- **Merged by**: Marc Foley (m4rc1e) on 2023-03-01
- **Commit**: `65c9b9722` — "[gftools-packager] Mate: Version 1.003; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.24] added"
- The commit message explicitly states: "taken from the upstream repo https://github.com/etunni/mate at commit 2ea8febc952610379af663b1651411493d34beea"

### Source Block History

1. The initial source block (repository_url, commit, files, branch) was added by gftools-packager in commit `65c9b9722` (2023-02-24).
2. The `config_yaml: "sources/mate.yaml"` field was added and `branch` was removed in commit `53995c52a` (2025-03-25) — "[METADATA.pb] Populate font sources related fields for a few font families" by Felipe Sanches.
3. The `branch: "master"` field was re-added in commit `f19b6da7d` (2025-03-26) — "revert removal of branch values on METADATA.pb files" by Felipe Sanches, as gftools-packager may still rely on that field.

## Build Configuration

The upstream repo contains a config.yaml at `sources/mate.yaml`:

```yaml
sources:
  - Mate.glyphs
  - Mate-Italic.glyphs
outputDir: "../fonts/mate"
```

This is a valid gftools-builder configuration. The `config_yaml` field in METADATA.pb correctly points to `sources/mate.yaml`.

Note: The repo also contains `sources/matesc.yaml` for the Mate SC family (a separate family in google/fonts).

## Findings

### Binary File Verification

Both TTF files in google/fonts are byte-identical to the files in the upstream repo at the referenced commit:
- `Mate-Regular.ttf`: MD5 `7b63a0807aee78be5f88e75974251dc5` — **match**
- `Mate-Italic.ttf`: MD5 `7169eb8afa4d442f410baded248b1b1c` — **match**

### Commit Hash Verification

The commit hash `2ea8febc952610379af663b1651411493d34beea` was verified:
- It is the only commit in the upstream repository (a merge commit from 2023-02-24)
- It is explicitly referenced in the gftools-packager commit message and PR #5930 body
- The binary files at this commit match those in google/fonts
- **Confidence: HIGH** — the commit hash is correct

### Summary

The source block is complete and accurate. All fields are populated correctly:
- Repository URL is valid and accessible
- Commit hash is verified (only commit in the repo, binary match confirmed)
- Config YAML path points to a valid gftools-builder configuration
- File mappings are correct
- Branch is correctly set to "master"

No corrections are needed.

## Recommended Source Block

The current source block is already correct. No changes recommended:

```
source {
  repository_url: "https://github.com/etunni/mate"
  commit: "2ea8febc952610379af663b1651411493d34beea"
  config_yaml: "sources/mate.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/mate/ttf/Mate-Regular.ttf"
    dest_file: "Mate-Regular.ttf"
  }
  files {
    source_file: "fonts/mate/ttf/Mate-Italic.ttf"
    dest_file: "Mate-Italic.ttf"
  }
  branch: "master"
}
```
