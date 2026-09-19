# Investigation: Libre Barcode 39 Extended Text

**Family Name**: Libre Barcode 39 Extended Text
**Directory**: `ofl/librebarcode39extendedtext`
**Designer**: Lasse Fister
**Date Added**: 2017-08-21
**Date Investigated**: 2026-03-03
**Model**: Claude Opus 4.6

## Summary

| Field | Value |
|---|---|
| Repository URL | `https://github.com/graphicore/librebarcode` |
| Commit Hash | `f9864c42b2c467f255659c8851c124e4cd56c67a` |
| Config YAML | none (custom JS build system) |
| Status | complete |
| Confidence | HIGH |

## METADATA.pb Current State

The source block in METADATA.pb already contained:
- `repository_url`: `https://github.com/graphicore/librebarcode`
- `commit`: `f9864c42b2c467f255659c8851c124e4cd56c67a`
- `branch`: `master`
- `files` mapping for `OFL.txt` and `fonts/LibreBarcode39ExtendedText-Regular.ttf`

The repository URL was present from the upstream.yaml merge (commit `66f91f10f`). The commit hash was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). No `config_yaml` field was set.

## Upstream Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Owner**: graphicore (Lasse Fister)
- **Cached at**: `upstream_repos/fontc_crater_cache/graphicore/librebarcode`
- **Default branch**: `master`
- **Status**: Clean, up to date with remote
- **Total commits**: 140

The repository hosts multiple Libre Barcode font families (Code 39, Code 39 Text, Code 39 Extended, Code 39 Extended Text, Code 128, Code 128 Text, and EAN13 Text) in a single monorepo.

## Build System

Libre Barcode uses a **custom Node.js/JavaScript build system**, not gftools-builder. The build pipeline works as follows:

1. **`app/bin/buildAll`** (bash script): Orchestrates the build for all barcode types. Calls a `configure` function for each target (CODE39, CODE39TEXT, CODE39EXTENDED, CODE39EXTENDEDTEXT, CODE128, CODE128TEXT, EAN13TEXT), then builds each.

2. **`app/bin/build`** (Node.js): The core builder that takes a code type and UFO output directory. It uses RequireJS to load `LibreBarcode/builder` which programmatically generates UFO sources via `ufojs/UFOWriter`.

3. **`app/lib/builder.js`** and `app/lib/builder/*.js`**: JavaScript modules that define barcode glyph generation logic for each code type (code39.js, code39Extended.js, code128.js, ean13.js).

4. The build process:
   - Generates UFO sources programmatically from JavaScript
   - Compiles UFOs to TTF using `fontmake` with `--keep-overlaps --keep-direction`
   - Applies `gftools fix-font` post-processing

This is fundamentally incompatible with gftools-builder/fontc, as the font sources are generated procedurally at build time rather than existing as static source files. There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files checked into the repository. A `config.yaml` is therefore not applicable.

## Commit Hash Verification

### Referenced Commit
- **Hash**: `f9864c42b2c467f255659c8851c124e4cd56c67a`
- **Date**: 2020-12-16
- **Author**: Lasse Fister
- **Message**: "[ean13] bump version add binary v1.008; updates copyright srting to include 2020."

### Provenance

The commit hash was explicitly recorded by gftools-packager in PR [#2912](https://github.com/google/fonts/pull/2912), the most recent update to this font family:

> "Libre Barcode 39 Extended Text Version 1.005; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a."

PR #2912 was authored by Lasse Fister (graphicore) himself and merged on 2021-02-03.

### Binary Verification

The font binary `LibreBarcode39ExtendedText-Regular.ttf` was compared across three sources:

| Source | MD5 Hash |
|---|---|
| google/fonts (current) | `0c4d0eb4d8ec5f630280c3e582a19b7b` |
| Upstream at `f9864c4` | `0c4d0eb4d8ec5f630280c3e582a19b7b` |
| Upstream at `63e8744` | `0c4d0eb4d8ec5f630280c3e582a19b7b` |

All three match. The binary was actually added to the upstream repo in commit `63e8744` ("[code39/128] add binaries v1.005", 2020-12-16), and `f9864c4` (one minute later) only modified the EAN13 binary. Both commits were part of the same v1.005 release session.

### Post-Merge Activity

After the google/fonts merge date (2021-02-03), only two commits were made to the upstream repo:
- `93bb140` (2022-05-02): "[ean 13] Add bulk encoder as requested in #52"
- `e44a85e` (date unknown): "Fixes #64; Wrong variable used"

Neither of these commits modified any font binaries in the `fonts/` directory.

## Google Fonts History

| Date | Commit | Description |
|---|---|---|
| 2017-08-21 | `b2f4c900c` | Initial onboarding via PR [#1145](https://github.com/google/fonts/pull/1145) (by Dave Crossland) |
| 2017 | `e79aa1803` | Update to v1.002 via PR [#1182](https://github.com/google/fonts/pull/1182) |
| 2017 | `f4c49a299` | Update to v1.003 (add zwsp) via PR [#1228](https://github.com/google/fonts/pull/1228) |
| 2021-02-03 | `d6d517e00` | Update to v1.005 via PR [#2912](https://github.com/google/fonts/pull/2912) (most recent) |

## Conclusion

The source metadata for Libre Barcode 39 Extended Text was already correctly populated in METADATA.pb. The commit hash `f9864c42` was verified through:
1. Explicit gftools-packager recording in PR #2912
2. Binary MD5 hash match across google/fonts and the upstream commit
3. Confirmation that no font binary changes occurred in upstream after this commit

No config.yaml is applicable because the project uses a custom JavaScript build system that programmatically generates UFO sources, making it incompatible with gftools-builder. No changes to METADATA.pb are needed.
