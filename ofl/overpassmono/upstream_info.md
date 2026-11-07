# Overpass Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Overpass Mono shares its upstream repository with the Overpass proportional family. The canonical upstream repository was identified at https://github.com/RedHatOfficial/Overpass, maintained by Red Hat's GitHub organization. The METADATA.pb source block was already present with the correct repository URL and commit, which corresponds to the HEAD of the `master` branch.

## Repository

- **URL**: https://github.com/RedHatOfficial/Overpass
- **Default branch**: `master`
- **Description**: Overpass open source web font family — Sponsored by Red Hat
- **Note**: This repository contains both Overpass (proportional) and Overpass Mono. The mono variable fonts are located in `fonts/variable_mono/`.

## Commit

- **Pinned commit**: `c580d28bfab7f39013568e684a65eeb23eff588d`
- **Commit message**: Merge pull request #87 from DelveFonts/master — Bumping Mono variant to v4.00
- **Commit date**: 2021-09-10
- **Status**: This is the HEAD of the `master` branch — the repository is up-to-date with the pinned commit.

## Font Details

Overpass Mono is a monospaced companion to the Overpass proportional family, designed by Delve Withrington, Dave Bailey, and Thomas Jockin and sponsored by Red Hat. It is described as a "thoughtful, monospaced re-imagining" of the Overpass proportional design, optimized for programming use. The family covers five weights in a variable font with a `wght` axis (300–700).

The Google Fonts version ships a single variable font: `OverpassMono[wght].ttf`, sourced from `fonts/variable_mono/` in the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/RedHatOfficial/Overpass
- `commit`: `c580d28bfab7f39013568e684a65eeb23eff588d`
- `branch`: master
- `config_yaml`: sources/config.yaml
- File mappings for OverpassMono[wght].ttf and OFL.txt are present.

No changes to METADATA.pb were required.
