# Mingzat — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/silnrsi/font-mingzat
- **Branch**: master
- **Commit (v1.100)**: `bfe7e714b737d9d0b3b43ad88e3b844449175560`
- **Latest tag**: v1.200 (`59ed20ce52c89b343fda8a0d338f24aaff6e952a`)

## Source Files

- `source/Mingzat.designspace` — designspace file
- `source/Mingzat-Regular.ufo` — UFO source with embedded `features.fea`
- Additional OpenType feature sources in `source/opentype/`

## Build System

- **Smith** (SIL's font build tool), configured via `wscript`
- The `config.yaml` in google/fonts already points to `source/Mingzat.designspace`, which allows Google Fonts infrastructure to rebuild from source using fontmake/fontc.

## config.yaml

Already present and correct — points to `sources: [source/Mingzat.designspace]`. No changes needed.

## Notes

- The METADATA.pb references the v1.100 release archive. A newer release (v1.200) exists upstream. The current enrichment adds the commit hash for the version currently served by Google Fonts (v1.100).
- The archive URL (`https://github.com/silnrsi/font-mingzat/releases/download/v1.100/Mingzat-1.100.zip`) was verified accessible (HTTP 302 redirect to GitHub asset CDN, as expected).
- The repository URL (`https://github.com/silnrsi/font-mingzat`) was verified accessible (HTTP 200).

## Confidence

**High** — The v1.100 tag clearly corresponds to the release archive referenced in METADATA.pb. The commit hash is unambiguous.
