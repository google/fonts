**Model**: Claude Opus 4.6

## Unna

**Designer**: Omnibus-Type
**License**: OFL
**Category**: SERIF

### Upstream Repository

The canonical upstream repository for Unna was identified at **https://github.com/Omnibus-Type/Unna**, maintained by the Omnibus-Type foundry. The repository contained Glyphs source files (`Unna.glyphs` and `Unna Italic.glyphs`) in the `sources/` directory, confirming it as the primary source of truth for the font.

### Source Files

The repository contained:
- `sources/Unna.glyphs` — Glyphs source for regular and bold upright styles
- `sources/Unna Italic.glyphs` — Glyphs source for italic styles
- `fonts/` — compiled TTF output files
- `docs/` — specimen documentation

### Investigation Notes

The repository was located by searching for the Omnibus-Type organization on GitHub, which manages many of its Google Fonts contributions under the [Omnibus-Type](https://github.com/Omnibus-Type) organization. The email address `omnibus.type@gmail.com` in the copyright string matched the organization's known contact. The repository was last updated in July 2019.

**Repo**: https://github.com/Omnibus-Type/Unna
**Commit**: ff1d2046ceeb64bca7410573ef7af2744596825d
**Status**: Glyphs sources present
**Confidence**: High

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/unna/` referencing the upstream gftools-builder-compatible source at the pinned commit `826be2a` (`sources/Unna.glyphs`, `sources/Unna Italic.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`826be2ab`](https://github.com/Omnibus-Type/Unna/commit/826be2ab) (the 2019 v2.008 expansion, never onboarded) to [`ff1d2046`](https://github.com/Omnibus-Type/Unna/commit/ff1d2046) ("sources | fonts: updated designer name and win asc", 2016-12-06, on `master` through the merge [`24c4c3e9`](https://github.com/Omnibus-Type/Unna/commit/24c4c3e9)).

The four shipped v2.007 TTFs ([google/fonts#519](https://github.com/google/fonts/pull/519), [google/fonts `246377a5`](https://github.com/google/fonts/commit/246377a5)) are byte-identical to `fonts/Unna-*.ttf` as committed with both Glyphs sources in `ff1d2046`: Regular md5 `ed59380bfcb0c35c8dbebf5a3189fc8f`, Italic `7b5160b27c9da07075eb0cebbabac7c0`, Bold `f704e17e44550cc73b344f54de6aac95`, BoldItalic `f3728c4b26d473ac70566b0853521dc1`. The v2.008 expansion ([`f07e2404`](https://github.com/Omnibus-Type/Unna/commit/f07e2404)) deleted those binaries.

At `ff1d2046` the italic source is `sources/Unna-italic.glyphs`, not `sources/Unna Italic.glyphs`, so that path in the override `config.yaml` was corrected.
