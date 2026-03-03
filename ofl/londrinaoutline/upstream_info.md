# Londrina Outline — Source Investigation

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

The source block was added in two stages:
1. Simon Cozens added the `repository_url` in the "Update upstreams" commit (e75f824, 2023-12-14).
2. Felipe Sanches added the `commit` hash and an override `config.yaml` in commit 7d0f8f9 (2025-12-12), titled "sources info for Londrina Outline: v1.002 (PR #1087)".

No `config_yaml` field is set in METADATA.pb, which is correct because an override `config.yaml` exists in the google/fonts family directory.

## Repository Analysis

**Upstream repo**: https://github.com/marcelommp/Londrina-Typeface
**Repo type**: Multi-family repository (contains sources for Londrina Outline, Shadow, Sketch, and Solid)
**Cached at**: `upstream_repos/fontc_crater_cache/marcelommp/Londrina-Typeface/`
**Repo status**: Clean, up to date with origin/master.

### Structure at referenced commit (7f4129e)

At commit `7f4129e`, the repo contained:
- `FONTLAB_UFO_FILES/` — UFO source files for all Londrina families, including `LondrinaOutline-Regular.ufo`
- `FONTLAB_UFO_FILES/vfb/` — FontLab VFB source files
- `TTF/` — Pre-compiled TrueType fonts
- `OTF/` — Pre-compiled OpenType fonts
- `LICENSE` (OFL)
- `README.md`
- `.gitignore`

No `config.yaml` existed in the upstream repo at this commit or any subsequent commit.

### Later commits (post-onboarding)

The upstream repo received additional commits after the onboarding:
- `f7aed96` (2019-04-02): Added `.glyphs` source files in a "Source Glyphs " directory (note trailing space)
- `239d89c` (2022-10-21): Added a new `Londrina_Masters.glyphs` file in "Source Glyphs/" directory
- `cc7b65f` (2023-06-15): "Update of Londrina Family" — various cleanup

These later commits represent new work by the designer that has not been incorporated into Google Fonts.

## Onboarding History

### Initial addition (2015)

Londrina Outline was part of the initial commit (`90abd17`, 2015-03-07) when the google/fonts repository was created.

### v1.002 update (2017)

The font was updated to v1.002 through the work of Marc Foley (m4rc1e):

1. **Upstream PR #2** (m4rc1e/gf-mastering branch): Marc Foley mastered the entire Londrina family for Google Fonts compliance. The branch contained 12 commits covering:
   - Renaming source filenames
   - Mastering Outline and Solid families
   - Fixing vertical metrics
   - Running GF spec fixes
   - Readjusting metrics
   - Fixing copyright strings
   - Disabling subroutines and removing hints
   - Fixing RFN in copyright strings (final commit: `7f4129e`)

2. The upstream PR was merged on 2017-07-17 (commit `a2b7062`).

3. **google/fonts PR #904** (2017-05-08): Initial hotfix — updated the TTF binary and METADATA.pb.

4. **google/fonts PR #1087** (2017-07-31): Final v1.002 update by Marc Foley. This commit (`c04d61c0e`) updated the TTF binary to 167,112 bytes, along with FONTLOG.txt, METADATA.pb, and OFL.txt.

### Binary verification

The TTF binary in google/fonts (`LondrinaOutline-Regular.ttf`, 167,112 bytes) was verified to be byte-identical to the file at `TTF/LondrinaOutline-Regular.ttf` in the upstream repo at commit `7f4129e`:
- SHA-256: `773c655bc6a2e9b699cfa8c4a5f615c6348686d018281bb8e6cdc470b2f05f4d`

This confirms `7f4129e` is the correct onboarding commit.

## Build Configuration

**Upstream config.yaml**: None. The upstream repo has never had a `config.yaml` file.

**Override config.yaml**: Present in the google/fonts family directory (`ofl/londrinaoutline/config.yaml`), added in commit 7d0f8f9 (2025-12-12):

```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaOutline-Regular.ufo
```

This is correct. The source path points to the UFO file that existed at commit `7f4129e` in the upstream repo. Since this is a single-weight static font (Regular 400 only), `buildVariable: false` is appropriate.

## Findings

1. **Source block is complete and correct.** The repository URL, commit hash, and override config.yaml are all properly set.
2. **Commit hash verified.** Binary comparison confirmed the TTF in google/fonts is byte-identical to the one at the referenced commit.
3. **Override config.yaml is appropriate.** The upstream repo has no config.yaml; the override correctly references the UFO source path.
4. **No `config_yaml` in METADATA.pb is correct.** google-fonts-sources auto-detects the local override.
5. **Multi-family repo.** The Londrina-Typeface repo contains sources for four families (Outline, Shadow, Sketch, Solid). Each family in google/fonts needs its own source block pointing to this same repo.
6. **Designer activity post-onboarding.** The designer (Marcelo Magalhaes) added `.glyphs` source files in 2019 and 2022-2023, suggesting potential future updates that would need separate QA review.

## Recommended Source Block

The current source block is correct. No changes needed:

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

The override `config.yaml` in the google/fonts family directory should remain as-is:

```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaOutline-Regular.ufo
```
