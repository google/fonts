# Changa One

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Eduardo Tunni
**METADATA.pb path**: `ofl/changaone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/etunni/changa-one |
| Commit | `e8d7a3159a17875eb09b35b06e78ae706d8affe9` |
| **Config YAML** | Override in google/fonts |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL `https://github.com/etunni/changa-one` was already present in the METADATA.pb `source { repository_url }` field. It was added in commit `c8f729cbd` ("Add more upstreams (c,d)") in google/fonts. The `etunni` GitHub account belongs to Eduardo Tunni, the designer of the font, which matches the METADATA.pb designer field and the copyright string ("Copyright (c) 2011, Eduardo Tunni (http://www.tipo.net.ar edu@tipo.net.ar)").

## How the Commit Hash Was Identified

The commit `e8d7a3159a17875eb09b35b06e78ae706d8affe9` is the **only commit** in the upstream repository (2013-12-30, "Adobe Latin 3 encoding"). This is a single-commit repository, making the hash unambiguous. The commit was added to the METADATA.pb source block in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25).

The font files in google/fonts were last updated in commit `27a1664cc` (2015-04-27, "Updating ofl/changaone/*ttf with nbspace and fsType fixes") by Dave Crossland. The original font was added in the initial commit `90abd17b4`.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory (`ofl/changaone/`).

The upstream repository contains UFO sources that are compatible with gftools-builder:
- `ChangaOne-Regular.otf.ufo/` (Regular weight)
- `ChangaOne_Italic.otf.ufo/` (Italic)

These are `.ufo` format sources which **can** be used with gftools-builder. A `config.yaml` could be created to reference these sources, either as an override in the google/fonts family directory or as a PR to the upstream repository.

A potential `config.yaml` would look like:
```yaml
sources:
  - ChangaOne-Regular.otf.ufo
  - ChangaOne_Italic.otf.ufo
buildVariable: false
```

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2013-12-30 11:00:12 -0300
- Commit message: "Adobe Latin 3 encoding"
- Source files at commit: `ChangaOne-Regular.otf.ufo/`, `ChangaOne_Italic.otf.ufo/`, `ChangaOne-Regular.ttf`, `ChangaOne-Italic.ttf`
- UFO sources present: Yes (gftools-buildable)

## Confidence

**High**: The repository URL and commit hash are straightforward -- the repo has only one commit, and the designer's own GitHub account confirms ownership. The UFO sources are present and could support a gftools-builder configuration, but no config.yaml has been created yet.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - ChangaOne-Regular.otf.ufo
  - ChangaOne_Italic.otf.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. A `config.yaml` needs to be created for this family. The UFO sources are available, so an override config.yaml in google/fonts (`ofl/changaone/config.yaml`) would be the simplest approach without requiring changes to the upstream repo.
2. The UFO files have unconventional naming (`ChangaOne-Regular.otf.ufo` and `ChangaOne_Italic.otf.ufo` -- note the inconsistent separator: hyphen vs underscore). This may require testing to ensure gftools-builder handles them correctly.
3. The upstream repo contains pre-built TTF files alongside the UFO sources. It would be worth verifying that building from the UFO sources produces equivalent output to the existing TTFs.
