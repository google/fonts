# Parastoo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Parastoo was identified at https://github.com/googlefonts/parastoo-font, hosted under the `googlefonts` GitHub organization. The METADATA.pb file referenced commit `80a254f68aa51a80a97e33218e3e23e9d3229b10` on the `master` branch, with build configuration at `sources/config.yaml`. The font was added to Google Fonts on 2025-05-22.

## Font Description

Parastoo is an Arabic-script typeface with Latin support, designed by Saber Rastikerdar. It is primarily intended for Persian (Farsi) text and is classified as a serif typeface. The font supports a weight axis from 400 (Regular) to 700 (Bold), making it a variable font. The name "Parastoo" (پرستو) means "swallow" (the bird) in Persian.

## Designer

Saber Rastikerdar is the designer. The copyright dates to 2016, indicating the project originated well before its addition to Google Fonts.

## Repository

- **URL**: https://github.com/googlefonts/parastoo-font
- **Commit**: `80a254f68aa51a80a97e33218e3e23e9d3229b10`
- **Branch**: `master`
- **Config**: `sources/config.yaml`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | SERIF |
| Primary Script | Arabic (Arab) |
| Primary Language | Persian (fa_Arab) |
| Stroke | SERIF |
| Weight Axis | 400–700 |
| Subsets | arabic, latin, latin-ext, vietnamese |
| Variable | Yes (wght) |

## File Mapping

The source block specified explicit file mappings: `OFL.txt`, `fonts/variable/Parastoo[wght].ttf`, `article/ARTICLE.en_us.html`, and `article/sample.png` were all mapped from the upstream repository.

## Confidence

**High** — The repository is hosted under the `googlefonts` organization. The commit is explicitly referenced and the copyright notice matches the repository URL.
