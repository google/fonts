# Redaction 35: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/redaction35/METADATA.pb` had a source block with `repository_url` https://github.com/jeremymickel/Redaction, `commit` d6d5404e094773468db8fe07069c8e681949790c and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit 35c684b78 ("Redaction 35: Version 1.004 added", Emma Marichal, 2026-10-14).

## Actions taken

- Verified the recorded commit: the three shipped fonts (`Redaction35-Regular.ttf`, `-Bold.ttf`, `-Italic.ttf`) and `OFL.txt` are byte-identical to `fonts/ttf/` and `OFL.txt` at that commit.
- The repository has two gftools-builder configurations. `sources/config.yaml` builds the base family, Redaction, hinted. `sources/config-bitmap.yaml` builds the six optical-size families (Redaction 10, 20, 35, 50, 70 and 100), unhinted. This family is one of the six, so its config is the second one; that config also builds the other five.
- Built `sources/config-bitmap.yaml` with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the three Redaction 35 fonts have the shipped codepoints and glyph count (389).
- Added `config_yaml: "sources/config-bitmap.yaml"` to the source block.

## Final state

- The source block records the repository, commit d6d5404e, branch `main` and `config_yaml: "sources/config-bitmap.yaml"`. No override `config.yaml` is used.
