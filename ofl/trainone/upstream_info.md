# Train One — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/fontworks-fonts/Train
- **Commit**: `2972a9857a8332c2af86b221799558c177ba9012`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("master") fields but was missing a commit hash. The latest commit on the master branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/fontworks-fonts/Train/commits/{hash}`.

## Notes
- Repository is maintained by Fontworks Inc.
- Font supports cyrillic, japanese, and latin subsets.
