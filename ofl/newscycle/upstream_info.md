# News Cycle — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The authoritative upstream source for News Cycle is hosted on **Launchpad** under the Bazaar VCS, not GitHub.

- **Project page**: https://launchpad.net/newscycle
- **Branch**: https://code.launchpad.net/~n8/newscycle/trunk (`lp:newscycle`)
- **Designer**: Nathan Willis (nwillis@glyphography.com)
- **Latest revision**: #165 (2015-10-03), commit message: "Syncing minor updates."
- **Latest release**: v0.5.2 (2015-07-30), download: `newscycle-0.5.2.zip`

A GitHub mirror exists at https://github.com/typesource/newscycle but it is a single-commit clone from the old Google Font Directory on Google Code (clone date 2014-01-22) and does not reflect upstream development. It contains only TTF binaries and a `src/` directory with metadata comments and a subsetting shell script — no font source masters.

No active GitHub repository by Nathan Willis was found.

## Source Files

The Launchpad release archive (`newscycle-0.5.2.zip`) contains only TTF binaries (Regular and Bold). No editable source masters (.sfd, .ufo, .glyphs) are distributed in the release download. The Bazaar branch at `lp:newscycle` may contain source files but the Launchpad file browser returned 404 errors; the branch has 165 revisions and is browsable by cloning via `bzr branch lp:newscycle`.

The version in Google Fonts (Regular and Bold TTF) appears to correspond to the v0.5.2 release. The copyright string names Nathan Willis at nwillis@glyphography.com.

## Build System

No build system (Makefile, build script, config.yaml) is present in the GitHub mirror or in the release downloads. The Bazaar trunk branch may contain source-to-binary build tooling; this cannot be confirmed without cloning it locally.

## config.yaml Status

No `config.yaml` exists in the Google Fonts working copy for this family. None can be created until source masters are confirmed.

## Notes

- The upstream project has been dormant since October 2015 (165 revisions, last push 2015-10-03).
- The Launchpad Bazaar infrastructure is still accessible as of 2026-03-12.
- The AUR package (`newscycle-font`) confirmed the Launchpad download URL pattern: `https://launchpad.net/newscycle/trunk/$pkgver/+download/newscycle-$pkgver.zip`.
- Google Fonts carries Regular and Bold; the METADATA.pb also references Cyrillic, Greek, and Vietnamese subsets, which aligns with the project's stated goals. The font version in the GF binary is consistent with the 0.5.x release series.
- **Confidence**: Medium. The upstream repo location is confirmed (Launchpad) but source masters have not been directly inspected. A `bzr branch lp:newscycle` clone would be needed to verify source file contents before adding a `source` block to METADATA.pb.
