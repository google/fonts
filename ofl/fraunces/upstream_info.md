# Investigation Report: Fraunces

## Family Information
- **Family name**: Fraunces
- **Designer**: Undercase Type, Phaedra Charles, Flavia Zimbardi
- **License**: OFL
- **Category**: Serif
- **Date added**: 2020-10-29
- **Google Fonts path**: `ofl/fraunces/`
- **Minisite**: https://fraunces.undercase.xyz

## Upstream Repository
- **URL**: https://github.com/undercasetype/Fraunces
- **Status**: Active, accessible
- **Default branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/undercasetype/Fraunces`

## Source Files
- **Type**: Designspace + UFO
- **Roman source**: `sources/Roman/Fraunces.designspace` (at onboarding commit)
- **Italic source**: `sources/Italic/FrauncesItalic.designspace` (at onboarding commit; later renamed to `Fraunces-Italic.designspace`)
- **Static designspaces**: `sources/Roman/Fraunces_static.designspace`, `sources/Italic/FrauncesItalic_static.designspace`
- **UFO masters**: 8 per style (Roman/Italic), covering 4 axis combinations (9pt/144pt x S000/S100 x Thin/Black)
- **Custom axes**: SOFT (Softness, 0-100), WONK (Wonky, 0-1), opsz (Optical Size, 9-144), wght (Weight, 100-900)

## Font Files in google/fonts
- `Fraunces[SOFT,WONK,opsz,wght].ttf` (360,440 bytes)
- `Fraunces-Italic[SOFT,WONK,opsz,wght].ttf` (414,904 bytes)

## Onboarding History

### Initial addition: PR #2570 (Jul 27, 2020)
- **Title**: "Fraunces 1.000"
- **Author**: Yanone (yanone)
- **Merged by**: Marc Foley (m4rc1e)
- **PR body**: References upstream PR undercasetype/Fraunces#210 ("Fraunces ready for Google Fonts")
- **Note**: Upstream PR #210 head commit `8ec7ad363` was dated Jul 23, 2020, but that PR was not merged to undercasetype/Fraunces until Aug 14, 2020. So the fonts in google/fonts PR #2570 were taken from Yanone's fork before the upstream merge.
- **Binary files**: `Fraunces[SOFT,WONK,opsz,wght].ttf` (373,268 bytes) and `Fraunces-Italic[SOFT,WONK,opsz,wght].ttf` (408,448 bytes)
- **Commit in google/fonts**: `581699fcc`

### Update: PR #2776 (Dec 9, 2020) -- CURRENT BINARIES
- **Title**: "fraunces: v1.000 added."
- **Author**: Stephen Nixon (arrowtype)
- **Merged by**: Marc Foley (m4rc1e)
- **PR body**: "Taking over for PR #2755, using a shell script to update rather than the gftools packager." References mastering work at https://github.com/arrowtype/Fraunces/issues/1
- **Predecessor**: PR #2755 (closed, not merged) -- same content but submitted earlier by arrowtype
- **Binary files**: `Fraunces[SOFT,WONK,opsz,wght].ttf` (360,440 bytes) and `Fraunces-Italic[SOFT,WONK,opsz,wght].ttf` (414,904 bytes)
- **Commit in google/fonts**: `ac502d8ef`

### Source block addition (Jan 14, 2024)
- Commit `c8a4f8556` by Simon Cozens added the `source { repository_url }` block to METADATA.pb (as part of "More upstreams (e,f)" batch).

## Commit Hash Identification

### Verification of onboarding commit
The current binary files in google/fonts match the pre-built fonts at upstream commit **`d6d385783`** (Oct 29, 2020, "Merge pull request #257 from arrowtype/mastering"):

| File | google/fonts size | Upstream `d6d385783` size | Match |
|------|------------------|--------------------------|-------|
| `Fraunces[SOFT,WONK,opsz,wght].ttf` | 360,440 | 360,440 | YES |
| `Fraunces-Italic[SOFT,WONK,opsz,wght].ttf` | 414,904 | 414,904 | YES |

The fonts in the upstream repo at `d6d385783` were located at `fonts/Fraunces[SOFT,WONK,opsz,wght].ttf` and `fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf`. This is also confirmed by the `upstream.yaml` file in `mastering/googlefonts/upstream.yaml` which maps `fonts/Fraunces[SOFT,WONK,opsz,wght].ttf` to the google/fonts path.

The upstream PR #257 by arrowtype (merged Oct 29, 2020) was the last commit to touch the `fonts/` directory before the google/fonts PR #2776 was merged on Dec 9, 2020. Between `d6d385783` and the google/fonts merge, no additional upstream commits modified font binaries.

**Recommended commit hash**: `d6d385783609ceb11ac0f220f3abd9f1631c8a36` (short: `d6d385783`)
**Confidence**: HIGH

## Build Configuration

### At onboarding commit (`d6d385783`)
- **No config.yaml or build.yaml** at repo root
- Build was performed by Stephen Nixon (arrowtype) using custom shell scripts in `mastering/` directory
- An `upstream.yaml` (gftools-packager format) existed at `mastering/googlefonts/upstream.yaml` for file mapping

### At current HEAD (`7ccdec31c`, Oct 21, 2025)
- **`build.yaml`** exists (not `config.yaml`)
- Uses gftools-builder recipe format with `recipeProvider: googlefonts` and custom `recipe:` block
- Contains advanced build steps including `--filter ... --filter FlattenComponentsFilter --filter DecomposeTransformedComponentsFilter` and `gftools fix-nonhinting` exec operations
- Sources: `sources/Roman/Fraunces.designspace` and `sources/Italic/Fraunces-Italic.designspace`

### Need for override config.yaml
Since there was no config.yaml at the onboarding commit, an override config.yaml is needed in the google/fonts family directory. The sources at the onboarding commit use `.designspace` files suitable for gftools-builder.

## Post-Onboarding Upstream Activity
There has been significant upstream work since the onboarding commit (29 commits between `d6d385783` and HEAD `7ccdec31c`), including:
- Renamed designspace files (e.g., `FrauncesItalic.designspace` -> `Fraunces-Italic.designspace`)
- Added Unicode support, `locl` feature, case feature for accents
- STAT table improvements (moved to designspace labels)
- Modernized build system (added `build.yaml` at HEAD, PR #275)
- A `gf-fix` PR #274 by m4rc1e was merged then reverted (PR #281)
- All this post-onboarding work would need separate review before incorporation into Google Fonts

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/undercasetype/Fraunces"
}
```
Missing: `commit`, `config_yaml`

