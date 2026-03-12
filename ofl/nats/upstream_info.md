# NATS — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/appajid/nats
- **Owner**: Appaji Ambarisha Darbha (`appajid`), the project lead named in the DESCRIPTION
- **Latest relevant commit**: `7e1486a72988cb8ec1802e2dc2d7e4f59df35582` (2014-11-26) — "updated copyright & version, no latin characters"
- **Default branch**: `master`
- **Confidence**: High — the DESCRIPTION.en_us.html in the google/fonts directory directly links to `github.com/appajid/nats`

## Source Files

The repository contains:
- `NATS.ufo/` — UFO3 source directory with full glyph set (Telugu + Latin glyphs)
- `NATS.sfd` — FontForge SFD source file
- `OFL.txt`

No Latin source is included in this repo. The copyright in OFL.txt credits both Silicon Andhra (Telugu) and Indian Type Foundry; the Latin glyphs are derived from Montserrat (Julieta Ulanovsky).

## Build System

No build system files are present in the repository (no Makefile, build.py, or similar). The repository appears to contain only the raw source files with no automated build pipeline.

## config.yaml Status

A `config.yaml` file is listed in the repository tree, but its content could not be decoded (the API returned an empty payload). It may be an empty or zero-byte placeholder. No gftools-based build configuration could be confirmed.

## Notes

- The repository has only a single commit; it is effectively a snapshot rather than an actively developed project.
- The font is a Telugu handwriting face (SANS_SERIF category) designed by Purushoth Kumar Guttula and released by Silicon Andhra. The Latin component is borrowed from Montserrat.
- `fonts.siliconandhra.org` (the copyright URL) is no longer reachable.
- The font was added to Google Fonts on 2014-12-10 and has not been updated since the initial addition; the upstream repo similarly has had no activity since 2014.
- The `nikstoj/neuton-font` GitHub repo seen in search results is unrelated to this family.
- No upstream mirror exists in `/mnt/shared/upstream_repos/fontc_crater_cache/`.
