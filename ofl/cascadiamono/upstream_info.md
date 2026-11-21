# Cascadia Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Aaron Bell, Mohamad Dakak, Viktoriya Grabowska, Liron Lavi Turkenich
**METADATA.pb path**: `ofl/cascadiamono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/microsoft/cascadia-code |
| Commit | `56bcca3f2c1e4cb19458954f0e2bb4635960df91` |
| Config YAML | Override in google/fonts family directory |
| Branch | (not specified) |

## How the Repository URL Was Found

The repository URL `https://github.com/microsoft/cascadia-code` was present in the METADATA.pb `source { repository_url }` field from the initial onboarding. The original onboarding commit `e64c73014` (2025-03-18) by Aaron Bell explicitly states: "Taken from the upstream repo https://github.com/microsoft/cascadia-code at commit https://github.com/microsoft/cascadia-code/commit/56bcca3f2c1e4cb19458954f0e2bb4635960df91".

Cascadia Mono is the non-ligature variant of Cascadia Code. Both families share the same upstream repository (microsoft/cascadia-code). This is correct -- the upstream repo produces multiple font families from the same sources.

## How the Commit Hash Was Identified

The commit hash `56bcca3f2c1e4cb19458954f0e2bb4635960df91` was explicitly stated in the onboarding commit message (`e64c73014`, author: Aaron Bell, date: 2025-03-18). This is the same commit used for Cascadia Code, which makes sense since both are produced from the same upstream source.

Cross-verification: The upstream commit `56bcca3f` in the microsoft/cascadia-code repo has the message "Update FONTLOG and Build for v2407.24 (#785)", authored by Dustin L. Howett on 2024-11-18. The google/fonts commit message states "Cascadia Mono: version 2407.024", matching precisely.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. An override `config.yaml` was created in the google/fonts family directory (`ofl/cascadiamono/config.yaml`) as part of the sources info enrichment commit `692a7f508` (2025-04-02). The override config is identical to the one used for Cascadia Code:

```yaml
buildVariable: true
sources:
  - sources/CascadiaCode_variable.designspace
  - sources/CascadiaCode_variable_italic.designspace
```

Note that the config references `CascadiaCode_variable.designspace` (not CascadiaMono), because the Mono variant is built from the same source as Code -- the upstream build system filters out ligatures for the Mono variant. Since an override config exists in google/fonts, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-18
- Commit message: "Update FONTLOG and Build for v2407.24 (#785)"
- Source files at commit: `sources/CascadiaCode_variable.designspace`, `sources/CascadiaCode_variable_italic.designspace`
- Override config.yaml in google/fonts: Yes
- Font was added to Google Fonts on 2025-03-18

## Confidence Level

**HIGH** -- The commit hash was directly stated in the onboarding commit message by one of the font's designers. The version number and upstream commit both match. Sharing the same repo and commit with Cascadia Code is expected and correct.

## Open Questions

None. This family is fully documented and verified.
