# Coda - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Coda |
| Designer | Vernon Adams |
| Repository URL | https://github.com/vernnobile/CodaFont |
| Commit Hash | 41ce6c5246c919290b49dc97cc233815428636f2 |
| Branch | master (default) |
| **Config YAML** | Override in google/fonts |
| Override Config | Yes |
| **Status** | complete |

## How URL Was Found

The repository URL `https://github.com/vernnobile/CodaFont` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on January 14, 2024. Vernon Adams (vernnobile) is the designer listed in the METADATA.pb and the owner of this GitHub repository.

## How Commit Was Determined

The commit hash `41ce6c5246c919290b49dc97cc233815428636f2` is the HEAD (latest and final) commit on the master branch of the CodaFont repository. The entire commit history spans from September 2012 to January 2014, with only 13 commits total. Since the upstream repo has been inactive since 2014 and the font was last updated in google/fonts via PR #879 ("hotfix-coda: v2.001 added") by Marc Foley on May 8, 2017, using the HEAD commit is the correct approach -- it was the only available state of the repo when the font was onboarded.

The commit itself (message: "as") only adds .DS_Store files, which is typical of Vernon Adams' casual commit style visible throughout the repo.

## Config YAML Status

**No config.yaml exists** in the upstream repository. The repo contains scattered UFO files in various subdirectories:
- `coda/in-progress/Heavy/src/Coda-Heavy-IN.ufo`
- `coda/in-progress/Regular/src/Coda.ufo`
- `coda/1.0/Heavy/src/Coda-Heavy.ufo`
- `coda/1.0/Regular/src/Coda.ufo`

These are individual UFO masters with no designspace file or build configuration. The directory structure suggests work-in-progress state. The repo also contains CodaCaption sources.

The override config.yaml in google/fonts names the two `coda/1.0` UFOs, which the published Coda-Regular.ttf and Coda-ExtraBold.ttf correspond to (see the last section).

## Verification

- **Repository accessible**: Yes, https://github.com/vernnobile/CodaFont is accessible
- **Commit exists**: Yes, `41ce6c52` is the HEAD of master
- **Commit is HEAD**: Yes, this is the latest commit in the repository
- **Font binaries match**: The font was last updated in PR #879 (2017), using sources from this repo
- **Source block on main**: repository_url and commit

## Confidence Level

**High** for repository URL and commit hash. The repo is clearly the correct upstream for Coda. The commit hash is the HEAD and only possible commit to reference since no newer commits exist.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - coda/1.0/Regular/src/Coda.ufo
  - coda/1.0/Heavy/src/Coda-Heavy.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Override config corrected (2026-11-13)

**Model**: Claude Opus 5.5

The override named the `coda/in-progress` UFOs, unreleased v3 work that encodes U+021A twice. The shipped v2.001 matches the 2012 binaries in `coda/1.0`, which sit next to their sources, so the override now names `coda/1.0/Regular/src/Coda.ufo` and `coda/1.0/Heavy/src/Coda-Heavy.ufo`.

With gftools 0.10.8 and fontmake 3.12.2, Regular matches the shipped cmap, and every glyph's bounds and advance are within 1 unit. Heavy still fails: its `lib.plist` and glyph libs are malformed. With those repaired in a scratch copy, it matches the shipped ExtraBold exactly.

### Note on Coda.ufo (2026-11-14)

**Model**: Claude Fable 5.2

On a case-sensitive filesystem (Linux, so also fontc_crater's CI) `coda/1.0/Regular/src/Coda.ufo` does not load: `glyphs/contents.plist` names 147 of its 393 files with capitals (`A_.glif`), but the repository has them in lower case (`a_.glif`). fontmake stops with "The file 'A_.glif' associated with glyph 'A' in contents.plist does not exist". The Regular result above holds on a case-insensitive filesystem; in a scratch copy with the 147 files renamed, the build has the shipped cmap and all 392 paired glyphs are within 1 unit in bounds and advance. So on Linux both sources of this override fail today.

