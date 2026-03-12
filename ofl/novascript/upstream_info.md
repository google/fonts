# Nova Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novascript
  - Branch: `master`
  - Latest commit: `b58a53e910b4c401089e816c85f2e59cb169412f` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Script is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Script and Nova Oval fonts. These fonts didn't fit to all Nova family." The designer removed Nova Script from the active family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novascript` repo contains:
- `src/NovaScript.sfd` — FontForge source file (primary editable source)
- `NovaScript.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novascript` repo or in `ofl/novascript/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaScript-Regular.ttf`) is labeled v2.001; a hotfix was applied to the Google Fonts repo (commit `a9ad19397`: "hotfix-novascript: v2.001 added"), suggesting the file in google/fonts may be slightly newer than the `librefonts` repo snapshot.
- Per the designer's history notes: "NovaScript is based on my NovaOval font, and it's a part of the Nova set. I created it because the Nova family was missing an oblique font."
- Nova Script was officially removed from the active family in 2020. The `librefonts/novascript` repo is the best available source of record.
- Nova Script only covers Latin (no latin-ext), unlike most other Nova fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded. The v2.001 hotfix may not be reflected in the librefonts repo.
