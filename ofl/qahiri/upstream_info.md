# Qahiri — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/alif-type/qahiri
- **Commit**: `2fbfe8ca2e5ed04b0455e15c717774766f174ad1`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed and verified. The repository was confirmed to exist under the `alif-type` GitHub organization. The repository description is "Qahiri (قاهري) is a manuscript Kufic typeface". The pinned commit was confirmed to exist in the repository's `main` branch. The source block correctly references the pre-built TTF binary (`Qahiri-Regular.ttf`) along with the OFL license file.

## Build System
The repository contains a custom Python-based build system. At the pinned commit, the following build-related files were present:

- `build.py` — primary build script
- `Makefile` — build automation wrapper
- `Qahiri.glyphs` — Glyphs source file
- `Qahiri-Regular.fea` — OpenType feature code
- `requirements.in` / `requirements.txt` — Python dependencies

No `config.yaml` (gftools builder) was present; the build relied on a bespoke `build.py` script. The METADATA.pb source block maps the pre-built binary directly rather than using a config-driven build.

## Notes
- The font is an Arabic-primary typeface (script: `Arab`) designed by Khaled Hosny, a manuscript Kufic revival.
- The repository also hosts a web app (`app/`) and a GitHub Pages site (`arabic.md`, `_layouts/`, `assets/`).
- The source block includes an explicit `branch: "main"` field, consistent with the repository's default branch.
- Only a single weight (Regular 400) is present, which is appropriate for a display Kufic design.
