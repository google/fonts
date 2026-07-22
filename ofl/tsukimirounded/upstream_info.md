# Tsukimi Rounded — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/mt-funa/Tsukimi-Rounded
- **Commit**: `7199ebaed5a78b14f7824cc3ea44f5694e790807`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("master") fields but was missing a commit hash. The latest commit on the master branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/mt-funa/Tsukimi-Rounded/commits/{hash}`.

## Notes
- Repository is maintained by Takashi Funayama (mt-funa).
- Font supports japanese, latin, and latin-ext subsets.
- The family includes five weights: Light, Regular, Medium, SemiBold, Bold.
