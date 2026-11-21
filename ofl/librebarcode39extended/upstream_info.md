# Investigation Report: Libre Barcode 39 Extended

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Family**: Libre Barcode 39 Extended
**Slug**: librebarcode39extended
**Designer**: Lasse Fister
**License**: OFL
**Date Added**: 2017-08-21

## Summary

Libre Barcode 39 Extended is part of the Libre Barcode family of fonts by Lasse Fister (graphicore). The fonts are generated using a custom Node.js build system rather than traditional font sources (.glyphs, .ufo, .designspace). The repository contains JavaScript code that programmatically constructs barcode font glyphs. The current binary in google/fonts was taken from the upstream repository at commit `f9864c4` via gftools-packager in PR #2911 (merged 2021-02-03), and the binary matches the upstream exactly.

## Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Branch**: master
- **Status**: Clean, up to date with origin

The repository is a monorepo containing multiple Libre Barcode font variants: Code 39, Code 39 Extended, Code 39 Text, Code 39 Extended Text, Code 128, Code 128 Text, and EAN-13 Text.

## Build System

This project uses a **custom Node.js-based build system**, not gftools-builder. The build infrastructure is located in `app/`:

- `app/bin/build` - Node.js script that creates barcode fonts by codetype (Code128 or Code39)
- `app/bin/buildAll` - Bash script that builds all variants
- `app/lib/builder/` - JavaScript builder modules (`abstract.js`, `code39.js`, `code39Extended.js`, `code128.js`, `ean13.js`)

The builder programmatically generates UFO font data from barcode specifications and then compiles them. No traditional font source files (.glyphs, .ufo, .designspace, .sfd) exist in the repository. Pre-built binaries are committed to the `fonts/` directory.

**No config.yaml is possible**: Since the project does not use gftools-builder and has no traditional font sources, a gftools-builder config.yaml cannot be created. An override config.yaml is also not applicable.

## Commit Hash Verification

### METADATA.pb source block (current)

```
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcode39Extended-Regular.ttf"
    dest_file: "LibreBarcode39Extended-Regular.ttf"
  }
  branch: "master"
}
```

The source block has the repository URL, file mappings, and branch, but **no commit hash** is recorded in the current METADATA.pb.

### Tracking data

The tracking JSON (`data/gfonts_library_sources.json`) records commit `f9864c42b2c467f255659c8851c124e4cd56c67a` which was referenced in PR #2911.

### Referenced commit: `f9864c4` (2020-12-16)

PR #2911 (merged 2021-02-03) stated the font was "taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a."

This commit (`f9864c4`) has the message "[ean13] bump version add binary v1.008; updates copyright srting to include 2020" and only modified `fonts/LibreBarcodeEAN13Text-Regular.ttf` and `app/bin/buildAll`. It did **not** modify `LibreBarcode39Extended-Regular.ttf`.

### Actual commit for the binary: `63e8744` (2020-12-16)

The commit that actually added the `fonts/LibreBarcode39Extended-Regular.ttf` binary (v1.005, 17396 bytes) was `63e8744e4154bec00d3d9da4b9e9286f41f1c030` with message "[code39/128] add binaries v1.005", made just one minute earlier on the same day (2020-12-16 01:39:13 vs 01:40:33).

### Binary verification

The SHA-256 checksums of the binary files matched exactly:
- google/fonts: `4fd24568bda30f28cf430f5a9ba2aa3fcce3677e08f306edf30ab42fd6187535`
- upstream (at HEAD): `4fd24568bda30f28cf430f5a9ba2aa3fcce3677e08f306edf30ab42fd6187535`

The binary was not modified after commit `63e8744`. Since `f9864c4` is one commit after `63e8744` and the binary is unchanged between them, both commits contain the same binary. Using `f9864c4` (as gftools-packager recorded) is acceptable since the font file is identical at both commits.

### Commits after `f9864c4` in upstream

Only two commits exist after the referenced commit:
- `93bb140` (2022-05-02): "[ean 13] Add bulk encoder as requested in #52"
- `e44a85e` (2024-06-25): "Fixes #64; Wrong variable used; Use const instead of var"

Neither of these modified the LibreBarcode39Extended-Regular.ttf binary.

## google/fonts History

| Date | Commit | Description |
|------|--------|-------------|
| 2017-08-21 | `b2f4c900c` | Initial onboarding via PR #1145 (by Dave Crossland) |
| 2017-09-11 | `e79aa1803` | Updated to v1.002 via PR #1182 |
| 2017-10-18 | `f4c49a299` | Updated to v1.003 via PR #1228 |
| 2021-02-03 | `22df91c23` | Updated to v1.005 via PR #2911 (by Lasse Fister via gftools-packager) |
| 2026-02-25 | `9a14639f3` | Source block added to METADATA.pb |

## Status Assessment

- **Repository URL**: Correct (https://github.com/graphicore/librebarcode)
- **Commit hash**: `f9864c42b2c467f255659c8851c124e4cd56c67a` is the commit recorded by gftools-packager. The actual binary was added in the immediately preceding commit `63e8744`, but `f9864c4` contains the identical binary. The gftools-packager reference is acceptable.
- **Config**: Not applicable. The project uses a custom Node.js build system, not gftools-builder. No config.yaml can be created.
- **Branch**: master (correct)
- **Status**: **complete** (no config.yaml possible due to custom build system)
- **Confidence**: **HIGH**

## Recommendation

The source block in METADATA.pb should have a `commit` field added with the value `f9864c42b2c467f255659c8851c124e4cd56c67a` to match what gftools-packager recorded. No config.yaml is needed or possible since the project uses a custom JavaScript-based font generation system rather than traditional font sources with gftools-builder.
