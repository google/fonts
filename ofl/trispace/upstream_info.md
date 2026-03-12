# Trispace — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/Etcetera-Type-Co/Trispace
- **Commit**: `8f332ade4a0e4be1cab60eafcbac95a53a3d46f6`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained only a repository_url with no files, branch, or commit fields. The latest commit hash was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/Etcetera-Type-Co/Trispace/commits/{hash}`.

## Notes
- The source block has no explicit file mappings or branch specification, meaning it relies on default behavior.
- This is a variable font with two axes: wdth and wght.
- Repository is maintained by Etcetera Type Co (Tyler Finck).
