# Roboto Condensed — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/roboto-classic
- **Commit**: `8aa699a9a715be7ecf6be41171e2851a580f0fb8`
- **Status**: Commit hash was added to existing source block

## What Was Done
The repository at https://github.com/googlefonts/roboto-classic was inspected. The METADATA.pb already contained an `archive_url` pointing to the `v3.008` release (`https://github.com/googlefonts/roboto-classic/releases/download/v3.008/Roboto_v3.008.zip`). The annotated tag `v3.008` was resolved via the GitHub API: the tag object SHA `561e928f706e4d6deab3617354b0b30378176f1d` was dereferenced to the underlying commit SHA `8aa699a9a715be7ecf6be41171e2851a580f0fb8`. This commit was verified and added to the source block in METADATA.pb to match the pinned release.

## Build System
The repository uses UFO source files with a designspace (`sources/Roboto.designspace`) and contains both regular and condensed masters. Scripts in `scripts/` and a `setup.py` suggest a Python-based build pipeline. A `requirements.txt` is present. The repository produces the full Roboto family including condensed variants.

## Notes
The Roboto Condensed family in Google Fonts was updated in 2023 (date_added: 2023-07-28) to use the new variable font format from the `roboto-classic` repository. The commit pinned here corresponds to the `v3.008` release, which is the release referenced by the existing `archive_url` in METADATA.pb.
