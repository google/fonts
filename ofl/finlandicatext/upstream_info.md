# Finlandica Text: upstream source metadata

## Initial state

- METADATA.pb had a source block with `repository_url` https://github.com/HelsinkiTypeStudio/FinlandicaText, `commit` 402f5abf41b8bcde2d3091dbbc1a3604f812625a, `branch` main and two `files` entries (`fonts/variable/FinlandicaText[wght].ttf`, `fonts/variable/FinlandicaText-Italic[wght].ttf`), but no `config_yaml`.
- The family directory had no override config.yaml and no upstream_info.md.
- The family was onboarded by Emma Marichal in PR #10443 ("Finlandica Text: Version 3.103 added", google/fonts commit 3f2500a, 2026-04-17), merged by Marc Foley on 2026-04-29 (0d2798e).

## Actions taken

- The recorded commit was verified. Both shipped binaries have the same git blob ids (and sha256) as `fonts/variable/` at upstream 402f5ab. That commit merges 38706d8 ("rebuild fonts just in case", 2026-04-16) with no further changes, and the shipped fonts carry a head.modified of 2026-04-16 14:15 UTC, two minutes before 38706d8. The sources were last changed in b35bad6 ("new weight distribution v3.103", 2026-04-10); the later commits only rebuilt binaries and removed a `Tests/` folder. When the repo archive mirror was refreshed on 2026-09-27, 402f5ab was still the head of `main`.
- The upstream tree at 402f5ab was found to contain `sources/config.yaml` (unchanged since 462cc24, 2026-03-12), a gftools-builder config listing `FinlandicaText.glyphs` and `FinlandicaText-Italic.glyphs` with explicit STAT tables.
- The fonts were rebuilt from 402f5ab with gftools-builder3 (commit e851b8b, fontc 1.0.0) using that config (`gftools-builder sources/config.yaml` from the repo root). The build succeeded without warnings. The variable fonts matched the shipped ones in table set, glyph set, cmap (964 codepoints), fvar instances, avar, STAT values, vertical metrics and advance widths, and `functional_gate.py` (cmap, shaping, rendering, names, line spacing, advances, GDEF) passed for both styles.
- The remaining differences did not come from the sources. fontc appended ";fontc 1.0.0" to name ID 5, and head.flags differed (3 shipped, 11 built). Name IDs 13 and 25 differed because builder3 did not apply the gftools license and name ID 25 fixes; running `gftools fix-font` on the builder3 output made name IDs 13, 14 and 25 match the shipped fonts. The fvar instance and STAT name strings were the same but were stored under different name IDs.
- `config_yaml: "sources/config.yaml"` was added to the source block of METADATA.pb.

## Final state

- METADATA.pb points at https://github.com/HelsinkiTypeStudio/FinlandicaText, commit 402f5abf41b8bcde2d3091dbbc1a3604f812625a, branch main, with `config_yaml: "sources/config.yaml"`.
- No override config.yaml was created.
- Status: complete. Confidence: HIGH.
