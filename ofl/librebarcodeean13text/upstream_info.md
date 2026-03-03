# Investigation Report: Libre Barcode EAN13 Text

**Family Name**: Libre Barcode EAN13 Text
**Directory**: `ofl/librebarcodeean13text`
**Designer**: Lasse Fister
**Date Added**: 2020-10-26
**Model**: Claude Opus 4.6

## Summary

Libre Barcode EAN13 Text is a barcode font that encodes EAN-13 barcodes with human-readable text below. It is part of the Libre Barcode project by Lasse Fister (graphicore), which also includes Code 39, Code 39 Extended, and Code 128 variants. The font uses a custom JavaScript/Node.js build system that programmatically generates UFO sources from barcode specifications, then compiles them with fontmake. This is fundamentally different from the standard gftools-builder workflow and cannot be built with a `config.yaml`.

## Upstream Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Branch**: `master`
- **Shared repo**: This repository contains all seven Libre Barcode font families (39, 39 Text, 39 Extended, 39 Extended Text, 128, 128 Text, EAN13 Text)

## Source Block in METADATA.pb

The current METADATA.pb contains:

```
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  commit: "f9864c42b2c467f255659c8851c124e4cd56c67a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcodeEAN13Text-Regular.ttf"
    dest_file: "LibreBarcodeEAN13Text-Regular.ttf"
  }
  branch: "master"
}
```

The `repository_url`, `commit`, and `branch` fields are present. No `config_yaml` field is set.

## Commit Hash Verification

### Referenced commit: `f9864c42b2c467f255659c8851c124e4cd56c67a`

- **Date**: 2020-12-16
- **Message**: "[ean13] bump version add binary v1.008; updates copyright srting to include 2020."
- **Verification**: This is the last commit that modified `fonts/LibreBarcodeEAN13Text-Regular.ttf` in the upstream repo.

### Cross-verification with google/fonts

- **PR #2915**: "Libre Barcode EAN13 Text: Version 1.008; ttfautohint (v1.8.3) added"
  - Opened and authored by graphicore (Lasse Fister)
  - Merged by m4rc1e (Marc Foley) on 2021-02-03
  - PR body explicitly states: "taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a"

### Binary file verification

SHA-256 hash comparison confirmed that the binary in `google/fonts/ofl/librebarcodeean13text/LibreBarcodeEAN13Text-Regular.ttf` is byte-for-byte identical to the binary at `fonts/LibreBarcodeEAN13Text-Regular.ttf` in upstream commit `f9864c4`.

### Post-commit upstream activity

After commit `f9864c4` (2020-12-16), there were three additional commits on master:
1. `93bb140` (2022-05-02): "[ean 13] Add bulk encoder as requested in #52" -- documentation/web encoder changes only
2. `86c3ec5` / `e44a85e` (2024-06-25): "Fixes #64; Wrong variable used" -- JavaScript encoder fix only

None of these commits touched font binary files.

**Confidence**: HIGH -- The commit hash was stated by the upstream author himself in PR #2915, and the binary hash matches exactly.

## Build System Analysis

The Libre Barcode project uses a custom JavaScript/Node.js build pipeline:

1. **`app/bin/build`**: A Node.js script that takes a barcode type and UFO output directory as arguments. It uses RequireJS modules under `app/lib/builder/` to programmatically generate barcode glyph outlines based on barcode specifications (EAN-13, Code 128, Code 39).

2. **`app/bin/buildAll`**: A Bash script that orchestrates building all seven font variants. For EAN13 Text, it:
   - Configures parameters specific to EAN-13 (UPM=1024, module-based metrics, barcode height/drop settings)
   - Runs the Node.js builder to generate a UFO
   - Compiles with `fontmake -u ... --keep-overlaps --keep-direction -a"--symbol" -o ttf`
   - Post-processes with `gftools fix-font`

3. **Source files**: There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files in the repository. The "sources" are JavaScript modules (`app/lib/builder/ean13.js`, `app/lib/builder/abstract.js`) that generate UFO files at build time. The font also uses `app/assets/Inconsolata-Regular.ttf` as the text-below-barcode font.

4. **Dependencies**: `commander`, `fontkit`, `jsdom`, `libxmljs`, `requirejs`, and a custom fork of `commander.js`

This build system is incompatible with gftools-builder and cannot be represented by a `config.yaml` file. The font binary is committed directly to the upstream repository at `fonts/LibreBarcodeEAN13Text-Regular.ttf`.

## config.yaml Assessment

A `config.yaml` is **not applicable** for this family. The build system is entirely custom (JavaScript-based programmatic glyph generation). There are no standard font source files that gftools-builder could process. The pre-built binary is taken directly from the upstream repository.

## PR History in google/fonts

| PR | Title | Merged |
|----|-------|--------|
| #2771 | Libre Barcode EAN13 Text: Version 1.004; ttfautohint (v1.8.3) added | 2020-10-26 (initial onboarding) |
| #2850 | Libre Barcode EAN13 Text: Version 1.005; ttfautohint (v1.8.3) added | -- |
| #2852 | Libre Barcode EAN13 Text: Version 1.005; ttfautohint (v1.8.3) added | -- |
| #2860 | Libre Barcode EAN13 Text: Version 1.006; ttfautohint (v1.8.3) added | -- |
| #2891 | Libre Barcode EAN13 Text: Version 1.007; ttfautohint (v1.8.3) added | -- |
| #2915 | Libre Barcode EAN13 Text: Version 1.008; ttfautohint (v1.8.3) added | 2021-02-03 (latest) |

All PRs were authored by graphicore (Lasse Fister), the upstream developer himself.

## Current Status

- **Repository URL**: Verified (https://github.com/graphicore/librebarcode)
- **Commit hash**: Verified (`f9864c42b2c467f255659c8851c124e4cd56c67a`)
- **Branch**: `master` (confirmed)
- **config.yaml**: Not applicable (custom JS build system, no standard font sources)
- **Status**: **complete** (repository URL and commit hash are correct; config.yaml is not applicable)

## Conclusion

The source block for Libre Barcode EAN13 Text is complete and accurate. The repository URL and commit hash were both verified through PR history, the upstream author's own statements, and binary hash comparison. No `config.yaml` is needed or possible because the project uses a custom JavaScript build system that programmatically generates font files from barcode specifications. The pre-built binary is taken directly from the upstream repository.
