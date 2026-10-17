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

## Recent upstream/main activity (post-investigation)

The original investigation predicted that v1.200 would be a future onboarding. That onboarding has now landed:

- **2026-03-06** — Emma Marichal, commit [`5120f9830`](https://github.com/google/fonts/commit/5120f9830) ("Mingzat: Version 1.200 added"): advanced the recorded commit and binaries to v1.200. METADATA.pb at HEAD now reads:
  - `commit`: `613ac08e03fe5cecd4a3cdb636775f4ce33225dd` (was the placeholder for v1.100; now the upstream HEAD as of v1.200 release)
  - `archive_url`: `https://github.com/silnrsi/font-mingzat/releases/download/v1.200/Mingzat-1.200.zip` (was v1.100)
  - File mappings now reference `Mingzat-1.200/...` paths (was `Mingzat-1.100/...`)

The v1.200 tag itself points to `59ed20ce52c89b343fda8a0d338f24aaff6e952a` (an earlier commit on `master`); the recorded `613ac08e0` is HEAD-after-tag (Lorna Evans, "Prep for subsequent development."). The shipping `Mingzat-Regular.ttf` (159916 bytes, md5 `f8675f56bf966b5598e88481f0e4acb6`) is byte-identical to upstream `references/Mingzat-Regular.ttf` AND `references/v1.200/Mingzat-Regular.ttf` at commit `613ac08e0`. `head.fontRevision = 1.2000`, `name` ID 5 = "Version 1.200".

### Updated source-of-truth fields (post-onboarding)

- **Repository URL**: https://github.com/silnrsi/font-mingzat (unchanged)
- **Branch**: `master` (unchanged)
- **Commit**: `613ac08e03fe5cecd4a3cdb636775f4ce33225dd`
- **Archive URL**: `https://github.com/silnrsi/font-mingzat/releases/download/v1.200/Mingzat-1.200.zip`
- **Override config.yaml**: present in `ofl/mingzat/config.yaml` (unchanged from earlier)
