# ADLaM Display

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Mark Jamra, Neil Patel, Andrew Footit
**METADATA.pb path**: `ofl/adlamdisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/microsoft/ADLaM-Display |
| Commit | `879176243e9f7161a8aefdab8c36a4a7318ebe15` |
| Config YAML | `Sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/microsoft/ADLaM-Display` was already present in METADATA.pb. It was originally added by the gftools-packager onboarding commit `40699510e` (2023-07-10), which explicitly states in its commit body: "taken from the upstream repo https://github.com/microsoft/ADLaM-Display". The remote URL of the cached repo at `fontc_crater_cache/microsoft/ADLaM-Display` confirms this matches `https://github.com/microsoft/ADLaM-Display`.

Note: The user's initial prompt mentioned `nicholasko/ADLaM-Display` as a possible alternative, but the METADATA.pb contains `microsoft/ADLaM-Display` and no `nicholasko` variant exists in the cache.

## How the Commit Hash Was Identified

The commit `879176243e9f7161a8aefdab8c36a4a7318ebe15` was verified through multiple sources:

1. **gftools-packager commit body** (commit `40699510e` in google/fonts, dated 2023-07-10): Explicitly references this commit hash with a direct link.
2. **Upstream repo verification**: The commit exists in the cached repo. It is the **only commit** in the entire repository, authored by "Aaron" on 2023-07-10, with message "Build". It is the initial commit creating the full repo contents (18 files, 76,624 insertions).
3. **Merge PR**: google/fonts PR #6522 merged on 2023-07-21, confirming the onboarding was completed shortly after the upstream commit date.

Since there is only one commit in the repo, there is no ambiguity about which commit was used for onboarding.

## How Config YAML Was Resolved

The file `Sources/config.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - ADLaM-Display.glyphs
familyName: "ADLaM Display"
buildOTF: false
```

This path was added to METADATA.pb in two steps:
1. Commit `19cdcec59` (2025-03-31, Batch 1/4) added `config_yaml: "sources/config.yaml"` (lowercase "s") ported from fontc_crater targets.
2. Commit `7190093b1` (2025-05-22) corrected the case to `config_yaml: "Sources/config.yaml"` (uppercase "S"), matching the actual directory name in the upstream repo.

The upstream repo has `.glyphs` source files in the `Sources/` directory, confirming gftools-builder compatibility.

## Conclusion

ADLaM Display has a fully complete source block in METADATA.pb. The repository URL, commit hash, branch, config_yaml path, and file mappings are all present and verified. The repository is hosted under the Microsoft organization on GitHub and contains a single commit that was used for the original onboarding via gftools-packager (google/fonts PR #6522, merged 2023-07-21). No further action is needed.
