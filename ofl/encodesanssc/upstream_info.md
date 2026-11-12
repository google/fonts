# Investigation Report: Encode Sans SC

## Family Details
- **Family name**: Encode Sans SC
- **Designer**: Impallari Type, Andres Torresi, Jacques Le Bailly
- **License**: OFL
- **Category**: SANS_SERIF
- **Date added**: 2020-06-24
- **METADATA.pb path**: `ofl/encodesanssc/METADATA.pb`

## Source Repository
- **Repository URL**: https://github.com/thundernixon/Encode-Sans
- **Verified**: Yes (matches METADATA.pb `repository_url`)
- **Upstream cache**: `thundernixon/Encode-Sans`

## Upstream Repository Details

The upstream repository (`thundernixon/Encode-Sans`) is Stephen Nixon's fork/upgrade of the original Encode Sans project by Pablo Impallari. It contains both Encode Sans and Encode Sans SC variants, built from a single `.glyphs` source.

### Commit Analysis
- **Only commit in repo**: `6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc` (2020-06-24) - "build v3.002 with fixed static names"
- **Branch**: `master`
- **Repo status**: Clean, up to date with origin

### Binary Verification
The font file `EncodeSansSC[wdth,wght].ttf` in google/fonts matches the upstream repo exactly:
- **File size**: 217,392 bytes (both)
- **SHA256**: `fcad22c3440992bf42216e6a0ad6e8640d2d1dfff1ddc5573934933152123bd0` (both)
- **Conclusion**: Binary match confirmed. The font in google/fonts was taken directly from the upstream repo's `fonts/EncodeSansSC/` directory.

## Onboarding History

### google/fonts commit history for `ofl/encodesanssc/`:
1. `a13d629c8` (2021-03-25) - "encodesanssc: v3.002 added. (#2439)" -- Initial onboarding by Stephen Nixon (thundernixon), co-authored by Rosalie Wagner
2. `d0623a232` - "Fix incorrect file permissions"
3. `70b0fc8a8` - "Remove static fonts for unhinted variable font families (#3695)"
4. `cd5db6b6e` (2023-12-14) - "Update upstreams" by Simon Cozens -- Added the `source { repository_url }` block to METADATA.pb

### PR #2439 (onboarding)
- **Author**: Stephen Nixon (thundernixon)
- **Related to**: PR #2438 (Encode Sans VF, the non-SC variant)
- **Description**: Adds the small caps (SC) version of Encode Sans as a variable font
- **Process**: Fonts were generated from the `Encode-Sans.glyphs` source using a custom build script that:
  1. Builds the variable font with `fontmake`
  2. Freezes the `smcp` feature into the font using `pyftfeatfreeze`
  3. Subsets out replaced lowercase glyphs
  4. Applies name table fixes and various post-processing

## Source Files
- **Primary source**: `sources/Encode-Sans.glyphs` (shared with Encode Sans)
- **Source format**: GlyphsApp (.glyphs)
- **No `.designspace` or `.ufo` files** -- only `.glyphs`

## Config.yaml Status

### Upstream repo
- **No `config.yaml` found** in the upstream repository
- The build process uses custom shell scripts (`sources/scripts/build.sh`, `sources/scripts/build-vf.sh`) with `fontmake` and extensive post-processing

### google/fonts family directory
- **No `config.yaml`** in `ofl/encodesanssc/`

### Config.yaml Feasibility
Creating a standard gftools-builder `config.yaml` for Encode Sans SC is **not straightforward**. The SC variant requires a multi-step build process:
1. Build the base Encode Sans VF with fontmake from the `.glyphs` source
2. Freeze the `smcp` OpenType feature into the font (pyftfeatfreeze)
3. Subset out replaced lowercase glyphs and unnecessary ligatures
4. Apply custom name table fixes
5. Add STAT table, fix DSIG/GASP, remove MVAR table

This pipeline goes well beyond what a simple `config.yaml` with gftools-builder can express. A config.yaml could only handle step 1 (building the base VF from sources); the SC-specific post-processing steps would require additional tooling.

## Commit Hash for METADATA.pb
- **Commit**: `6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc`
- **Confidence**: HIGH
- **Reasoning**: The repo has only one commit. Binary SHA256 hashes match exactly between the upstream repo and google/fonts. The commit date (2020-06-24) aligns with the project timeline (PR #2439 was created around the same time, merged later on 2021-03-25).

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/thundernixon/Encode-Sans"
}
```

## Recommended METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/thundernixon/Encode-Sans"
  commit: "6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc"
}
```

Note: `config_yaml` is omitted because no standard gftools-builder config exists. The SC variant's custom build pipeline (feature freezing + subsetting) cannot be expressed in a simple config.yaml.

## Summary
- **Status**: missing_config (but config.yaml creation is not straightforward due to custom SC build process)
- **Repository URL**: Correct, verified
- **Commit hash**: `6407de8` (HIGH confidence -- single commit in repo, binary match confirmed)
- **Config.yaml**: Not available; custom build pipeline required for SC variant
- **Action needed**: Add `commit` field to source block in METADATA.pb. Config.yaml creation would require either gftools-builder enhancements or a creative workaround for the feature-freeze + subset pipeline.
