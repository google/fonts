# BenchNine - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | BenchNine |
| Repository URL | https://github.com/librefonts/benchnine |
| Commit Hash | 0b2979e19186f9b477fd3bde7ae77932933707eb |
| Config YAML | (none) |
| **Status** | complete |
| Category | SANS_SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/benchnine` comes from the librefonts organization on GitHub, which was created by Marc Foley to host decompiled TTX versions of fonts in the Google Fonts catalog. The URL was recorded in the tracking data and added to METADATA.pb in commit `9a14639f3` (on branch `sources_info_2026-02-25`, not yet merged to main).

## How the Commit Hash Was Determined

The commit hash `0b2979e19186f9b477fd3bde7ae77932933707eb` is the latest (HEAD) commit in the librefonts/benchnine repo, dated 2014-10-17. This was set because the librefonts repo only contains TTX-decomposed font files and Travis CI configuration, and this is the last commit in the repo.

**Context**: The font was originally added to google/fonts in the initial commit `90abd17b4` and last updated via hotfix PR #853 ("hotfix-benchnine: v0.921 added") by Marc Foley on 2017-05-08. The librefonts repo predates this hotfix (last commit 2014-10-17), so the TTX sources in the repo may not match the current TTFs in google/fonts.

## Config YAML Status

- **No `config.yaml`** exists in the upstream librefonts repo (not at the recorded commit, not at any commit)
- **No override `config.yaml`** in `google/fonts/ofl/benchnine/`
- The repo contains UFO sources (`src/BenchNine-Bold.ufo`, `src/BenchNine-Light.ufo`, `src/BenchNine-Regular.ufo`) alongside SFD and TTX files, but no gftools-builder configuration
- The repo also has SFD sources (`src/BenchNine-*-TTF.sfd`, `src/BenchNine-*.sfd`)

## Verification

- Commit hash `0b2979e` exists in the repo (message: "update .travis.yml", dated 2014-10-17)
- It is the HEAD commit of the master branch
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/benchnine`
- PR #853 body was empty, providing no additional context about the hotfix source

## Confidence Level

**Medium** - The commit hash is simply HEAD of the librefonts mirror repo. The librefonts repo is a secondary mirror (decompiled TTX + original sources), not the original design source. The original font was designed by Vernon Adams. The hotfix by Marc Foley in 2017 may have used a different build process than what's captured in this repo. The connection between the librefonts repo and the actual hotfix TTFs is not directly documented.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - src/BenchNine-Light.ufo
  - src/BenchNine-Regular.ufo
  - src/BenchNine-Bold.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

- The librefonts repo was last updated in 2014, but the hotfix was applied in 2017 -- the hotfix TTFs may have been built from different sources or a different process
- Vernon Adams (the original designer) passed away in 2014; the font has not had active upstream development since
- The repo has UFO sources which could theoretically be used with gftools-builder, but it's unclear if they match the current TTFs in google/fonts
- An override `config.yaml` would be needed for gftools-builder compatibility, but verifying that the UFOs produce matching output would be important first
