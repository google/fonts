# Miss Fajardose — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

No official upstream source repository was found for Miss Fajardose.

- **Designer**: Alejandro Paul / Sudtipos (`sudtipos@sudtipos.com`)
- **Copyright**: "Copyright (c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name "MissFajardose""
- **Date added to Google Fonts**: 2011-11-30 (very early era, predates most open source font hosting practices)

The only relevant GitHub repository found is an unofficial archive mirror:

- **librefonts/missfajardose**: https://github.com/librefonts/missfajardose
  - This is not the official upstream. It was created 2014-07-16 ("Move missfajardose font files to separate repository") by the LibreFonts archiving project.
  - Last pushed: 2014-10-17. Only 11 commits. No stars, no forks.
  - Contains decomposed TTX files and a `.vfb`/`.sfd` pair in `src/`, not a maintained development repository.

Searches were also conducted for:
- A `sudtipos` GitHub user or organization — not found (404)
- `MissFajardose` or `fajardose` repositories on GitHub — no results
- An official Sudtipos repository — Sudtipos does not appear to have a public GitHub presence

## Source Files

From the `librefonts/missfajardose` archive (non-authoritative):

- `src/MissFajardose-Regular-TTF.sfd` — FontForge SFD source (TTF production)
- `src/MissFajardose-Regular-OTF.vfb` — FontLab VFB source (OTF production)
- Multiple `.ttx` files representing decomposed TTF and OTF tables

## Build System

Unknown. No `config.yaml` or build scripts are present in any known repository. The `.sfd` and `.vfb` sources in the archive suggest the font was originally built with FontForge or FontLab respectively. No gftools/fontmake-based build pipeline has been identified.

## config.yaml Status

No `config.yaml` exists. No build pipeline is available in any known repository.

## Notes

- Miss Fajardose is a legacy handwriting font from 2004, added to Google Fonts in the very early days (2011). It predates the modern open source font development workflow.
- Sudtipos does not appear to have a public GitHub presence. The designer (Alejandro Paul) has not published source files through any discoverable public channel.
- The `librefonts/missfajardose` archive is not suitable as an upstream source for METADATA.pb — it is a third-party archive with no connection to the original author, last updated in 2014.
- **Conclusion**: No upstream source repository can be identified for this family. The `source` block in METADATA.pb cannot be populated without the designer's cooperation or discovery of an authoritative source.
