# Albert Sans

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: needs_correction
**Designer**: Andreas Rasmussen
**METADATA.pb path**: `ofl/albertsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/usted/Albert-Sans |
| Commit (current in METADATA.pb) | `f7f46082233f5a29cb71d6ae1d8d0ef9c7962d6c` |
| Commit (correct for onboarding) | `929c7d5058afd06870d1dd4ebc3a0ee98bb77420` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/usted/Albert-Sans` was present in METADATA.pb since the original onboarding commit. It was also referenced in the copyright string of the font files and in the PR #4756 commit message. The cached upstream repo at `usted/Albert-Sans` confirms the remote matches.

## How the Commit Hash Was Identified

### Original onboarding commit: `929c7d5`

The font was onboarded in google/fonts via PR #4756 (commit `6b612533`, merged 2022-06-16) by Emma Marichal. The commit message explicitly states:

> Albert Sans Version 1.025 taken from the upstream repo https://github.com/usted/Albert-Sans at commit https://github.com/usted/Albert-Sans/commit/929c7d5058afd06870d1dd4ebc3a0ee98bb77420.

This commit was dated 2022-06-03 in the upstream repo with message "fonts folder". Binary file verification confirms this is the correct onboarding commit: the SHA-256 hash of `fonts/variable/AlbertSans[wght].ttf` at commit `929c7d5` matches the file currently in `ofl/albertsans/AlbertSans[wght].ttf` exactly (`8fe5d4cf5822d7096d4d17ad781c90f97c745ac13a22be619db74966fba45fda`).

### Current (incorrect) commit: `f7f4608`

The commit hash was changed from `929c7d5` to `f7f4608` by the "[Batch 1/4] port info from fontc_crater targets list" commit (`19cdcec5`, 2025-03-31). This batch operation ported commit hashes from fontc_crater's `targets.json`, which tracks the latest upstream HEAD for building/testing purposes, not the original onboarding commits.

Commit `f7f4608` is dated 2024-07-30, over two years after the onboarding. At this commit, the `fonts/variable/` directory no longer exists (it was removed in commit `8ec0279` on 2024-03-29), which means the `files` block in METADATA.pb (which references `fonts/variable/AlbertSans[wght].ttf`) is now inconsistent with the referenced commit.

### Recommendation

The commit hash should be reverted to `929c7d5058afd06870d1dd4ebc3a0ee98bb77420`, which is the verified original onboarding commit. This restores consistency between the commit hash, the file mappings, and the actual font binaries in google/fonts.

## How Config YAML Was Resolved

The upstream repo has `sources/config.yaml` present at both commits, but with different content:

- **At `929c7d5` (onboarding)**: A more detailed config with source file references (`AlbertSans.glyphs`, `AlbertSans-Italic.glyphs`), axis order (`wght`, `ital`), family name, and full STAT table definitions.
- **At `f7f4608` (current HEAD)**: A simpler config referencing renamed source files (`AlbertSans-Roman.glyphs`, `AlbertSans-Italic.glyphs`) with axis order (`wght`, `wdth`) and no STAT table.

The `config_yaml: "sources/config.yaml"` field in METADATA.pb is valid for either commit. No override config.yaml is needed since the upstream repo provides one.

## Detailed Timeline

| Date | Event |
|------|-------|
| 2022-06-03 | Upstream commit `929c7d5` ("fonts folder") - adds compiled variable fonts |
| 2022-06-16 | PR #4756 merged in google/fonts by Emma Marichal, onboarding Albert Sans v1.025 from commit `929c7d5` |
| 2024-04-03 | Commit `66f91f1` by Simon Cozens merges upstream.yaml into METADATA.pb, adding `files`, `branch` fields (commit hash unchanged at `929c7d5`) |
| 2024-03-29 | Upstream commit `8ec0279` removes the `fonts/` directory entirely |
| 2024-07-30 | Upstream commit `f7f4608` (current HEAD) - source file updates |
| 2025-03-31 | Batch 1/4 commit `19cdcec5` changes commit hash from `929c7d5` to `f7f4608` and adds `config_yaml` field |

## Conclusion

**Status**: needs_correction
**Confidence**: HIGH

The repository URL is correct. The `config_yaml` path (`sources/config.yaml`) is valid. However, the commit hash `f7f4608` currently in METADATA.pb is incorrect -- it was introduced by a batch import from fontc_crater targets and represents the latest upstream HEAD, not the original onboarding commit.

The correct onboarding commit is `929c7d5058afd06870d1dd4ebc3a0ee98bb77420`, confirmed by:
1. The explicit reference in the PR #4756 commit message
2. Binary file hash verification (exact SHA-256 match)
3. The `fonts/variable/` directory existing at `929c7d5` but not at `f7f4608`, making the current `files` block inconsistent

The commit hash should be reverted to `929c7d5`. Note that the `config_yaml` field is valid at both commits, so it can remain as-is.
