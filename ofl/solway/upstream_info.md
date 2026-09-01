# Solway — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/mashavp/Solway
- **Commit**: `41e054e45760c690e2a2b770feb86a5e125360c2`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/mashavp/Solway was identified as the source for Solway. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `sources/` directory alongside pre-built fonts in the `fonts/` directory. A `requirements.txt` file is present, indicating a Python-based build workflow. No Makefile or explicit build script was found at the root level.

## Notes
Solway is a serif typeface by Mariya Lish and The Northern Block, available in 5 weights (Light, Regular, Medium, Bold, ExtraBold) without italic styles. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification.
