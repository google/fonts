# Sansita Swashed — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/Omnibus-Type/Sansita-Swashed
- **Commit**: `4b18bac65511ce185c1dc687472a8c77bdc6cc4d`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/Omnibus-Type/Sansita-Swashed was identified as the source for Sansita Swashed. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `sources/` directory alongside pre-built fonts in the `fonts/` directory. No Makefile or build script was found at the root level.

## Notes
Sansita Swashed is a variable font with a `wght` axis ranging from 300 to 900. The source block in METADATA.pb did not previously include any file mappings or branch specification.
