# Investigation Report: Libre Barcode 128

**Family Name**: Libre Barcode 128
**Directory**: `ofl/librebarcode128`
**Designer**: Lasse Fister
**Date Added**: 2017-07-31
**License**: OFL
**Model**: Claude Opus 4.6

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcode128-Regular.ttf"
    dest_file: "LibreBarcode128-Regular.ttf"
  }
  branch: "master"
}
```

The source block has `repository_url` and `branch` but is missing both `commit` and `config_yaml`.

## Upstream Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Owner**: graphicore (Lasse Fister)
- **Branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/graphicore/librebarcode`

This is a monorepo containing sources for multiple Libre Barcode font families: Code 39, Code 39 Text, Code 39 Extended, Code 39 Extended Text, Code 128, Code 128 Text, and EAN13 Text.

## Build System Analysis

The Libre Barcode project uses a **custom Node.js-based build system** that is fundamentally different from standard font workflows:

1. **No static font sources exist** in the repository. There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files checked in.
2. The build script (`app/bin/buildAll`) uses a Node.js application (`app/bin/build`) that programmatically generates UFO files from JavaScript code in `app/lib/builder/` (specifically `code128.js` for this family).
3. The generated UFO files are then compiled to TTF using `fontmake`.
4. The build script deletes the source directory and recreates it each time (`rm -rf $SOURCE_DIR`), so UFO files are ephemeral build artifacts.
5. There is **no `config.yaml`** anywhere in the repository, and the build system is **not compatible with gftools-builder**.

Dependencies include Node.js packages (`fontkit`, `jsdom`, `commander`, etc.) and Python tools (`fontmake`, `gftools`, `font-v`).

## Commit Hash Verification

### gftools-packager Reference

PR [#2913](https://github.com/google/fonts/pull/2913) (merged 2021-02-03) was the last update to this font in google/fonts. The commit message states:

> Libre Barcode 128 Version 1.005; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a.

The PR was authored by Lasse Fister (graphicore), the font's designer.

### Cross-Verification

The referenced commit `f9864c4` (2020-12-16) is titled "[ean13] bump version add binary v1.008; updates copyright string to include 2020." This commit only modified the EAN13 font binary, not the Code 128 binary.

The actual commit that added `fonts/LibreBarcode128-Regular.ttf` to the upstream repo was `63e8744` (2020-12-16, one minute earlier), titled "[code39/128] add binaries v1.005".

**Binary comparison confirms all three references point to the same file**:
- `google/fonts` at PR #2913 merge: SHA256 `bece6b86...`
- Upstream at `f9864c4`: SHA256 `bece6b86...` (same, file unchanged from `63e8744`)
- Upstream at `63e8744`: SHA256 `bece6b86...` (same, this is where the file was first added)

The hashes match because commit `f9864c4` did not modify the Code 128 binary -- it only came one commit after `63e8744` and only touched the EAN13 binary. Since gftools-packager references the latest commit at the time of onboarding (not necessarily the one that last modified the specific file), `f9864c4` is the correct reference commit.

### Post-Reference Commits

Only two commits exist on master after `f9864c4`:
- `93bb140` (2022-05-02): "[ean 13] Add bulk encoder as requested in #52" -- unrelated to Code 128
- `e44a85e` (2024-06-25): "Fixes #64; Wrong variable used" -- JavaScript fix for the encoder app

Neither of these modified any font binaries.

## Commit Hash Assessment

**Commit `f9864c42b2c467f255659c8851c124e4cd56c67a`** is the correct reference. It was explicitly recorded by gftools-packager in PR #2913, authored by the font designer himself, and the binary file at that commit matches what was delivered to google/fonts. The commit predates the google/fonts merge date (2021-02-03), and no font binary changes occurred between this commit and the merge.

## config.yaml Assessment

**No config.yaml is possible.** The Libre Barcode project uses a custom Node.js build pipeline that programmatically generates UFO sources from JavaScript code, then compiles them with fontmake. There are no static font sources (no `.glyphs`, `.ufo`, or `.designspace` files) that gftools-builder could work with. Creating an override config.yaml is not feasible for this project.

The pre-compiled binaries in the `fonts/` directory of the upstream repo are the deliverables that google/fonts consumes directly.

## Font Binary History in google/fonts

| Date | Commit | Description |
|------|--------|-------------|
| 2017-07-31 | `d92c6a1` | Initial addition via PR #1109 |
| 2017-08-21 | `b2f4c90` | Update and add Barcode fonts (PR #1145) |
| 2017-08-30 | `e79aa18` | Updated to v1.002 (PR #1182) |
| 2017-09-27 | `f4c49a2` | Updated to v1.003, add zwsp (PR #1228) |
| 2021-02-03 | `2c8be09` | Updated to v1.005 via gftools-packager (PR #2913) |

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/graphicore/librebarcode |
| **Commit Hash** | `f9864c42b2c467f255659c8851c124e4cd56c67a` |
| **Branch** | master |
| **config.yaml** | None (custom Node.js build system; no gftools-builder compatible sources) |
| **Status** | `missing_config` |
| **Confidence** | **HIGH** |

The source block in METADATA.pb needs only a `commit` field added. No config.yaml can be provided due to the non-standard build system. The status remains `missing_config` because the project cannot be built with gftools-builder.
