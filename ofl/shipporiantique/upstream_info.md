# Shippori Antique — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/fontdasu/ShipporiAntique
- **Commit**: `5653d23ee96e457921b2dbec7692e8e5d243e5fe`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/fontdasu/ShipporiAntique was identified as the source for Shippori Antique. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. The repository contains a `build.py` script for building the fonts from sources.

## Build System
The repository contains a `build.py` Python script at the root level for building font files from the sources in the `sources/` directory. Pre-built fonts are available in the `fonts/ttf/` directory.

## Notes
The Shippori Antique repository hosts both the Shippori Antique and Shippori Antique B1 variants. The METADATA.pb source block already included file mappings and a branch specification (`master`); only the commit hash was missing.
