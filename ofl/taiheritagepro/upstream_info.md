# Tai Heritage Pro — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/silnrsi/font-taiheritagepro
- **Commit**: `1ac0dd04cf5dd23435f37cecfe825e0eaf230a4c`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb already contained a repository_url, archive_url pointing to the v2.600 release, and a branch field. The commit hash corresponding to the v2.600 release tag was retrieved from the GitHub API (`refs/tags/v2.600` points directly to commit `1ac0dd04cf5dd23435f37cecfe825e0eaf230a4c`). The commit field was added to the source block. The hash was verified via `gh api repos/silnrsi/font-taiheritagepro/commits/{hash}`.

## Notes
- The source block uses an archive_url referencing the v2.600 release zip rather than direct file references from the repository tree. The commit hash recorded corresponds to the tagged release commit.
- Repository is maintained by SIL International.
