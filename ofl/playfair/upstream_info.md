# Playfair — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Playfair was investigated. The upstream repository is hosted at https://github.com/googlefonts/Playfair and the pinned commit is `a49f9f9dc9a2924641cefba3f5e33ac1c5aa4264` on the `master` branch.

## Font Description

Playfair is a transitional serif display typeface designed by Claus Eggers Sørensen. It was initially published in 2011 and had a major update in 2017. In 2023, a complete redesign was released as a variable font, adding an optical size axis (`opsz`) that allows the design to be used across both body text and display sizes.

The design takes influence from the work of John Baskerville and from Scotch Roman letterforms, reflecting the typographic conventions of the European Enlightenment — a period when broad nib quills gave way to pointed steel pens, enabling high-contrast letterforms with delicate hairlines.

## Repository

- **Repository**: https://github.com/googlefonts/Playfair
- **Commit**: `a49f9f9dc9a2924641cefba3f5e33ac1c5aa4264`
- **Branch**: master
- **Config**: `sources/config.yaml`

## Font Files

The Google Fonts distribution included two variable font files:
- `Playfair[opsz,wdth,wght].ttf` — upright variable font
- `Playfair-Italic[opsz,wdth,wght].ttf` — italic variable font

## Axes

| Axis | Min | Max |
|------|-----|-----|
| opsz | 5.0 | 1200.0 |
| wdth | 87.5 | 112.5 |
| wght | 300.0 | 900.0 |

## Scripts and Subsets

The font supported Cyrillic, Cyrillic Extended, Latin, Latin Extended, and Vietnamese character sets.

## Designer

Claus Eggers Sørensen, type designer based in Amsterdam, Netherlands.

## License

Open Font License (OFL).

## Notes

The copyright notice in the italic font file referenced `https://github.com/googlefonts/Playfair`, while the upright referenced `https://github.com/clauseggers/Playfair`. The repository URL in the source block pointed to the googlefonts mirror. The family is a successor to Playfair Display, with the older family remaining on Google Fonts for backward compatibility.
