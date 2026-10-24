# Kameron — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kameron`
**Status**: complete

## Initial State

METADATA.pb already contained a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/kameronFont"
  commit: "c13447c3b5fc11abd2eb640bd4a8dd789e38d76f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Kameron[wght].ttf"
    dest_file: "Kameron[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

No override `config.yaml` existed in the google/fonts family directory.

## Investigation

### Onboarding History

Kameron was originally added to Google Fonts on 2011-06-08 as a static font. The most recent update was onboarded on 2023-09-08 by Emma Marichal via gftools-packager in PR #6685 ("Kameron: Version 1.100 added"), merged 2023-09-12 by Rosalie Wagner.

The gftools-packager commit message explicitly stated: "Kameron Version 1.100 taken from the upstream repo https://github.com/googlefonts/kameronFont at commit https://github.com/googlefonts/kameronFont/commit/4c36d3f42f93806b911562d50927406fbb043f89."

### Commit Hash History

The original onboarding commit was `4c36d3f42f93806b911562d50927406fbb043f89`. This was recorded in the initial source block added during the upstream.yaml merge (commit `66f91f1`, 2024-04-03).

Later, the Batch 2/4 commit (`4ad8ac6`, 2025-03-31) changed the commit hash to `c13447c3b5fc11abd2eb640bd4a8dd789e38d76f` and added the `config_yaml: "sources/config.yaml"` field. This happened because the fontc_crater targets.json referenced this newer commit.

### Upstream Repository State

The upstream repo at `https://github.com/googlefonts/kameronFont` contains only a single commit:
- `c13447c3b5fc11abd2eb640bd4a8dd789e38d76f` (2025-02-24): "add sources/config.yaml"

This commit is a root commit that contains the entire repo contents (all fonts, sources, documentation, plus config.yaml) in a single squashed commit. The original commit `4c36d3f` no longer exists in the repo history — the repo was apparently rebuilt/force-pushed as a single commit when config.yaml was added.

### Binary Font Verification

The `Kameron[wght].ttf` in google/fonts and the `fonts/variable/Kameron[wght].ttf` in the upstream repo at HEAD are identical:
- SHA-256: `b7e9bf8756c3403c1acb1d93d225dcd14dbafc9864ee891268c89459e99db410`

This confirms that the current HEAD commit in the upstream repo contains the same binary fonts that were onboarded.

### Source Files and Config

The upstream repo contains gftools-builder compatible sources:
- `sources/Kameron.glyphs` — Glyphs source file
- `sources/config.yaml` — gftools-builder configuration referencing `Kameron.glyphs`

The config.yaml is minimal and correct:
```yaml
sources:
  - Kameron.glyphs
```

### Assessment

The current METADATA.pb source block is correct and complete:
- **repository_url**: Valid, points to the correct upstream repo
- **commit**: Points to the only existing commit in the repo (HEAD of master), which contains all sources and matching binary fonts
- **config_yaml**: Correctly references `sources/config.yaml` which exists at the referenced commit
- **files**: Correctly maps `OFL.txt` and `fonts/variable/Kameron[wght].ttf`

While the original onboarding commit (`4c36d3f`) no longer exists due to repo reconstruction, the current commit (`c13447c`) contains identical font binaries and additionally includes the config.yaml. This is acceptable because the font content is verified identical and the referenced commit is the only one available.

## Actions Taken

No actions were needed. The source block in METADATA.pb is complete and verified.

## Final State

The Kameron family has a complete and verified source block in METADATA.pb. The repository URL is valid, the commit hash references the only existing commit in the upstream repo (which contains identical binary fonts to those in google/fonts), and the config.yaml path is correctly specified.

## Source Block

```
source {
  repository_url: "https://github.com/googlefonts/kameronFont"
  commit: "c13447c3b5fc11abd2eb640bd4a8dd789e38d76f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Kameron[wght].ttf"
    dest_file: "Kameron[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```
