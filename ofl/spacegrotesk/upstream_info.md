# Space Grotesk — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/floriankarsten/space-grotesk
- **Commit**: `03507d024a01282884232081fc6011c09ff4e849`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/floriankarsten/space-grotesk was identified as the source for Space Grotesk. The latest commit on the master branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. Tagged releases were found (latest: `2.0.0`), but the head of the master branch was used as it represents the most current state of the repository.

## Build System
The repository contains a `sources/` directory alongside pre-built fonts in the `fonts/ttf/` directory. A `requirements.txt` file is present, indicating a Python-based build workflow. A `.github/` directory suggests CI/CD automation.

## Notes
Space Grotesk is a variable sans-serif typeface by Florian Karsten with a `wght` axis ranging from 300 to 700. The METADATA.pb source block already included detailed file mappings and a branch specification (`master`); only the commit hash was missing. The repository has a minisite at https://floriankarsten.github.io/space-grotesk.
