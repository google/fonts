# Playfair Display SC — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Playfair Display SC was investigated. The upstream repository is hosted at https://github.com/clauseggers/Playfair and the pinned commit is `80a334101928546b04fa9e709ad4b2f11f8a9e10` — the same commit as its sibling family Playfair Display.

## Font Description

Playfair Display SC is the small-caps sibling family of Playfair Display, sharing the same upstream repository and designer. It was added to Google Fonts on 2012-10-26 as a dedicated small-caps family. The design features the same high-contrast transitional serif aesthetic as Playfair Display, optimized for small capitals usage.

Unlike the main Playfair Display family, this family was distributed as static (non-variable) fonts across three weights (Regular, Bold, Black) in both upright and italic styles, providing six font files total.

## Repository

- **Repository**: https://github.com/clauseggers/Playfair
- **Commit**: `439686b0f8b056caa5ccc181fd0ea8c4397229bb`
- **Config**: `sources/config.yaml`

## Font Files

The Google Fonts distribution included six static font files:
- `PlayfairDisplaySC-Regular.ttf`
- `PlayfairDisplaySC-Italic.ttf`
- `PlayfairDisplaySC-Bold.ttf`
- `PlayfairDisplaySC-BoldItalic.ttf`
- `PlayfairDisplaySC-Black.ttf`
- `PlayfairDisplaySC-BlackItalic.ttf`

## Scripts and Subsets

The font supported Cyrillic, Latin, Latin Extended, and Vietnamese character sets.

## Designer

Claus Eggers Sørensen, type designer based in Amsterdam, Netherlands.

## License

Open Font License (OFL). Reserved Font Name: "Playfair Display".

## Notes

This family shared the same upstream repository and pinned commit as Playfair Display (`clauseggers/Playfair`). It was the only family in this investigation batch distributed as static (non-variable) fonts at the time of the metadata snapshot. The source block did not specify an explicit `branch` or `files` mapping, relying on the config.yaml for build instructions.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`80a33410`](https://github.com/clauseggers/Playfair/commit/80a33410) (tag 2.203, the Playfair 2 family) to [`439686b0`](https://github.com/clauseggers/Playfair/commit/439686b0) ("Regenerated fonts", 2017-11-03), which is on `master` and in every tag from 1.201 on. [google/fonts#1299](https://github.com/google/fonts/pull/1299) ([google/fonts `c0b8d90a`](https://github.com/google/fonts/commit/c0b8d90a)) added v1.200 the same day.

The six shipped TTFs are byte-identical to `fonts/GF_TTF/PlayfairDisplaySC-*.ttf` at `439686b0`: Regular md5 `0b245014684dc4a1c82f60e12bb73b94`, Italic `7358a2d2d45b8ecb812c7440ab3aba47`, Bold `70411fcb5f728dd858c916adee3ce0ac`, BoldItalic `2c9fb2b5388ed1575ce8d743e08c19b4`, Black `b88a997bc470f06138f8a84763d00894`, BlackItalic `9786f1c14d237c7d12ff9870d4ae5237`. They are Glyphs.app exports of the "Playfair Display SC" instances in `sources/Playfair-Display-Roman.glyphs` and `-Italic.glyphs` (with Rename Glyphs and Remove Glyphs parameters), post-processed by `sources/generate_gf_version.py`. The 1.200 tag, [`eb6b6988`](https://github.com/clauseggers/Playfair/commit/eb6b6988), is a sibling commit: it lacks Marc Foley's GF-spec edits to both Glyphs sources and does not carry these binaries. The "Fixed ligatures containing j" commits that followed changed the sources without regenerating them.

`439686b0` has no `sources/config.yaml`, so `config_yaml` was dropped from METADATA.pb and an override `config.yaml` names both Glyphs sources.
