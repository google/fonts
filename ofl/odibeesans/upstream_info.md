# Odibee Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Odibee Sans was identified at https://github.com/barnard555/odibeesans, authored by James Barnard. The repository is a personal GitHub account repo, not a librefonts mirror. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/barnard555/odibeesans
- **Default branch**: master
- **License**: OFL (Other/custom OFL variant)
- **Description**: "A free display font created by James Barnard"

## Pinned Commit

- **Commit**: `c72b102fec681b3b74f025e70a673d2ef4ac664e`
- **Date**: 2019-11-07
- **Message**: "Merge pull request #2 from yanone/master — Ready for Google Fonts"
- **Author**: James Barnard

The pinned commit is the HEAD of the master branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Source Files

The repository contains a Glyphs source file at `sources/Odibee-Sans-v2.glyphs`, along with prebuilt TTF, OTF, EOT, and WOFF binaries in separate directories. The METADATA.pb does not specify a `config_yaml`, indicating fonts were taken directly from the prebuilt binaries.

## Confidence

**High** — The repository URL is referenced in the font's copyright string and matches the designer attribution. The commit is the latest on the repository.
