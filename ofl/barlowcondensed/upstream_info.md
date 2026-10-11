# Barlow Condensed

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Jeremy Tribby
**METADATA.pb path**: `ofl/barlowcondensed/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/jpt/barlow |
| Commit | b4726ddf91525818e85e5fce111c285b9273d764 |
| **Config YAML** | Override in google/fonts |
| Branch | main |

## How the Repository URL Was Found
The METADATA.pb file already contains `repository_url: "https://github.com/jpt/barlow"`. This matches the copyright string in font entries: "Copyright 2017 The Barlow Project Authors (https://github.com/jpt/barlow)". Barlow Condensed is part of the Barlow superfamily, all generated from a single `sources/Barlow.glyphs` source file in the jpt/barlow repository.

## How the Commit Hash Was Identified
The last commit to modify .ttf files in `ofl/barlowcondensed/` was `89f5431ff0db41bd2fe3f7ba21a723a01622428b` (2018-12-05, "barlow family updated to v1.408 (#1330) - major fixes"). PR #1330 was submitted by Jeremy Tribby (the designer, @jpt) himself with body: "This is a few versions ahead now, fixes a number of issues, some small some big (see jpt/barlow/releases)".

The v1.408 tag in the upstream repo points to commit `b4726ddf91525818e85e5fce111c285b9273d764` (2018-11-06, "Fixes #34 and #37"). Since PR #1330 references version v1.408 and was submitted by the designer who would have built the fonts from this tagged release, this commit hash is the correct onboarding reference.

The initial onboarding was via PR #1279 ("barlowcondensed: v1.101 added", by Marc Foley, merged 2017-10-31), but the v1.408 update replaced those binaries.

## How Config YAML Was Resolved
No `config.yaml` exists in the upstream repository at any commit. No override `config.yaml` exists in the google/fonts `ofl/barlowcondensed/` directory either. The Barlow.glyphs source file is a multi-axis source (including width axis for Condensed/Semi Condensed variants), so a config.yaml would need to be created to specify which instances to build.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2018-11-06
- Commit message: "Fixes #34 and #37"
- Source files at commit: `sources/Barlow.glyphs`, `sources/CUST_Barlow.csv`
- v1.408 tag points to this commit: Yes
- Pre-built Condensed binaries present at this commit: Yes (in `fonts/ttf/`)

## Confidence
**High**: The v1.408 tag clearly identifies the commit, and the PR was submitted by the designer himself. The commit hash is already correctly recorded in the tracking data.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Barlow.glyphs
familyName: Barlow Condensed
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions
- A config.yaml needs to be created to build Barlow Condensed instances from the Barlow.glyphs source. This config would need to specify the Condensed width instances specifically.
- Since Barlow, Barlow Condensed, and Barlow Semi Condensed all share the same source file, the config.yaml would ideally need to be coordinated across all three families.
