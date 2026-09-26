# Nova Round — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novaround/src/`

### Source Files in googlefontdirectory-hg

- `NovaRound.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novaround
  - Branch: `master`
  - Latest commit: `eedf80c86b226640d3e1ba0ad99bb01c96627b71` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - The `wmk69/Nova` repo **does** include Nova Round (as `NovaRound-Book.sfd`, etc.) with a substantially redesigned v3.x version including Bold, Oblique, and Slim variants. However, the Google Fonts version is v2.000 from 2011 and the googlefontdirectory-hg / librefonts repo holds the matching source.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaRound.ttf`) corresponds to version 2.000 (2011).
- The designer released an extensively redesigned Nova Round v3.x (with Bold/Oblique/Slim variants) in `wmk69/Nova` in 2020, but this has not been adopted by Google Fonts.
- In the v3.x family, "Nova Slim" was absorbed into Nova Round as "NovaRound Slim."
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.
