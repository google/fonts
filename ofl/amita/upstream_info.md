# Amita

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Eduardo Tunni, Brian Bonislawsky
**License**: OFL
**METADATA.pb**: `ofl/amita/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/etunni/Amita |
| Commit | `92680c07f01285a23744cda1190690c5c7f3f73c` |
| Config YAML | `sources/config.yaml` |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field.
- Commit date: 2023-02-01 13:08:50 -0300
- Commit message: "Merge pull request #7 from emmamarichal/master"

### Config YAML
Found `sources/config.yaml` in upstream repository at the recorded commit hash.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/etunni/Amita`
- `commit`: `92680c07f01285a23744cda1190690c5c7f3f73c`
- `config_yaml`: `sources/config.yaml`

### google/fonts history
- Last font modification: `c7beb6552615`
- Date: 2017-08-07 21:45:27 +0100
- Subject: "hotfix-amita: v1.004 added (#762)"

### Upstream repo cache
- Cached at: `etunni/Amita`
- Commit `92680c07f012` verified ✓

## Confidence

**High**: URL pre-existing in METADATA.pb; commit pre-existing in METADATA.pb

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`92680c07`](https://github.com/etunni/Amita/commit/92680c07) to [`bc05021c`](https://github.com/etunni/Amita/commit/bc05021c). `92680c07` (2023-02-01) merges a variable-font rework that was never onboarded; it was copied from fontc_crater's targets list in [google/fonts `19cdcec5`](https://github.com/google/fonts/commit/19cdcec5).

Google Fonts ships the 2015 static Regular and Bold ([google/fonts `7079657f`](https://github.com/google/fonts/commit/7079657f), 2015-05-19, hotfixed to v1.004 by [google/fonts#762](https://github.com/google/fonts/pull/762)). They are the `TTF/Amita-*.ttf` committed with `sources/Amita.glyphs` in [`4238b766`](https://github.com/etunni/Amita/commit/4238b766) ("New ttf fonts with scaled lowercases"). `bc05021c` (on `master`) is the merge a week later that only removed older TTFs; nothing else changed until 2023. Compared with the TTFs at `bc05021c`, the shipped fonts have identical outlines, hmtx, cmap, GDEF, maxp, post, cvt and gasp, and identical GSUB/GPOS content. The differences are google/fonts' edits: name and head (v1.004), OS/2 fsType 8 to 0, the vertical metrics, and a TTX round-trip that re-encoded GSUB/GPOS and the hinting push instructions without changing their content. md5 shipped vs upstream: Regular `98227adb57f0f3c8176a02bc87a1814f` vs `06b2567e94cf17248181c6d120b61726`, Bold `28c9ffbc9901ec8b87f09df41599db11` vs `ae07ba68dbb0793c9209137538d06668`.

`bc05021c` has no `sources/config.yaml`, so `config_yaml` was dropped from METADATA.pb and an override `config.yaml` names `sources/Amita.glyphs`, whose active instances are Regular and Bold.
