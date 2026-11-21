# Libre Caslon Condensed

## Initial state

- METADATA.pb had a source block with repository_url https://github.com/ertekinno/libre-caslon-condensed, commit `fe610911976af0ac73e15f9f5cdbc83fc42efdbd`, branch `main` and file mappings for OFL.txt and the two variable fonts, but no `config_yaml`. The family directory had no override config.yaml and no earlier upstream_info.md.
- At that commit the upstream repository has a gftools-builder config, `sources/config.yaml`, listing `LibreCaslonCondensed.glyphs` and `LibreCaslonCondensed-Italic.glyphs` (Glyphs 3, one `wght` axis; `buildVariable`, explicit `stat` block).
- The upstream history continues the Libre Caslon Text repository (https://github.com/thundernixon/Libre-Caslon): its first own commit, `08d16e7` (2023-08-01), has that repository's HEAD `52200a7` as parent.

## Actions taken

- The recorded commit was verified. `fe61091` ("Update contributors", 2026-08-10) is the upstream `main` HEAD and is the commit named by the gftools-packager commit (PR #10801, merged 2026-09-04). Both shipped binaries are byte-identical to `fonts/variable/` at that commit. They were committed in `3465018` ("build fonts", 2026-07-31); after that commit only CONTRIBUTORS.txt changed.
- The source state the binaries were compiled from was identified. Their `head.modified` is 2026-07-31 12:18:07 UTC (14:18:07 +0200), between `95dc46f` (14:17:25 +0200) and `9443742` (14:21:58 +0200). `9443742` (Emma Marichal) removed the CR (U+000D) and NULL glyphs from the Italic source, for the googlefonts/family/equalcodepointcoverage FAIL named in its commit message. A Python gftools-builder build of `95dc46f` was `ttx`-identical to both shipped binaries except `head.modified` and `checkSumAdjustment`.
- The commit was kept at `fe61091`: the `files` mappings take the shipped binaries from that commit (at `95dc46f` those paths hold an older build), and its sources differ from the compiled ones only by the CR/NULL removal in the Italic.
- `config_yaml: "sources/config.yaml"` was added to the source block.
- `fe61091` was build-tested with `sources/config.yaml`, and the output was compared with the shipped fonts (fontTools, `ttx`, and the sfd-reland `functional_gate.py`):
  - gftools-builder (Python; gftools from a local development checkout with unpublished builder fixes, fontmake 3.11.1, glyphsLib 6.12.7, fontTools 4.61.1): the Upright was `ttx`-identical to the shipped font except `head.modified` and `checkSumAdjustment`. The Italic matched in shaping, rendering, names, line spacing, shared glyph advances, GDEF and STAT, but lacks CR (U+000D) and NULL (563 glyphs against 565).
  - gftools-builder3 (e851b8b, fontc): functional gate PASS for the Upright; the Italic failed only on the missing U+000D/CR. builder3 did not apply the config's `stat` block (its recipe runs buildStat without the `--src` file the Python builder passes), so STAT gained a `wdth` axis with a "Condensed" 75 value. It also wrote no name ID 25 and set name ID 5 to "Version 2.000;fontc 1.0.0". These are builder3 gaps, not config errors.

## Final state

METADATA.pb records repository_url, commit `fe610911976af0ac73e15f9f5cdbc83fc42efdbd`, branch `main` and `config_yaml: "sources/config.yaml"`. A Python gftools-builder rebuild at that commit reproduces the shipped Upright, and the shipped Italic except for the CR (U+000D) and NULL glyphs, which `9443742` removed from the Italic source after the release binaries had been compiled.
