# Nova Round — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novaround
  - Branch: `master`
  - Latest commit: `eedf80c86b226640d3e1ba0ad99bb01c96627b71` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo **does** include Nova Round (as `NovaRound-Book.sfd`, etc.) with a substantially redesigned v3.x version including Bold, Oblique, and Slim variants. However, the Google Fonts version is v2.000 from 2011 and the `librefonts/novaround` repo holds the matching source.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novaround` repo contains:
- `src/NovaRound.sfd` — FontForge source file (primary editable source)
- `NovaRound.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novaround` repo or in `ofl/novaround/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaRound.ttf`) corresponds to version 2.000 (2011).
- The designer released an extensively redesigned Nova Round v3.x (with Bold/Oblique/Slim variants) in `wmk69/Nova` in 2020, but this has not been adopted by Google Fonts.
- In the v3.x family, "Nova Slim" was absorbed into Nova Round as "NovaRound Slim."
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
