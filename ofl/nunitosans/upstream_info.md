# Nunito Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/NunitoSans
- **Branch**: `main`
- **Pinned commit**: `058bd7a2f33d6ad5ef1df985b3db403622016a8c`
- **Commit date**: 2023-03-31
- **Commit message**: "Merge pull request #20 from emmamarichal/main — YTLC values"
- **Latest upstream activity**: 2023-12-11 (repo has had some activity since the pinned commit)

Note: The original upstream source was at `https://github.com/Fonthausen/NunitoSans` (referenced in the copyright string). The authoritative working repo is now at `googlefonts/NunitoSans`.

## Source Files

The `sources/` directory contains:

- `NunitoSans.glyphs` — primary Glyphs source for the Roman
- `NunitoSans-Italic.glyphs` — primary Glyphs source for the Italic
- `config.yaml` — gftools builder configuration

The `config.yaml` specifies both `.glyphs` files as sources, with `familyName: Nunito Sans`, `buildOTF: False`, `buildWebfont: False`, axis order `[YTLC, opsz, wdth, wght, ital]`, and a detailed STAT table definition covering the YTLC, opsz, wdth, and wght axes with named values for both the Roman and Italic variable fonts.

## Build System

- **Tool**: `gftools builder` (driven by `sources/config.yaml`)
- **Static fonts**: Not built (`buildOTF: False`)
- **Output**: Two variable fonts — `NunitoSans[YTLC,opsz,wdth,wght].ttf` and `NunitoSans-Italic[YTLC,opsz,wdth,wght].ttf`
- **Axes**: YTLC (440–540), opsz (6–12), wdth (75–125), wght (200–1000)

## config.yaml Status

`config.yaml` is present at `sources/config.yaml` and is already referenced in `METADATA.pb` (`config_yaml: "sources/config.yaml"`). The METADATA.pb source block is fully configured.

The pinned commit is from March 2023 and the repo has had at least one push since then (2023-12-11). The METADATA.pb may be slightly behind the latest state of the `main` branch; an update to the pinned commit should be considered.

## Notes

- Nunito Sans was originally developed by Vernon Adams and Jacques Le Bailly at Fonthausen. The `googlefonts` organization took over as the canonical maintainer.
- Manvel Shmavonyan and Alexei Vanyashin are credited for Cyrillic extension work.
- The font has an unusual YTLC (Lowercase Height) axis, custom to this family. The `registry_default_overrides` in METADATA.pb sets opsz default to 12.0.
- The `wdth` axis covers Condensed (75) through Expanded (125), providing a wide range of width variants.
- No cached upstream repo found at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/NunitoSans`.
