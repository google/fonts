# Yuji Boku — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/Kinutafontfactory/Yuji
- **Commit**: `efec977b14b57c19eb85d468edcfbbad13139e67`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("master") fields but was missing a commit hash. The latest commit on the master branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/Kinutafontfactory/Yuji/commits/{hash}`.

## Notes
- Repository is maintained by Kinuta Font Factory.
- The Yuji repository contains multiple font families; METADATA.pb references the YujiBoku-specific files.
- Font supports cyrillic, japanese, latin, and latin-ext subsets.
