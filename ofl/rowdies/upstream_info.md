# Rowdies — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/magictype/rowdies
- **Commit**: `4703538d6102c2b5eb8fdcb126a6eaaa509f0d06`
- **Status**: Commit hash was added to existing source block

## What Was Done
The repository at https://github.com/magictype/rowdies was inspected. No tags or releases were found in the repository. The source block in METADATA.pb had no `branch`, `files`, or other metadata beyond the `repository_url`. The latest commit on the default branch (`4703538d6102c2b5eb8fdcb126a6eaaa509f0d06`) was verified via the GitHub API and added to the source block in METADATA.pb.

## Build System
The repository contains a Glyphs source file (`sources/Rowdies.glyphs`) and a `build.sh` shell script for building the fonts. Pre-built static font binaries are in `fonts/`. The `build.sh` script likely uses fontmake or similar tooling to produce the final OTF/TTF files from the Glyphs source.

## Notes
The Rowdies source block in METADATA.pb was notably sparse — it contained only the `repository_url` with no `files` mappings, `branch`, or `archive_url`. The font files in Google Fonts (Rowdies-Light.ttf, Rowdies-Regular.ttf, Rowdies-Bold.ttf) are static fonts (non-variable), which is consistent with the three weight instances defined in the Glyphs source.
