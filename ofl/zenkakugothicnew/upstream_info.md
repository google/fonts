# Zen Kaku Gothic New — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Zen Kaku Gothic New was identified as [https://github.com/googlefonts/zen-kakugothic](https://github.com/googlefonts/zen-kakugothic), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zen-kakugothic` was queried via the GitHub API to retrieve the latest commit on the `main` branch. The repository hosts both Zen Kaku Gothic Antique and Zen Kaku Gothic New.

The latest commit on `main` was identified as `2705757e17e42954f3acbdf921ac0ae24d1270cd`, authored on 2024-08-02, with message: "Update AUTHORS.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zen-kakugothic
Commit: 2705757e17e42954f3acbdf921ac0ae24d1270cd
Branch: main
Status: commit hash added
Confidence: high (verified via GitHub API)
```
