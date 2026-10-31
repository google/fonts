# Dosis

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Impallari Type
**METADATA.pb path**: `ofl/dosis/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dosis-vf |
| Commit | `3407d52f1d1b1c36c14e756ad0b36561d8d44a3b` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dosis-vf`. This URL is confirmed by the gftools-packager commit message in google/fonts PR #3821, which explicitly states the font was "taken from the upstream repo https://github.com/googlefonts/dosis-vf". The copyright string in the font files also references this URL ("Copyright 2011 The Dosis Project Authors (https://github.com/googlefonts/dosis-vf)").

The `dosis-vf` repo is a variable font rework of the original Dosis project by Pablo Impallari. The repo is under the `googlefonts` GitHub organization.

## How the Commit Hash Was Identified

The commit hash `3407d52f1d1b1c36c14e756ad0b36561d8d44a3b` was identified from the gftools-packager commit in google/fonts. The commit `59f86d8fc` (2021-09-10, PR #3821 by Aaron Bell) explicitly states: "Dosis Version 3.002 taken from the upstream repo https://github.com/googlefonts/dosis-vf at commit https://github.com/googlefonts/dosis-vf/commit/3407d52f1d1b1c36c14e756ad0b36561d8d44a3b."

This commit is the only commit in the upstream repository (which is a shallow clone in the local cache, but it is also the HEAD of the `master` branch). It is a merge commit by Marc Foley merging PR #18 from aaronbell/master ("Updated copyright string and fonts rebuilt"), dated 2021-09-09.

**Binary verification**: The SHA256 hash of `fonts/variable/Dosis[wght].ttf` at this upstream commit matches exactly with the file in `ofl/dosis/Dosis[wght].ttf` in google/fonts (`b2238eef0b3464904fed097ef274c704bc63d21407369b7d7a5be7b0821a0e82`). This confirms the font binary was taken directly from this commit.

## Build Configuration

The upstream repository has a valid gftools-builder `config.yaml` at `sources/config.yaml`:

```yaml
sources:
  - Dosis.glyphs
axisOrder:
  - wght
familyName: "Dosis"
```

The source file is `sources/Dosis.glyphs` (Glyphs format). No override config.yaml exists in the google/fonts family directory. The METADATA.pb correctly references this config file via `config_yaml: "sources/config.yaml"`.

## Timeline

- **2015-03-07**: Dosis initially added to google/fonts (initial commit) as static fonts (7 weights)
- **2018-10-23**: Variable font version 3.000 added by Eli Heuer (commit `fb60908eb`), replacing static fonts with `Dosis[wght].ttf`
- **2019-07-26**: Version 3.001 update by Marc Foley (commit `e08d7ee8b`)
- **2021-09-10**: Version 3.002 added by Aaron Bell (commit `59f86d8fc`, PR #3821) from upstream commit `3407d52` (current)

## Issues Found

None. The METADATA.pb source block is complete and accurate:
- Repository URL correctly points to `https://github.com/googlefonts/dosis-vf`
- Commit hash `3407d52` is verified via binary hash comparison
- Config YAML path `sources/config.yaml` exists in the upstream repo at the referenced commit
- Branch is correctly set to `master`
- File mappings for `Dosis[wght].ttf` and `OFL.txt` are correctly specified
