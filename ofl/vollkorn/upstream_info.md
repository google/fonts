# Vollkorn — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/FAlthausen/Vollkorn-Typeface
- **Commit**: `38ab7a896bd6b163ac7f834ec696d6c68e5dedd6`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("master") fields but was missing a commit hash. The latest commit on the master branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/FAlthausen/Vollkorn-Typeface/commits/{hash}`.

## Notes
- This is a variable font with a wght axis.
- Repository is maintained by Friedrich Althausen.
- Font also has a minisite at `http://vollkorn-typeface.com/`. The HTTPS version of this URL could not be verified (SSL error), so the existing HTTP URL was left unchanged.
- The same commit hash applies to both Vollkorn and Vollkorn SC, as they share the same upstream repository.
