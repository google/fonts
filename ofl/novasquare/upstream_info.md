# Nova Square — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novasquare
  - Branch: `master`
  - Latest commit: `86d7d2eb056b9570622e665e20fb3b40f41010cf` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo **does** include Nova Square (as `NovaSquare-Book.sfd`, etc.) with a substantially redesigned v3.x version including Bold, Oblique, and Slim variants. However, the Google Fonts version is v2.000 from 2011 and the `librefonts/novasquare` repo holds the matching source.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novasquare` repo contains:
- `src/NovaSquare.sfd` — FontForge source file (primary editable source)
- `NovaSquare.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novasquare` repo or in `ofl/novasquare/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaSquare.ttf`) corresponds to version 2.000 (2011). Nova Square was added to Google Fonts slightly later than the other Nova fonts (2011-04-14 vs 2011-03-23).
- The designer released a substantially redesigned Nova Square v3.x (with Bold/Oblique/Slim variants) in `wmk69/Nova` in 2020, but this has not been adopted by Google Fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
