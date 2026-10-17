# Zen Maru Gothic — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Zen Maru Gothic was identified as [https://github.com/googlefonts/zen-marugothic](https://github.com/googlefonts/zen-marugothic), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zen-marugothic` was queried via the GitHub API to retrieve the latest commit on the `main` branch.

The latest commit on `main` was identified as `553c872b216d1290e2902a466edcdc9682f0df6a`, authored on 2024-08-02, with message: "Update AUTHORS.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zen-marugothic
Commit: 553c872b216d1290e2902a466edcdc9682f0df6a
Branch: main
Status: commit hash added
Confidence: high (verified via GitHub API)
```
