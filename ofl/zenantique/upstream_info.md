# Zen Antique — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Zen Antique was identified as [https://github.com/googlefonts/zen-antique](https://github.com/googlefonts/zen-antique), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zen-antique` was queried via the GitHub API to retrieve the latest commit on the `main` branch. The repository also hosts Zen Antique Soft.

The latest commit on `main` was identified as `3521a97dfa21d4c985725be88e9beb5edef517b9`, authored on 2024-08-02, with message: "Update AUTHORS.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zen-antique
Commit: 3521a97dfa21d4c985725be88e9beb5edef517b9
Branch: main
Status: commit hash added
Confidence: high (verified via GitHub API)
```
