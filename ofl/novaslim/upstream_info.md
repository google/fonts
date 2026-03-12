# Nova Slim — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary upstream (librefonts mirror)**: https://github.com/librefonts/novaslim
  - Branch: `master`
  - Latest commit: `feafcbc2bc2477576ee6c71a812eda28cb25f538` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Slim as a standalone font is **not present** in `wmk69/Nova`. In the v3.x redesign (2020), "Nova Slim" was absorbed into "NovaRound Slim" (`NovaRoundSlim-Book.sfd`, etc.), and slim variants were also added for Nova Flat and Nova Square. The standalone Nova Slim font was discontinued as a separate family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Source Files

The `librefonts/novaslim` repo contains:
- `src/NovaSlim.sfd` — FontForge source file (primary editable source)
- `NovaSlim.ttf.*.ttx` — TTX-decomposed TTF tables (generated artifact)
- `src/VERSIONS.txt`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`

The `.sfd` file is the authoritative source.

## Build System

The repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present.

## config.yaml Status

No `config.yaml` exists in the `librefonts/novaslim` repo or in `ofl/novaslim/` in google/fonts. One would need to be created for any rebuild attempt.

## Notes

- The Google Fonts binary (`NovaSlim.ttf`) corresponds to version 2.000 (2011).
- The designer merged Nova Slim into Nova Round Slim in v3.x (2020), ending it as a standalone family. Per the wmk69/Nova FONTLOG v3.0.0: "Nova Slim is now Nova Round Slim, because I did slim versions of other fonts."
- The `librefonts/novaslim` repo is the only available source for the v2.000 design.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the `librefonts` repo is the known Google Fonts upstream mirror and the commit matches what was previously recorded.
