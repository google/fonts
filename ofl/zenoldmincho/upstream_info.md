# Zen Old Mincho — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Zen Old Mincho was identified as [https://github.com/googlefonts/zen-oldmincho](https://github.com/googlefonts/zen-oldmincho), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zen-oldmincho` was queried via the GitHub API to retrieve the latest commit on the `main` branch.

The latest commit on `main` was identified as `490d363e7886839ba1f86971cf874a1d70ad27f0`, authored on 2024-08-02, with message: "Update AUTHORS.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zen-oldmincho
Commit: 490d363e7886839ba1f86971cf874a1d70ad27f0
Branch: main
Status: commit hash added
Confidence: high (verified via GitHub API)
```
