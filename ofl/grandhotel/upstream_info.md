# Grand Hotel — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/librefonts/grandhotel |
| Commit | `b0716771fb1056ca9db1d65d94e62ecf9dbedefa` |
| Confidence | Medium |

## Source Types

The repository contains:
- `src/GrandHotel-Regular.vfb` — FontLab VFB source
- TTX-decompiled files

## Build Compatibility

Not buildable with gftools-builder. The VFB (FontLab Studio) format is a proprietary binary format that requires FontLab to open. No modern Glyphs, UFO, or Designspace sources are available. No native Astigmatic (Brian J. Bonislawsky) repository was found on GitHub.

## Investigation Notes

This is a librefonts mirror repository. The `src/` directory contains a FontLab VFB file, which represents the original design source but in a proprietary format. The TTX files are decompiled binary dumps.

**Note on librefonts mirrors**: This repository is a community archive. The VFB source is closer to the original design than TTX dumps, but still requires proprietary software (FontLab Studio) to edit.

The binary in google/fonts dates from the initial commit (2015-03-07).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Medium

Librefonts mirror with VFB source; not buildable with modern open-source tooling.
