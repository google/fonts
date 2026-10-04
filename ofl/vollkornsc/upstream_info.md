# Vollkorn SC — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/FAlthausen/Vollkorn-Typeface
- **Commit**: `38ab7a896bd6b163ac7f834ec696d6c68e5dedd6`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained only a repository_url with no files, branch, or commit fields. The latest commit hash was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/FAlthausen/Vollkorn-Typeface/commits/{hash}`.

## Notes
- The source block has no explicit file mappings or branch specification, meaning it relies on default behavior.
- Repository is maintained by Friedrich Althausen.
- Vollkorn SC shares the same upstream repository as Vollkorn; both receive the same commit hash.
- The family includes four weights: Regular, SemiBold, Bold, Black.
