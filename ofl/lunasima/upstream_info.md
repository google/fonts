# Lunasima — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/docrepair-fonts/lunasima-fonts"
  commit: "88f44d7a6c3693aa455dc7194c6e5a01cb2a39ae"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lunasima-Regular.ttf"
    dest_file: "Lunasima-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Lunasima-Bold.ttf"
    dest_file: "Lunasima-Bold.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

**Repository**: https://github.com/docrepair-fonts/lunasima-fonts
**Description**: Lunasima OFL fonts
**Created**: 2023-03-17
**Last pushed**: 2023-06-15
**Default branch**: main

The upstream repository contains a standard Google Fonts project structure based on the googlefonts-project-template. It includes:

- `sources/config.yaml` — gftools-builder configuration
- `sources/Lunasima-Regular.designspace` — designspace file defining weight (400-700) and width (1-200) axes
- `sources/masters/Lunasima-Regular.ufo` — Regular master UFO source
- `sources/masters/Lunasima-Bold.ufo` — Bold master UFO source
- `fonts/ttf/Lunasima-Regular.ttf` — compiled Regular TTF (195,140 bytes)
- `fonts/ttf/Lunasima-Bold.ttf` — compiled Bold TTF (196,420 bytes)
- `packager.yaml` — gftools-packager configuration
- `Makefile` — build automation (uses fontmake directly, not gftools-builder)

The `config.yaml` at `sources/config.yaml` contains:

```yaml
buildOTF: false
buildVariable: false
buildWebfont: false
familyName: Lunasima
outputDir: ../fonts
sources:
  - Lunasima-Regular.designspace
```

This config builds static TTF instances only (Regular and Bold), no variable font, no OTF, no webfont. The designspace defines two axes (weight and width) but the instances are fixed at specific locations.

Lunasima is a DocRepair project font, intended to improve compliance with the ISO/IEC 29500 standard by providing fallback for Lucida Grande. It is based on Noto Sans.

## Onboarding History

Lunasima was added to Google Fonts through PR #6253, created by Yanone on 2023-05-05 and merged on 2023-06-16.

### Commit timeline in google/fonts:

1. **`4c30359`** (2023-06-15) — `[gftools-packager] Lunasima: Version 2.009 added` — Original onboarding by Yanone. The commit message explicitly referenced upstream commit `88f44d7a6c3693aa455dc7194c6e5a01cb2a39ae`.
2. **`66f91f1`** (2024-04-03) — `Merge upstream.yaml into METADATA.pb [skip ci]` — Simon Cozens merged the upstream.yaml file mappings into the METADATA.pb source block.
3. **`4ad8ac6`** (2025-03-31) — `[Batch 2/4] port info from fontc_crater targets list` — Added `config_yaml: "sources/config.yaml"` to the source block.

### PR body discrepancy:

The PR #6253 body originally referenced commit `3e135f62521c769a7a6ad724e21113cb2c92163d` ("Removed polytonic Greek" by twardoch, 2023-04-18). However, the final commit in google/fonts referenced `88f44d7a6c3693aa455dc7194c6e5a01cb2a39ae` ("Use production names" by Yanone, 2023-06-15). This is consistent with the gftools-packager workflow: the PR was created on 2023-05-05 with the then-latest commit, but additional upstream work continued (including glyphs remapping and new font builds by Yanone on 2023-06-14 and 2023-06-15). The packager was re-run before the final merge, updating the referenced commit to the latest one.

### Contributors:

- **Yanone** (post@yanone.de) — Font engineer who created the PR and made the final upstream commits
- **twardoch** (Adam Twardoch) — Contributor to the upstream repo, made earlier commits

## Build Configuration

**Config path**: `sources/config.yaml`
**Config status**: Present in upstream repo, correctly referenced in METADATA.pb

The config.yaml is a standard gftools-builder configuration that produces static TTF files only. The Makefile in the repo uses `fontmake` directly for building, but the `config.yaml` is compatible with gftools-builder as well.

Note: The local clone is a shallow clone (depth 1), which means only the latest commit (`88f44d7`) is available locally. The GitHub API confirmed that the full history has 30 commits, including the `3e135f6` commit referenced in the PR body.

## Findings

1. **Source block is complete and correct**: The METADATA.pb source block contains all required fields — repository_url, commit hash, file mappings, branch, and config_yaml.

2. **Commit hash verified**: The commit `88f44d7a6c3693aa455dc7194c6e5a01cb2a39ae` is the latest (and only visible in the shallow clone) commit on the main branch. It was authored by Yanone on 2023-06-15, one day before the PR was merged on 2023-06-16.

3. **Binary files match**: The SHA-256 hashes of both `Lunasima-Regular.ttf` and `Lunasima-Bold.ttf` in google/fonts exactly match the files in the upstream repo at commit `88f44d7`, confirming these are the pre-compiled binaries from the upstream repo (not re-built by gftools-builder).

4. **No additional upstream changes**: The upstream repo has not been updated since `88f44d7` (last pushed 2023-06-15), so there is no risk of drift between google/fonts and the upstream.

5. **No action needed**: All metadata is correct and complete.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/docrepair-fonts/lunasima-fonts"
  commit: "88f44d7a6c3693aa455dc7194c6e5a01cb2a39ae"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lunasima-Regular.ttf"
    dest_file: "Lunasima-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Lunasima-Bold.ttf"
    dest_file: "Lunasima-Bold.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
