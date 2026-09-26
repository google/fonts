# ZCOOL XiaoWei — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for ZCOOL XiaoWei was identified as [https://github.com/googlefonts/zcool-xiaowei](https://github.com/googlefonts/zcool-xiaowei), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zcool-xiaowei` was queried via the GitHub API to retrieve the latest commit on the default (`main`) branch.

The latest commit on `main` was identified as `e94fc01eed059b3396129a48f756a46f7737fe2f`, authored on 2018-12-05, with message: "append ZCOOL".

Note: The copyright notice in METADATA.pb listed a different URL (`https://www.github.com/googlefonts/xiaowei`), but the `repository_url` field correctly points to `https://github.com/googlefonts/zcool-xiaowei`.

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zcool-xiaowei
Commit: e94fc01eed059b3396129a48f756a46f7737fe2f
Branch: main (default)
Status: commit hash added
Confidence: high (verified via GitHub API)
```
