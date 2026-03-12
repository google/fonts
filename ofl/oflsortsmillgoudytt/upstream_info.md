# OFL Sorts Mill Goudy TT — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository with UFO sources was found at `theleagueof/sorts-mill-goudy` on GitHub. The METADATA.pb was updated to add a `source` block pointing to this repository.

## Family Details

- **Designer**: Barry Schwartz
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2010-05-18

## Upstream Repository

- **URL**: https://github.com/theleagueof/sorts-mill-goudy
- **Owner**: The League of Moveable Type (the designer's chosen publishing collective)
- **Description**: "A 'revival' of Goudy Oldstyle and Italic."
- **Last pushed**: 2024-02-19

The repository was published by Barry Schwartz (GitHub: `chemoelectric`) through The League of Moveable Type, a designer collective he is associated with. Barry Schwartz is identified in the copyright string as "chemoelectric@chemoelectric.org" and separately maintains the `chemoelectric/sortsmill` repository (an older Mercurial mirror from Google Code, last updated 2013 with FontForge SFD sources).

The `theleagueof/sorts-mill-goudy` repository contains UFO (Unified Font Object) sources in the `source/` directory:
- `source/OFLGoudyStM.ufo` — roman UFO
- `source/OFLGoudyStM-Italic.ufo` — italic UFO

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Commit Used

- **SHA**: `06072890c7b05f274215a24f17449655ccb2c8af`
- **Date**: 2011-05-25
- **Message**: "Initial commit with readme and licenses"

The repository has only one commit; the UFO sources were included in this initial commit.

## METADATA.pb Changes

A `source` block was added to METADATA.pb:
```
source {
  repository_url: "https://github.com/theleagueof/sorts-mill-goudy"
  commit: "06072890c7b05f274215a24f17449655ccb2c8af"
}
```

## Confidence

**High** — The repository is owned by The League of Moveable Type with Barry Schwartz as the credited designer, matching the designer field in METADATA.pb. UFO sources are present. The repository description matches the font description exactly.
