# Sora — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/sora-xor/sora-font
- **Commit**: `7f9a9c5d0ccd1c099cfac420aa27133df1c5fdc4`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/sora-xor/sora-font was identified as the source for Sora. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `sources/` directory alongside pre-built fonts in the `fonts/` directory. A `requirements.txt` file is present, indicating a Python-based build workflow. No Makefile or explicit build script was found at the root level.

## Notes
Sora is a variable sans-serif typeface designed by Jonathan Barnbrook and Julián Moncada for the SORA project. It has a `wght` axis ranging from 100 to 800. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sora/` referencing the upstream gftools-builder-compatible source at the pinned commit `7f9a9c5` (`sources/sora.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
