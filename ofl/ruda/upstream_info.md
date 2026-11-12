# Ruda — Upstream Source Investigation

**Designer**: Mariela Monsalve, Angelina Sanchez
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at `m4rc1e/Ruda-new` containing a Glyphs source file. The METADATA.pb was updated with the source block.

## Investigation

The METADATA.pb copyright line referenced `https://github.com/marmonsalve/Ruda-new` as the upstream source, but that repository does not exist on GitHub.

The repository `m4rc1e/Ruda-new` was found to be a non-fork repository containing a Glyphs source file (`Ruda_new.glyphs`) and a README. Examination of the commit history confirmed that the designer marmonsalve (Mariela Monsalve) committed directly to this repository, making it the canonical upstream despite being hosted under a different GitHub user's namespace.

## Repository Details

| Field | Value |
|-------|-------|
| Repository | https://github.com/m4rc1e/Ruda-new |
| Source format | Glyphs (`Ruda_new.glyphs`) |
| Latest commit | `a63532e04ffb0f46b635cf9e000966155958e19d` |
| Commit date | 2018-05-04 |
| Commit author | marmonsalve |
| Is fork | No |

## Changes Made

Added `source` block to `ofl/ruda/METADATA.pb`:

```
source {
  repository_url: "https://github.com/m4rc1e/Ruda-new"
  commit: "a63532e04ffb0f46b635cf9e000966155958e19d"
}
```

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/ruda/` referencing the upstream gftools-builder-compatible source at the pinned commit `a63532e` (`Ruda_new.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source repository and pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The source block moved from `m4rc1e/Ruda-new` at [`a63532e0`](https://github.com/m4rc1e/Ruda-new/commit/a63532e0) (the designer's 2018 v1.0 Glyphs upload, whose masters are incompatible) to `aaronbell/Ruda-new` at [`0a66529f`](https://github.com/aaronbell/Ruda-new/commit/0a66529f) ("Rebuilding static instances with autohinting", 2021-07-22, on the fork's `master`).

The shipped `Ruda[wght].ttf` (v2.001, [google/fonts#3652](https://github.com/google/fonts/pull/3652), [google/fonts `b275aee5`](https://github.com/google/fonts/commit/b275aee5)) is byte-identical to `fonts/variable/Ruda[wght].ttf` at `0a66529f` (md5 `5386bebf2c7be5c4458c8f7330496a42`). The fork descends from TypeNetwork/Ruda-new, where the masters were made compatible as UFOs ([`795097ef`](https://github.com/aaronbell/Ruda-new/commit/795097ef)); the designer's own repository is gone ([google/fonts#9393](https://github.com/google/fonts/issues/9393)). The only later commit in the fork edits the README.

`Ruda_new.glyphs` does not exist in the fork, so the override `config.yaml` now names `sources/Ruda.designspace`, the source the fork's own `sources/config.yaml` builds.
