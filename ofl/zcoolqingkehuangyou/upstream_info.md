# ZCOOL QingKe HuangYou — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for ZCOOL QingKe HuangYou was identified as [https://github.com/googlefonts/zcool-qingke-huangyou](https://github.com/googlefonts/zcool-qingke-huangyou), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zcool-qingke-huangyou` was queried via the GitHub API to retrieve the latest commit on the default (`main`) branch.

The latest commit on `main` was identified as `c9dac424b0a9f47d3b113cff4a4922f632d82c94`, authored on 2018-11-20, with message: "First commit". This repository has had no commits since its initial creation.

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zcool-qingke-huangyou
Commit: c9dac424b0a9f47d3b113cff4a4922f632d82c94
Branch: main (default)
Status: commit hash added
Confidence: high (verified via GitHub API)
```
