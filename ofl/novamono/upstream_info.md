# Nova Mono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novamono/src/`

### Source Files in googlefontdirectory-hg

- `NovaMono.sfd` — FontForge source file (primary editable source)
- `NovaMono.png` — specimen image
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novamono
  - Branch: `master`
  - Latest commit: `33c70f6f3fb14b38512b00b6bc36004a227f7fbc` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Mono is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Mono. I've stopped developing this font." Development was halted for Nova Mono. The designer discontinued it from the Nova family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaMono.ttf`) corresponds to version 1.2 (February 2011) — the last release before development was halted.
- Nova Mono was officially discontinued by the designer and is not part of the active wmk69/Nova repo. The librefonts mirror and googlefontdirectory-hg are the only available sources of record.
- Nova Mono has broader Unicode coverage than the other Nova fonts: full Greek, mathematical operators, arrows, currency, etc.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.
