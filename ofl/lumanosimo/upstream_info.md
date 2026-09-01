# Lumanosimo — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/docrepair-fonts/lumanosimo-fonts"
  commit: "a7395fda4d79523ae6f0a798e2ea2d8ed524fc80"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lumanosimo-Regular.ttf"
    dest_file: "Lumanosimo-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

The source block is fully populated with repository_url, commit hash, file mappings, branch, and config_yaml.

## Repository Analysis

**Repository**: https://github.com/docrepair-fonts/lumanosimo-fonts
**Owner**: docrepair-fonts
**Cached at**: `upstream_repos/fontc_crater_cache/docrepair-fonts/lumanosimo-fonts/`

The upstream repository contained only a single commit (`a7395fd`) on the `main` branch, with the message "Decomposed nested components" dated 2023-06-15. This indicated the repository was force-pushed or rebased at some point, as earlier commit hashes referenced in google/fonts PRs (e.g., `9c7040fd`, `5f7b8f5e`, `8f8b4fa1`) no longer existed in the repo history.

### Repository Structure

```
.github/workflows/build.yaml
sources/config.yaml
sources/Lumanosimo-Regular.designspace
sources/masters/Lumanosimo-Regular.ufo/
fonts/ttf/Lumanosimo-Regular.ttf
packager.yaml
OFL.txt
DESCRIPTION.en_us.html
Makefile
README.md
```

The repo used the standard google-fonts-template structure with a `packager.yaml` for gftools-packager integration.

### Source Files

- **Designspace**: `sources/Lumanosimo-Regular.designspace` — defined weight and width axes but only contained a single master (Regular), so the font was built as a static TTF (not variable).
- **UFO source**: `sources/masters/Lumanosimo-Regular.ufo/`
- **Config**: `sources/config.yaml` — configured to build static TTF only (`buildOTF: false`, `buildVariable: false`).

## Onboarding History

### Initial Onboarding — PR #6179 (merged 2023-04-13)

- Created by **Yanone** (post@yanone.de)
- Commit message: `[gftools-packager] Lumanosimo: Version 1.010; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28.dev5+ged2979d] added`
- PR body referenced upstream commit `5f7b8f5ef520ddb71a50751887c4c85f512e1878`
- The actual google/fonts commit (`682819999`) referenced a different hash: `9c7040fdb64635624ba28c03458e29778414c4a0`
- The binary was 65,896 bytes (hinted with ttfautohint)

### Update — PR #6250 (merged 2023-06-16)

- Also created by **Yanone**
- Commit message: `[gftools-packager] Lumanosimo: Version 1.010 added`
- PR body referenced upstream commit `8f8b4fa1901a36e8a56fd15ab93ec1bea40580eb`
- The actual google/fonts commit (`85974606d`) referenced commit `a7395fda4d79523ae6f0a798e2ea2d8ed524fc80`
- The binary was replaced — shrunk from 65,896 to 38,736 bytes (unhinted version)
- The METADATA.pb commit hash was updated from `9c7040fd` to `a7395fd`

### Source Block Enrichment — Batch 2/4 (2025-03-31)

- Commit `4ad8ac68` added the `config_yaml: "sources/config.yaml"` field
- This was part of a batch import from fontc_crater's targets list

## Build Configuration

**Config file**: `sources/config.yaml` (in upstream repo)

```yaml
---
buildOTF: false
buildVariable: false
familyName: Lumanosimo
outputDir: ../fonts
sources:
  - Lumanosimo-Regular.designspace
```

The config was valid and present in the upstream repo at the referenced commit. It built a single static TTF from the designspace, outputting to the `fonts/` directory.

## Findings

1. **Source block is complete and correct.** The METADATA.pb had all required fields: repository_url, commit hash, file mappings, branch, and config_yaml.

2. **Commit hash was verified.** The commit `a7395fda4d79523ae6f0a798e2ea2d8ed524fc80` was the only commit in the upstream repository. The binary file at `fonts/ttf/Lumanosimo-Regular.ttf` in the upstream repo matched the file in google/fonts exactly (SHA-256: `768d2bbe3b9dcfe5cdd89a01cf4f90b9729b58ae565233a2fab0f7f48b42f662`).

3. **Repository was force-pushed.** The upstream repo contained only a single commit, yet the google/fonts history referenced three different upstream commit hashes across two PRs (`5f7b8f5e` in PR #6179 body, `9c7040fd` in the initial commit message, and `8f8b4fa1` in PR #6250 body vs `a7395fd` in the final commit). The current sole commit `a7395fd` ("Decomposed nested components") dated 2023-06-15 was the correct and current one.

4. **All mapped files matched.** OFL.txt, DESCRIPTION.en_us.html, and the binary TTF were identical between the upstream repo and google/fonts.

5. **No action needed.** The source block was fully populated and accurate.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/docrepair-fonts/lumanosimo-fonts"
  commit: "a7395fda4d79523ae6f0a798e2ea2d8ed524fc80"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lumanosimo-Regular.ttf"
    dest_file: "Lumanosimo-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
