# Playfair Display — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Playfair Display was investigated. The upstream repository is hosted at https://github.com/clauseggers/Playfair and the pinned commit is `80a334101928546b04fa9e709ad4b2f11f8a9e10`.

## Font Description

Playfair Display is a transitional serif typeface designed by Claus Eggers Sørensen. Originally published in 2011 and substantially updated in 2017, it became a variable font supporting a weight axis. The design takes influence from John Baskerville and Scotch Roman styles, embodying the high-contrast, refined aesthetic of 18th-century European typography. It was designed specifically for display use and succeeded in 2023 by the expanded Playfair variable family which added an optical size axis.

The family included a sibling small-caps family (Playfair Display SC) and its font files contained a full set of small caps, common ligatures, and discretionary ligatures.

## Repository

- **Repository**: https://github.com/aaronbell/Playfair-Display
- **Commit**: `e9c6c4f96e929d6b39cf13d8349816c4424e4254`
- **Config**: `sources/config.yaml`

## Font Files

The Google Fonts distribution included two variable font files:
- `PlayfairDisplay[wght].ttf` — upright variable font
- `PlayfairDisplay-Italic[wght].ttf` — italic variable font

## Axes

| Axis | Min | Max |
|------|-----|-----|
| wght | 400.0 | 900.0 |

## Scripts and Subsets

The font supported Cyrillic, Latin, Latin Extended, and Vietnamese character sets.

## Designer

Claus Eggers Sørensen, type designer based in Amsterdam, Netherlands.

## License

Open Font License (OFL). Reserved Font Name: "Playfair Display".

## Notes

The repository URL pointed to `clauseggers/Playfair`, the designer's personal repository, which served as the upstream source for both Playfair Display and Playfair Display SC. The family was first added to Google Fonts on 2011-11-16, making it one of the earlier entries in the catalog.

## Source repository and pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The source block moved from `clauseggers/Playfair` at [`80a33410`](https://github.com/clauseggers/Playfair/commit/80a33410) (tag 2.203) to `aaronbell/Playfair-Display` at [`e9c6c4f9`](https://github.com/aaronbell/Playfair-Display/commit/e9c6c4f9). `80a33410` builds the separate Playfair 2 family; it was copied from fontc_crater's targets list in [google/fonts `5fa1b4a6`](https://github.com/google/fonts/commit/5fa1b4a6).

The shipped v1.203 VFs came from Aaron Bell's conversion of the family to UFR ([google/fonts#3649](https://github.com/google/fonts/pull/3649), [google/fonts `1e1aa08e`](https://github.com/google/fonts/commit/1e1aa08e)). At `e9c6c4f9` ("Fixed weird kern value in Italics", 2021-09-30, the fork's `master` HEAD), `fonts/variable/PlayfairDisplay-Italic[wght].ttf` is byte-identical to the shipped Italic (md5 `a94bf8e2798ad379919855c03694568d`). The shipped Roman (md5 `038aec929d8d05c5de0bb20e040f9973`) is byte-identical to the one at [`49230566`](https://github.com/aaronbell/Playfair-Display/commit/49230566); `e9c6c4f9` only edits the Italic source before rebuilding, and its Roman differs from the shipped one only in head.modified and the checksum.

The fork's `sources/config.yaml` (family "Playfair Display", both Glyphs sources) is the file `config_yaml` already names, so no config change is needed.
