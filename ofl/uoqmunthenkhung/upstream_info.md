# UoqMunThenKhung — Upstream Source Info

**Model**: Claude Opus 4.6

## Repository

- **URL**: https://github.com/MoonlitOwen/ThenKhung
- **Commit**: `cdf0805fd0db0aba5c7789f60033060e1566d4cc`
- **Branch**: main

## Summary

UoqMunThenKhung (宇文天穹) was designed by Moonlit Owen and published under the OFL. It was a Traditional Chinese serif typeface providing a single Regular weight covering Traditional Chinese, Cyrillic, Latin, and Symbols2 subsets, with Traditional Han (`Hant`) as its primary script. The TTF was sourced from `fonts/ttf/` in the repository and the build configuration from `source/config.yaml`. The font was added to Google Fonts on 2025-05-16.


## Source-metadata correction (2026-06-02) — override config from the committed .ufoz (KNOWN-INCOMPLETE)

**Model**: Claude Opus 4.8

fontc_crater reported `missing source 'temp/UoqMunThenKhung-Regular.ufo'`: the upstream `source/config.yaml` declares `temp/UoqMunThenKhung-Regular.ufo`, which the repo's build.sh produces at build time by extracting the committed `source/UoqMunThenKhung-Regular.ufoz` and then `.gitignore`s. fontc_crater never runs build.sh, so the source appears absent.

An override `config.yaml` was added in this family directory that declares the committed `source/UoqMunThenKhung-Regular.ufoz` (a zipped UFO) directly, with the path relative to the repository root.

Dependencies:
- **fontmake** already reads `.ufoz`. The fontc / fontc_crater path additionally needs **[googlefonts/fontc#2028](https://github.com/googlefonts/fontc/pull/2028)** (ufo2fontir reads `.ufoz`) and **[googlefonts/gftools#1192](https://github.com/googlefonts/gftools/pull/1192)** (gftools.builder recognises `.ufoz`).

### ⚠ Still-unaddressed issue: the Font Creator post-processing is not applied

The committed `.ufoz` is a **raw Font Creator 15 export**. The upstream build does not build it directly — it first runs `source/fcp_ufo_process.py` on the extracted UFO, which:
- strips a UTF-8 BOM from the UFO's XML files,
- repairs `fontinfo.plist` (adds the missing `encodingID` after `platformID`),
- corrects invalid `features.fea` data,
- sets `useTypoMetrics`, the version number, and fixes localized name records, and
- adds the `public.openTypeMeta` and `BASE` tables.

Several of these are **parse-breaking defects** (BOM, malformed plist/fea), so building directly from the raw `.ufoz` will likely **fail**, and even if it builds it will **differ substantially** from the shipped binary (missing the meta/BASE tables, the metric and version overrides, and the name fixes). This override therefore only addresses the *target-discovery* (`missing source`) failure; it is **not** a reproducible build.

A complete fix requires an **upstream PR** that commits the processed UFO (the output of `fcp_ufo_process.py`, conventionally under `sources/generated/`) and points the config at it.
