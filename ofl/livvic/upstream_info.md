# Livvic — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/Fonthausen/Livvic"
  commit: "30f612bf37946b0462c91ba2b4323e955a519463"
}
```

The source block contains a `repository_url` and `commit` hash. There is no `config_yaml` field, which is correct because an override `config.yaml` exists in the google/fonts family directory (auto-detected by google-fonts-sources).

## Repository Analysis

**Repository**: https://github.com/Fonthausen/Livvic
**Owner**: Fonthausen (Jacques Le Bailly)
**Default branch**: master
**Status**: Clean, up to date with origin

### Repository Structure

```
.gitignore
OFL.txt
README.md
requirements.txt
fonts/
  Livvic_v1.000.zip
  otf/    (16 OTF files)
  ttf/    (16 TTF files)
sources/
  build.sh
  LV_Livvic.glyphs
  LV_Livvic_Italic.glyphs
```

### Contributors

- **Marc Foley** (m4rc1e) — 6 commits, handled mastering and onboarding
- **Jacques Le Bailly** (Fonthausen) — 3 commits, original designer

### Tags

- `v1.000` — tagged release

### Source Files

The repository contained two Glyphs source files:
- `sources/LV_Livvic.glyphs` — upright masters
- `sources/LV_Livvic_Italic.glyphs` — italic masters

A `build.sh` script existed in `sources/` using fontmake to generate static TTF and OTF instances. No `config.yaml` was present in the upstream repository.

## Onboarding History

### v1.000 — Initial onboarding (2019-06-27)

- **google/fonts commit**: `cabd9770b` by Marc Foley
- **PR**: #2049, merged 2019-07-08
- **Upstream commit**: `885959cd198c1f825d110c125f73c70ca3a14244` ("Merge pull request #1 from m4rc1e/gf-mastering")
- **PR body**: "Taken from the upstream repo https://github.com/Fonthausen/Livvic at commit https://github.com/Fonthausen/Livvic/commit/885959cd198c1f825d110c125f73c70ca3a14244"
- **Files**: 16 TTF files, DESCRIPTION, METADATA.pb, OFL.txt

### v1.001 — Ligature fix update (2019-09-02)

- **google/fonts commit**: `f290a5845` by Marc Foley
- **PR**: #2150, merged 2019-09-02
- **Upstream commit**: `30f612bf37946b0462c91ba2b4323e955a519463` ("Merge pull request #5 from Fonthausen/lig-fix — fix ffi and ffj ligs")
- **PR body**: "Taken from the upstream repo https://github.com/Fonthausen/Livvic at commit https://github.com/Fonthausen/Livvic/commit/30f612bf37946b0462c91ba2b4323e955a519463"
- **Files**: 16 TTF files updated (ligature fixes)
- **Timeline**: Upstream commit at 15:46 UTC+1, google/fonts commit at 16:24 UTC+1, PR merged at 17:13 UTC+1 — all on the same day

### Source block additions

1. **2023-12-14**: Simon Cozens added the `source { repository_url }` block in commit `e75f8240` ("Update upstreams")
2. **2025-11-12**: Felipe Sanches added the `commit` hash and override `config.yaml` in commit `89367de39` ("sources info for Livvic: v1.001 (PR #2150)")

## Build Configuration

**Upstream config.yaml**: Not present in the upstream repository.

**Override config.yaml in google/fonts**: Present, created in commit `89367de39` (2025-11-12).

```yaml
buildVariable: false
sources:
  - sources/LV_Livvic.glyphs
  - sources/LV_Livvic_Italic.glyphs
```

The override config references the two Glyphs source files relative to the upstream repo root. The `buildVariable: false` flag indicates static instance generation only, which matched the original `build.sh` behavior.

## Findings

1. **Commit hash is verified and correct**: The commit `30f612bf37946b0462c91ba2b4323e955a519463` in METADATA.pb matched the one explicitly referenced in PR #2150's commit message and body. It was the latest commit in the upstream repo at the time of onboarding, and remained the latest commit (no subsequent upstream activity).

2. **Binary file sizes match exactly**: All 16 TTF files in `google/fonts ofl/livvic/` had identical sizes to the files in the upstream repo's `fonts/ttf/` directory at commit `30f612b`, confirming the fonts were taken directly from the pre-built binaries in the upstream repo.

3. **Override config.yaml is appropriate**: Since the upstream repo had no `config.yaml` (only a `build.sh` script using fontmake), the override config in google/fonts was the correct approach. The source file paths in the config matched the actual files in the upstream repo.

4. **No `config_yaml` field needed in METADATA.pb**: The override `config.yaml` in the google/fonts family directory was auto-detected by google-fonts-sources, so omitting the `config_yaml` field from the source block was correct.

5. **Source block is complete**: The current source block had both `repository_url` and `commit` hash, and the override `config.yaml` existed locally. No corrections were needed.

6. **Upstream repo is dormant**: The last upstream commit was from 2019-09-02. No subsequent changes were made after the v1.001 onboarding.

## Recommended Source Block

The current source block is correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/Fonthausen/Livvic"
  commit: "30f612bf37946b0462c91ba2b4323e955a519463"
}
```

With the override `config.yaml` in the google/fonts family directory:

```yaml
buildVariable: false
sources:
  - sources/LV_Livvic.glyphs
  - sources/LV_Livvic_Italic.glyphs
```

**Confidence**: HIGH — Both the commit hash and repository URL were explicitly documented in the original PR commit messages by the onboarder (Marc Foley). Binary file sizes matched exactly. The upstream repo had no subsequent activity.
