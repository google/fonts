# Slackside One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/ManiackersDesign/slackside
- **Commit**: `e5a03bb81c7a6c6eb9f901b993c2164213f143d4`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/ManiackersDesign/slackside was identified as the source for Slackside One. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. The repository contains a `build.py` script for building the fonts.

## Build System
The repository contains a `build.py` Python script at the root level for building font files from the sources in the `source/` directory. Pre-built fonts are available in the `fonts/` directory.

## Notes
Slackside One is a Japanese handwriting typeface by Maniackers Design. The METADATA.pb source block already included file mappings and a branch specification (`master`); only the commit hash was missing. Note that the license file in the repository is named `ofl.txt` (lowercase), which the file mapping correctly reflects.
