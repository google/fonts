# Zen Kurenaido — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Zen Kurenaido was identified as [https://github.com/googlefonts/zen-kurenaido](https://github.com/googlefonts/zen-kurenaido), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zen-kurenaido` was queried via the GitHub API to retrieve the latest commit on the `main` branch.

The latest commit on `main` was identified as `cd751ced55d4ebb1fb2fbd90602eb9351dd03fd6`, authored on 2024-08-02, with message: "Update AUTHORS.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zen-kurenaido
Commit: cd751ced55d4ebb1fb2fbd90602eb9351dd03fd6
Branch: main
Status: commit hash added
Confidence: high (verified via GitHub API)
```
