# Investigation: Elsie Swash Caps

- **Date investigated**: 2026-02-27
- **Status**: missing_config (SFD/VFB-only sources, no gftools-builder compatible files)
- **Designer**: Alejandro Inler
- **METADATA.pb path**: `ofl/elsieswashcaps/METADATA.pb`

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/librefonts/elsieswashcaps |
| commit_hash      | f48faa350a1a9641bd984b6945f791914a652c65 |
| config_yaml      | none (SFD/VFB-only sources) |

## How URL Was Found

The METADATA.pb file for Elsie Swash Caps currently has no `source {}` block at all. The upstream repo URL was identified by checking the fontc_crater_cache at `upstream_repos/fontc_crater_cache/librefonts/elsieswashcaps/`, which has its git remote set to `https://github.com/librefonts/elsieswashcaps`. The repo was confirmed accessible (HTTP 200) on GitHub.

Note: A previously-used URL `https://github.com/googlefonts/elsiefont` (which was associated with the sibling family "Elsie") returns 404 and was removed from the Elsie METADATA.pb in a prior fix (commit `3fabc27ef`). No `googlefonts/elsieswashcaps` repo exists either (404).

## How Commit Hash Was Identified

The `librefonts/elsieswashcaps` repository has only a single commit:

- `f48faa3` (2014-10-17) by hash3g: "update .travis.yml"

This is the only commit and therefore the only possible reference point. However, this commit is from 2014, well before the current fonts in google/fonts were produced. The fonts have been updated multiple times since:

1. **PR #885** (2017-05-08): Marc Foley updated to v1.002 as a hotfix
2. **PR #7522** (2024-04-08): Yanone fixed fi/fj ligature rendering and bumped to v1.003

Both of these updates were binary hotfixes made directly in google/fonts. In PR #7522, Yanone explicitly stated: *"We don't have sources"* and *"I literally fixed only the requirements (outlines of the fi and fj ligature)"*. The current v1.003 fonts do NOT correspond to any commit in the upstream repository.

## How Config YAML Was Resolved

No config.yaml exists in the `librefonts/elsieswashcaps` repository. The repo uses an old Travis CI build pipeline (`fontbakery-build.py`) from 2014, which is not compatible with modern gftools-builder.

The source files in the repo are:
- **SFD** (FontForge): `src/ElsieSwashCaps-Regular-TTF.sfd`, `src/ElsieSwashCaps-Black-TTF.sfd` (plus backup copies)
- **VFB** (FontLab): `src/ElsieSwashCaps-Regular-OTF.vfb`, `src/ElsieSwashCaps-Black-OTF.vfb` (plus .vfbak backups)
- **TTX** (decompiled font tables): Numerous `.ttx` files for both Regular and Black weights

None of these formats (.sfd, .vfb) are compatible with gftools-builder, which requires .glyphs, .ufo, or .designspace sources. Creating an override config.yaml is not possible without compatible source files.

## Verification

- **Repository accessible**: Confirmed (HTTP 200)
- **Fonts match upstream**: NO. The current fonts in google/fonts are v1.003 (binary-hotfixed by Yanone in April 2024). The upstream repo has only one commit from 2014 and contains older-generation sources.
- **Sources usable**: NO. The SFD/VFB sources are not compatible with gftools-builder. Yanone confirmed in PR #7522 that sources are effectively lost.
- **config.yaml**: None exists and none can be created (no compatible sources)

## Confidence

**MEDIUM** -- The repository URL is correct (librefonts/elsieswashcaps is the historical upstream for this family), but the repo is essentially archived/stale. The current fonts in Google Fonts are the result of binary hotfixes and no longer correspond to any upstream source. The commit hash `f48faa3` is the only commit in the repo and represents the original source deposit, but it predates the current binaries significantly.

## Notes

- Elsie Swash Caps is a sibling family to "Elsie" (non-swash-caps), both by Alejandro Inler. They share a similar situation: lost sources.
- The `googlefonts/elsiefont` repo (previously referenced for "Elsie") is a 404 and was never associated with the Swash Caps variant.
- The librefonts org created separate repos for `elsie` and `elsieswashcaps` in July 2014, each with only one commit (Travis CI config update by hash3g in October 2014).
- Future source recovery would require contacting Alejandro Inler (alejandroinler@gmail.com) to obtain original editable sources in a modern format.
- The font was originally added to Google Fonts on 2012-11-12.
