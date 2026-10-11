# Bahiana

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Omnibus-Type
**METADATA.pb path**: `ofl/bahiana/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Bahiana |
| Commit | `43505501149a661266ef6c7603fe0d6ddd58984e` (not in METADATA.pb, inferred) |
| **Config YAML** | Override in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL was added to METADATA.pb by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)") on 2024-01-14. The original onboarding PR #490 also referenced the same URL: "Source repo [here](https://github.com/Omnibus-Type/Bahiana)".

## How the Commit Hash Was Identified

The Bahiana font was onboarded on 2016-12-02 via PR #490. The commit message in google/fonts is simply "bahiana: v1.005 added (#490)" with no upstream commit reference. The PR body also does not reference a specific commit.

The upstream repository has a full history available (not a shallow clone). The latest commits before the onboarding date (2016-12-02) were:

1. `4350550` (2016-12-01) "README: moved bagiana.gif to top level"
2. `222a04e` (2016-12-01) "fonts: regenerated"
3. `99c26ff` (2016-12-01) "FONTLOG: entry added for today's v1.005 update"
4. Several more on 2016-12-01 related to restructuring

All these commits were from the same day (2016-12-01), the day before onboarding. The font regeneration at `222a04e` and subsequent README fix at `4350550` represent the state at onboarding time. The tracking file uses `4350550` as the inferred commit.

**Important**: The repository was later restructured on 2018-05-01 (commit `410e221` "GF Latin plus commit"), moving the Bahiana sources under a `BahianaGF/` subdirectory and adding a new `Bahianita/` subdirectory. At the time of onboarding, the sources were at the repo root under `sources/`.

## How Config YAML Was Resolved

No config.yaml or builder.yaml exists anywhere in the upstream repository (neither at the onboarding commit nor at HEAD). No override config.yaml exists in the google/fonts family directory. The source file at the onboarding commit was `sources/Bahiana.glyphs` (and `sources/Bahiana.ufo`). After the restructure, sources moved to `BahianaGF/sources/Bahiana.glyphs`.

An override config.yaml would need to be created in google/fonts to resolve this. Given the repository restructuring, the config would need to reference the current path `BahianaGF/sources/Bahiana.glyphs` if the commit is updated to reflect the restructured state, or use the old path `sources/Bahiana.glyphs` if the commit stays at the pre-restructure point.

## Verification

- Commit exists in upstream repo: Yes (commit `4350550` is in the full history)
- Commit date: 2016-12-01 16:06:55 +0100
- Commit message: "README: moved bagiana.gif to top level"
- Source files at commit: `sources/Bahiana.glyphs`, `sources/Bahiana.ufo`

## Confidence

**Medium**: The commit `4350550` is a reasonable inference as it was the latest upstream commit before the onboarding date, but no explicit commit reference exists in the google/fonts PR or commit body. The font files at this commit match what was onboarded (v1.005). The repository restructuring adds complexity since current source paths differ from onboarding-time paths.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Bahiana.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. An override config.yaml needs to be created for this family. Should it reference the sources at the onboarding-era path (`sources/Bahiana.glyphs`) with commit `4350550`, or should the commit be updated to a post-restructure commit and reference `BahianaGF/sources/Bahiana.glyphs`?
2. The METADATA.pb source block has no commit hash, no branch, no config_yaml, and no file mappings. A PR to google/fonts would be needed to complete the source documentation.
