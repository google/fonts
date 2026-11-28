# Finlandica Headline: upstream source metadata

**Model**: Claude Opus 5.5

## Initial state

- `METADATA.pb` had a source block with `repository_url` https://github.com/HelsinkiTypeStudio/FinlandicaHeadline, `commit` c97bd4dd9fd949cf6bc1b854fef368a43c6741f0, `branch` main and two file mappings (`fonts/variable/FinlandicaHeadline[wght].ttf`, `fonts/variable/FinlandicaHeadline-Italic[wght].ttf`). It had no `config_yaml`, and the family directory had no override `config.yaml`.
- The family was onboarded at Version 3.103 by gftools-packager (commit 72aecac, "Finlandica Headline: Version 3.103 added", which names upstream commit c97bd4dd), merged through PR #10454 on 2026-04-29.
- No earlier `upstream_info.md` existed for this family.

## Actions taken

- Verified the recorded commit. The two shipped binaries are byte-identical to `fonts/variable/` at c97bd4dd (git blobs 2d4d47e5 and 9df7f8a2). c97bd4dd (2026-04-18) merged upstream PR #4, whose last commit 786c22d ("rebuild fonts", 2026-04-17, by the onboarder) produced these binaries; its tree equals that of c97bd4dd. No upstream commit landed between c97bd4dd and the google/fonts merge. The next upstream commits, 80e954c and its merge 59c9529 ("Refine Cyrillic glyphs", 2026-09-25/26, both `.glyphs` sources changed), postdate the merge and were not onboarded.
- Found `sources/config.yaml` at c97bd4dd. It builds `sources/FinlandicaHeadline.glyphs` and `sources/FinlandicaHeadline-Italic.glyphs` and sets `familyName`, `axisOrder`, `cleanUp` and per-font `stat` tables.
- Added `config_yaml: "sources/config.yaml"` to the source block. No override `config.yaml` was needed.
- Build-tested the upstream config at c97bd4dd with gftools-builder3 (e851b8b, fontc 1.0.0). The build succeeded. Both variable fonts matched the shipped ones functionally (sfd-reland `tools/functional_gate.py`: PASS): 964 codepoints with an exact cmap, 0 of about 5.5 million shaped runs differing per font, 0 diffenator3 glyph or word diffs, equal names 1/2/4/6/16/17/21/22, equal line spacing, 1165 equal advances, equal GDEF. The version (3.103), glyph set (1172), fvar axis and 9 instances, and STAT were also equal. Differences that were reported but not gated: name ID 5 gained ";fontc 1.0.0", name ID 13 kept the license URL of the sources (https://scripts.sil.org/OFL instead of https://openfontlicense.org), name ID 25 was absent, instance names were renumbered from ID 257, head.flags was 11 instead of 3, and some outlines differed by 1-unit rounding. builder3 built no OTFs, and its static set had no upright Regular: the Italic instance was written as `FinlandicaHeadline-Regular.woff2` and as either `FinlandicaHeadline-Regular.ttf` or `FinlandicaHeadline-Italic.ttf`, depending on the run. Google Fonts ships only the two variable fonts, so these static outputs do not affect this family.
- Also built the same config with the Python gftools builder (0.9.100.dev6). The upright variable font matched the shipped file in every table except the `head` timestamp and checksum; the italic one also differed by 1 unit in the `gvar` deltas of one glyph (uni03020303).

## Final state

- The source block records `repository_url`, `commit` c97bd4dd9fd949cf6bc1b854fef368a43c6741f0, `branch` main, the two file mappings and `config_yaml: "sources/config.yaml"`.
- Status: complete. Confidence: HIGH.
