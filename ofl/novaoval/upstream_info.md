# Nova Oval — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novaoval/src/`

### Source Files in googlefontdirectory-hg

- `NovaOval.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novaoval
  - Branch: `master`
  - Latest commit: `ae9beab7121fa7eae3d0021d4a65009f35f82ce4` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Oval is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Script and Nova Oval fonts. These fonts didn't fit to all Nova family." The designer removed Nova Oval from the active family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaOval.ttf`) corresponds to version 2.000 (2011).
- Nova Oval was officially removed from the designer's active Nova family in 2020 as it "didn't fit to all Nova family." The librefonts mirror and googlefontdirectory-hg are the only available sources of record.
- Nova Script (a separate Google Fonts family) is described as being based on Nova Oval.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.
