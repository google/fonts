# Raleway — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/theleagueof/raleway
- **Commit**: `7b288c6faaed52cd237ec3a2e82c637d2a941fa7`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
Designed by Matt McInerney, Pablo Impallari, and Rodrigo Fuenzalida. Originally a single thin weight by McInerney, later expanded into a full variable family. Hosted under The League of Moveable Type organization. Sans-serif variable font with a weight (wght) axis from 100 to 900. Supports Cyrillic, Cyrillic Extended, Latin, Latin Extended, and Vietnamese subsets.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the pinned commit was not usable: it is either absent from the repository (a phantom/deleted hash) or predates the declared source, so the source could not be found.

Corrected the METADATA.pb source block:
- commit: `7b288c6faaed52cd237ec3a2e82c637d2a941fa7` → `938ac770222935d0d9d7b7b60e9373afd0cc5543` (2020-08-26)  (repository_url unchanged: `https://github.com/theleagueof/raleway`)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The shipped binary's exact build commit is not recoverable from the current upstream, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.
