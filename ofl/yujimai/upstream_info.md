# Yuji Mai — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Yuji Mai was identified as [https://github.com/Kinutafontfactory/Yuji](https://github.com/Kinutafontfactory/Yuji), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `Kinutafontfactory/Yuji` was queried via the GitHub API to retrieve the latest commit on the `master` branch. The repository hosts multiple Yuji typeface variants (Hentaigana Akari, Hentaigana Akebono, Mai, and Syuku) in a single monorepo.

The latest commit on `master` was identified as `efec977b14b57c19eb85d468edcfbbad13139e67`, authored on 2021-09-27, with message: "Merge pull request #5 from aaronbell/master — Decomposing transformed components".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/Kinutafontfactory/Yuji
Commit: efec977b14b57c19eb85d468edcfbbad13139e67
Branch: master
Status: commit hash added
Confidence: high (verified via GitHub API)
```
