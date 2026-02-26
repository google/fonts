# Big Shoulders Text

**Status**: `complete` (but commit hash needs correction)
**Date**: 2026-02-26
**Designer**: Patric King
**License**: OFL
**METADATA.pb**: `ofl/bigshoulderstext/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `465a9c592f06d493841b35dca5d248c8142b75f8` |
| Config YAML | Override config.yaml in google/fonts |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url` and confirmed by the copyright string. All Big Shoulders variants share the same upstream repository.

### Commit Hash
**Binary-verified to be `465a9c592f06d493841b35dca5d248c8142b75f8`**, not `41153e6fe01d218e933919a1d08c8e45065bc8fe` as recorded in the tracking data.

Evidence for `465a9c5`:
1. The merged commit `7f3f5f3c7` in google/fonts explicitly states: "Big Shoulders Text Version 2.002 taken from the upstream repo ... at commit 465a9c592f06d493841b35dca5d248c8142b75f8"
2. **Binary blob verification**: The file `Big-Shoulders/fonts/variable/text/BigShouldersText[wght].ttf` at commit `465a9c5` in upstream has blob hash `d5798cca9e756cc337224e1da0da04d7c9a2025f`, which exactly matches the current google/fonts file
3. At commit `41153e6` (May 2021), the directory `Big-Shoulders/fonts/variable/text/` does not contain `BigShouldersText[wght].ttf` -- the variable font structure had not yet been reorganized. The VF file path in METADATA.pb would not resolve at `41153e6`.

PR history shows the initial push referenced `b465ae3` (v2.000), then the packager was re-run with `465a9c5` (v2.002) before the PR was merged.

**Tracking data correction needed**: The tracking data records `41153e6` from an unmerged PR branch (`sources_info_2026-02-25`). The correct commit is `465a9c5`. The METADATA.pb on main does NOT have a `commit` field at all.

### Config YAML
An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshoulderstext/config.yaml`, added by Simon Cozens on 2024-05-30 (commit `3c65c4e01`). It uses a recipe-based build that:
1. Builds from `Big-Shoulders/sources/BigShoulders.glyphs`
2. Subspaces to `opsz=10` (text optical size)
3. Renames to "Big Shoulders Text"

The config.yaml was added for future rebuild capability but the current binary was NOT rebuilt -- it is still the binary from PR #3432 at commit `465a9c5`.

The config.yaml also includes the Text SC variant build recipe.

## Evidence

### METADATA.pb source block (current main)
```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "Documentation/DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "Big-Shoulders/fonts/variable/text/BigShouldersText[wght].ttf" dest_file: "BigShouldersText[wght].ttf" }
  branch: "master"
}
```
Note: No `commit` field on main branch.

### google/fonts history
- `4fd9e2392` (PR branch): Added commit `41153e6` to METADATA.pb (INCORRECT, on unmerged `sources_info_2026-02-25` branch)
- `3c65c4e01` (2024-05-30): "Add config for parent bigshoulderstext too" (override config.yaml)
- `7f3f5f3c7` (2021-09-08): "Big Shoulders Text: Version 2.000 added (#3432)" -- landed with commit `465a9c5`
- `c172a915d`: "Big Shoulders Text: Version 1.101 added (#2745)"
- `afb44322d`: "bigshoulderstext: v1.000 added"

### PR #3432
- Title: "Big Shoulders Text: Version 2.000 added"
- Author: vv-monsalve (Viviana Monsalve)
- Merged: 2021-09-08
- PR body initially mentioned `b465ae3` (v2.000)
- Merged commit message says `465a9c5` (v2.002 -- packager re-run with updated commit)

### Binary blob verification
| Source | Blob Hash |
|--------|-----------|
| Upstream at `465a9c5` | `d5798cca9e756cc337224e1da0da04d7c9a2025f` |
| google/fonts current | `d5798cca9e756cc337224e1da0da04d7c9a2025f` |
| Upstream at `41153e6` | File does not exist at this path |

### Upstream repo cache
- Cached at: `xotypeco/big_shoulders`
- Commit `465a9c5` verified ("Merge pull request #39 from vv-monsalve/master", 2021-08-27)
- `Big-Shoulders/fonts/variable/text/BigShouldersText[wght].ttf` exists at this commit with matching blob
- Commit `41153e6` verified but does NOT contain the VF font binary at the expected path

## Confidence

**High**: Binary blob verification conclusively proves `465a9c5` is the correct commit. The merged commit message in google/fonts corroborates this.

## Notes
- Part of the Big Shoulders superfamily (all in https://github.com/xotypeco/big_shoulders)
- First added as v1.000 (PR #2597), updated to v1.101 (PR #2745), then v2.002 (PR #3432)
- The tracking data needs correction: should be `465a9c5`, not `41153e6`
- The METADATA.pb on main is missing the `commit` field entirely
- Override config.yaml was added in 2024 but the binary was not rebuilt
- Same font family tree as Big Shoulders Text SC (the override config builds both)
