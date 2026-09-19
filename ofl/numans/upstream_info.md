# Numans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `numans/src/`

### Source Files in googlefontdirectory-hg

- `Numans-Regular.vfb` — FontLab source (proprietary format, not buildable with gftools)
- `Numans-Regular-TTF.sfd` — FontForge SFD (likely converted from VFB for TTF generation, not buildable with gftools-builder)
- `Numans-Regular.otf` — compiled OTF binary (not a design source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The primary design source is the `.vfb` file (FontLab proprietary format). The `.sfd` file is a TTF-flavored conversion. Neither format is buildable with gftools-builder.

## Search Results

- GitHub repository search for "Numans font", "Numans", "jovanny numans" — no results
- GitHub user search for Jovanny Lemonad — no GitHub profile found under that name; related fonts (Philosopher, Yeseva One) were maintained by others (alexeiva) after acquisition
- Designer's website (jovanny.ru / www.jovanny.ru) — not reachable (connection refused)
- The font binary references `http://www.jovanny.ru/` as the vendor URL, but the site is down
- No cached clone found in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Font Metadata

- **Designer**: Jovanny Lemonad
- **Copyright**: Copyright (c) 2011 by Jovanny Lemonad. All rights reserved.
- **Vendor URL**: http://www.jovanny.ru/
- **Version**: 001.001

## Notes

- Numans is a modern grotesque sans-serif with open forms, designed in 2011.
- The designer Jovanny Lemonad also designed Philosopher and Yeseva One (both on Google Fonts), but those fonts have been maintained in separate GitHub repos by third parties (alexeiva).
- No GitHub repository under Jovanny Lemonad's name was found. The original website (jovanny.ru) is unreachable.
- The googlefontdirectory-hg monorepo is the only known location of the original source files.
- Confidence in source identification: **Medium** — the VFB source in googlefontdirectory-hg is the original design source, but the proprietary format limits its usefulness for rebuilding.
