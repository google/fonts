# Neuton — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **Primary URL**: https://github.com/googlefonts/neuton
- **Latest relevant commit**: `b376055d272ab8a54d490bfad487e96c1d047c97` (2013-06-12) — "Added description to README"
- **Default branch**: `main`
- **Mirror / auto-export**: https://github.com/nikstoj/neuton-font — described as "Automatically exported from code.google.com/p/neuton-font"; last pushed 2015-08-19. This is a partial export (only Regular + Italic TTFs + src SFDs) and is secondary to the `googlefonts/neuton` repo.
- **Original hosting**: `code.google.com/p/neuton-font` (now archived, JavaScript-only, not accessible via CLI)
- **Confidence**: High — `googlefonts/neuton` is under the canonical Google Fonts org and contains the full multi-weight source tree.

## Source Files

In `googlefonts/neuton` (top-level structure):
- `Source/` — FontForge `.sfd` files for all weights and variants:
  - `Neuton-Regular.sfd`, `Neuton-Italic.sfd`, `Neuton-Light.sfd`, `Neuton-Bold.sfd`, `Neuton-Extrabold.sfd`, `Neuton-Extralight.sfd`, `Neuton-ExtralightItalic.sfd`
  - Small-caps variants: `Neuton-SC-*.sfd`
  - `NeutonAlt-Italic.sfd`, `NeutonCursive-Regular.sfd`
- `Release/` — versioned TTF releases (1.1 through 1.46a), including a `Neuton-1.46.zip`
- `Release/1.46/` — the most recent release TTFs
- `Progress/` — historical `.sfd` snapshot files
- `Background/` — design reference scans
- `Tools/` — specimens, test files, descriptions

The `nikstoj/neuton-font` mirror contains only `Neuton-Regular.sfd`, `NeutonCursive-Italic.sfd`, `Neuton-Italic.sfd`, `NeutonItalic.glyphs` in its `src/` folder (a subset).

## Build System

No automated build system files are present in `googlefonts/neuton` (no Makefile, no build.py, no config.yaml, no `.github/` workflows). The release TTFs appear to have been built manually from FontForge.

## config.yaml Status

No `config.yaml` is present in `googlefonts/neuton`. No gftools build configuration exists.

## Notes

- Neuton was designed by Brian Zick. The copyright URL `http://www.21326.info/` is no longer active.
- The last commit to `googlefonts/neuton` is from June 2013; the project has been dormant for over a decade.
- The latest release in the repo is v1.46; the Google Fonts directory TTFs appear to correspond to this release (file names match).
- The family was originally planned to comprise 60 fonts (5 weights × Regular/Italic/Cursive/Extended/SC) but was never completed; the current release covers 7 styles.
- The repo contains Small Caps and Cursive source variants (`Neuton-SC-*`, `NeutonCursive`) that are not currently published on Google Fonts.
- No upstream mirror exists in `/mnt/shared/upstream_repos/fontc_crater_cache/`.
