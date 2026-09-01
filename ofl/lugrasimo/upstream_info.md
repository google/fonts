# Lugrasimo — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/docrepair-fonts/lugrasimo-fonts"
  commit: "18103084964ae884ad65dc31115dbc650b164a1a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lugrasimo-Regular.ttf"
    dest_file: "Lugrasimo-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

- **Repository**: https://github.com/docrepair-fonts/lugrasimo-fonts
- **Owner**: docrepair-fonts (The DocRepair Project)
- **Status**: Active, public repository
- **Branch**: main (single branch)
- **Contributors**: Adam Twardoch (twardoch), Yanone (post@yanone.de), Dave Crossland
- **Description**: A DocRepair font intended to improve ISO/IEC 29500 compliance by providing a fallback for Lucida Calligraphy. Based on Fondamento.

### Repository Structure

```
sources/
  config.yaml
  Lugrasimo-Regular.designspace
  masters/
    Lugrasimo-Regular.ufo/
fonts/
  ttf/
    Lugrasimo-Regular.ttf
packager.yaml
Makefile
```

The repository contains UFO sources with a designspace file and gftools-builder configuration at `sources/config.yaml`.

### Source Files

- **Designspace**: `sources/Lugrasimo-Regular.designspace` (single-axis weight, but only one master at 400)
- **UFO source**: `sources/masters/Lugrasimo-Regular.ufo`
- **Config**: `sources/config.yaml` (builds TTF only, no OTF/variable/webfont)

### config.yaml Contents

```yaml
buildOTF: false
buildVariable: false
buildWebfont: false
familyName: Lugrasimo
outputDir: ../fonts
sources:
  - Lugrasimo-Regular.designspace
```

## Onboarding History

### First Attempt — PR #6181 (merged 2023-04-13)

The first onboarding was submitted by Yanone via gftools-packager. The PR body referenced upstream commit `902c24b` (2023-04-01, "Copyright & metadata updates, switched Makefile to fontmake, nbspace = space"). However, the actual google/fonts commit body referenced a different upstream commit `d4f3068` (2023-04-11, "Update DESCRIPTION.en_us.html"). This discrepancy suggests the packager was run multiple times during the onboarding process.

### Second Onboarding — PR #6251 (merged 2023-06-16)

A second onboarding PR was submitted, also by Yanone. The PR body referenced upstream commit `98d6e63` (2023-05-05, "New binary"), but the actual google/fonts commit body referenced upstream commit `40395a6` (2023-06-15, "Changed copyright string"). Again, the packager was run at a different upstream commit than what appears in the PR body.

The google/fonts commit `751eba93` explicitly states: "Lugrasimo Version 1.001 taken from the upstream repo at commit 40395a6877a6bcdfe74deb2a7e355c0a4c7228e7."

### Binary Verification

- The font binary (`Lugrasimo-Regular.ttf`) in google/fonts has MD5 hash `0ae236079be078f034add6fd68ca69e1`.
- The binary at upstream commit `40395a6` matches: `0ae236079be078f034add6fd68ca69e1`.
- The binary at upstream commit `1810308` (HEAD) also matches: `0ae236079be078f034add6fd68ca69e1` (binary was not rebuilt after onboarding).
- The binary at upstream commit `98d6e63` does NOT match: `e1a3a8306cfa49a53884f19476f7e752`.

### Source Block History in METADATA.pb

1. **Commit `751eba93`** (PR #6251, 2023-06-15): Set commit to `40395a6` (was `d4f3068` from first onboarding)
2. **Commit `ea42b7c3`** (2023-08-14): Added stroke/classifications, no source block changes
3. **Commit `66f91f10`** (2024-04-03): Added files and branch entries to the source block
4. **Commit `4ad8ac68`** (2025-03-31): Changed commit from `40395a6` to `1810308` (HEAD), added config_yaml field

### Commit Hash Change Analysis

The Batch 2/4 commit (`4ad8ac68`) changed the upstream commit hash from `40395a6` to `1810308` based on fontc_crater's targets.json. However, `1810308` is a merge commit from 2023-07-23 — over a month AFTER the font was onboarded via PR #6251 (merged 2023-06-16). Between these two commits:
- 4 auto-generated commits were added (timestamps 2023-06-09)
- The `mu.glif` source file was added
- The font binary was NOT rebuilt

The correct onboarding commit is `40395a6`, which was the commit explicitly referenced by the gftools-packager in the onboarding commit message, and whose binary matches the one in google/fonts.

## Build Configuration

The upstream repo has a valid `sources/config.yaml` with gftools-builder configuration. It builds only a static TTF from the designspace file. The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly points to this file.

## Findings

1. **Incorrect commit hash**: The current METADATA.pb references commit `1810308` (HEAD, a merge commit from 2023-07-23), but the correct onboarding commit is `40395a6` (2023-06-15, "Changed copyright string"). The Batch 2/4 fontc_crater import incorrectly used the HEAD hash instead of the original onboarding commit.

2. **Binary verification confirms**: The font binary at both `40395a6` and `1810308` is identical (MD5: `0ae236079be078f034add6fd68ca69e1`), matching google/fonts. However, sources diverged — `mu.glif` was added between the two commits.

3. **Repository URL is correct**: `https://github.com/docrepair-fonts/lugrasimo-fonts` is valid and matches the copyright string in the font.

4. **config_yaml is correct**: `sources/config.yaml` exists in the upstream repo and is a valid gftools-builder configuration.

5. **Complex onboarding history**: The font went through two onboarding PRs (#6181 and #6251), each with discrepancies between the commit hash in the PR body and the commit hash in the google/fonts commit message. This is consistent with the gftools-packager being re-run at newer upstream commits after the PR was initially created.

## Recommended Source Block

The commit hash should be reverted to `40395a6877a6bcdfe74deb2a7e355c0a4c7228e7`, the commit explicitly used for onboarding:

```
source {
  repository_url: "https://github.com/docrepair-fonts/lugrasimo-fonts"
  commit: "40395a6877a6bcdfe74deb2a7e355c0a4c7228e7"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Lugrasimo-Regular.ttf"
    dest_file: "Lugrasimo-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
