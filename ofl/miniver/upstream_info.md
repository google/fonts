# Miniver — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/miniver
- **Owner**: librefonts (archival/mirror org)
- **Latest commit**: `b301973d6822dc2661ce510355b4d7f9ed573926`
- **Commit date**: 2014-10-17
- **Commit message**: `update .travis.yml`
- **Default branch**: `master`

The repository is under the `librefonts` GitHub organization, which hosts archival copies of older free/libre fonts. The FONTLOG confirms this is the correct source: "Designed by Dathan Boardman of Open Window" with contact `dathanboardman@gmail.com`, matching the copyright in METADATA.pb exactly.

No canonical repository by the designer (Open Window / Dathan Boardman) was found — the `librefonts` copy appears to be the only known upstream source on GitHub.

## Source Files

The `src/` directory contains:

- `src/Miniver-Regular-TTF.vfb` — FontLab Studio source file (63 KB)
- `src/VERSIONS.txt` — version history
- `src/METADATA_comments.txt` — notes on metadata

The repo root also contains TTX decompositions of the built font:
- `Miniver-Regular.ttf.ttx` (main TTX)
- Multiple per-table TTX files (`_g_l_y_f`, `_h_m_t_x`, `_n_a_m_e`, etc.)

## Build System

A `.travis.yml` CI configuration file is present, suggesting an automated build was attempted at some point. However, there is no Makefile or build script in the repository. The source format is FontLab VFB (proprietary binary). No open build pipeline exists.

## config.yaml Status

No `config.yaml` exists in the upstream repo or in the `ofl/miniver/` directory in google/fonts.

## Notes

- The repository has been dormant since October 2014.
- The source format is FontLab VFB — a proprietary binary format with no open toolchain support. Migration to UFO or Glyphs would be required before a modern gftools build pipeline could be established.
- No evidence of an authoritative repository from the original designer (Open Window / Dathan Boardman) was found on GitHub.
- The `librefonts` organization appears to have archived this font as-is; it is unlikely to receive further upstream development.
- Confidence in repo identification: **High** — FONTLOG text, designer name, email, and font name all match the METADATA.pb.
