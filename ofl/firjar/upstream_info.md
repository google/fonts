# Firjar: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/firjar/METADATA.pb` had a source block with `repository_url` https://github.com/Mestaratype/Firjar, `commit` ba21292cd3b08bfeb7dba987b60ef790059a2930 and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit 6b7bfb442 ("Firjar: Version 2.971 added", Emma Marichal, 2026-10-15).

## Actions taken

- Verified the recorded commit: the shipped `Firjar[wdth,wght].ttf` and `OFL.txt` are byte-identical to `fonts/variable/Firjar[wdth,wght].ttf` and `OFL.txt` (the article differs: it was edited in google/fonts) at that commit.
- Found the gftools-builder configuration at `sources/config.yaml`; every source it lists exists at that commit.
- Built it with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the variable font has the shipped codepoints and glyph count (651).
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The source block records the repository, commit ba21292c, branch `main` and `config_yaml: "sources/config.yaml"`. No override `config.yaml` is used.
