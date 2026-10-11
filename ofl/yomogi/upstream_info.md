# Yomogi — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/satsuyako/YomogiFont
- **Commit**: `8551d68706679b88ce6ff40e093a993e546e593e`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("ver3.00") fields but was missing a commit hash. The latest commit on the ver3.00 branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/satsuyako/YomogiFont/commits/{hash}`.

## Notes
- Repository is maintained by Satsuyako.
- The source uses a non-standard branch name "ver3.00" — this is an actual branch in the repository, not a tag.
- Font supports cyrillic, japanese, latin, latin-ext, and vietnamese subsets.
