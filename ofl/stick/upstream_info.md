# Stick — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/fontworks-fonts/Stick
- **Commit**: `069a1101e3fd51e60205710157f8b6a996ffea61`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/fontworks-fonts/Stick was identified as the source for Stick. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb.

## Build System
The repository contains a `build.py` Python script at the root level for building font files from sources in the `sources/` directory. Pre-built fonts are available in the `fonts/ttf/` directory.

## Notes
Stick is a Japanese sans-serif display typeface by Fontworks Inc. The METADATA.pb source block already included file mappings and a branch specification (`master`); only the commit hash was missing.
