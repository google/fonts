# Yusei Magic — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Yusei Magic was identified as [https://github.com/tanukifont/YuseiMagic](https://github.com/tanukifont/YuseiMagic), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `tanukifont/YuseiMagic` was queried via the GitHub API to retrieve the latest commit on the `master` branch.

The latest commit on `master` was identified as `d622b0ea84059a411a1344bd2f948d9e0df92a1b`, authored on 2024-10-31, with message: "Update CONTRIBUTORS.txt — email".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/tanukifont/YuseiMagic
Commit: d622b0ea84059a411a1344bd2f948d9e0df92a1b
Branch: master
Status: commit hash added
Confidence: high (verified via GitHub API)
```

## Recent upstream/main activity (post-investigation)

- **2026-01-09** — evanwadams (Google), commit [`254f22c5e`](https://github.com/google/fonts/commit/254f22c5e) ("Update METADATA.pb (#10121)"): corrected the ISO 15924 script code in `primary_script` from `"Japn"` to `"Jpan"` (the canonical 4-letter code for Japanese). Edit is outside the `source { ... }` block; no source-block impact.
