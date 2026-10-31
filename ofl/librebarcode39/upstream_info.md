# Investigation Report: Libre Barcode 39

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Family**: Libre Barcode 39
**Directory**: `ofl/librebarcode39`
**Designer**: Lasse Fister

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/graphicore/librebarcode"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/LibreBarcode39-Regular.ttf"
    dest_file: "LibreBarcode39-Regular.ttf"
  }
  branch: "master"
}
```

The source block was present with repository URL, file mappings, and branch. No `commit` field and no `config_yaml` field were set.

## Upstream Repository

- **URL**: https://github.com/graphicore/librebarcode
- **Local cache**: `upstream_repos/fontc_crater_cache/graphicore/librebarcode`
- **Default branch**: master
- **Author**: Lasse Fister (graphicore)

The repository was verified as accessible. The remote URL matched the `repository_url` in METADATA.pb.

## Build System Analysis

This project used a **custom JavaScript-based build system**, not the standard gftools-builder pipeline. The build process worked as follows:

1. **JavaScript builder** (`app/bin/build`) programmatically generated UFO source directories from barcode encoding definitions in `app/lib/builder/code39.js` (and related files for other barcode types).
2. The generated UFO sources were written to a `sources/` directory (which was listed in `.gitignore` and not committed).
3. **fontmake** compiled the generated UFOs into TTF files.
4. **gftools fix-font** performed post-processing.
5. The final TTF binaries were committed to the `fonts/` directory.

The `app/bin/buildAll` shell script orchestrated the full build, calling the Node.js builder for each barcode variant and then invoking `fontmake`. Dependencies included Node.js, npm, bower, Python 3 (with `fontmake` and `gftools`), and `ttfautohint`.

Because there were no persistent `.glyphs`, `.ufo`, or `.designspace` source files in the repository (they were generated at build time by the JavaScript code), a standard gftools-builder `config.yaml` was not applicable. The project's "source" was the JavaScript barcode generator code itself.

## Commit History in google/fonts

| Commit | Date | Description |
|--------|------|-------------|
| `d92c6a1` | 2017-07-31 | Initial onboarding via PR #1109 |
| `b2f4c90` | 2017-08-21 | Update + add extended variants via PR #1145 |
| `f4c49a2` | 2017-09-27 | Update to v1.003 via PR #1228 |
| `e79aa18` | (undated in log) | Update to v1.002 via PR #1182 |
| `9afc75e` | 2021-02-03 | Update to v1.005 via PR #2909 (latest binary update) |
| `66f91f1` | 2024-04-03 | Merge upstream.yaml into METADATA.pb |
| `151547c` | 2025-05-01 | Custom sample text added |

## Commit Hash Verification

PR #2909 (the last binary update) was authored by Lasse Fister himself and referenced upstream commit `f9864c42b2c467f255659c8851c124e4cd56c67a`. The gftools-packager message stated:

> "Libre Barcode 39 Version 1.005; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/graphicore/librebarcode.git at commit https://github.com/graphicore/librebarcode/commit/f9864c42b2c467f255659c8851c124e4cd56c67a."

**Verification**: Commit `f9864c4` was an EAN13-related commit ("[ean13] bump version add binary v1.008") that did not directly modify `LibreBarcode39-Regular.ttf`. The actual Code39 binary was added one commit earlier at `63e8744` ("[code39/128] add binaries v1.005"). However, both commits were authored on the same date (2020-12-16) as part of the same batch of changes. At commit `f9864c4`, the `fonts/LibreBarcode39-Regular.ttf` file contained the v1.005 binary from `63e8744`.

**Binary match confirmed**: MD5 checksums were identical across all three locations:
- Upstream at `f9864c4`: `ade869a1fbdd772d64c0cdd28110b882`
- Upstream at `63e8744`: `ade869a1fbdd772d64c0cdd28110b882`
- google/fonts current: `ade869a1fbdd772d64c0cdd28110b882`

The font binary at HEAD of the upstream repo also matched (no changes to Code39 binaries occurred after `63e8744`).

The referenced commit `f9864c4` was valid as the point-in-time snapshot used by gftools-packager, even though the Code39 binary was introduced one commit earlier.

## Config.yaml Assessment

**No config.yaml was possible for this project.** The repository used a custom JavaScript build system that programmatically generated UFO sources from barcode encoding definitions. There were no static `.glyphs`, `.ufo`, or `.designspace` files to reference in a gftools-builder config.

The `source { }` block in METADATA.pb correctly mapped pre-built binary files from `fonts/LibreBarcode39-Regular.ttf` rather than pointing to buildable sources. This was the appropriate approach for this non-standard build system.

An override config.yaml in google/fonts would also not be feasible, as there were no standard font sources to build from.

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/graphicore/librebarcode |
| **Commit** | `f9864c42b2c467f255659c8851c124e4cd56c67a` |
| **Branch** | master |
| **Config** | None (custom JS build system, no standard font sources) |
| **Status** | `no_config_possible` |
| **Confidence** | HIGH |

The source block in METADATA.pb was correctly configured for a binary-copy workflow. The commit hash `f9864c4` was verified as the correct reference point used during the v1.005 update in PR #2909, with binary match confirmed via MD5 checksums. No `config_yaml` field was needed because the project did not use gftools-builder-compatible source files.

## Recommendations

1. **Add commit hash to METADATA.pb**: The `commit` field should be added to the source block with value `f9864c42b2c467f255659c8851c124e4cd56c67a` to fully document the provenance.
2. **No config.yaml action needed**: The custom build system makes gftools-builder integration impossible without a fundamental rearchitecture of the upstream project.
3. **Status should remain `no_config_possible`**: This is a legitimate case where the font sources are programmatically generated and cannot be represented in a standard config.yaml.
