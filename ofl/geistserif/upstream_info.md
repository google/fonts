# Geist Serif: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/geistserif/METADATA.pb` had a source block with `repository_url` https://github.com/vercel/geist-font, `commit` a2026e99b3f1b36ffb6c0473fdf383e97d3f9d5a and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit fdc4f0753 ("Geist Serif: update to upstream 1.003", christopherkindl, 2026-11-06).

## Actions taken

- Verified the recorded commit: the shipped `GeistSerif[ELSH].ttf` is byte-identical to `fonts/GeistSerif/variable/GeistSerif[ELSH].ttf` at that commit.
- Found the gftools-builder configuration at `sources/config-GeistSerif.yaml`; every source it lists exists at that commit.
- Built it with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the variable font has the shipped codepoints and glyph count (898).
- Upstream's comment in that config says the release is built by `make build-serif` (`scripts/build-geist-serif.py`), because fontmake alone breaks the corner-component serifs; the config documents the family and its STAT. So a plain gftools build is not expected to reproduce the outlines of the shipped font. The repository also holds configs for Geist, Geist Mono and Geist Pixel.
- Added `config_yaml: "sources/config-GeistSerif.yaml"` to the source block.

## Final state

- The source block records the repository, commit a2026e99, branch `main` and `config_yaml: "sources/config-GeistSerif.yaml"`. No override `config.yaml` is used.
