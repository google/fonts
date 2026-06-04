# Preahvihear — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Preahvihear was investigated. The upstream repository is hosted at https://github.com/danhhong/Preahvihear and the pinned commit is `86b9102c4580df7b52e3320d835ab2ded591dd15` on the `master` branch.

## Font Description

Preahvihear is a Khmer display typeface designed by Danh Hong. It was added to Google Fonts on 2011-03-02, making it one of the earliest Khmer fonts in the catalog. The font was designed for use in headlines, titles, subtitles, and banner designs. The copyright year in the font files was 2020, suggesting a substantial revision or re-release after the initial addition.

The typeface was named after Preah Vihear, a significant Khmer temple site in Cambodia.

## Repository

- **Repository**: https://github.com/danhhong/Preahvihear
- **Commit**: `86b9102c4580df7b52e3320d835ab2ded591dd15`
- **Branch**: master
- **Config**: `Source/builder.yaml`

## Font Files

The Google Fonts distribution included one static font file:
- `Preahvihear-Regular.ttf`

The source files mapping pointed to `Release/ttf/Preahvihear-Regular.ttf` in the repository.

## Scripts and Subsets

The font supported Khmer and Latin character sets. The primary script was Khmer (`Khmr`).

## Designer

Danh Hong.

## License

Open Font License (OFL).

## Notes

The config file used an unusual path (`Source/builder.yaml`) rather than the more conventional `sources/config.yaml`. The repository was hosted under the `danhhong` personal GitHub account. The `config_yaml` field in the source block pointed to `Source/builder.yaml`, while the files mapping explicitly listed the TTF source path under `Release/ttf/`.
