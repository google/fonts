# Average

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Eduardo Tunni
**METADATA.pb path**: `ofl/average/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/etunni/average |
| Commit | `6583341221fb0625ba1b9c3ee2a7490d57df951f` |
| Config YAML | override in google/fonts |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { }` block (added by PR #5292). It is also referenced in the font copyright string: "Copyright 2012 The Average Project Authors (https://github.com/etunni/average)". The repo at https://github.com/etunni/average is active and belongs to Eduardo Tunni.

## How the Commit Hash Was Identified

The commit hash `6583341221fb0625ba1b9c3ee2a7490d57df951f` was set in METADATA.pb by the gftools-packager in PR #5292 (merged 2022-10-07). There is a discrepancy: the PR body text references an earlier commit `6388db3a611d1d489a19a5511a90bb426bd2bae4` ("Merge pull request #1 from emmamarichal/master", 2022-08-05), but the METADATA.pb was written with `6583341` ("Merge pull request #2 from emmamarichal/master", 2022-10-06). This suggests the gftools-packager picked up the HEAD of the upstream repo at the actual packaging time, which was a newer commit than when the PR description was first drafted. Since the binary TTF was built at packaging time, the commit `6583341` in METADATA.pb is the correct one -- it was the latest upstream commit at the time the font was actually packaged.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository at `etunni/average`. An override `config.yaml` exists in the google/fonts family directory at `ofl/average/config.yaml` with the following content:

```yaml
buildVariable: false
sources:
  - sources/Average.glyphs
```

This was added by commit `bfd8bf8bd` ("sources info for Average: Version 1.003 (PR #5292)"). The upstream repo has a `.glyphs` source file at `sources/Average.glyphs`, which the override config references. Since an override exists in google/fonts, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-10-06 07:42:11 -0300
- Commit message: "Merge pull request #2 from emmamarichal/master"
- Source files at commit: `sources/Average.glyphs`, `old/Average-Regular.otf.ufo/` (legacy UFO)

## Confidence

**High**: The repository URL, commit hash, and config override are all properly documented and verified. The upstream repo contains the correct `.glyphs` source. The only minor note is the PR body referencing an older commit, but the METADATA.pb commit is the correct one used for actual packaging.

## Open Questions

None
