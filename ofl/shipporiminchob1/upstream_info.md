# Shippori Mincho B1 — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/fontdasu/ShipporiMincho
- **Commit**: `63431fee6c2cfea772325d6251d2935b7cfa7c6d`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/fontdasu/ShipporiMincho was identified as the source for Shippori Mincho B1. This family shares the same repository as Shippori Mincho. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb.

## Build System
The repository contains a `build.py` Python script at the root level for building font files from sources. Pre-built fonts are available in the `fonts/ttf/` directory. Sources are stored in the `source/` directory.

## Notes
Shippori Mincho B1 is a variant of Shippori Mincho with different character mapping, both hosted in the same repository. The METADATA.pb source block already included detailed file mappings and a branch specification (`master`); only the commit hash was missing. The same commit hash applies to both Shippori Mincho and Shippori Mincho B1 since they share a repository.
