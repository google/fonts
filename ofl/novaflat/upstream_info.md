# Nova Flat — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novaflat
  - Branch: `master`
  - Latest commit: `0079428df91b7951d6ad73ba1fa9fa7ca3b28f01` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo covers the redesigned Nova 3.x family and **does** include Nova Flat (as `NovaFlat-Book.sfd`, etc.), but the v3.x designs are substantially different from the v2.000 version currently on Google Fonts. The `librefonts/novaflat` repo holds the v2.000 source that matches the Google Fonts binary.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novaflat` repo contains:
- `src/NovaFlat.sfd` — FontForge source file (primary editable source)
- `NovaFlat.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt` — records version
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novaflat` repo or in `ofl/novaflat/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaFlat.ttf`) corresponds to version 2.000.
- The designer released a substantially redesigned Nova Flat (v3.x with Bold/Oblique variants) in 2020 at `wmk69/Nova`, but this has not been adopted by Google Fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
