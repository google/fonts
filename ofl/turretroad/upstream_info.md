# Turret Road — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/noponies/Turret-Road
- **Commit**: `c77a268e22034f5427de1bbed2d13fdf7b91b1d8`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained only a repository_url with no files, branch, or commit fields. The latest commit hash was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/noponies/Turret-Road/commits/{hash}`.

## Notes
- The source block has no explicit file mappings or branch specification, meaning it relies on default behavior.
- Repository is maintained by Dale Sattler (noponies).
- The family includes six weights: ExtraLight, Light, Regular, Medium, Bold, ExtraBold.
