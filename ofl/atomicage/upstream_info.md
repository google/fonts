# Atomic Age

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: James Grieshaber
**METADATA.pb path**: `ofl/atomicage/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EbenSorkin/Atomic-Age |
| Commit | `bb96b179ca5c48149011237c64781fa94817e711` |
| Config YAML | — |
| Branch | — |

## How the Repository URL Was Found

The repository URL is already present in the METADATA.pb source block on the main branch, added by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)", 2024-01-14).

## How the Commit Hash Was Identified

The commit `bb96b179ca5c48149011237c64781fa94817e711` is the latest commit in the upstream repository (2016-01-16, "Merge pull request #3 from davelab6/master"). This is the head of the repo.

The font was last updated in google/fonts via PR #830 (`89276381`, "hotfix-atomicage: v1.008 added", 2017-08-07) by Marc Foley. The hotfix claims v1.008, but the upstream repo only contains up to v1.007 (commit `5e7452c`, "Updating to v1.007 (vertical metrics)", 2016-01-15). This suggests the v1.008 hotfix was done directly on the binary font file (likely vertical metrics adjustments) without corresponding upstream source changes. The PR #830 body and comments are empty, providing no further details.

The repo has 14 total commits, with the most recent being from January 2016. The repo appears to be inactive.

## How Config YAML Was Resolved

No `config.yaml` or `builder.yaml` exists in the upstream repository. No override `config.yaml` exists in `google/fonts/ofl/atomicage/`.

The only source file in the repo is a VFB (FontLab) binary: `SRC/AtomicAge-Regular.vfb`. The original UFO was created and then removed (commit `7190e2a`, "Remove UFO"). VFB files are proprietary FontLab format and cannot be used with gftools-builder.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2016-01-16 23:13:27 -0500
- Commit message: "Merge pull request #3 from davelab6/master"
- Source files at commit:
  - `SRC/AtomicAge-Regular.vfb` (FontLab binary, not gftools-compatible)
  - `fonts/ttf/AtomicAge-Regular.ttf` (pre-compiled binary)
  - `fonts/otf/AtomicAge-Regular.otf` (pre-compiled binary)

## Confidence

**Medium**: The repository URL is confirmed in METADATA.pb. The commit hash is the latest commit, which is a reasonable default since the repo predates the google/fonts hotfix. However, the v1.008 hotfix in google/fonts does not correspond to any upstream commit, indicating the binary was modified directly. The VFB-only source means this family cannot be built with gftools-builder without source conversion.

## Open Questions

- The google/fonts version is v1.008 but the upstream only has v1.007. The v1.008 changes appear to be direct binary modifications (copyright and metadata updates per the METADATA.pb diff). Should the commit hash reference the latest upstream commit even though the actual binary diverges?
- The VFB source would need to be converted to UFO or .glyphs format before a config.yaml could be useful. Is there a plan to convert the sources?
