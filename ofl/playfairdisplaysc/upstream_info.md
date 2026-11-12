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
- **Commit**: `80a334101928546b04fa9e709ad4b2f11f8a9e10`
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
