# Roboto Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/RobotoMono
- **Commit**: `111eb14e367888c9374da4da0b018e72cf8ac46d`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
Designed by Christian Robertson. A monospace variable font with a weight axis from 100 to 700, available in upright and italic styles. Licensed under Apache 2.0 (not OFL). Covers Cyrillic, Cyrillic Extended, Greek, Latin, Latin Extended, and Vietnamese subsets.

## Recent upstream/main activity (post-investigation)

The Apache 2.0 vs OFL note above was based on the upstream repo's `LICENSE` file. However, the google/fonts catalog distributes Roboto Mono under OFL, and the METADATA.pb `license` field was corrected to reflect that:

- **2026-02-09** — Aaron Bell, commit [`21406e8f5`](https://github.com/google/fonts/commit/21406e8f5) ("Fixing license in Roboto Mono"): changed the `license` field in METADATA.pb from `"APACHE2"` to `"OFL"`. The family directory has always been `ofl/robotomono/` (the directory naming reflects the catalog's licensing of the family), but the METADATA.pb `license` field had drifted. Aaron's fix re-aligns the field with the catalog convention.

Edit is outside the `source { ... }` block; the `repository_url`, `commit`, and `config_yaml` fields are unchanged.
