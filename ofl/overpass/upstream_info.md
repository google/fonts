# Overpass — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/RedHatOfficial/Overpass, maintained by Red Hat's GitHub organization. The METADATA.pb source block was already present with the correct repository URL and commit, which corresponds to the HEAD of the `master` branch.

## Repository

- **URL**: https://github.com/RedHatOfficial/Overpass
- **Default branch**: `master`
- **Description**: Overpass open source web font family — Sponsored by Red Hat
- **Website**: https://overpassfont.org/

## Commit

- **Pinned commit**: `c580d28bfab7f39013568e684a65eeb23eff588d`
- **Commit message**: Merge pull request #87 from DelveFonts/master — Bumping Mono variant to v4.00
- **Commit date**: 2021-09-10
- **Status**: This is the HEAD of the `master` branch — the repository is up-to-date with the pinned commit.

## Font Details

Overpass is an open source typeface designed by Delve Withrington, Dave Bailey, and Thomas Jockin, sponsored by Red Hat. The design is an interpretation of the "Highway Gothic" letterforms from the Standard Alphabets for Traffic Control Devices published by the U.S. Federal Highway Administration, adjusted for optimal on-screen legibility at small sizes. The same repository also contains the Overpass Mono companion family.

The Google Fonts version ships two variable fonts:
- `Overpass[wght].ttf` (upright, wght 100–900)
- `Overpass-Italic[wght].ttf` (italic, wght 100–900)

Both are sourced from `fonts/variable/` in the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/RedHatOfficial/Overpass
- `commit`: `c580d28bfab7f39013568e684a65eeb23eff588d`
- `branch`: master
- `config_yaml`: sources/config.yaml
- File mappings for Overpass[wght].ttf, Overpass-Italic[wght].ttf, and OFL.txt are present.

No changes to METADATA.pb were required.
