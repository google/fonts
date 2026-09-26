# News Cycle — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/newscycle/src/`
- **Buildable**: No — no font design sources in monorepo

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files in Monorepo

| File | Type |
|------|------|
| `subset.sh` | Subsetting shell script (build tooling, not a source file) |
| `OFLB-sample-image.svg` | Sample image (not a source file) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

No font design sources are present in the monorepo `src/` directory — only a subsetting script, a sample image, and metadata comments.

## Upstream on Launchpad

The authoritative upstream source for News Cycle is hosted on **Launchpad** under the Bazaar VCS:

- **Project page**: https://launchpad.net/newscycle
- **Branch**: https://code.launchpad.net/~n8/newscycle/trunk (`lp:newscycle`)
- **Designer**: Nathan Willis (nwillis@glyphography.com)
- **Latest revision**: #165 (2015-10-03), commit message: "Syncing minor updates."
- **Latest release**: v0.5.2 (2015-07-30), download: `newscycle-0.5.2.zip`

The Launchpad release archive (`newscycle-0.5.2.zip`) contains only TTF binaries (Regular and Bold). The Bazaar branch at `lp:newscycle` has 165 revisions and may contain editable source files, but they have not been directly inspected. A `bzr branch lp:newscycle` clone would be needed to verify source file contents.

A GitHub mirror exists at https://github.com/typesource/newscycle but it is a single-commit clone from the old Google Font Directory on Google Code (2014-01-22) and does not reflect upstream development.

## Build System

No build system (Makefile, build script, config.yaml) is present in the monorepo, the GitHub mirror, or the release downloads.

## config.yaml

Does not exist. Cannot be created until source masters are confirmed from the Launchpad Bazaar branch.

## Notes

- The upstream project has been dormant since October 2015 (165 revisions, last push 2015-10-03).
- The Launchpad Bazaar infrastructure was still accessible as of 2026-03-12.
- The AUR package (`newscycle-font`) confirmed the Launchpad download URL pattern: `https://launchpad.net/newscycle/trunk/$pkgver/+download/newscycle-$pkgver.zip`.
- Google Fonts carries Regular and Bold; the METADATA.pb references Cyrillic, Greek, and Vietnamese subsets.
- The font version in Google Fonts is consistent with the 0.5.x release series.
- **Confidence**: Medium. The upstream repo location is confirmed (Launchpad) but source masters have not been directly inspected.
