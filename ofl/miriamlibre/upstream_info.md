# Miriam Libre — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/simoncozens/Miriam-Libre
- **Branch**: `main`
- **Pinned Commit**: `fc1dbbb7ef6f331b10771c22d33b4bf7543efbd8`
- **Latest Commit**: `fc1dbbb7ef6f331b10771c22d33b4bf7543efbd8` (shallow clone confirms this is the tip of `main`)

## Source Files

- `sources/MiriamLibre.glyphs` — primary Glyphs source file
- `sources/config.yaml` — gftools builder configuration (referenced in METADATA.pb)
- `fonts/variable/MiriamLibre[wght].ttf` — pre-built variable font (wght axis, 400–700)
- `fonts/ttf/MiriamLibre-Regular.ttf` — pre-built static Regular
- `fonts/ttf/MiriamLibre-Bold.ttf` — pre-built static Bold
- `fonts/ttf/MiriamLibre-Medium.ttf` — pre-built static Medium
- `fonts/ttf/MiriamLibre-SemiBold.ttf` — pre-built static SemiBold

## Build System

- **gftools builder** — configured via `sources/config.yaml`
- The `config.yaml` specifies:
  ```yaml
  sources:
    - MiriamLibre.glyphs
  autohintTTF: true
  ```
- Build is invoked via `Makefile` using `gftools builder` over all `sources/config*.yaml` files
- The Makefile also includes targets for `fontbakery` testing, proof documents, and specimen images

## config.yaml Status

The `config.yaml` is present at `sources/config.yaml` in the upstream repo, and METADATA.pb correctly references it as `config_yaml: "sources/config.yaml"`. No changes needed.

## Notes

- The font is a variable font with a `wght` axis (400–700), covering Hebrew and Latin scripts (`primary_script: "Hebr"`).
- METADATA.pb references only the variable TTF (`fonts/variable/MiriamLibre[wght].ttf`), not the static instances.
- The build system is modern (gftools builder + Glyphs source), fully reproducible by the Google Fonts infrastructure.
- The pinned commit (`fc1dbbb`) is the current tip of `main`, so the repo is up to date with what is served.
- Designer: Michal Sahar; repository maintained by Simon Cozens.

## Confidence

**High** — The pinned commit matches the current tip of `main`. The `config.yaml` path in METADATA.pb matches what exists in the upstream repo. Source file paths in METADATA.pb (`fonts/variable/MiriamLibre[wght].ttf`) are present in the repo.
