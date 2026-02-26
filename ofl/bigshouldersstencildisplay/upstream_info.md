# Big Shoulders Stencil Display

**Status**: `complete`
**Date**: 2026-02-26
**Designer**: Patric King
**License**: OFL
**METADATA.pb**: `ofl/bigshouldersstencildisplay/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `2f924dd1205484c5e0054b1f3955f434224ba72e` |
| Config YAML | Override config.yaml in google/fonts |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url` and confirmed by the copyright string. All Big Shoulders variants share the same upstream repository.

### Commit Hash
**Binary-verified to be `2f924dd1205484c5e0054b1f3955f434224ba72e`**, not `41153e6fe01d218e933919a1d08c8e45065bc8fe` as previously recorded in the tracking data.

Evidence for `2f924dd`:
1. The individual PR commits in PR #3436 explicitly state: "Big Shoulders Stencil Display Version 2.001 taken from the upstream repo ... at commit 2f924dd1205484c5e0054b1f3955f434224ba72e"
2. The squash merge commit `081d4ba5b` also references `2f924dd`
3. **Binary SHA256 verification**: The file `Big-Shoulders-Stencil/fonts/variable/display/BigShouldersStencilDisplay[wght].ttf` at commit `2f924dd` in upstream has SHA256 `93bbefb9f3a497fcfeec5d1ac85c4a947a32b8e5bcaf3b7b5efff52f1b11b0e4`, which exactly matches the current google/fonts file
4. At commit `41153e6` (May 2021), the directory `Big-Shoulders-Stencil/fonts/variable/` does not exist -- the font files were in `Big-Shoulders-Stencil/fonts/ttf/` instead. The file paths in METADATA.pb could only resolve at `2f924dd` or later.

The PR body mentioned `41153e6` because the PR was initially created referencing that commit, but the packager was re-run with `2f924dd` before the PR was merged.

**Tracking data correction needed**: The tracking data and the pending branch `sources_info_2026-02-25` both incorrectly record `41153e6`. The correct commit is `2f924dd`.

### Config YAML
An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersstencildisplay/config.yaml`. It uses a recipe-based build that:
1. Builds from `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`
2. Subspaces to `opsz=72` (display optical size)
3. Renames to "Big Shoulders Stencil Display"

It also builds the SC variant (BigShouldersStencilDisplaySC) in the same config, using `smcp -> ccmp` remap.

The upstream repo has `Big-Shoulders-Stencil/sources/config.yml` but it builds the full family, not the display-specific subspace.

The METADATA.pb on main does NOT have a `commit` field. The commit was added on the `sources_info_2026-02-25` branch but with the incorrect value `41153e6`.

## Evidence

### METADATA.pb source block (current main)
```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "Documentation/DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "Big-Shoulders-Stencil/fonts/variable/display/BigShouldersStencilDisplay[wght].ttf" dest_file: "BigShouldersStencilDisplay[wght].ttf" }
  branch: "master"
}
```
Note: No `commit` field on main branch.

### google/fonts history
- `84014a94c`: "Add config for parent bigshouldersstencildisplay too" (override config.yaml added)
- `081d4ba5b` (2021-09-08): "Big Shoulders Stencil Display: Version 2.000 added (#3436)" -- squash merge references `2f924dd`
- `6eb21f3b2`: "Big Shoulders Stencil Display: Version 1.000 added (#2744)" -- initial add from commit `3f1061046298`

### PR #3436
- Title: "Big Shoulders Stencil Display: Version 2.000 added"
- Author: vv-monsalve (Viviana Monsalve)
- PR body references commit `41153e6` (initial PR creation)
- Individual PR commits reference commit `2f924dd` (packager was re-run)

### Binary verification
| Source | SHA256 |
|--------|--------|
| Upstream at `2f924dd` | `93bbefb9f3a497fcfeec5d1ac85c4a947a32b8e5bcaf3b7b5efff52f1b11b0e4` |
| google/fonts current | `93bbefb9f3a497fcfeec5d1ac85c4a947a32b8e5bcaf3b7b5efff52f1b11b0e4` |
| Upstream at `41153e6` | File path does not exist (`fonts/variable/display/` directory absent) |

### Upstream repo cache
- Cached at: `xotypeco/big_shoulders`
- Commit `2f924dd1205484c5e0054b1f3955f434224ba72e` verified ("Merge pull request #40 from vv-monsalve/master", 2021-09-02)
- `Big-Shoulders-Stencil/fonts/variable/display/BigShouldersStencilDisplay[wght].ttf` exists at this commit

## Confidence

**High**: Binary SHA256 verification conclusively proves `2f924dd` is the correct commit. Multiple sources (PR commits, squash merge message) corroborate this.

## Notes
- Part of the Big Shoulders superfamily (all in https://github.com/xotypeco/big_shoulders)
- First added as v1.000 from commit `3f10610` (PR #2744), then updated to v2.000 from commit `2f924dd` (PR #3436)
- The tracking data needs correction: should be `2f924dd`, not `41153e6`
- The METADATA.pb on main is missing the `commit` field
- Same font update batch as Big Shoulders Stencil Text (both PR #3435 and #3436, same upstream commit)
- Date added to Google Fonts: 2020-10-13 (v1.000), updated 2021-09-08 (v2.000)
