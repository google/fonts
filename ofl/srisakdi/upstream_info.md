# Srisakdi — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/cadsondemak/Srisakdi
- **Commit**: `db08a3a88093caf28fddb5ec3e90825114c9ea8d`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/cadsondemak/Srisakdi was identified as the source for Srisakdi. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. No tagged releases were found in the repository.

## Build System
The repository contains a `source/` directory alongside pre-built fonts in the `fonts/` directory. The root directory also includes HTML, CSS, and JavaScript files consistent with a specimen website. No Makefile or explicit build script was found at the root level.

## Notes
Srisakdi is a Thai display typeface by Cadson Demak, available in Regular and Bold weights. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`fc86bd7f`](https://github.com/cadsondemak/Srisakdi/commit/fc86bd7f) (a 2024 "Fix t caron" commit that never shipped) to [`db08a3a8`](https://github.com/cadsondemak/Srisakdi/commit/db08a3a8), the merge of [PR #10](https://github.com/cadsondemak/Srisakdi/pull/10) (2018-08-24, on `master`), which is the commit named by [google/fonts `cb65e453`](https://github.com/google/fonts/commit/cb65e453) ("Updated fonts to avoid clipping").

The fonts uploaded in `cb65e453` are byte-identical to `fonts/Srisakdi-*.ttf` at `db08a3a8`. [google/fonts `d1834306`](https://github.com/google/fonts/commit/d1834306) ("unhinted fonts") then dehinted them: the shipped files lack cvt, fpgm, prep and glyph instructions, have no outline differences, and all other tables are byte-identical apart from name ID 5, head and maxp's hinting fields. md5 shipped vs upstream: Regular `ba1d593f3d55e36f1c236fbf79abf259` vs `2c53ab6d6d570fe96928bdcae5d37767`, Bold `927e1de7963ac74ce0cebf89e0fddd8c` vs `52a0a57e18859a747d83ba65b0d51021`.

The override `config.yaml` (`source/Srisakdi.glyphs`) resolves at `db08a3a8` and is not changed here.
