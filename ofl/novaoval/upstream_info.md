# Nova Oval — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novaoval
  - Branch: `master`
  - Latest commit: `ae9beab7121fa7eae3d0021d4a65009f35f82ce4` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Oval is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Script and Nova Oval fonts. These fonts didn't fit to all Nova family." The designer removed Nova Oval from the active family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novaoval` repo contains:
- `src/NovaOval.sfd` — FontForge source file (primary editable source)
- `NovaOval.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novaoval` repo or in `ofl/novaoval/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaOval.ttf`) corresponds to version 2.000 (2011).
- Nova Oval was officially removed from the designer's active Nova family in 2020 as it "didn't fit to all Nova family." The `librefonts/novaoval` repo is the only available source of record.
- Nova Script (a separate Google Fonts family) is described as being based on Nova Oval.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
