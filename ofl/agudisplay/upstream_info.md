# Agu Display

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Seun Badejo
**METADATA.pb path**: `ofl/agudisplay/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/theseunbadejo/Agu-Display |
| Commit | `d520ebead8de4091a82040fe3d8f94d84c38c66f` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/theseunbadejo/Agu-Display` was already present in the METADATA.pb source block from the original onboarding commit `6913b39` (2024-11-25), authored by Nathan Willis. The commit message explicitly states: "Taken from the upstream repo https://github.com/theseunbadejo/Agu-Display". The copyright string in METADATA.pb also references this same URL. The cached repo remote confirms the URL is correct.

## How the Commit Hash Was Identified

**Important discrepancy noted**: The original onboarding commit (`6913b39`, dated 2024-11-25) referenced commit `17a7ce91583f40d9e8f21eab6c57870a59c1b668` in both the commit message and the original METADATA.pb. However, this commit hash no longer exists in the upstream repo.

The upstream repo currently contains only a single commit: `d520ebead8de4091a82040fe3d8f94d84c38c66f` (dated 2025-02-10), which is a merge of PR #35 ("Update build.yaml to restore actions"). This commit appears to be the result of a force-push that squashed all prior history into a single commit. Evidence:
- The `--stat` of this commit shows 55 files added (entire repo contents), indicating it is an initial/squashed commit
- No other commits exist in the repo (`git log --all` shows only this one commit)
- The commit date (2025-02-10) is AFTER the google/fonts onboarding date (2024-11-25)

The current commit hash `d520ebe` was set by the "[Batch 1/4] port info from fontc_crater targets list" commit (`19cdcec`, 2025-03-31), which imported data from fontc_crater's `target.json`. Since the original commit `17a7ce9` no longer exists in the repo, `d520ebe` (the only existing commit, containing the full repo contents) is the best available reference. The source files and config at this commit match what would have been used for the original build.

## How Config YAML Was Resolved

The file `sources/config.yaml` exists at commit `d520ebe` in the upstream repo and contains valid gftools-builder configuration:

```yaml
sources:
  - AguDisplay.glyphs
axisOrder:
  - morf
familyName: Agu Display
autohintOTF: False
stat:
  - name: Morph
    tag: MORF
    values:
    - name: Uzo
      value: 0
    - name: Ala
      value: 30
    - name: Osisi
      value: 60
```

The source file `sources/AguDisplay.glyphs` (3.1 MB) is present at this commit. The `config_yaml` field was added to METADATA.pb by the Batch 1/4 commit. No override config.yaml exists in the google/fonts family directory.

## Additional Notes

- **Archive URL**: The `archive_url` points to a GitHub release: `https://github.com/theseunbadejo/Agu-Display/releases/download/1.05/Agu-Display-1.05.zip`. The `files` entries in the source block reference paths within this archive (e.g., `fonts/variable/AguDisplay[MORF].ttf`), not paths in the git repo (no `fonts/variable/` directory exists in the repo itself).
- **Variable axis**: The font has a custom `MORF` (Morph) axis with range 0-60.
- **Minisite**: The font has a dedicated minisite at https://www.agudisplay.com.
- **Date added**: 2024-11-14.
- **Onboarding engineer**: Nathan Willis (commit `6913b39`).
- **Repository history anomaly**: The upstream repo was apparently force-pushed/rebased after onboarding, losing the original commit `17a7ce9`. The current single commit (`d520ebe`) contains the complete repo contents including all source files, so it is functionally equivalent for build purposes.

## Conclusion

The source block is **complete** with all required fields: repository URL, commit hash, branch, config_yaml path, archive_url, and file mappings. While the original onboarding commit `17a7ce9` no longer exists in the repo due to a force-push, the current commit `d520ebe` contains the same source files and config needed for building. The config.yaml in the upstream repo is valid and correctly referenced. **Confidence: HIGH** for repository URL and config; **MEDIUM** for commit hash (original hash lost due to force-push, current hash is the only available reference but post-dates the onboarding).
