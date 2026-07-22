# TikTok Sans — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/TikTok/TikTokSans
- **Commit**: `baa2f381f9102da9fbc3c83843ad224774240516`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, branch ("main"), and config_yaml fields but was missing a commit hash. The latest commit on the main branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/TikTok/TikTokSans/commits/{hash}`.

## Notes
- This is a variable font with four axes: opsz, slnt, wdth, wght.
- Repository is maintained by TikTok Inc.
- The source references a config.yaml at `sources/config.yaml`.
