# Philosopher — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Philosopher was identified at https://github.com/alexeiva/philosopher, maintained by Alexei Vanyashin under the `alexeiva` GitHub account. The METADATA.pb file referenced commit `9983715d443b6be727d886cd16bce241cf9ad0b7` on the `master` branch, with build configuration at `sources/config.yaml`.

## Font Description

Philosopher is a humanist sans-serif typeface designed by Jovanny Lemonad, with later maintenance by Alexei Vanyashin. The font covers Latin, Cyrillic (including Extended), and Vietnamese scripts. It is available in four styles: Regular, Italic, Bold, and Bold Italic. Originally added to Google Fonts in 2011, it is one of the earlier catalog entries.

## Designer

Jovanny Lemonad is the original designer. The repository is maintained by Alexei Vanyashin (`alexeiva`), a type engineer who has worked on several Cyrillic-extended Google Fonts. The copyright dates to 2011.

## Repository

- **URL**: https://github.com/alexeiva/philosopher
- **Commit**: `9983715d443b6be727d886cd16bce241cf9ad0b7`
- **Branch**: `master`
- **Config**: `sources/config.yaml`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | SANS_SERIF |
| Styles | Regular, Italic, Bold, Bold Italic |
| Subsets | latin, latin-ext, cyrillic, cyrillic-ext, vietnamese |
| Variable | No |

## File Mapping

The source block specified explicit file mappings for all four font files (`Philosopher-Regular.ttf`, `Philosopher-Italic.ttf`, `Philosopher-Bold.ttf`, `Philosopher-BoldItalic.ttf`), as well as `OFL.txt` and `DESCRIPTION.en_us.html`, all sourced from the `fonts/ttf/` directory of the upstream repository.

## Confidence

**High** — The repository is referenced directly in both the METADATA.pb `repository_url` and the copyright notice. The commit and branch are explicitly specified.
