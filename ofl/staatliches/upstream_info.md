# Staatliches — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/staatliches
- **Commit**: `0d69eea1ad9a6312fbfdf9afa54fa38933a21b42`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/googlefonts/staatliches was identified as the source for Staatliches. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `sources/` directory alongside pre-built fonts in the `fonts/` directory. No Makefile or explicit build script was found at the root level; however, the presence of documentation in `docs/` suggests the font was developed as part of a Google Fonts project.

## Notes
Staatliches is a display sans-serif typeface designed by Brian LaRossa and Erica Carras. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification. The repository is hosted under the `googlefonts` GitHub organization.
