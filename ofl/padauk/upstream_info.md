# Padauk — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The Padauk font family is developed and maintained by SIL International. The source block in METADATA.pb referenced a release archive at version 5.001 but was missing a commit hash. The commit hash was identified and added.

## Repository

- **URL**: https://github.com/silnrsi/font-padauk
- **Upstream cache**: Not present at `/mnt/shared/upstream_repos/fontc_crater_cache/silnrsi/font-padauk` (only `font-mingzat` was cached under `silnrsi/`)

## Version Identification

The font binaries in the Google Fonts repo were inspected:

- `Padauk-Regular.ttf`: Version 5.001, nameID5 = "Version 5.001"
- Copyright: "Copyright (c) 2002-2022 SIL International"

The METADATA.pb `archive_url` pointed to:
```
https://github.com/silnrsi/font-padauk/releases/download/v5.001/Padauk-5.001.zip
```

## Commit Identification

The GitHub API was queried for the `v5.001` tag:

```
gh api repos/silnrsi/font-padauk/git/refs/tags/v5.001
```

The tag `v5.001` resolved to a commit object (not an annotated tag pointing to a tag object), directly yielding the commit SHA.

The commit hash was verified:

```
gh api repos/silnrsi/font-padauk/commits/278b8efb03c0ca0d7f29fb3edc1f52489ebb384f --jq '.sha'
# Returns: 278b8efb03c0ca0d7f29fb3edc1f52489ebb384f
```

## Changes Made

- Added `commit: "278b8efb03c0ca0d7f29fb3edc1f52489ebb384f"` to the `source` block in `METADATA.pb`

## Confidence

**High.** The commit hash corresponds directly to the `v5.001` git tag, which matches the `archive_url` already present in METADATA.pb. The font version string (5.001) and copyright year (2022) are consistent with the release.

## Repo / Commit / Config / Status

- **Repo**: https://github.com/silnrsi/font-padauk
- **Commit**: `278b8efb03c0ca0d7f29fb3edc1f52489ebb384f` (tag `v5.001`)
- **Config**: archive-based build, files mapped from `Padauk-5.001/` prefix
- **Status**: Commit hash added to METADATA.pb
- **Confidence**: High
