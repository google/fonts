# Sarabun — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/cadsondemak/Sarabun
- **Commit**: `854cdbc6afa002ff8c2ce6aa7b86f99c7f71c9eb`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/cadsondemak/Sarabun was identified as the source for the Sarabun family. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `source/` directory with font sources, alongside a `fonts/` directory with pre-built files. The root directory also includes HTML, CSS, and JavaScript files consistent with a specimen website. No Makefile or explicit build script was found at the root level.

## Notes
Sarabun is a Thai typeface with 16 styles (8 weights × regular + italic). The family is maintained by Cadson Demak. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification.
