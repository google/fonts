# Cascadia Code

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Aaron Bell, Mohamad Dakak, Viktoriya Grabowska, Liron Lavi Turkenich
**METADATA.pb path**: `ofl/cascadiacode/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/microsoft/cascadia-code |
| Commit | `56bcca3f2c1e4cb19458954f0e2bb4635960df91` |
| Config YAML | Override in google/fonts family directory |
| Branch | (not specified) |

## How the Repository URL Was Found

The repository URL `https://github.com/microsoft/cascadia-code` was present in the METADATA.pb `source { repository_url }` field from the initial onboarding. The original onboarding commit `0ed266781` (2025-03-18) by Aaron Bell explicitly states: "Taken from the upstream repo https://github.com/microsoft/cascadia-code at commit https://github.com/microsoft/cascadia-code/commit/56bcca3f2c1e4cb19458954f0e2bb4635960df91". The copyright in the font files also states "(c) 2021 Microsoft Corporation", consistent with the Microsoft-owned repository.

## How the Commit Hash Was Identified

The commit hash `56bcca3f2c1e4cb19458954f0e2bb4635960df91` was explicitly stated in the onboarding commit message (`0ed266781`, author: Aaron Bell, date: 2025-03-18). This is not a gftools-packager automated commit -- it was a direct onboarding by one of the font's designers (Aaron Bell).

Cross-verification: The upstream commit `56bcca3f` in the microsoft/cascadia-code repo has the message "Update FONTLOG and Build for v2407.24 (#785)", authored by Dustin L. Howett on 2024-11-18. This aligns with the google/fonts commit message stating "Cascadia Code: version 2407.024". The version number matches precisely.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository at the recorded commit hash. The upstream repo uses a custom `build.py` script and Azure Pipelines for building. An override `config.yaml` was created in the google/fonts family directory (`ofl/cascadiacode/config.yaml`) as part of the sources info enrichment commit `692a7f508` (2025-04-02). The override config references:

```yaml
buildVariable: true
sources:
  - sources/CascadiaCode_variable.designspace
  - sources/CascadiaCode_variable_italic.designspace
```

Both designspace files exist in the upstream repo at the recorded commit. Since an override config exists in google/fonts, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-18
- Commit message: "Update FONTLOG and Build for v2407.24 (#785)"
- Source files at commit: `sources/CascadiaCode_variable.designspace`, `sources/CascadiaCode_variable_italic.designspace`, plus 6 UFO master sources
- Override config.yaml in google/fonts: Yes
- Font was added to Google Fonts on 2025-03-18

## Confidence Level

**HIGH** -- The commit hash was directly stated in the onboarding commit message by one of the font's designers. The version number (2407.024) matches between the google/fonts commit and the upstream commit. Both the repository URL and commit hash are fully verified.

## Open Questions

None. Both Cascadia Code and Cascadia Mono share the same upstream repository and commit hash, which is expected since they are built from the same source (Cascadia Mono is the non-ligature variant of Cascadia Code).
