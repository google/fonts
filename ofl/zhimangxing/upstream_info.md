**Model**: Claude Opus 4.6

# Zhi Mang Xing — Upstream Source Investigation

## Summary

The upstream source repository for Zhi Mang Xing was identified and a source block was added to `METADATA.pb`. Note that the font copyright string referenced `https://github.com/googlefonts/zhimangxing`, which does not exist; the actual source repository is at `m4rc1e/zhimangxing`.

## Repository

- **URL**: https://github.com/m4rc1e/zhimangxing
- **Owner**: Marc Foley (m4rc1e)
- **Designer**: Wei Zhimang
- **Source format**: Glyphs (`ZhiMangXing.glyphs`)
- **Branch**: master
- **Commit**: `15cb1b0d4c78da973e8459a8e2f23a9aef00d8a6`
- **Commit date**: 2019-05-08
- **Commit message**: "uncamelcase name"

## Investigation Notes

The repository was found at `m4rc1e/zhimangxing`. The `sources/` directory contained `ZhiMangXing.glyphs` along with a `build.sh` script and `requirements.txt`. The repository is not a fork. The copyright string in METADATA.pb referenced `https://github.com/googlefonts/zhimangxing`, but that URL returned a 404 — this appears to be a stale URL from a planned but never-created googlefonts mirror. Marc Foley is a Google Fonts engineer who developed and maintained the build tooling for this font. No other repository with the original Chinese calligraphy source was found.

## Confidence

Medium — the `m4rc1e/zhimangxing` repository is the only known source with a Glyphs file for this font, and Marc Foley is a known contributor to Google Fonts tooling. However, the true origin from calligrapher Wei Zhimang could not be traced to a public repository.
