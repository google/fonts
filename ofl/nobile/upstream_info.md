# Nobile — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The authoritative upstream source for Nobile is the designer's own GitHub repository:

- **Repository**: https://github.com/vernnobile/NobileFont
- **Designer**: Vernon Adams (vern@newtypography.co.uk)
- **Default branch**: master
- **Latest commit**: `d3f6ea2c6434d6ebfdc0534bd199d14370f12fee` (2014-05-04), message: "added"
- **Last pushed**: 2014-05-08

The FONTLOG in the repository explicitly states: "To contribute to the project contact Vernon Adams at vern@newtypography.co.uk and use the gitHub repository at https://github.com/vernnobile/NobileFont". This confirms it as the official canonical source.

## Source Files

The repository is organized into versioned directories. The most relevant source files are:

### `version1.0/` — initial release
- `Regular/src/Nobile.sfd` — FontForge source (regular)
- `Regular/src/Nobile.ufo/` — UFO source (regular)
- `Regular/src/Nobile-Italic.sfd` — FontForge source (italic)
- `Bold/src/Nobile-Bold.sfd` — FontForge source (bold)
- `Bold/src/Nobile-Bold.ufo/` — UFO source (bold)
- `Bold-italic/Nobile-BoldItalic.sfd` — FontForge source (bold italic)

### `version1.2/` — intermediate release (used for Northern Block collaboration)
- `src/Nobile-Regular.ufo/`
- `src/Nobile-Medium.ufo/`
- `src/Nobile-Bold.ufo/`
- `src/Nobile-Extra-Bold.ufo/`
- `src/Nobile-Extra-Light.ufo/`
- `src/Nobile-Heavy.ufo/`
- (No italic UFOs in this directory)

### `in-progress/` — development work
- `src/Nobile-Regular.ufo/`
- `src/Nobile-Medium.ufo/`
- `src/Nobile-Bold.ufo/`
- `src/Nobile-Extra-Bold.ufo/`
- `src/Nobile-Extra-Light.ufo/`
- `src/Nobile-Heavy.ufo/`
- (Italics present in `STASH/` subdirectory as earlier versions)

The Google Fonts build ships 6 styles (Regular, Italic, Medium, MediumItalic, Bold, BoldItalic). The version in GF is 001.001.

## Build System

No Makefile, build scripts, or `config.yaml` are present anywhere in the repository. The FONTLOG notes sources in `.sfd` (FontForge) and `.ufo` formats; build was presumably done manually. The `version1.2/` and `in-progress/` directories contain only `.ufo` sources, indicating a shift to UFO-based toolchain, but no build automation is present.

## config.yaml Status

No `config.yaml` exists in either the upstream repository or the Google Fonts working copy. To add one, source masters would need to be confirmed against the shipped binaries. The most likely candidate for a rebuild would be the UFO sources in `in-progress/src/` combined with a new `config.yaml`, but italic UFOs are not present in that directory (they exist only as older SFD/UFO files in `version1.0/` and `STASH/`).

## Notes

- Vernon Adams passed away in 2014; the repository has been unmaintained since May 2014.
- The repository is the designer's own and is the canonical source, even though it is no longer actively maintained.
- The `version1.2/README.md` indicates the 1.2 branch was a collaboration with Northern Block — this may not be the version shipped to Google Fonts (which shows version 001.001, matching the version 1.0 era).
- The `in-progress/` directory shows planned expansion to a wider weight range (ExtraLight through Heavy) that was never completed or published.
- No italic UFOs exist in the `in-progress/` directory; the italic masters appear only in `version1.0/` (SFD format) and in `in-progress/STASH/`.
- A full rebuild using modern tooling (fontmake + ufo2ft) would require collecting and reconciling sources from across the scattered version directories.
- **Confidence**: High for repository identification (designer's own repo, explicitly referenced in FONTLOG). Medium for build readiness — UFO sources exist but are fragmented across directory versions and lack italic masters in the most recent directories.
