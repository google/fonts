# Yuyu: upstream source metadata

**Model**: Claude Opus 5.5
**Date**: 2026-09-27

## Initial state

- METADATA.pb had a source block with `repository_url` https://github.com/JuliaGarciaLopez/Yuyu-Font, `commit` 38e2939cbadbd7c8deddcbe8e43437972c1fbfe4, `branch` main and file mappings for `OFL.txt` and `fonts/Yuyu/ttf/Yuyu-Regular.ttf`, but no `config_yaml`. The family directory had no override config.yaml.
- The family was added by gftools-packager commit 3a144d4 ("Yuyu: Version 1.004; ttfautohint (v1.8.4.16-eb64) added", 2026-06-05), merged through PR #10595 on 2026-06-08.
- The family directory had no earlier upstream_info.md.

## Actions taken

- Verified the recorded commit. 38e2939 (2026-06-05 14:20 +0200) merges upstream PR #6 (`QA-GFspecs`) and has the same tree as its second parent a32aacf ("build fonts", 2026-06-03). The shipped `Yuyu-Regular.ttf` is byte-identical to `fonts/Yuyu/ttf/Yuyu-Regular.ttf` at that commit (git blob 18148c8b). The next upstream commit, 912e618, is dated 2026-06-16, after the google/fonts merge.
- Found a gftools-builder config at the recorded commit: `sources/config.yaml` (`sources: [Yuyu.glyphs]`, `familyName: "Yuyu"`). Its sibling `sources/config-short.yaml` builds Yuyu Short.
- Build-tested `sources/config.yaml` at 38e2939:
  - gftools-builder3 e851b8b (fontc 1.0.0) built the font. The functional gate passed against the shipped font: 334 codepoints exact, 0 shaping differences, 0 rendering differences, names, line spacing and 339 advances equal. The builder3 recipe for this single-master static config has no autohint step (fontc then fix, plus compress for the woff2), so its build has no `fpgm`/`cvt` tables.
  - The Python gftools builder (0.9.100.dev6+g2db1fe32f.d20260315, fontmake 3.11.1, glyphsLib 6.12.7, ttfautohint-py 0.6.0) rebuilt the shipped font: every table except `head` is byte-identical; `head` differs only in `modified` and `checkSumAdjustment`.
- Added `config_yaml: "sources/config.yaml"` to the METADATA.pb source block.

## Final state

- The source block records `repository_url`, `commit` 38e2939cbadbd7c8deddcbe8e43437972c1fbfe4, `branch` main and `config_yaml` `sources/config.yaml`. No override config.yaml was needed.
- Pending upstream work: 912e618 ("Changes in U+0022 U+2018", 2026-06-16) changed five glyphs in `sources/Yuyu.glyphs` (quotedbl, quoteleft, quotedblleft, quotedblright, ij) after onboarding and did not rebuild the binaries. The shipped font does not include these changes; they need their own review and QA in a future update.

**Status**: complete
**Confidence**: HIGH
