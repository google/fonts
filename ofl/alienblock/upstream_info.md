# Alien Block: upstream source information

## Initial state

- `ofl/alienblock/METADATA.pb` had a source block with `repository_url` https://github.com/koci-design/AlienBlock, `commit` 036f8f19c165a455a9c967618557492ed9db94e3 and `branch` main, but no `config_yaml`. The family directory had no override `config.yaml` and no earlier `upstream_info.md`.
- gftools-packager onboarded the family in google/fonts commit cde5536d23 ("Alien Block: Version 1.000; ttfautohint (v1.8.4.16-eb64) added", 2026-05-01 10:30 +0200), merged by PR #10491 on 2026-05-01 11:27 +0100.

## Actions taken

- Verified the recorded commit. 036f8f1 is koci-design's merge of upstream PR #1 ("Add Alien Block", from emmamarichal/main) at 2026-05-01 10:58 +0900 (03:58 +0200). Its tree is identical to its second parent 6c7f57a ("fonts built", 2026-04-30). It predates the google/fonts commit, and it was still the upstream HEAD on 2026-09-27, so there are no later upstream commits. The shipped `AlienBlock-Regular.ttf` is byte-identical to `fonts/ttf/AlienBlock-Regular.ttf` at that commit (git blob 8c829244), and `OFL.txt` is identical as well.
- Found a gftools-builder config at `sources/config.yaml` in the upstream tree at that commit (added in 647da2c, "added config.yaml to build"):

  ```yaml
  sources:
    - AlienBlock.glyphs
  familyName: Alien Block
  cleanUp: true
  ```

- Rebuilt that config at 036f8f1 with the Python gftools builder (gftools 0.9.100.dev6+g2db1fe32f.d20260315, fontmake 3.11.1, glyphsLib 6.12.7, ttfautohint-py 0.6.0). Every table of the built TTF was byte-identical to the shipped binary except `head`, where only `modified` and `checkSumAdjustment` differed.
- Built the same config with gftools-builder3 (simoncozens/gftools-builder3 e851b8b, fontc 1.0.0). The build succeeded and wrote `fonts/ttf/AlienBlock-Regular.ttf`. `functional_gate.py` (sfd-reland 218e487) passed all seven checks: cmap (321 codepoints, exact), shaping (807425 runs, 0 differ), rendering, names, line_spacing, advances (322 glyphs, 0 differ) and gdef. It reported these differences outside the verdict: the builder3 build is unhinted, because builder3's single-master static recipe has no autohint step, while the release is ttfautohinted. Name ID 5 reads "Version 1.000;fontc 1.0.0" instead of "Version 1.000; ttfautohint (v1.8.4.16-eb64)". 60 glyphs store their outlines differently (point structure, rounding) but draw the same ink.
- Added `config_yaml: "sources/config.yaml"` to the source block of METADATA.pb. No override config.yaml was needed.

## Final state

- The source block records `repository_url`, `commit` 036f8f19c165a455a9c967618557492ed9db94e3, `branch` main and `config_yaml` sources/config.yaml.
- The recorded commit and config rebuild the shipped font. The Python builder reproduces it apart from the `head` timestamp, and builder3 produces a functionally equivalent, unhinted build.
- Status: complete. Confidence: HIGH.
