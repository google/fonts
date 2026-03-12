# New Rocker — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Best available URL**: https://github.com/librefonts/newrocker
- **Latest relevant commit**: `1dae287590768daa0a3fe426aaf62fb159389abe` (2014-10-17) — "update .travis.yml"
- **Default branch**: `master`
- **Confidence**: Medium — this appears to be a third-party mirror/packaging repo (`librefonts` org, maintained by "hash3g" / Mikhail Kashkin), not the canonical designer repository.

No official upstream repository from Pablo Impallari / Impallari Type was found:
- The `impallari` GitHub account has 26 repositories but none named `New-Rocker`, `NewRocker`, or similar.
- The designer website `impallari.com` and the project page `impallari.com/projects/overview/newrocker` are currently unreachable (HTTP 523).
- No repository exists under `googlefonts/new-rocker` or `googlefonts/NewRocker`.
- No upstream mirror exists in `/mnt/shared/upstream_repos/fontc_crater_cache/`.

## Source Files

In `librefonts/newrocker`:
- `src/`
  - `NewRocker-Regular-OTF.vfb` — FontLab VFB source (OTF variant)
  - `NewRocker-Regular-TTF.vfb` — FontLab VFB source (TTF variant)
  - `NewRocker-Regular.vfb` — FontLab VFB source
  - Various `.ttx` files (TTX decompilation of the TTF and OTF)
  - `VERSIONS.txt`
- Root level:
  - `NewRocker-Regular.ttf.*` — decomposed TTX table files
  - `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `METADATA.json`, `OFL.txt`

The `.vfb` files are FontLab Studio 5 proprietary format sources. The `.ttx` files are FontTools XML decompilations that could serve as a rebuild path, but are not editable design sources.

## Build System

The repository uses a CI-based fontbakery build pipeline (circa 2014):
- `.travis.yml` — installs `python-fontforge`, `ttfautohint`, and `fontbakery-cli`, then runs `fontbakery-build.py .`
- `config.yaml` — present (a fontbakery-era configuration file)
- `Makefile` — present

This build pipeline relies on the deprecated `fontbakery-build.py` workflow, which is not compatible with modern gftools-based builds.

## config.yaml Status

A `config.yaml` is present in the repository root. It is a legacy fontbakery-era configuration, not a gftools `config.yaml`. The file content could not be verified (the raw URL returned 404), but its presence was confirmed via the GitHub API.

## Notes

- New Rocker was designed by Pablo Impallari, Brenda Gallo, and Rodrigo Fuenzalida (Impallari Type), with v1.0 released on 28 November 2012.
- The FONTLOG references `http://www.impallari.com/projects/overview/newrocker` as the project page, which is currently unreachable.
- The `librefonts/newrocker` repo is a third-party packaging effort and may not reflect the canonical sources; the VFB files it contains are the closest available sources but are in a proprietary, largely unsupported format.
- A modern rebuild would require converting the VFB files (e.g., via FontLab or vfb2ufo) or using the TTX decompilations as the base.
- The Google Fonts binary dates to 2012 (v1.0) and has never been updated.
- A new `config.yaml` (gftools format) would need to be created from scratch for any future rebuild.
