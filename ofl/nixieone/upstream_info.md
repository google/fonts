# Nixie One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The best available upstream source for Nixie One is the **librefonts** organization mirror on GitHub:

- **Repository**: https://github.com/librefonts/nixieone
- **Designer**: Jovanny Lemonad (lemonad@jovanny.ru, https://jovanny.ru/)
- **Default branch**: master
- **Latest commit**: `14c80bdf78aae3412c98eaea215fa8a1fa2ca993` (2014-10-17), message: "update .travis.yml"
- **Last pushed**: 2014-10-17

No official repository maintained by Jovanny Lemonad (the designer) was found on GitHub. A search for his name and common aliases returned no relevant matches. The designer's website `jovanny.ru` is unreachable (connection refused). The `librefonts` organization on GitHub hosted a collection of Google Fonts source files circa 2014; this appears to be the closest available canonical source.

## Source Files

The `librefonts/nixieone` repository contains the following source files under `src/`:

| File | Type |
|------|------|
| `src/NixieOne-Regular-TTF.sfd` | FontForge source (TTF workflow, ~406 KB) |
| `src/NixieOne-Regular.otf.*` + `.ttx` | TTX table dumps from OTF |
| `src/VERSIONS.txt` | Records version 1.004 |

The root of the repository also contains the full TTX decomposition of the TTF (`NixieOne-Regular.ttf.*.ttx`).

The font in Google Fonts is Version 1.004 (confirmed from binary name table), which exactly matches the version in `src/VERSIONS.txt`.

Note: Nixie One is a single-weight family (Regular only); no italic or bold sources exist in the repository.

## Build System

No Makefile, build script, or automated build system is present in the repository. The `.travis.yml` file exists (last touched in the final commit of 2014). The source workflow appears to be a manual FontForge export from the `.sfd` file.

## config.yaml Status

No `config.yaml` exists. The family is single-weight and has no variable font potential apparent from the source. Given the designer's website is offline and no active maintainer is known, the font is unlikely to receive upstream updates.

## Notes

- The designer's personal website (`jovanny.ru`) is currently unreachable (ECONNREFUSED).
- Jovanny Lemonad designed several other Google Fonts (e.g., Philosopher, Yeseva One), and some of those have GitHub repos under `alexeiva/` — but no Nixie One repo was found under that or any other account.
- The `librefonts/nixieone` repo is the best available source and the version matches what Google Fonts ships (1.004).
- The SFD file (`NixieOne-Regular-TTF.sfd`) is the practical source for rebuilding the TTF.
- **Confidence**: Medium-High. The librefonts mirror matches the shipped version exactly; however, it is not a designer-maintained repository.
