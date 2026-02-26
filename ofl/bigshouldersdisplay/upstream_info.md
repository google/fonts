# Investigation Report: Big Shoulders Display

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Display |
| Designer | Patric King |
| License | OFL |
| Date Added | 2019-09-11 |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | `41153e6fe01d218e933919a1d08c8e45065bc8fe` (recorded) |
| Correct Commit Hash | `465a9c592f06d493841b35dca5d248c8142b75f8` (see below) |
| Branch | master |
| Config YAML | Override config.yaml in google/fonts |
| Status | **Complete** (but commit hash may need correction) |

## How URL Found

The repository URL is documented in the copyright field ("Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)") and in multiple google/fonts commits referencing this upstream repo.

## How Commit Determined

The commit history for Big Shoulders Display in google/fonts is complex:

### Version History in google/fonts

1. `0e29996d5` - "bigshouldersdisplay: added" (initial, 2019)
2. `c92513650` - "Big Shoulders Display v1.100 added"
3. `ca3fc76f0` / `2c7775fed` - "Big Shoulders Display: Version 1.101 added"
4. `94ee6b8b9` - **PR #3434**: "Big Shoulders Display: Version 2.000 added" by vv-monsalve (2021-09-08) - the last font binary update

### The Commit Hash Discrepancy

PR #3434 contains **two different commit references**:

1. **PR body** (first commit in PR): States commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`
2. **Actual commit message** (merged into google/fonts): States commit `465a9c592f06d493841b35dca5d248c8142b75f8`

The **upstream.yaml** file updated in PR #3434 references the path `Big-Shoulders/fonts/variable/display/BigShouldersDisplay[wght].ttf`. This path:
- Does **NOT exist** at commit `41153e6` (at that commit, the file was at `Big-Shoulders/fonts/ttf/BigShouldersDisplay[wght].ttf`)
- **DOES exist** at commit `465a9c5` (the `variable/display/` subdirectory was introduced between these commits)

The commit `0309399` ("Stat table fix") first introduced the `Big-Shoulders/fonts/variable/display/` path, and this was merged into master via `465a9c5`.

**Conclusion**: The correct commit for the v2.000 update is `465a9c592f06d493841b35dca5d248c8142b75f8`, not `41153e6fe01d218e933919a1d08c8e45065bc8fe`. The PR body recorded the initial attempt, but the final merged state used the later commit.

### Currently Recorded Commit

The METADATA.pb currently records `41153e6fe01d218e933919a1d08c8e45065bc8fe`, which was added in our batch update (`4fd9e2392`). This appears to have been based on the PR body text rather than the commit message, and should potentially be corrected to `465a9c5`.

## Config YAML Status

An **override config.yaml** exists at `ofl/bigshouldersdisplay/config.yaml` in google/fonts, added by Simon Cozens in commit `8d115a6cf` ("Add config for parent bigshouldersdisplay too", 2024-05-30).

This config builds both Big Shoulders Display and Big Shoulders Display SC from the same Glyphs source file, using recipe operations to:
- Build variable font from `BigShoulders.glyphs`
- Subspace to `opsz=72` (display optical size)
- Rename to "Big Shoulders Display"
- For SC variant: apply smcp -> ccmp layout remapping

Because an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- **Commit `41153e6` exists in upstream repo**: Yes
- **Commit `465a9c5` exists in upstream repo**: Yes
- **File path at `41153e6`**: `Big-Shoulders/fonts/ttf/BigShouldersDisplay[wght].ttf` (different from METADATA.pb)
- **File path at `465a9c5`**: `Big-Shoulders/fonts/variable/display/BigShouldersDisplay[wght].ttf` (matches METADATA.pb)
- **Override config.yaml in google/fonts**: Yes
- **Source block in METADATA.pb**: Has repository_url, commit, files mapping, branch; no config_yaml (correct, override exists)

## Confidence Level

**Medium-High** - The repository URL is certain. The commit hash has a discrepancy: the currently recorded `41153e6` was from the initial PR body, but the final merged commit message and the file paths both point to `465a9c5` as the correct commit. The override config.yaml is verified and working.

## Open Questions

1. **Commit hash correction**: The recorded commit hash `41153e6` should likely be updated to `465a9c592f06d493841b35dca5d248c8142b75f8` to match the actual commit used for the v2.000 update. The file path in METADATA.pb (`Big-Shoulders/fonts/variable/display/BigShouldersDisplay[wght].ttf`) only exists at the later commit.
2. **Relationship to parent family**: Big Shoulders Display is a derivative of the parent Big Shoulders family (same upstream repo, different optical size slice). The parent family uses commit `8ba99c9` (HEAD of master), while Big Shoulders Display uses an older commit from 2021.
