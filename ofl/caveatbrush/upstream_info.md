# Caveat Brush

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Impallari Type (Pablo Impallari)
**METADATA.pb path**: `ofl/caveatbrush/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/caveat |
| Commit | `59745e818ef7973e11e70cb1358d0e902b56c5fc` |
| Config YAML | -- |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/caveat` was added to METADATA.pb by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on 2024-01-14 as part of PR #7159. Caveat Brush shares its upstream repository with the Caveat family. Both fonts were designed by Pablo Impallari. The upstream repo contains a dedicated source file `sources/Caveat-Brush.glyphs` for Caveat Brush alongside the Caveat designspace sources.

## How the Commit Hash Was Identified

**The METADATA.pb currently has no commit hash in the source block.** The tracking JSON previously recorded commit `7fb0cea`, which is the very first commit in the repo (2015-10-07) containing only a README.md -- this was incorrect and had no source files at all.

The recommended commit is `59745e818ef7973e11e70cb1358d0e902b56c5fc` (2020-08-23, "Fix /Ldot /ldot /AE /OE and new build.sh" by Jill Pichotta). This is the HEAD of the main branch and the same commit used for the Caveat family's source block. At this commit, `sources/Caveat-Brush.glyphs` exists and contains the most current version of the Brush source.

### Important context about the binary vs. source mismatch

The Caveat Brush binary currently in Google Fonts (`CaveatBrush-Regular.ttf`, version 1.096) was added by Dave Crossland on 2015-09-18 (google/fonts commit `b05d7ed92`) and has **never been updated since**. This binary predates the upstream repo's first commit (2015-10-07).

The `Caveat-Brush.glyphs` source was only added to the repo on 2017-09-01 by Marc Foley (commit `527fdc2`, "Added vfb conversion for Caveat Brush. Source provided by @davelab6"). The same day, a README note was added (commit `09182d3`) stating: **"Sources for Caveat Brush are not the latest. Source is kept in sources/wip until it is located."**

The source file was subsequently moved through several directory reorganizations but its content has remained identical (MD5: `21ab4ab9a53eda521b7dd2c9de36944b`) across all commits since `d0e25e0`.

Timeline:
1. **2015-09-18**: Binary added to google/fonts by Dave Crossland (compiled from VFB source outside git)
2. **2015-10-07**: First commit in upstream repo -- README only (`7fb0cea`)
3. **2017-09-01**: Marc Foley added .glyphs conversion of Brush source (`527fdc2`), then moved it to `sources/wip/` with a note that it's "not the latest" (`09182d3`)
4. **2020-08-21**: Denis Moyogo Jacquerye moved it from `source glyphs/wip/` to `sources/` (`38fd0ee`)

## How Config YAML Was Resolved

There is **no config.yaml** in the upstream repository. The existing `sources/build.sh` only builds Caveat (from the .designspace), not Caveat Brush. No override `config.yaml` exists in `ofl/caveatbrush/` in google/fonts either.

An override config.yaml could be created for gftools-builder using the `sources/Caveat-Brush.glyphs` file, but this would produce a rebuilt font that may differ from the current binary. Building from the existing .glyphs source would require QA review since the source is acknowledged as potentially not matching the original binary.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2020-08-23 22:27:34 -0400
- Commit message: "Fix /Ldot /ldot /AE /OE and new build.sh"
- Source files at commit:
  - `sources/Caveat-Brush.glyphs` (57,509 lines, single-master Glyphs format)
  - `sources/Caveat.designspace` (Caveat family, not Brush)
  - `sources/Caveat-Regular.ufo`
  - `sources/Caveat-Bold.ufo`
  - `sources/build.sh` (builds Caveat only)

## Additional Notes

- The font binary has never been rebuilt since its 2015 onboarding
- The upstream repo README explicitly states: "Sources for Caveat Brush are not the latest"
- Copyright discrepancy: METADATA.pb says "Copyright 2015 Google Inc." while the Caveat family says "Copyright 2014 The Caveat Project Authors"
- The original VFB source used to compile the binary was provided by Dave Crossland and may not be available in any public repository

## Confidence

**MEDIUM**: The repository URL is correct -- the Caveat Brush source file exists in the googlefonts/caveat repo. The recommended commit (`59745e8`) is the HEAD of main where the source is in its final location. However, the source is explicitly noted as potentially not matching the binary currently served by Google Fonts, and there is no config.yaml for building it. If the font were to be rebuilt from the current source, it would need QA review as a new version rather than a reproduction of the original.
