# Redaction: upstream source metadata

**Model**: Claude Fable 5.2

## Initial state

- `ofl/redaction/METADATA.pb` had a source block with `repository_url` https://github.com/jeremymickel/Redaction, `commit` 57eb211f0f61516fe60f2d417bb50930223c85bf and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no `upstream_info.md`.
- The fonts were last changed in google/fonts commit eb8d02aab ("Redaction: Version 1.004; ttfautohint (v1.8.4.16-eb64) added", Emma Marichal, 2026-10-09).

## Actions taken

- Verified the recorded commit: the three shipped fonts (`Redaction-Regular.ttf`, `-Bold.ttf`, `-Italic.ttf`) and `OFL.txt` are byte-identical to `fonts/ttf/` and `OFL.txt` at that commit.
- The repository has two gftools-builder configurations. `sources/config.yaml` builds the base family, Redaction, hinted. `sources/config-bitmap.yaml` builds the six optical-size families (Redaction 10, 20, 35, 50, 70 and 100), unhinted. This family is the base one.
- Built `sources/config.yaml` with gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1: the three Redaction fonts have the shipped codepoints and glyph count (389).
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The source block records the repository, commit 57eb211f, branch `main` and `config_yaml: "sources/config.yaml"`. No override `config.yaml` is used.
