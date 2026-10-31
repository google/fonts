# Investigation Report: Faustina

## Family Overview

- **Family name**: Faustina
- **Designer**: Omnibus-Type (Alfonso Garcia)
- **License**: OFL
- **Category**: Serif
- **Date added**: 2016-12-03
- **Path in google/fonts**: `ofl/faustina`
- **Font files**: `Faustina[wght].ttf`, `Faustina-Italic[wght].ttf` (variable, wght axis 300-800)

## Upstream Repository

- **Repository URL**: https://github.com/Omnibus-Type/Faustina
- **Branch**: `master`
- **Commit**: `eaed5823e55b6256571a2bb379b5203083cab452` ("Bumping version again", 2021-09-02)
- **Source files**: `sources/Faustina.glyphs`, `sources/Faustina-Italic.glyphs`
- **Config file**: `sources/config.yaml`

## Source Block in METADATA.pb

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/Omnibus-Type/Faustina"
  commit: "eaed5823e55b6256571a2bb379b5203083cab452"
  files {
    source_file: "fonts/variable/Faustina[wght].ttf"
    dest_file: "Faustina[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Faustina-Italic[wght].ttf"
    dest_file: "Faustina-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation Details

### Font File History in google/fonts

The font files in google/fonts were last updated in commit `ce3ec5d1e` (PR #3806, "Faustina: Version 1.200 added", merged 2021-09-08 by Marc Foley). This commit was authored by Aaron Bell using gftools-packager. The commit message explicitly states:

> "Faustina Version 1.200 taken from the upstream repo https://github.com/Omnibus-Type/Faustina at commit https://github.com/Omnibus-Type/Faustina/commit/eaed5823e55b6256571a2bb379b5203083cab452."

Prior updates:
- `aa2a0f51` (2019-03-11): "faustina: v1.100 vf added" -- variable font first added
- `05fe8d84` (2017): "faustina: v1.006 added. (#498)" -- original static font onboarding

### Commit Hash Verification

The referenced commit `eaed5823e55b6256571a2bb379b5203083cab452` exists in the upstream repo. It is the only commit in the repository (shallow clone with depth 1, but also appears to be the HEAD of master). The commit message is "Bumping version again" with note "Looks like GF version is 1.1. so pushing this to 1.2.", dated 2021-09-02, by Aaron Bell.

This commit is the latest on master and predates the google/fonts merge date (2021-09-08), which is consistent with gftools-packager having used this exact commit.

### Binary File Verification

SHA256 hashes of the font files in google/fonts match exactly with those in the upstream repo at the referenced commit:
- `Faustina[wght].ttf`: `2ce2606f0ee1d493873c24818a391e02606ee76ac924b3d985cbb820c0a53ea5` -- **MATCH**
- `Faustina-Italic[wght].ttf`: `215b9bf63da0c9584b5a0aa8e2270da6a2b62c1281f5c39089613c3aaeffa2be` -- **MATCH**

The font binaries in google/fonts are identical to those in the upstream repository's `fonts/variable/` directory. This confirms that the fonts were taken directly from the upstream repo's pre-built binaries (not re-compiled).

### Config File Verification

The upstream repo contains `sources/config.yaml` with a valid gftools-builder configuration:
- Sources: `Faustina.glyphs`, `Faustina-Italic.glyphs` (relative to `sources/` directory)
- Axis order: `wght`
- Family name: `Faustina`
- STAT table entries defined for both upright and italic files

A `Makefile` in the repo root also references `gftools builder sources/config.yaml`, confirming this is the intended build configuration.

No override `config.yaml` exists in the google/fonts family directory.

### Source Block History in METADATA.pb

1. `66f91f10f` (2024-04-03, Simon Cozens): "Merge upstream.yaml into METADATA.pb" -- Added initial source block with `repository_url`, `files`, and `branch`, but without `commit` or `config_yaml`.
2. `f7455d788` (2023-08-15, Simon Cozens): "Populate source.repository_url" -- Added `repository_url` to METADATA.pb.
3. `19cdcec59` (2025-03-31, Felipe Sanches): "[Batch 1/4] port info from fontc_crater targets list" -- Added `commit` and `config_yaml` fields from fontc_crater's target.json.

## Status

- **Status**: Complete
- **Confidence**: HIGH
- **All fields verified**:
  - Repository URL: Confirmed valid (https://github.com/Omnibus-Type/Faustina)
  - Commit hash: Confirmed correct (`eaed5823e55b6256571a2bb379b5203083cab452`)
  - Config path: Confirmed exists at `sources/config.yaml` in upstream repo
  - Branch: `master` confirmed
  - Binary files: SHA256 match confirmed
- **No action needed**: The METADATA.pb source block is already complete and accurate.
