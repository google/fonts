# Maitree — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/cadsondemak/maitree"
  commit: "e530c1fb68e167a5e990b8125e62231cbedfe4be"
}
```

No `config_yaml` field is set in the source block. An override `config.yaml` exists in the google/fonts family directory, so the field is correctly omitted (google-fonts-sources auto-detects local overrides).

## Repository Analysis

**Repository**: https://github.com/cadsondemak/maitree
**Owner**: Cadson Demak (Thai type foundry)
**Default branch**: master
**Total commits**: ~60+ (across master and gh-pages branches)
**Latest commit**: `8caddd1` (2021-05-03) — "Solve the Ỗ ỗ in Vietnamese."

### Repository Structure (at referenced commit `e530c1f`)

```
fonts/
  Maitree-{200,300,400,500,600,700}.otf
  Maitree-{200,300,400,500,600,700}.ttf
source/
  Maitree-{200,300,400,500,600,700}.glyphs
  Maitree-{200,300,400,500,600,700}.ufo/
  Maitree-{200,300,400,500,600,700}.vfb
BRIEF.md
OFL
OFL.txt
README.md
```

The upstream repository contains:
- 6 separate `.glyphs` source files (one per weight: 200, 300, 400, 500, 600, 700)
- Corresponding `.ufo` and `.vfb` source files for each weight
- Pre-compiled TTF and OTF font files in the `fonts/` directory
- No `config.yaml` file — the upstream repo has no gftools-builder configuration

### Source Type

Static font with 6 individual weights (not a variable font). Each weight has its own separate source file rather than using a multi-master designspace.

## Onboarding History

### PR #998 — "hotfix-maitree: v1.003 added"

- **Author**: Marc Foley (@m4rc1e)
- **Merged**: 2017-05-23
- **Commit**: `5d0ea41cd` in google/fonts
- **PR body**: "This partially resolves https://github.com/google/fonts/issues/271 by adding a family already in the API back to this repo."

The font was added to google/fonts as a "hotfix" — it was already available in the Google Fonts API but had not been added to the git repository. Marc Foley added it as part of resolving issue #271.

### Source Block History

1. **2024-03-04** — Simon Cozens (`658d6674d`, "Update upstreams"): Added the initial `source { repository_url }` block and `primary_script: "Thai"` to METADATA.pb.
2. **2025-11-19** — Felipe Sanches (`d5aef7c0b`, "sources info for Maitree: v1.003 (PR #998)"): Added the `commit` hash to the source block and created the override `config.yaml`.

### Font File Provenance

The TTF files in google/fonts do not match the upstream binaries byte-for-byte. For example, `Maitree-Regular.ttf` is 194,476 bytes in google/fonts but 208,876 bytes at the upstream commit `e530c1f`. This indicates the fonts were recompiled by the onboarder (Marc Foley) from the upstream sources rather than being direct copies of the pre-built fonts.

## Build Configuration

### Override config.yaml (in google/fonts)

An override `config.yaml` exists in the google/fonts family directory with the following content:

```yaml
buildVariable: false
sources:
  - source/Maitree-200.glyphs
  - source/Maitree-300.glyphs
  - source/Maitree-400.glyphs
  - source/Maitree-500.glyphs
  - source/Maitree-600.glyphs
  - source/Maitree-700.glyphs
```

This config correctly references the 6 individual `.glyphs` source files in the upstream repo's `source/` directory. The `buildVariable: false` flag is appropriate since this is a static font family with separate sources per weight.

### Upstream config.yaml

No `config.yaml` exists in the upstream repository. The override in google/fonts provides the necessary build configuration.

## Findings

1. **Source block is complete**: The METADATA.pb source block has both `repository_url` and `commit` hash. The `config_yaml` field is correctly omitted because an override `config.yaml` exists locally.

2. **Commit hash is valid**: The referenced commit `e530c1fb68e167a5e990b8125e62231cbedfe4be` (2016-03-11) exists in the upstream repo and is a merge commit by Dave Crossland. It predates the google/fonts PR merge date (2017-05-23), which is consistent with it being the source used for onboarding.

3. **Later upstream changes exist**: There is one commit after the referenced hash — `8caddd1` (2021-05-03, "Solve the Ỗ ỗ in Vietnamese") — which modified source files and font binaries to fix Vietnamese diacritics. This change has NOT been incorporated into google/fonts and would need separate review if desired.

4. **Override config.yaml is correct**: The override config references the correct source files at the paths they exist in the upstream repo at the referenced commit.

5. **No issues found**: All metadata appears accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/cadsondemak/maitree"
  commit: "e530c1fb68e167a5e990b8125e62231cbedfe4be"
}
```

The `config_yaml` field is intentionally omitted because the override `config.yaml` in the google/fonts family directory is auto-detected by google-fonts-sources.
