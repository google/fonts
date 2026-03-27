# Nuosu SIL — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/silnrsi/font-nuosu
- **Branch**: `master`
- **Archive URL (pinned)**: `https://github.com/silnrsi/font-nuosu/releases/download/v2.300/NuosuSIL-2.300.zip`
- **Release v2.300 date**: 2022-09-14
- **Latest upstream activity**: 2025-10-31 (significant activity well beyond the pinned release — a Bold weight is in active development)

Note: Unlike the Nunito families, this METADATA.pb uses `archive_url` (pointing to a versioned release ZIP) rather than a commit SHA. There is no `config_yaml` field.

## Source Files

The `source/` directory in the repository contains:

- `NuosuSIL.designspace` — full designspace (likely includes Bold master)
- `NuosuSILR.designspace` — Regular-only designspace
- `NuosuSILRB.designspace` — Regular + Bold designspace
- `NuosuSIL-WOFF-metadata.xml` — WOFF metadata
- `glyph_data.csv` — glyph data table
- `masters/` — UFO master sources:
  - `NuosuSIL-Regular.ufo`
  - `NuosuSIL-Bold.ufo`

The repository root also contains `wscript` (a Python-based `smith` build configuration) and helper scripts (`makeftml`, `makeglyphs`, `preflight*`, `preglyphs`).

## Build System

- **Tool**: `smith` (SIL's font build tool, using a `wscript` configuration file)
- **Smith config**: `wscript` at repo root — specifies `NuosuSILRB.designspace` as the primary target, produces `NuosuSIL.ttf` plus WOFF variants for web
- **Build system is NOT gftools-based** — this is a SIL project using their own toolchain
- **Static fonts**: The distributed font is a static Regular (`NuosuSIL-Regular.ttf`)
- **FONTLOG.txt**: Present, documents change history

## config.yaml Status

No `config.yaml` is present or referenced. The `METADATA.pb` does not have a `config_yaml` field, which is consistent with this being an archive-based source (release ZIP) rather than a build-from-source workflow. The METADATA.pb source block uses `archive_url` pointing to the v2.300 release.

## Notes

- Nuosu SIL is a specialized font for the Yi script (Unicode block Yiii), developed by SIL International. It is one of the few high-quality fonts covering the Yi syllabary.
- The copyright spans 1999–2022, reflecting long development history.
- **Active upstream development**: As of the investigation date, the upstream repo has commits through 2025-10-31, including Bold weight design work (`NuosuSIL-Bold.ufo` is present) and copyright/naming updates. The pinned v2.300 release from 2022 is significantly behind the current `master` branch.
- **v2.300 release notes**: Fixed character U+FF02 (Fullwidth Quotation Mark), added new punctuation: U+3018–U+301B, fullwidth U+FF0D, and halfwidth U+FF61–U+FF65.
- A future update to v2.400 or later (once a new release is made upstream) would be warranted, especially if the Bold weight is released.
- No cached upstream repo found at `/mnt/shared/upstream_repos/fontc_crater_cache/silnrsi/font-nuosu`.
- The `primary_script: "Yiii"` field in METADATA.pb correctly identifies this as a Yi script font.

## Commit Added (HIGH confidence)

Commit `1e9b50a3cb69f6ae01c8ca5da1af2d03a85c517f` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2023-06-22). This is the most reliable method.
