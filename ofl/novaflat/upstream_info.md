# Nova Flat — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novaflat/src/`

### Source Files in googlefontdirectory-hg

- `NovaFlat.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novaflat
  - Branch: `master`
  - Latest commit: `0079428df91b7951d6ad73ba1fa9fa7ca3b28f01` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo covers the redesigned Nova 3.x family and **does** include Nova Flat (as `NovaFlat-Book.sfd`, etc.), but the v3.x designs are substantially different from the v2.000 version currently on Google Fonts. The `librefonts/novaflat` repo holds the v2.000 source that matches the Google Fonts binary.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaFlat.ttf`) corresponds to version 2.000.
- The designer released a substantially redesigned Nova Flat (v3.x with Bold/Oblique variants) in 2020 at `wmk69/Nova`, but this has not been adopted by Google Fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.
