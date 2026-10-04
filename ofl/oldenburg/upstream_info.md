# Oldenburg — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oldenburg/src/`

### Source Files in googlefontdirectory-hg

- `Oldenburg-Regular.vfb` — FontLab source (proprietary format, not buildable with gftools)
- `Oldenburg-Regular-TTF.sfd` — FontForge SFD (likely converted from VFB for TTF generation, not buildable with gftools-builder)
- `Oldenburg-Regular.otf` — compiled OTF binary (not a design source)
- `Oldenburgh-test.html` — test file (not a source file)
- `METADATA_comments.txt` — metadata notes (not a source file)

The primary design source is the `.vfb` file (FontLab proprietary format). The `.sfd` file is a TTF-flavored conversion. Neither format is buildable with gftools-builder.

## Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/oldenburg — contains the same VFB and SFD files as googlefontdirectory-hg. This is a mirror, not a canonical designer-owned repository.

## Family Details

- **Designer**: Nicole Fally (typeface design); Eben Sorkin (spacing and mastering)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2011-12-19
- **Copyright**: "Copyright (c) 2010 by Sorkin Type Co (eben@eyebytes.com) with Reserved Font Name Oldenburgh."

## Search Results

- GitHub was searched for "Oldenburg font", "Oldenburg font Nicole Fally", and "SorkinType Oldenburg" — no designer-owned repositories found
- The SorkinType GitHub organization (`github.com/SorkinType`) was inspected directly — Oldenburg was not among its repositories
- The DESCRIPTION.en_us.html referred to `http://code.google.com/p/googlefontdirectory/` (the original Google Code repository, now defunct)
- The FONTLOG recorded: Nicole Fally completed the design in FontLab VFB format (9 Dec 2011); Eben Sorkin mastered VFB to TTF (13 Dec 2011)

## Notes

- No canonical upstream repository with Glyphs or UFO sources exists for Oldenburg.
- The sources originated as a FontLab VFB file which was then converted to TTF by Eben Sorkin.
- The googlefontdirectory-hg monorepo preserves the original VFB source, but the proprietary format limits its usefulness for rebuilding.
- Confidence in source identification: **High** — the VFB is confirmed as the original design source via the FONTLOG. However, no modern buildable sources exist.
