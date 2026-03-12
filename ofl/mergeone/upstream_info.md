# Merge One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

No public upstream source repository was found for Merge One.

Searches conducted:
- GitHub search for `kosal sen font`, `MergeOne font`, `philatype`, `merge one font` — all returned 0 results.
- GitHub user `kosal-sen` exists but has no public repositories.
- GitHub org `philatype` does not exist.
- `github.com/googlefonts/mergeone` — 404 Not Found.
- `github.com/googlefonts/MergeOne` — 404 Not Found.
- `philatype.com` website lists Merge (and commercial Merge Pro) but links to no source repository; the font is also sold commercially under a proprietary license on the same site.

The font was added to Google Fonts on 2012-10-05, predating the common practice of maintaining open source font development on GitHub. The only upstream contact information embedded in the font and FONTLOG is `holla@philatype.com` and `http://www.philatype.com`.

## Source Files

No upstream source files (UFO, Glyphs, FontForge, etc.) have been located. The Google Fonts distribution contains only the compiled binary:

- `MergeOne-Regular.ttf` — single weight, Regular (400), normal style

The font covers Latin and Latin Extended subsets.

## Build System

Unknown. No build scripts, source files, or tooling configuration were found. No `Makefile`, `build.sh`, or Python build scripts are accessible.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/mergeone/`. None can be created without a known upstream source repository.

## Notes

- The copyright string embedded in the font reads: `Copyright (c) 2012, Kosal Sen, Philatype (holla@philatype.com), with Reserved Font Name 'Merge'`. The reserved name is `Merge`, not `Merge One`.
- The Philatype website (`philatype.com`) sells a commercial version called "Merge Pro" with additional weights (Regular, Bold, Black), suggesting the OFL release of Merge One (Light weight) was an intentional partial open-source release.
- The font family has not been updated since its initial release in October 2012. There is no evidence of active maintenance.
- Designer Kosal Sen's GitHub account (`github.com/KosalSen`) exists but has zero public repositories.
- **Confidence**: No upstream repo exists publicly. This family likely has no accessible source repository that would enable a rebuild or update via standard Google Fonts tooling.
- If source files are desired, direct outreach to `holla@philatype.com` would be necessary.
