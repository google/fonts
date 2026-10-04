# Saira Stencil

**Status**: `complete`
**Date**: 2026-04-27
**Designer**: Hector Gatti, Omnibus-Type
**License**: OFL
**METADATA.pb**: `ofl/sairastencil/METADATA.pb`
**Model**: Claude Opus 4.7 (1M context)

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Saira_Stencil |
| Commit | `426fb33c0deade38404978462b01c09829003a17` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field. Confirmed canonical Omnibus-Type repo (default branch `main`, full history, no squash/rewrite).

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field; further confirmed by the body of onboarding commit `a4d1ba810` (Emma Marichal, 2026-03-20), which explicitly records: "Taken from the upstream repo https://github.com/Omnibus-Type/Saira_Stencil at commit https://github.com/Omnibus-Type/Saira_Stencil/commit/426fb33c0deade38404978462b01c09829003a17."

- Commit date: 2026-03-19 22:25:03 -0300
- Commit author: Omnibus-Type
- Commit subject: "Update README.md"
- Currently equal to `refs/heads/main` HEAD (no upstream activity since onboarding).

### Config YAML
Found at `sources/config.yaml` in the upstream repository at the recorded commit. Contains gftools-builder configuration (sources: `SairaStencil.glyphs`, `SairaStencil-Italic.glyphs`; axisOrder `wdth`, `wght`; full STAT table). Now referenced from METADATA.pb.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/Omnibus-Type/Saira_Stencil`
- `commit`: `426fb33c0deade38404978462b01c09829003a17`
- `branch`: `main`
- `config_yaml`: `sources/config.yaml` (added 2026-04-27 by this commit)

### google/fonts history
- Last font modification: `a4d1ba810` (Emma Marichal, 2026-03-20) "Saira Stencil: Version 1.101 added"
- Prior history: family was deleted in `877762234` (PR #2002) after the original `10053565d` v1.003 onboarding; the 2026-03 commit is a fresh re-onboarding via gftools-packager.

### Binary verification
fontTools confirms `nameID 5` = `Version 1.101` on both shipping VFs.
- md5 of upstream `fonts/variable/SairaStencil[wdth,wght].ttf` at `426fb33c0` = `79fb92d4d68e799c28f6bc96a0c30160` = shipping `ofl/sairastencil/SairaStencil[wdth,wght].ttf`.
- md5 of upstream `fonts/variable/SairaStencil-Italic[wdth,wght].ttf` at `426fb33c0` = `792184edde67f6e6059cf625819d107c` = shipping italic.

Byte-identical match — the recorded commit produces exactly the binaries currently shipping.

### Upstream repo archive
- Mirrored at `/home/fsanches/compartilhado/upstream_repos/repo_archive/Omnibus-Type/Saira_Stencil.git` (cloned 2026-04-27 by this investigation).
- 24 commits, full history retained, default branch `main`.
- HEAD of `main` is the recorded commit.

## Initial state
- METADATA.pb already contained a complete `source { ... }` block with repository_url, commit, file mappings, and `branch: main`.
- No `upstream_info.md` existed in the family directory.
- METADATA.pb was missing `config_yaml`, despite a usable `sources/config.yaml` in the upstream repo.

## Actions taken
- Verified Omnibus-Type/Saira_Stencil is the canonical upstream and that the repo has full (non-squashed) history.
- Verified recorded commit `426fb33c0` exists, equals `main` HEAD, and produces the exact binaries shipping in google/fonts (md5 match for both VFs).
- Confirmed gftools-builder `sources/config.yaml` is present at the recorded commit.
- Cloned upstream as bare mirror into the repo archive.
- Authored this `upstream_info.md`.
- Added `config_yaml: "sources/config.yaml"` to METADATA.pb source block.

## Final state
- `upstream_info.md` present with full provenance.
- METADATA.pb source block has `config_yaml: "sources/config.yaml"` set.
- No override `config.yaml` is required — upstream is gftools-builder ready.

## Recent upstream/main activity (post-investigation)

- **2026-03-20** — Emma Marichal, commit [`a4d1ba810`](https://github.com/google/fonts/commit/a4d1ba810) ("Saira Stencil: Version 1.101 added"): re-onboarded the family after its earlier deletion (PR #2002) via gftools-packager, sourced from `Omnibus-Type/Saira_Stencil@426fb33c0`. This is the version currently shipping. No upstream activity after that commit (recorded commit is HEAD of upstream `main`).

## Confidence

**High**: URL pre-existing in METADATA.pb; commit pre-existing in METADATA.pb and explicitly cited in onboarding commit body; binary md5 match against upstream confirms the recorded commit produced the shipping fonts.
