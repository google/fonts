# Nova Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novascript/src/`

### Source Files in googlefontdirectory-hg

- `NovaScript.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novascript
  - Branch: `master`
  - Latest commit: `b58a53e910b4c401089e816c85f2e59cb169412f` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Script is **not included** in `wmk69/Nova`. Per the v3.0.0 FONTLOG (May 2020): "This version does not contain Nova Script and Nova Oval fonts. These fonts didn't fit to all Nova family." The designer removed Nova Script from the active family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

## Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

## Notes

- The Google Fonts binary (`NovaScript-Regular.ttf`) is labeled v2.001; a hotfix was applied to the Google Fonts repo (commit `a9ad19397`: "hotfix-novascript: v2.001 added"), suggesting the file in google/fonts may be slightly newer than the librefonts repo snapshot.
- Per the designer's history notes: "NovaScript is based on my NovaOval font, and it's a part of the Nova set. I created it because the Nova family was missing an oblique font."
- Nova Script was officially removed from the active family in 2020. The librefonts mirror and googlefontdirectory-hg are the best available sources of record.
- Nova Script only covers Latin (no latin-ext), unlike most other Nova fonts.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror. The v2.001 hotfix may not be reflected in the librefonts repo.
