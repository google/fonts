# Miltonian Tattoo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/impallari/Miltonian
- **Owner**: Pablo Impallari (impallari)
- **Latest commit**: `95d180e8744380f93a8437226e58032d484882c7`
- **Commit date**: 2016-01-15
- **Commit message**: `v1.7`
- **Default branch**: `master`

Note: The repository is named "Miltonian" and contains both the Miltonian and Miltonian Tattoo fonts in the same repo. The Miltonian Tattoo TTF binary and its VFB source file are both present.

## Source Files

The `source/` directory contains VFB (FontLab Studio) source files:

- `source/MiltonianTattoo-Regular.vfb` — main source file (216 KB)
- `source/MiltonianTattoo-Regular-OTF.vfb` — OTF-tuned variant
- `source/MiltonianTattoo-Regular-TTF.vfb` — TTF-tuned variant
- `source/Miltonian-Regular.vfb` — companion Miltonian (non-tattoo) source
- `source/Miltonian-Regular-OTF.vfb`
- `source/Miltonian-Regular-TTF.vfb`

Built TTF binaries are in `fonts/TTF/`:
- `fonts/TTF/MiltonianTattoo-Regular-TTF.ttf`
- `fonts/TTF/Miltonian-Regular-TTF.ttf`

## Build System

No automated build system is present. There is no Makefile, build script, or requirements file. The repo contains pre-built TTF and OTF binaries alongside the VFB sources. The workflow appears to be manual export from FontLab Studio.

## config.yaml Status

No `config.yaml` exists in the upstream repo or in the `ofl/miltoniantattoo/` directory in google/fonts.

## Notes

- The repository has been effectively dormant since January 2016 (last commit v1.7).
- The source format is FontLab VFB, which is a proprietary binary format. There are no open/interoperable source files (UFO, Glyphs, etc.).
- The repo covers both Miltonian and Miltonian Tattoo; the Google Fonts entries for these two families are separate (`miltoniantattoo` and `miltonian`), both pointing to the same upstream.
- No config.yaml or gftools build pipeline exists; a new one would need to be created from scratch.
- The designer, Pablo Impallari, passed away in 2021. The repo is unlikely to receive further upstream updates.
- Confidence in repo identification: **High** — the repo is authored by Impallari, explicitly named "Miltonian Fonts", and contains the exact filenames referenced in the METADATA.pb copyright notice.
