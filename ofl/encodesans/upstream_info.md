# Investigation: Encode Sans

- **Date investigated**: 2026-02-27
- **Status**: missing_config
- **Designer**: Impallari Type, Andres Torresi, Jacques Le Bailly (variable font upgrade by Stephen Nixon and Marc Foley)
- **METADATA.pb path**: `ofl/encodesans/METADATA.pb`

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | `https://github.com/thundernixon/Encode-Sans` |
| commit_hash      | `6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc` |
| config_yaml      | N/A (no config.yaml in upstream; override needed) |

## How URL Was Found

The repository URL `https://github.com/thundernixon/Encode-Sans` is already present in the METADATA.pb `source {}` block. It was added by Simon Cozens in commit `cd5db6b6e` ("Update upstreams", 2023-12-14). The URL is also referenced in the copyright notice in METADATA.pb, the DESCRIPTION.en_us.html file, and in the PR history for the font (PRs #2438, #2497, #2515).

Note: This repo is Stephen Nixon's fork where the variable font upgrade was developed. The original static font sources are at `https://github.com/impallari/Encode-Sans` (Pablo Impallari's repo), which is referenced in the METADATA.pb of the older static-only variants (Encode Sans Condensed, Expanded, Semi Condensed, Semi Expanded).

## How Commit Hash Was Identified

The commit hash `6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc` was explicitly stated in the PR #2515 body by the author Stephen Nixon:

> "This PR represents Encode Sans as of https://github.com/thundernixon/Encode-Sans/commit/6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc."

This commit ("build v3.002 with fixed static names", 2020-06-24) is the HEAD of the master branch and also the only commit in the shallow clone. The GitHub API confirms it remains the latest commit on master. PR #2515 was merged on 2020-07-15, and the upstream commit dates to 2020-06-24, consistent with the timeline.

### Timeline of Encode Sans variable font onboarding

1. **PR #2438** ("encodesans: v3.0 added"): Merged 2020-05-11, initial variable font onboarding by Stephen Nixon
2. **PR #2497** ("encodesans: v3.001 added"): Merged 2020-06-17, update to v3.001
3. **PR #2515** ("encodesans: v3.002 added"): Merged 2020-07-15, final update fixing static font naming issues; this is the version currently in google/fonts

The PR #2515 body explains that v3.002 corrected a naming issue in static files where they had an erroneous "SC" suffix. The variable font itself only changed in version numbering (3.001 -> 3.002), as confirmed by the fdiff output included in the PR.

## How Config YAML Was Resolved

No `config.yaml` file exists in the upstream repository. The repo uses custom shell build scripts (`sources/scripts/build.sh`, `sources/scripts/build-vf.sh`, `sources/scripts/build-statics.sh`) that invoke `fontmake` directly with various post-processing steps (STAT table addition, DSIG/GASP fixes, MVAR table removal, small caps subsetting, etc.).

No override `config.yaml` exists in the google/fonts family directory either.

The source file is a Glyphs source at `sources/Encode-Sans.glyphs`. An override config.yaml for gftools-builder would need to reference this source file. However, the build process is complex (custom scripts with post-processing), so a simple gftools-builder config may not reproduce the exact same output.

A minimal override config.yaml could be created:

```yaml
sources:
  - sources/Encode-Sans.glyphs
axisOrder:
  - wdth
  - wght
```

## Verification

- **Repository URL**: Confirmed valid via GitHub API and git remote. Repo created 2018-10-02, last pushed 2020-06-24.
- **Commit hash**: `6407de8` is the HEAD of master and matches the hash explicitly cited in PR #2515.
- **Font file**: `EncodeSans[wdth,wght].ttf` is a 2-axis variable font (wdth 75-125, wght 100-900).
- **Upstream repo is clean**: `git status` reports clean working tree on master, up to date with origin.
- **Shallow clone**: The local cache is a shallow clone (depth 1) of the master branch. Full history is available via GitHub API.
- **Related families**: Encode Sans SC (`ofl/encodesanssc/`) also uses this repo. The older static-only variants (Condensed, Expanded, Semi Condensed, Semi Expanded) point to `impallari/Encode-Sans`.

## Confidence

**HIGH** -- The commit hash is explicitly stated by the font author (Stephen Nixon) in PR #2515 body, and it is the HEAD of the upstream master branch. The repository URL is confirmed by multiple sources (METADATA.pb, copyright notice, PR history). The only gap is the missing config.yaml, which would need to be created as an override.