## Recommended METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/undercasetype/Fraunces"
  commit: "d6d385783609ceb11ac0f220f3abd9f1631c8a36"
}
```
Note: `config_yaml` should be omitted because the override config.yaml will be placed directly in the google/fonts family directory and auto-detected by google-fonts-sources.

## Recommended Override config.yaml
An override `config.yaml` should be created in `ofl/fraunces/` in the google/fonts repository, referencing the designspace sources at the onboarding commit:

```yaml
sources:
  - sources/Roman/Fraunces.designspace
  - sources/Italic/FrauncesItalic.designspace
```

Note: At the onboarding commit `d6d385783`, the Italic designspace was named `FrauncesItalic.designspace` (not `Fraunces-Italic.designspace` as at HEAD). The Roman designspace was `Fraunces.designspace`.

## Summary
- **Status**: missing_config (needs commit hash and override config.yaml added)
- **Repository URL**: https://github.com/undercasetype/Fraunces (correct, verified)
- **Commit**: `d6d385783609ceb11ac0f220f3abd9f1631c8a36` (verified by binary file size match)
- **Config**: Override config.yaml needed in google/fonts (no config at onboarding commit)
- **Confidence**: HIGH
- **Key people**: Stephen Nixon (arrowtype) did the mastering/v1.0 work; Yanone did the initial onboarding; Marc Foley merged both PRs
