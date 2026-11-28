# Madhuban: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/madhuban/METADATA.pb` had a source block with `repository_url` https://github.com/magictype/Madhuban, `commit` 9084d0e64255d1d30c191551f1a6e0fb5cb9e172 and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit 6f046ef17 ("Madhuban: Version 1.003 added", Emma Marichal, 2026-10-26).

## Actions taken

- Verified the recorded commit: the shipped `Madhuban[wght].ttf` is byte-identical to `fonts/variable/Madhuban[wght].ttf` (`OFL.txt` differs) at that commit.
- Found the gftools-builder configuration at `sources/config.yaml`; every source it lists exists at that commit.
- Built it with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the variable font has the shipped codepoints and glyph count (1361).
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The source block records the repository, commit 9084d0e6, branch `main` and `config_yaml: "sources/config.yaml"`. No override `config.yaml` is used.
