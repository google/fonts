# Cabin Sketch - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cabin Sketch |
| Designer | Impallari Type |
| License | OFL |
| Date Added | 2011-03-16 |
| Repository URL | https://github.com/impallari/CabinSketch |
| Commit Hash | f74674fd7ba37fdfcdad88b58d8d3983a320a68d |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Was Found

The repository URL `https://github.com/impallari/CabinSketch` was added to the METADATA.pb source block by Simon Cozens in commit `c8f729cbd` (2024-01-14) as part of a batch "Add more upstreams (c,d)" operation. The URL matches the impallari GitHub account, which belongs to Pablo Impallari, the designer behind Impallari Type.

## How Commit Was Determined

The commit hash `f74674fd7ba37fdfcdad88b58d8d3983a320a68d` is the HEAD of the upstream repository's master branch. This commit was made on 2016-11-10 with the message "FONTLOG: updated". It is the latest commit in the repository and corresponds to the v1.100 release that was onboarded via PR #459 by Marc Foley in December 2016.

The timeline is consistent:
- Upstream commit `f74674f` was made on 2016-11-10 (updating FONTLOG)
- PR #459 was submitted and merged on 2016-12-05, adding v1.100 to google/fonts
- No further commits were made to the upstream repo after this

The commit hash is not recorded in the current METADATA.pb source block, but is tracked in the `gfonts_library_sources.json` file.

## Config YAML Status

**No config.yaml exists** in the upstream repository. The repository contains Glyphs sources at `sources/CabinSketch.glyphs`, which is a gftools-buildable format, but there is no `config.yaml` to configure the build.

There is also no override `config.yaml` in the google/fonts family directory (`ofl/cabinsketch/`).

A config.yaml would need to be created (either in the upstream repo or as an override in google/fonts) for this family to be buildable with gftools-builder.

## Verification

- **Repository URL**: Valid. Points to the impallari/CabinSketch GitHub repository.
- **Commit Hash**: Verified. The hash `f74674fd7ba37fdfcdad88b58d8d3983a320a68d` exists in the repository and is HEAD.
- **Font Files Match**: The upstream repo at this commit contains `fonts/CabinSketch-Bold.ttf` and `fonts/CabinSketch-Regular.ttf`, matching the files in google/fonts.
- **Source Files**: The repo contains `sources/CabinSketch.glyphs` (Glyphs format).

## Confidence Level

**HIGH** - The repository URL and commit hash are well-established. The commit is HEAD of the repo, the timeline matches PR #459, and the font files match. The only gap is the missing config.yaml.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/CabinSketch.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Should a config.yaml override be created in google/fonts for this family to make it gftools-builder compatible?
2. The METADATA.pb source block currently lacks the commit hash - should it be added?
