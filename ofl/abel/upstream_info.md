# Abel

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: MADType
**METADATA.pb path**: `ofl/abel/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/abel |
| Commit | `adf2c7e74ecde8ca41959c0d974f039789fe7b9d` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The METADATA.pb file has no `source { }` block at all -- it only contains basic font metadata (name, designer, license, category, date_added, fonts, subsets). The repository URL `https://github.com/librefonts/abel` was discovered through prior research and is tracked in `gfonts_library_sources.json`. The `librefonts` GitHub organization hosts many legacy Google Fonts source repositories. The upstream repo cache at `upstream_repos/fontc_crater_cache/librefonts/abel` confirms the remote URL is `https://github.com/librefonts/abel`.

## How the Commit Hash Was Identified

The upstream repository contains only a single commit: `adf2c7e74ecde8ca41959c0d974f039789fe7b9d` (2014-10-17, message: "update .travis.yml"). This is the HEAD and only commit in the repository, so it is the only possible reference point.

The last font-modifying commit in google/fonts is `3b99d83d2625` (2020-06-17, "abel: four was overkerned to period and comma (#2352)", PR #2352). This PR was submitted by @laerm0 and fixed kerning between the numeral four and period/comma characters. Before that, commit `d3e16741d` (2017-05-01, "hotfix-abel: v1.003 added (#741)", PR #741 by @m4rc1e) added version 1.003. The font was originally added with the initial google/fonts commit `90abd17b4`.

Since Abel was added to Google Fonts in 2011 (date_added: "2011-08-03") and the upstream repo's only commit is from 2014, the font binary in google/fonts was not necessarily built from this repo using gftools-builder. The font edits (v1.003 hotfix and kerning fix) were done directly in google/fonts, not through the upstream repo.

## How Config YAML Was Resolved

No config.yaml exists anywhere:

1. **Upstream repo**: Contains no config.yaml. The source files are `.sfd` (FontForge SplineFont Database) and `.vfb` (FontLab) format files: `src/Abel-Regular-TTF.sfd`, `src/Abel-Regular-TTF.vfb`, `src/Abel-Regular.vfb`. These are legacy font editor formats that are not compatible with gftools-builder, which expects `.glyphs`, `.ufo`, or `.designspace` sources.
2. **google/fonts override**: No `config.yaml` file exists in `ofl/abel/` in the google/fonts repository.

The font was likely compiled from the `.sfd` or `.vfb` sources using FontForge or FontLab directly, not through the gftools-builder pipeline.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:32 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Abel-Regular-TTF.sfd`, `src/Abel-Regular-TTF.vfb`, `src/Abel-Regular.vfb` (plus TTX decomposition files for the compiled font)

## Confidence

**Medium**: The repository URL is established and the repo is accessible with the correct remote. The commit hash is the only commit in the repo, so it is unambiguous. However, the font was clearly not built using gftools-builder (no compatible source formats, no config.yaml), and the font binary in google/fonts has been modified directly (kerning fix in 2020, version hotfix in 2017) without going through the upstream repo. The `missing_config` status is correct and expected given the legacy source format.

## Open Questions

1. Can the .sfd sources in the upstream repo be used to reproduce the current font binary in google/fonts? The font was modified directly in google/fonts after onboarding (kerning fix PR #2352, version hotfix PR #741), so the upstream sources likely do not match the current binary.
2. Should an override config.yaml be created for this family? Given that the sources are in .sfd format (not supported by gftools-builder), this would require conversion to .glyphs or .ufo format first.
3. The copyright field lists "Matthew Desmond (http://www.madtype.com)" -- the designer credit says "MADType" which is Matthew Desmond's studio. The HTTP URL in the copyright may or may not still be valid.
