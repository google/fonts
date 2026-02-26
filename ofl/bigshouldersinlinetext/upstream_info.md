# Big Shoulders Inline Text

**Date investigated**: 2026-02-26
**Status**: needs_correction
**Designer**: Patric King
**METADATA.pb path**: `ofl/bigshouldersinlinetext/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit (current METADATA.pb) | `41153e6fe01d218e933919a1d08c8e45065bc8fe` |
| Commit (correct) | `2f924dd1205484c5e0054b1f3955f434224ba72e` |
| Config YAML | (omitted - override config.yaml in google/fonts) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/xotypeco/big_shoulders` was already present in the METADATA.pb `source { repository_url }` field, originally set via the `f7455d788` commit ("Populate source.repository_url"). It matches the copyright string and is shared across all Big Shoulders variants.

## How the Commit Hash Was Identified

**The current METADATA.pb commit hash `41153e6` is incorrect.** Binary comparison proves the correct commit is `2f924dd1205484c5e0054b1f3955f434224ba72e`.

The font was updated to Version 2.000 via PR #3437 (by vv-monsalve, merged 2021-09-08). This PR had multiple packager runs, exactly like the sibling PR #3438 for Inline Display:

1. **First run** (PR body, created 2021-05-21): Referenced upstream commit `41153e6fe01d218e933919a1d08c8e45065bc8fe` (dated 2021-05-20, "Merge upstream 'master' at commit b465ae3" by Viviana Monsalve). This was Version 2.000.

2. **Second run** (in squashed commit body): Referenced upstream commit `2f924dd1205484c5e0054b1f3955f434224ba72e` (dated 2021-09-02, "Merge pull request #40 from vv-monsalve/master"). This was Version 2.002 and was the final packager output that was actually merged.

**Binary verification**: The git blob hash of the font file `BigShouldersInlineText[wght].ttf` in google/fonts is `66b0b3d89b9c4e00bba7c4eede8e339f9210a266`, which matches exactly the blob hash of the same file at upstream commit `2f924dd`. This definitively confirms `2f924dd` as the source commit.

The incorrect commit `41153e6` was added to METADATA.pb by our own batch commit `4fd9e2392` ("Add source metadata to 125 METADATA.pb files"), which picked up the commit from the PR body (first packager run) rather than the squashed commit body (second/final packager run).

## How Config YAML Was Resolved

An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersinlinetext/config.yaml`. Therefore, the `config_yaml` field is correctly omitted from the METADATA.pb source block. The override was added by Simon Cozens (commit `6340d7788`, "Add config for parent bigshouldersinlinetext too") as part of PR #7786 for the Inline Display SC onboarding.

The override config defines a recipe that:
1. Builds from `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`
2. Subspaces to `opsz=10` (text optical size)
3. Renames to "Big Shoulders Inline Text"
4. Also builds the SC variant with `smcp -> ccmp` remapping

## Verification

- Commit `41153e6` exists in upstream repo: Yes, but is WRONG for this family
- Commit `2f924dd` exists in upstream repo: Yes, and is CORRECT
- Binary blob hash match at `2f924dd`: CONFIRMED (`66b0b3d89b9c4e00bba7c4eede8e339f9210a266`)
- Commit `2f924dd` date: 2021-09-02
- Commit `2f924dd` message: "Merge pull request #40 from vv-monsalve/master"
- Font binary at `2f924dd`: `Big-Shoulders-Inline/fonts/variable/text/BigShouldersInlineText[wght].ttf` exists
- Override config.yaml in google/fonts: Yes

## Confidence

**High** (for the corrected commit): Binary blob hash comparison provides definitive proof that `2f924dd` is the correct upstream commit. The squashed commit body in google/fonts also references this commit as the final packager output. The METADATA.pb needs correction from `41153e6` to `2f924dd`.

## Open Questions

1. **METADATA.pb needs correction**: The commit hash should be updated from `41153e6fe01d218e933919a1d08c8e45065bc8fe` to `2f924dd1205484c5e0054b1f3955f434224ba72e`. This should be included in a PR to google/fonts (same correction as Big Shoulders Inline Display). The tracking data in `gfonts_library_sources.json` also needs updating.
