# Agrave Pro: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/agravepro/METADATA.pb` had a source block with `repository_url` https://github.com/daanjobsis/agrave-pro, `commit` 5d33efa2126b9a8ffaeda67c15aa35c848882760 and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit 6887f2099 ("Agrave Pro: Version 1.100 added", Emma Marichal, 2026-10-09).

## Actions taken

- Verified the recorded commit: the shipped `AgravePro[wght].ttf` and `OFL.txt` are byte-identical to `fonts/variable/AgravePro[wght].ttf` and `OFL.txt` at that commit.
- Found the gftools-builder configuration at `sources/config.yaml`; every source it lists exists at that commit.
- Built it with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the variable font has the shipped codepoints and glyph count (810).
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The source block records the repository, commit 5d33efa2, branch `main` and `config_yaml: "sources/config.yaml"`. No override `config.yaml` is used.
