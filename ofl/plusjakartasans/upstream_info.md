# Plus Jakarta Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Plus Jakarta Sans was investigated. The upstream repository is hosted at https://github.com/tokotype/PlusJakartaSans and the pinned commit is `18d1cd2f7ea10481919d2f05c1f7064b7307fc26` on the `master` branch.

## Font Description

Plus Jakarta Sans is a geometric sans serif variable font designed by Tokotype. The font was first created in 2020 and added to Google Fonts on 2022-03-24. It covered a weight range from ExtraLight (200) to ExtraBold (800) in both upright and italic styles.

The typeface was designed as a clean, modern sans serif with broad Latin and Latin Extended coverage, also including Cyrillic Extended and Vietnamese character sets, making it suitable for multilingual typographic use.

## Repository

- **Repository**: https://github.com/tokotype/PlusJakartaSans
- **Commit**: `18d1cd2f7ea10481919d2f05c1f7064b7307fc26`
- **Branch**: master
- **Config**: `sources/config.yaml`

## Font Files

The Google Fonts distribution included two variable font files:
- `PlusJakartaSans[wght].ttf` — upright variable font
- `PlusJakartaSans-Italic[wght].ttf` — italic variable font

## Axes

| Axis | Min | Max |
|------|-----|-----|
| wght | 200.0 | 800.0 |

## Scripts and Subsets

The font supported Cyrillic Extended, Latin, Latin Extended, and Vietnamese character sets.

## Designer

Tokotype (type foundry).

## License

Open Font License (OFL).

## Notes

The copyright year listed in the font files was 2020, consistent with the repository origin year. The repository was maintained under the tokotype GitHub organization.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`18d1cd2f`](https://github.com/tokotype/PlusJakartaSans/commit/18d1cd2f) (2024-01-18) to [`163c006f`](https://github.com/tokotype/PlusJakartaSans/commit/163c006f), the commit named by the packager commit [google/fonts `8cd7d0de`](https://github.com/google/fonts/commit/8cd7d0de) (v2.071, 2023-06-14). `18d1cd2f` merges the 2023 Cyrillic work ([`5854bde9`](https://github.com/tokotype/PlusJakartaSans/commit/5854bde9)), which changed `sources/PlusJakartaSans.glyphs` without rebuilding the variable fonts and never shipped. It was copied from fontc_crater's targets list in [google/fonts `5fa1b4a6`](https://github.com/google/fonts/commit/5fa1b4a6).

Both shipped VFs are byte-identical to `fonts/variable/` at `163c006f` (on `master`): roman md5 `6b68a2205325ea49b65af07e4061f320`, italic `2845d500918e26b7974665b40fc74f61`. `163c006f` merges PR #37 and has the same tree as [`6d4ffaf7`](https://github.com/tokotype/PlusJakartaSans/commit/6d4ffaf7) ("Fonts exported and tested"). The stale binaries are still present at `18d1cd2f`, so byte identity alone does not tell the two apart; the source change after `163c006f` does.

`sources/config.yaml` and the `files` paths exist at `163c006f`.
