# Nova Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novamono
  - Branch: `master`
  - Latest commit: `33c70f6f3fb14b38512b00b6bc36004a227f7fbc` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Mono is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Mono. I've stopped developing this font." Development was halted for Nova Mono. The designer discontinued it from the Nova family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novamono` repo contains:
- `src/NovaMono.sfd` — FontForge source file (primary editable source)
- `NovaMono.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `menusubset.ff` — FontForge script for menu subset generation
- `src/NovaMono.png` — specimen image
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source. Nova Mono also has a `menusubset.ff` script not present in the other Nova family repos.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novamono` repo or in `ofl/novamono/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaMono.ttf`) corresponds to version 1.2 (February 2011) — the last release before development was halted.
- Nova Mono was officially discontinued by the designer and is not part of the active wmk69/Nova repo. The `librefonts/novamono` repo is the only available source of record.
- Nova Mono has broader Unicode coverage than the other Nova fonts: full Greek, mathematical operators, arrows, currency, etc.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
