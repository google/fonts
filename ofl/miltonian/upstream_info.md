# Miltonian — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The upstream source repository is on GitHub under the Impallari account:

- **URL**: https://github.com/impallari/Miltonian
- **Description**: "Miltonian Fonts"
- **Default branch**: `master`
- **Last commit**: `95d180e8744380f93a8437226e58032d484882c7` (2016-01-15, "v1.7")
- **Repository last updated on GitHub**: 2024-08-11 (metadata update, not a content commit)

This single repository contains sources for **both** Miltonian and Miltonian Tattoo.

## Source Files

Source files are located under `source/`:

- `source/Miltonian-Regular.vfb` — FontLab Studio source file (main master for Miltonian)
- `source/Miltonian-Regular-OTF.vfb` — FontLab source optimized for OTF output
- `source/Miltonian-Regular-TTF.vfb` — FontLab source optimized for TTF output
- `source/MiltonianTattoo-Regular.vfb` — FontLab source file (main master for Miltonian Tattoo)
- `source/MiltonianTattoo-Regular-OTF.vfb` — FontLab source for Tattoo OTF
- `source/MiltonianTattoo-Regular-TTF.vfb` — FontLab source for Tattoo TTF

Compiled fonts are under `fonts/OTF/` and `fonts/TTF/`.

The `.vfb` files (FontLab Studio native format) are the canonical source.

## Build System

No build scripts or Makefile were found in the repository root. The repo contains pre-compiled font binaries in `fonts/` but no documented build pipeline. No `.travis.yml`, `Makefile`, or `SConstruct` was found (unlike the `librefonts` mirrors). Building from `.vfb` source requires FontLab Studio (proprietary).

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/miltonian/` or in the upstream `impallari/Miltonian` repository.

## Notes

- The `impallari/Miltonian` repository covers both the Miltonian and Miltonian Tattoo families (see also `miltoniantattoo/upstream_info.md`).
- The most recent content commit is `95d180e` tagged "v1.7" from January 15, 2016. The repository has had no source changes since then.
- Co-designer credit: Igino Marini (`www.ikern.com`) appears in the copyright string for kerning work.
- Miltonian is a display typeface described as a fun "tattoo" font; Miltonian Tattoo has filled forms.
- The `.vfb` format requires FontLab Studio (proprietary) to edit; no open-source-friendly source format is available.
- A config.yaml would need to be authored from scratch for any future Google Fonts rebuild.
