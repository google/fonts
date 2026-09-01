# Londrina Shadow — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

The source block contains a repository URL and commit hash. No `config_yaml` field is set, which is correct because an override `config.yaml` exists in the google/fonts family directory.

## Repository Analysis

**Repository**: https://github.com/marcelommp/Londrina-Typeface
**Cached at**: `upstream_repos/fontc_crater_cache/marcelommp/Londrina-Typeface`
**Default branch**: master
**Repository status**: Clean, up to date with origin

The repository hosts the entire Londrina typeface family (Outline, Shadow, Sketch, and Solid variants). It was created by designer Marcelo Magalhaes (marcelommp).

### Structure at referenced commit (7f4129e)

The repo contained UFO sources in `FONTLAB_UFO_FILES/` and pre-compiled binaries in `TTF/` and `OTF/` directories:

- `FONTLAB_UFO_FILES/LondrinaShadow-Regular.ufo` — UFO source for the Shadow variant
- `FONTLAB_UFO_FILES/LondrinaOutline-Regular.ufo` — Outline variant source
- `FONTLAB_UFO_FILES/LondrinaSketch-Regular.ufo` — Sketch variant source
- `FONTLAB_UFO_FILES/LondrinaSolid-*.ufo` — Solid variant sources (Black, Light, Regular, Thin)
- `TTF/LondrinaShadow-Regular.ttf` — Pre-compiled binary
- No `config.yaml` existed at this commit or at any point in the repo's history

### Later activity

After the referenced commit, the designer continued making updates to the repository:
- 2018-07: Font adjustments (commit 6d492b4)
- 2019-04: Added Glyphs source files (commit f7aed96)
- 2022-10: New Glyphs App file and uploads (commits 239d89c, 80630a7, 6988bc4)
- 2023-06: Major update of Londrina Family (commit cc7b65f)

These later changes have NOT been incorporated into Google Fonts.

## Onboarding History

### Initial addition

The font was initially added to Google Fonts on 2015-03-07 (commit 90abd17b — "Initial commit"), with `date_added: "2012-03-14"` in METADATA.pb suggesting an earlier catalog presence.

### v1.002 update (PR #1086)

The most recent binary update was through **PR #1086** ("londrinashadow: v1.002 added"), authored by Marc Foley (m4rc1e) and merged on 2017-07-31. The PR body stated:

> Adds extra fonts request in #69
> Upstream has been merged, marcelommp/Londrina-Typeface#2 (comment)

This referred to upstream PR #2 (m4rc1e/gf-mastering branch), which was a batch of mastering work performed by Marc Foley on 2017-07-13 and merged by the designer on 2017-07-17.

### Source block history

1. **2023-12-14** (commit e75f824): Simon Cozens added the `repository_url` field in a batch "Update upstreams" commit
2. **2025-12-12** (commit 9456570): Felipe Sanches added the `commit` hash and override `config.yaml`

## Build Configuration

**No `config.yaml` exists in the upstream repository** at any commit.

An **override `config.yaml`** was added to the google/fonts family directory on 2025-12-12 (commit 9456570) with the following content:

```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaShadow-Regular.ufo
```

This correctly references the UFO source path at the documented commit hash. The `config_yaml` field is intentionally omitted from METADATA.pb because google-fonts-sources auto-detects local overrides.

## Findings

1. **Binary verification**: The TTF file at commit `7f4129e` in the upstream repo (`TTF/LondrinaShadow-Regular.ttf`) has an identical MD5 hash (`cc3afb5fa33f63f15866136819031465`) to the file in google/fonts. This confirms the commit hash is correct.

2. **Commit hash is accurate**: The referenced commit `7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060` ("fixed rfn in copyright strings", 2017-07-13) was the last commit in Marc Foley's mastering branch before it was merged upstream via PR #2 on 2017-07-17. The google/fonts PR #1086 was merged on 2017-07-31, and the binary matches exactly.

3. **Source block is complete**: The repository URL, commit hash, and override config.yaml are all correctly set. No corrections are needed.

4. **Upstream has diverged significantly**: The designer made substantial updates in 2022-2023 (new Glyphs source files, family update), but these have not been onboarded to Google Fonts yet.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

The override `config.yaml` in the google/fonts family directory is correctly configured and does not require a `config_yaml` field in METADATA.pb.
