# Isometra

## Initial state

METADATA.pb recorded https://github.com/field2/isometra at commit `06b2637a62ad47c2f28ae2220757f6b492d6f3b1` (branch `main`) with no `config_yaml`, and `ofl/isometra` had no override `config.yaml`. Without either, google-fonts-sources skipped the family, so fontc_crater had no build target for it.

The upstream tree at that commit has a gftools-builder config, `sources/config.yaml`, but it lists `Isometra.glyphs` while the committed source is `sources/isometra.glyphs` (lowercase). The name resolves only on a case-insensitive filesystem. On Linux, gftools-builder3 and gftools builder both stopped with "No such file or directory" when given that config. fontc_crater records "missing source" for a listed file that does not exist, so pointing `config_yaml` at `sources/config.yaml` would not have produced a buildable target.

## Actions taken

- The recorded commit was verified. It is the merge of upstream PR #2 (2026-08-20) and the last commit on `main`. The shipped `Isometra-Regular.ttf` is byte-identical to `fonts/ttf/Isometra-Regular.ttf` at that commit (git blob `6206f134`), which upstream commit `4afe4be` ("font built") added. Its `head.modified` (2026-08-20 14:34:07 UTC) falls 39 seconds before that commit. The gftools-packager commit of google/fonts PR #10834 (merged 2026-09-04) names the same commit.
- An earlier onboarding from `c8cdf0e` (PR #10785) was reverted by PR #10810. At `c8cdf0e`, 52 glyphs of the source had no outlines. The designer drew them in `183215f` (2026-08-06), before the final build at `4afe4be`. The glyph set (329 glyphs, 323 codepoints) did not change.
- An override `config.yaml` was added to `ofl/isometra`. It keeps the upstream settings (`familyName: Isometra`, `cleanUp: true`) and lists `sources/isometra.glyphs`, relative to the repository root.
- `config_yaml` was left unset in METADATA.pb because the override takes its place. METADATA.pb was not changed.

## Final state

The override builds at the recorded commit:

- gftools-builder3 (`e851b8b`, fontc 1.0.0) built one static TTF with 329 glyphs, 323 codepoints and Version 1.001. A functional comparison with the shipped font passed on cmap, shaping, rendering, names, line spacing, advances and GDEF. The output is unhinted; the shipped font is hinted with ttfautohint.
- gftools builder (fontmake 3.11.1, ttfautohint-py 0.6.0) built a TTF that matches the shipped font in every table except `head.modified` and `head.checkSumAdjustment`.

If upstream fixes the file name in `sources/config.yaml` and a later update moves to that commit, the override can be replaced by `config_yaml: "sources/config.yaml"`.
