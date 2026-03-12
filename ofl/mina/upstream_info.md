# Mina — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/suman51284/Mina
- **Branch**: (default, no branch specified in METADATA.pb)
- **Pinned Commit**: `20350840b9a0b08d7855d22e2890c3ed93237edd`
- **Latest Commit**: `20350840b9a0b08d7855d22e2890c3ed93237edd` (single commit repo — this is the only commit)

## Source Files

- `sources/sfd/Mina-bengali-0.sfd` — FontForge source for Regular weight
- `sources/sfd/Mina-bengali-1.sfd` — FontForge source for Bold weight
- `sources/Mina-Regular.ufo` — generated UFO (from build.py via FontForge)
- `sources/Mina-Bold.ufo` — generated UFO (from build.py via FontForge)
- `features/regular/features.fea` — OpenType feature code for Regular
- `features/bold/features.fea` — OpenType feature code for Bold
- `FONTS/ttf/Mina-Regular.ttf` — pre-built TTF output
- `FONTS/ttf/Mina-Bold.ttf` — pre-built TTF output

## Build System

- **FontForge** (`build.py`) — the primary build script uses `fontforge` Python bindings to open SFD files, generate UFOs, then produce TTF/OTF outputs
- The script uses Python 2 syntax (`print` without parentheses), indicating an older codebase
- No Makefile or gftools builder configuration exists in the upstream repo; the workflow is entirely FontForge-based

## config.yaml Status

A `config.yaml` already exists in the google/fonts family directory (`ofl/mina/config.yaml`) pointing to the UFO sources:

```yaml
buildVariable: false
sources:
  - sources/Mina-Regular.ufo
  - sources/Mina-Bold.ufo
```

This is reasonable given the build produces two static UFO-based fonts. The METADATA.pb `source` block references pre-built TTFs from `FONTS/ttf/` rather than building from source, which is consistent with the FontForge-based workflow that generates those TTFs.

## Notes

- The repository has only a single commit (`20350840b9a0b08d7855d22e2890c3ed93237edd`), meaning the pinned commit in METADATA.pb is effectively the entire history.
- The build script (`build.py`) uses Python 2 syntax and depends on FontForge Python bindings — this is not directly reproducible by the Google Fonts infrastructure without significant work.
- The pre-built TTFs are committed to the repo at `FONTS/ttf/`, which is what METADATA.pb references; this is the practical source of truth for the served files.
- The font covers Bengali and Latin scripts (`primary_script: "Beng"`).
- No upstream updates are expected given the single-commit state of the repository.

## Confidence

**High** — The pinned commit is the only commit in the repository, leaving no ambiguity about provenance. Pre-built TTFs are present at the paths referenced in METADATA.pb.
