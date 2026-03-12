# Nova Cut — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novacut
  - Branch: `master`
  - Latest commit: `aa17adb4fc22470e6f8e60843e7708e15bb59fbe` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - This repo covers the redesigned Nova 3.x family (2020–2022) and **intentionally excludes Nova Cut** — the designer removed it in v3.0.0 (May 2020) due to visual similarity with Gothica. The Google Fonts version (v2.000) predates this split.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG; individual page no longer available).

## Source Files

The `librefonts/novacut` repo contains:
- `src/NovaCut.sfd` — FontForge source file (primary editable source)
- `NovaCut.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt` — records version 2.000
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source. The TTX files appear to be decomposed from the binary and stored for diffing/CI purposes.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete; `fontbakery-cli` and `fontcrunch` are no longer maintained in that form. No `Makefile` or modern build script is present. Rebuilding from source would require FontForge and manual steps.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novacut` repo or in `ofl/novacut/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaCut.ttf`) corresponds to version 2.000 (2011), redesigned September 2011.
- Nova Cut was officially dropped from the designer's active Nova family in 2020 and has no maintained upstream. The `librefonts/novacut` repo is the best available source of record.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- The font covers Latin, Latin Extended, and a small set of Greek and mathematical symbols.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror for this family and the commit matches what was previously recorded.
