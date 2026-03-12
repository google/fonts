# STIX Two Math — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/stipub/stixfonts
- **Commit**: `c4afdf3fa5390159ef24aca1db5e957487c23897`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/stipub/stixfonts was identified as the source for STIX Two Math. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. Tagged releases were found (latest: `v2.13b171`).

## Build System
The repository contains a `build.sh` shell script at the root level, along with a `tools/` directory and `requirements.in`/`requirements.txt` files indicating a Python-based build toolchain. Pre-built fonts are available in `fonts/static_ttf/` and `fonts/variable_ttf/` directories.

## Notes
STIX Two Math is a mathematical OpenType font from the STIX Fonts project, designed by Tiro Typeworks, Ross Mills, John Hudson, and Paul Hanslow. It shares its upstream repository with STIX Two Text; both families were updated with the same commit hash. The METADATA.pb source block already included file mappings and a branch specification (`master`); only the commit hash was missing.
