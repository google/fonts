# Londrina Solid — Source Investigation

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

An override `config.yaml` exists in the google/fonts family directory (added in commit `cf231062f`, 2025-12-12), so the `config_yaml` field is correctly omitted from METADATA.pb.

## Repository Analysis

**Repository**: https://github.com/marcelommp/Londrina-Typeface
**Owner**: marcelommp (Marcelo Magalhaes)
**Cached at**: `upstream_repos/fontc_crater_cache/marcelommp/Londrina-Typeface`
**Repo status**: Clean, up to date with origin/master

The repository contains the full Londrina typeface family (Solid, Outline, Shadow, Sketch). It is organized as follows:

- `FONTLAB_UFO_FILES/` — UFO source files for all Londrina sub-families, including:
  - `LondrinaSolid-Black.ufo`
  - `LondrinaSolid-Light.ufo`
  - `LondrinaSolid-Regular.ufo`
  - `LondrinaSolid-Thin.ufo`
- `Source Glyphs/` — Glyphs App master file (`Londrina_Masters.glyphs`)
- `Source Glyphs /` (with trailing space) — Individual `.glyphs` files per style (added later by the designer)
- `TTF/` — Pre-compiled TrueType fonts
- `OTF/` — Pre-compiled OpenType fonts
- No `config.yaml` exists in the upstream repository

The UFO files in `FONTLAB_UFO_FILES/` were created by Marc Foley (m4rc1e) during the mastering process for Google Fonts onboarding in July 2017 (upstream PR #2).

## Onboarding History

**Initial addition**: The font was originally added to Google Fonts on 2012-03-14 (per `date_added` in METADATA.pb), appearing in the initial commit (`90abd17b4`). At that time, only LondrinaSolid-Regular.ttf was included.

**v1.002 update (PR #1084)**: On 2017-07-31, PR #1084 ("londrinasolid: v1.002 added") was merged (commit `c581a3f90`). This PR added three new weights (Thin, Light, Black) and updated the Regular weight. The PR body referenced:
- Issue #69: "Add new Lodrina family styles (Thin, Book, Black)" — a request from the designer @marcelommp
- Upstream PR #2 (m4rc1e/gf-mastering branch merged into marcelommp/Londrina-Typeface)

The mastering work was done by Marc Foley (`m4rc1e`) in the upstream repo, with the following key commits:
1. `d2d4469` (2017-07-13) — "Solid family mastered"
2. `2aa19f8` — "fixed vertical metrics"
3. `4e0ee2c` — "ran Fix fonts for GF spec"
4. `deed74a` — "readjusted metrics to visually appear like previous GF release"
5. `f80de6a` — "fixed copyright strings"
6. `0034a81` — "Generated v1.002 fonts"
7. `c51f8ae` — "disable subroutines"
8. `3754d39` — "remove hints"
9. `7f4129ee` — "fixed rfn in copyright strings" (final commit in the mastering branch)

The upstream PR #2 was merged by Marcelo Magalhaes on 2017-07-17 (merge commit `a2b7062`). The next upstream commit after the merge was `6d492b4` on 2018-07-12, well after the google/fonts PR was merged.

**Source block additions**:
- `e75f8240` (2023-12-14, "Update upstreams") — Added the `source { repository_url }` block
- `cf231062f` (2025-12-12, "sources info for Londrina Solid: v1.002 (PR #1084)") — Added `commit` hash and override `config.yaml`

## Build Configuration

**Upstream config.yaml**: None exists in the upstream repository.

**Override config.yaml** (in google/fonts family directory):
```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaSolid-Black.ufo
  - FONTLAB_UFO_FILES/LondrinaSolid-Light.ufo
  - FONTLAB_UFO_FILES/LondrinaSolid-Regular.ufo
  - FONTLAB_UFO_FILES/LondrinaSolid-Thin.ufo
```

This override was added in commit `cf231062f` (2025-12-12). It references the four UFO source files in the `FONTLAB_UFO_FILES/` directory, building four static (non-variable) fonts. The source paths are relative to the upstream repo root at the referenced commit.

## Findings

1. **Commit hash verified**: The commit `7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060` ("fixed rfn in copyright strings", 2017-07-13 by Marc Foley) is the last commit in the mastering branch before the upstream merge. TTF file sizes match exactly between this commit and the google/fonts files:
   - LondrinaSolid-Black.ttf: 93,408 bytes
   - LondrinaSolid-Light.ttf: 85,988 bytes
   - LondrinaSolid-Regular.ttf: 92,132 bytes
   - LondrinaSolid-Thin.ttf: 80,672 bytes

2. **Repository URL verified**: https://github.com/marcelommp/Londrina-Typeface is the correct upstream repository, matching the copyright strings in METADATA.pb and the references in PR #1084.

3. **Override config.yaml is appropriate**: The upstream repo has no `config.yaml`, but does have gftools-builder compatible UFO sources. The override correctly references these sources with `buildVariable: false`.

4. **Multi-family repo**: The upstream repository contains sources for all four Londrina sub-families (Solid, Outline, Shadow, Sketch). Each sub-family in google/fonts should have its own override config.yaml referencing the relevant source files.

5. **Source block is complete**: The current METADATA.pb source block has the correct `repository_url` and `commit` hash. The `config_yaml` field is correctly omitted because an override `config.yaml` exists in the google/fonts family directory.

6. **No further action needed**: All metadata is correct and complete for this family.

## Recommended Source Block

The current source block is correct and complete:

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

With the override `config.yaml` in the google/fonts family directory providing the build configuration. No changes are needed.
