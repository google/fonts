# Investigation Report: Libre Barcode 128 Text

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family**: Libre Barcode 128 Text
**Designer**: Lasse Fister
**Directory**: `ofl/librebarcode128text`
**Status**: complete (no config.yaml applicable)
**Confidence**: HIGH

## Summary

Libre Barcode 128 Text is a barcode font from the Libre Barcode project by Lasse Fister. The upstream repository uses a fully custom build pipeline (JavaScript/Node.js generates UFO sources programmatically, then fontmake compiles them to TTF). This architecture is fundamentally incompatible with gftools-builder, so no `config.yaml` is applicable. The source block in METADATA.pb already contains the correct repository URL and commit hash.

## Upstream Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Branch**: master
- **Local cache**: `upstream_repos/fontc_crater_cache/graphicore/librebarcode`
- **Repo status**: Clean, up to date with remote

## Source Block (Current)

The METADATA.pb source block contains:
```
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  commit: "f9864c42b2c467f255659c8851c124e4cd56c67a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcode128Text-Regular.ttf"
    dest_file: "LibreBarcode128Text-Regular.ttf"
  }
  branch: "master"
}
```

The `repository_url`, `commit`, and `branch` fields were added by commit `9a14639f3` on 2026-02-25 (source block enrichment batch). The `files` and `branch` fields originated from the upstream.yaml that was merged into METADATA.pb by commit `66f91f10f`.

## Commit Hash Verification

The commit hash `f9864c42b2c467f255659c8851c124e4cd56c67a` was referenced in PR #2914 by gftools-packager:

> "Libre Barcode 128 Text Version 1.005; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a."

**Cross-verification**:
- Commit `f9864c4` (2020-12-16) is titled "[ean13] bump version add binary v1.008" and only modifies EAN13 files
- The actual commit that added the Code 128 Text binary (v1.005) was `63e8744` (2020-12-16, one minute earlier)
- However, the font binary `fonts/LibreBarcode128Text-Regular.ttf` is byte-identical at both commits (SHA-256: `0e8a268749e77c8bf1644a19cdd65e83af6486bcadc06225e486cdf569d58f58`)
- The binary in google/fonts matches exactly (same hash, same size: 48,056 bytes)
- `f9864c4` was the HEAD of master when the PR was created on 2020-12-16, so it correctly represents the state of the repo at the time

**Conclusion**: The commit hash `f9864c4` is valid. It was the latest commit when the font was taken from upstream, and the Code 128 Text binary is unchanged between `63e8744` and `f9864c4`.

## PR History in google/fonts

| PR | Date | Description |
|---|---|---|
| #1109 | 2017 | Initial addition of Libre Barcode families |
| #1145 | 2017 | Update and add Barcode fonts |
| #1182 | 2017 | Updated to v1.002 |
| #1228 | 2017 | Updated to v1.003 (add zwsp) |
| #2914 | 2020-12-16 (created), 2021-02-03 (merged) | Updated to v1.005 with ttfautohint |

PR #2914 was the last update. It was authored by Lasse Fister (graphicore) himself and used gftools-packager. The PR title mentions "ttfautohint (v1.8.3) added" but the binary in google/fonts is byte-identical to the upstream binary, indicating ttfautohint was part of the upstream build process (the `buildAll` script pipes output through gftools fix-font).

## Build System Analysis

The Libre Barcode project uses a completely custom build pipeline:

1. **Source generation**: JavaScript/Node.js code in `app/lib/builder.js` programmatically generates UFO source files. It uses `ufojs/ufoLib/UFOWriter` to create barcode glyphs algorithmically based on the Code 128 specification.

2. **Compilation**: The `app/bin/buildAll` bash script orchestrates the build:
   - Calls the Node.js builder to generate UFOs into a `sources/` directory
   - Runs `fontmake -u $UFO_DIR --keep-overlaps --keep-direction -a"--symbol" -o ttf`
   - Copies autohinted output to `fonts/`
   - Runs `gftools fix-font` on each TTF

3. **Key details**:
   - The `sources/` directory is in `.gitignore` and never committed
   - No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist in the repository
   - Dependencies: python3 (fontmake, gftools), node.js, npm, bower, ttfautohint
   - The build requires `requirements.txt` (fontmake, gftools, font-v)

4. **Why config.yaml is not applicable**: The gftools-builder config.yaml format expects static source files (.glyphs, .ufo, .designspace) as input. The Libre Barcode project generates its sources programmatically, making a standard config.yaml impossible. The pre-compiled binaries in the `fonts/` directory are what google/fonts consumes directly.

## Config Status

- **Upstream config.yaml**: None (not applicable - custom build system)
- **Override config.yaml**: Not applicable
- **config_yaml in METADATA.pb**: Not needed (binary fonts are taken directly from upstream `fonts/` directory)

## Upstream Activity After Recorded Commit

Two commits exist after `f9864c4`:
- `93bb140` (2022-05-02): "[ean 13] Add bulk encoder as requested in #52" - EAN13 encoder change, does not affect Code 128 Text
- `e44a85e` (2024-06-25): "Fixes #64; Wrong variable used" - JavaScript fix, does not affect font binaries

The font binary `LibreBarcode128Text-Regular.ttf` has not been modified since commit `63e8744` (2020-12-16).

## Conclusion

The source block is correct and complete for this family's needs:
- **repository_url**: Correct (https://github.com/graphicore/librebarcode)
- **commit**: Correct (`f9864c4` - verified by binary hash comparison)
- **branch**: Correct (master)
- **config_yaml**: Not applicable (custom build system generates sources programmatically)

No changes are needed. The status should be updated from "missing_config" to "no_config_needed" or equivalent, reflecting that this family's custom build pipeline cannot use gftools-builder.
