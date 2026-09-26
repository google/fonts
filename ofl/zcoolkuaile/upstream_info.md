# ZCOOL KuaiLe — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for ZCOOL KuaiLe was identified as [https://github.com/googlefonts/zcool-kuaile](https://github.com/googlefonts/zcool-kuaile), which was already recorded in `METADATA.pb`. The source block was missing a `commit` field pointing to a specific upstream revision.

## Investigation

The repository at `googlefonts/zcool-kuaile` was queried via the GitHub API to retrieve the latest commit on the default (`main`) branch.

The latest commit on `main` was identified as `577cd45e035fa0cd27f74579de6ff47db62fde8c`, authored on 2026-01-30, with message: "Update OFL.txt".

## Result

The `commit` field was added to the `source` block in `METADATA.pb`:

```
Repo: https://github.com/googlefonts/zcool-kuaile
Commit: 577cd45e035fa0cd27f74579de6ff47db62fde8c
Branch: main (default)
Status: commit hash added
Confidence: high (verified via GitHub API)
```

## Recent upstream/main activity (post-investigation)

Three Aaron Bell commits affected the family between 2025-11-21 and 2026-01-29:

- **2025-11-21** — Aaron Bell, commit [`9b9bd8a16`](https://github.com/google/fonts/commit/9b9bd8a16) ("Update ZCOOLKuaiLe-Regular.ttf"): replaced the binary (3275404 → 1514832 bytes — substantial size reduction, likely subset/build optimisation). Binary-only commit; METADATA.pb untouched.
- **2026-01-29** — Aaron Bell, commit [`a606d6f31`](https://github.com/google/fonts/commit/a606d6f31) ("Updating the font to fix fonspector fails"): broader fix touching the binary, DESCRIPTION.en_us.html, OFL.txt, and METADATA.pb (B+D+L+M flags). Source block change was minor — not a `commit`/`repository_url` change but a sibling field tweak.
- **2026-01-29** — Aaron Bell, commit [`1874af3a7`](https://github.com/google/fonts/commit/1874af3a7) ("URL fix"): URL formatting cleanup in DESCRIPTION.en_us.html and OFL.txt.

The recorded `commit` field in METADATA.pb still refers to the post-onboarding upstream state; it has not advanced to reflect Aaron's local rebuild. Per the same pattern documented for Kurale, this is a known gap — the rebuild was done locally with post-processing, not pushed upstream, so the recorded commit identifies the *source state* but does not byte-reproduce the shipping binary.
