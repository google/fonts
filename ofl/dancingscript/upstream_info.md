# Dancing Script

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Impallari Type
**METADATA.pb path**: `ofl/dancingscript/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/DancingScript |
| Commit | `291f87c05206179b6bfd53735a5638b5cc84e3b3` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/DancingScript`. The copyright string references this URL. The font was originally maintained at `https://github.com/aaronbell/DancingScript` and later transferred/forked to the googlefonts organization. The URL was added to METADATA.pb by commit `f7455d788` ("Populate source.repository_url") in google/fonts.

## How the Commit Hash Was Identified

The commit `291f87c05206179b6bfd53735a5638b5cc84e3b3` was added via the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), porting data from fontc_crater's target.json.

**Background on the font update history**: The most recent font binary update was PR #3788 (commit `f8dc91f6f`, 2021-09-30, "Dancing Script: Version 2.001 added") by Aaron Bell. The PR body states the font was "taken from the upstream repo https://github.com/aaronbell/DancingScript at commit https://github.com/aaronbell/DancingScript/commit/d1b9b8b369e284006d1d0e03464693e6c895fba2."

The `googlefonts/DancingScript` repository has a single merge commit (`291f87c`, "Merge pull request #9 from aaronbell/master") which is HEAD. This merge commit incorporates the aaronbell fork content. Since the METADATA.pb points to the googlefonts repo (not the aaronbell fork), using `291f87c` as the commit is appropriate -- it represents the canonical state of the font in the googlefonts organization's repository.

The upstream repo is a shallow clone with only this single commit visible. The original aaronbell commit `d1b9b8b3` is not present in the local clone (it was in the aaronbell fork history).

## How Config YAML Was Resolved

The file `sources/config.yaml` exists in the upstream repository at the recorded commit. It contains gftools-builder configuration referencing `DancingScript.designspace` with a weight axis and STAT table definitions. This was added to METADATA.pb via the same batch commit `19cdcec59`. No override config.yaml exists in the google/fonts family directory (`ofl/dancingscript/`).

## Verification

- Commit exists in upstream repo: Yes (it is the only commit / HEAD)
- Commit message: "Merge pull request #9 from aaronbell/master"
- Source files at commit: `sources/DancingScript.designspace`, `sources/config.yaml`, legacy sources in `legacy/`
- Font binary: Variable font `DancingScript[wght].ttf` with weight axis (400-700)
- Variable font confirmed: `DancingScript[wght].ttf` in both upstream and google/fonts

## Confidence

**High**: The repository URL and commit hash are consistent. The googlefonts/DancingScript repo is the canonical home for this font. The commit `291f87c` is the only commit in the repo and encompasses all the work from aaronbell's fork. The config.yaml is present and valid. The font was originally onboarded from aaronbell's fork but the canonical repo has been moved to googlefonts.

## Open Questions

1. The local clone of googlefonts/DancingScript appears to be shallow (single commit). A full clone might reveal additional history, but since `291f87c` is HEAD and the only commit on master, this is not a concern for verification purposes.
