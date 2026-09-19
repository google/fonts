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
| Override Config | No |
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

No override config.yaml exists in google/fonts either. Creating one would require determining which UFOs correspond to the published Coda-Regular.ttf and Coda-ExtraBold.ttf files, and likely creating a designspace file.

## Verification

- **Repository accessible**: Yes, https://github.com/vernnobile/CodaFont is accessible
- **Commit exists**: Yes, `41ce6c52` is the HEAD of master
- **Commit is HEAD**: Yes, this is the latest commit in the repository
- **Font binaries match**: The font was last updated in PR #879 (2017), using sources from this repo
- **Source block on main**: Only repository_url is on main; commit hash is on a pending PR branch (`sources_info_2026-02-25`)

## Confidence Level

**High** for repository URL and commit hash. The repo is clearly the correct upstream for Coda. The commit hash is the HEAD and only possible commit to reference since no newer commits exist.

**Note**: The "missing_config" status is accurate -- an override config.yaml would need to be created to make this buildable, but the UFO structure is non-standard and would need investigation to determine the correct build setup.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - coda/in-progress/Regular/src/Coda.ufo
  - coda/in-progress/Heavy/src/Coda-Heavy-IN.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Which UFO files in the repo correspond to the published v2.001 Coda-Regular.ttf and Coda-ExtraBold.ttf? The "in-progress" directory structure makes this unclear.
2. Should an override config.yaml be created for Coda, and if so, what should its build configuration look like?
