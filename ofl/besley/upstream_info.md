# Besley - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Besley |
| Repository URL | https://github.com/indestructible-type/Besley |
| Commit Hash | eb8b1b7f62f9f328e4be345d3e5928fefba3c38e |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/indestructible-type/Besley` was present in the METADATA.pb file's source block. This URL is also referenced in the copyright string of the font files ("Copyright 2020 The Besley Project Authors (https://github.com/indestructible-type)") and was confirmed via PR #2942 body, which explicitly states: "taken from the upstream repo https://github.com/indestructible-type/Besley".

## How the Commit Hash Was Determined

The commit hash `eb8b1b7f62f9f328e4be345d3e5928fefba3c38e` was recorded in the METADATA.pb source block. Cross-verification reveals an important detail:

- **PR #2942 body** originally referenced commit `0aa18c1d1f45e4105a8c23e64c8c84a602b135e8` (dated 2020-12-20, message: "Besley 2.0")
- **METADATA.pb** records commit `eb8b1b7f62f9f328e4be345d3e5928fefba3c38e` (dated 2021-07-11, message: "Merge pull request #17 from aaronbell/master")

The recorded hash `eb8b1b7` is a descendant of the PR-mentioned hash `0aa18c1`. Between these two commits, the upstream repo saw significant cleanup (deleting old binary files, fixing STAT table, updating to UFR format). The commit message "Fixing STAT table and updating to UFR" (commit `07adb7e`) and the merge of Aaron Bell's contributions suggest the PR was revised during review to incorporate these improvements. The final onboarding to google/fonts (commit `85c5cea9d` on 2021-07-15) used the later commit.

The font binary files at `fonts/variable/Besley[wght].ttf` and `fonts/variable/Besley-Italic[wght].ttf` match the `files` mapping in METADATA.pb source block.

## Config YAML Status

- **Path**: `sources/config.yaml`
- **Exists at recorded commit**: Yes, verified via `git show eb8b1b7:sources/config.yaml`
- **Contents**: Proper gftools-builder config referencing `designspace/Besley.designspace` and `designspace/Besley-Italic.designspace`, with weight axis, STAT table configuration, and `autohintTTF: False`
- **No override config.yaml** exists in the google/fonts family directory
- **Note**: The config.yaml was later removed from the upstream repo (exists only in the v2.0 era commits). The current HEAD of the repo does not have it.

## Verification

1. Commit hash `eb8b1b7` verified to exist in the cached upstream repo at `upstream_repos/fontc_crater_cache/indestructible-type/Besley`
2. Font files `fonts/variable/Besley[wght].ttf` and `fonts/variable/Besley-Italic[wght].ttf` confirmed present at that commit
3. `sources/config.yaml` confirmed present at that commit with valid gftools-builder configuration
4. Repository URL confirmed accessible and matching
5. The `branch: "master"` field is correct (the upstream repo uses master branch)

## Confidence Level

**High** - The repository URL and commit hash are well-documented. The PR body provides clear provenance, and the recorded commit hash is the final version used during the review cycle (later than the initially proposed commit). All file mappings are verified. The config.yaml exists at the recorded commit.

## Open Questions

1. The config.yaml was removed from the upstream repo in later commits (post v2.0). If the font is ever rebuilt from source, the config would need to be recreated or an override placed in google/fonts.
2. The upstream repo has progressed significantly since the recorded commit (up to version 4.0 with Greek support), but those updates have not been onboarded to Google Fonts yet.
