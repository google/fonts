# Metal Mania — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/metalmania
- **Status**: Archived / inactive — last commit 2014-10-17, no activity since
- **Default branch**: `master`
- **Latest commit**: `7f5e5a82` (2014-10-17) — "update .travis.yml"
- **First commit**: `10c6697f` (2014-07-16) — "Move metalmania font files to separate repository"
- **Total commits**: 11

The designer, Dathan Boardman (Open Window), has a GitHub account at https://github.com/dathanboardman, but it has 0 public repositories. The `librefonts/metalmania` repo was created and maintained by a third party (Mikhail Kashkin / hash3g) as part of the `librefonts` infrastructure, not by the original designer.

The FONTLOG.txt references a Google+ profile (`https://profiles.google.com/openwindowfonts/about`) that no longer exists (404).

## Source Files

The repo's `src/` directory contains:
- `MetalMania-Regular-TTF.vfb` — FontLab Studio binary source file (300 KB), the original master
- `METADATA_comments.txt` — internal notes about subsetting operations
- `VERSIONS.txt` — records version 1.002 of MetalMania-Regular.ttf

The root of the repository contains TTX-format table dumps (`MetalMania-Regular.ttf.*.ttx`) generated from the binary, which serve as human-readable representations but are not the authoritative sources.

## Build System

The repository used **fontbakery-build.py** (the 2014-era build pipeline), invoked via Travis CI:

```
fontbakery-build.py . 2>&1 | tee -a builds/build/buildlog.txt
```

Dependencies at the time included FontForge (for VFB reading), ttfautohint, fontTools, fontcrunch, and jinja2. This build system is entirely obsolete — fontbakery-build.py no longer exists in the current fontbakery codebase, and `.vfb` files require FontLab Studio 5 to open natively. There is no UFO or Glyphs source.

## config.yaml Status

No `config.yaml` exists in the repository or in `/mnt/shared/google/fonts/ofl/metalmania/`. The font predates the current Google Fonts build infrastructure (gftools/fontmake era) and has never been set up for automated rebuilding.

## Notes

- The font was added to Google Fonts on 2012-07-11 and has not been updated since (still at version 1.002 from August 2012).
- The only authoritative source is the `.vfb` FontLab binary, which is not editable without FontLab Studio 5. Conversion to a modern open format (UFO or Glyphs) would be required for any future rebuild or update.
- The `librefonts` organization on GitHub appears to have been an early Google Fonts infrastructure project that is no longer active. The repo has no issues, no PRs, and no forks.
- No upstream source is maintained by the original designer. This family should be considered **orphaned** with no active upstream.
- Confidence in the repo identification is **high** — the `.vfb` filename matches the FONTLOG description exactly ("MetalMania-Regular-TTF.vfb TrueType outlines with hinting adjustments corresponding to the TTF file"), and version 1.002 matches.
