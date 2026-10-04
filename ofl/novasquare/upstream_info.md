# Nova Square — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novasquare/src/`

### Source Files in googlefontdirectory-hg

- `NovaSquare.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novasquare
  - Branch: `master`
  - Latest commit: `86d7d2eb056b9570622e665e20fb3b40f41010cf` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo **does** include Nova Square (as `NovaSquare-Book.sfd`, etc.) with a substantially redesigned v3.x version including Bold, Oblique, and Slim variants. However, the Google Fonts version is v2.000 from 2011 and the googlefontdirectory-hg / librefonts repo holds the matching source.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaSquare.ttf`) corresponds to version 2.000 (2011). Nova Square was added to Google Fonts slightly later than the other Nova fonts (2011-04-14 vs 2011-03-23).
- The designer released a substantially redesigned Nova Square v3.x (with Bold/Oblique/Slim variants) in `wmk69/Nova` in 2020, but this has not been adopted by Google Fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.
