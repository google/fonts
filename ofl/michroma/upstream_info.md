# Michroma — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/Michroma-font
- **Pinned commit**: `5822b9d1a733db7ae4f1a63a65a8b41b2d5b15cf`
- **Commit date**: 2023-05-19
- **Commit message**: "Merge pull request #1 from emmamarichal/master — Updated Michroma"
- **Branch**: `master`
- **Latest commit at investigation time**: `8602c0e9a86c0aa6529cc861926bf727568dcac8` (2025-02-25, "Add sources/config.yaml")

## Source Files

At the pinned commit, the repository contains:

- `sources/Michroma.glyphs` — primary Glyphs source (~463 KB)
- `sources/Michroma-Round.glyphs` — variant source (unused in current build)
- `fonts/ttf/Michroma-Regular.ttf` — pre-built TTF binary
- `fonts/otf/Michroma-Regular.otf` — pre-built OTF binary
- `fonts/webfonts/Michroma-Regular.woff2` — pre-built WOFF2
- `OFL.txt` — SIL Open Font License 1.1
- `AUTHORS.txt` — Vernon Adams `<vern@newtypography.co.uk>`
- `CONTRIBUTORS.txt` — Emma Marichal `<bonjour@emmamarichal.fr>`
- `requirements.txt` — lists `gftools` as the sole build dependency

## Build System

- **Build tool**: gftools builder (implied by `requirements.txt` listing `gftools`)
- **No `config.yaml` at the pinned commit**: The file `sources/config.yaml` was added in a later commit (`8602c0e9a86c0aa6529cc861926bf727568dcac8`, 2025-02-25, by Felipe Corrêa da Silva Sanches). At the pinned commit `5822b9d1a733db7ae4f1a63a65a8b41b2d5b15cf`, no config.yaml exists in the repository.
- **Local `config.yaml`** in `ofl/michroma/` reads:
  ```yaml
  buildVariable: false
  sources:
    - sources/Michroma.glyphs
  ```
  This config is present in the google/fonts working copy but was not part of the upstream repo at the pinned commit.
- No GitHub Actions workflow is present in the repo at the pinned commit; the build is manual.

## config.yaml Status

- **At pinned commit**: No `config.yaml` in upstream repo.
- **At HEAD** (8602c0e, 2025-02-25): `sources/config.yaml` added with content:
  ```yaml
  sources:
    - Michroma.glyphs
    - Michroma-Round.glyphs
  ```
- **Recommendation**: Update the pinned commit in METADATA.pb to `8602c0e9a86c0aa6529cc861926bf727568dcac8` and add `config_yaml: "sources/config.yaml"` to the source block to reflect the upstream config that now exists.

## Notes

- **Designer**: Vernon Adams (original author). Emma Marichal contributed the 2023 update (glyph set expansion, bug fixes). Emma is listed in CONTRIBUTORS.txt, not AUTHORS.txt, consistent with copyright ownership remaining with Vernon Adams.
- The local `config.yaml` in the google/fonts ofl/michroma directory predates the upstream config addition and only references `Michroma.glyphs` with `buildVariable: false`. The upstream config at HEAD lists both `Michroma.glyphs` and `Michroma-Round.glyphs` without a `buildVariable` flag.
- `Michroma-Round.glyphs` is present in the repo but not currently published as a separate family on Google Fonts; its status is unclear.
- The METADATA.pb `source` block does not have a `config_yaml` field, which is consistent with the pinned commit having no config.yaml at that point.
- **Confidence**: High — repository is hosted under `googlefonts` org, authorship and licensing are clear, all source files are present.
