# Geomini: upstream source metadata

**Model**: Claude Opus 5.5
**Date**: 2026-09-27
**Repository**: https://github.com/fontbob/geomini
**Commit**: 259385339d2974bf793425df09a25381939bd7aa (kept)
**Config**: sources/config.yaml (upstream)

## Initial state

- `METADATA.pb` had a source block with `repository_url`, `commit` 259385339d29, `archive_url` (release `2026-05-13`, asset `fonts.zip`), two file mappings and `branch: "main"`, but no `config_yaml`.
- The family directory had no override `config.yaml` and no earlier `upstream_info.md`.
- gftools-packager onboarded the family in google/fonts PR #10527 ("Geomini: Version 1.000 added", commit d198aa8, authored 2026-05-20, merged 2026-06-23).

## Actions taken

- Verified the recorded commit against the shipped binary:
  - The shipped `Geomini[wght].ttf` (sha1 987301b4) is byte-identical to `fonts/variable/Geomini[wght].ttf` in the release asset `fonts.zip`.
  - The release tag `2026-05-13` points to 63193a3, but the binary is later. Its `head.created` is 2026-05-15 12:25:33 UTC (14:25:33 +0200), 22 seconds after 1472af1 (merge of upstream PR #2, 14:25:11 +0200). Its name ID 13 is the multi-line text that `scripts/post_build_patch_fonts.py` wrote up to 1472af1; c5a05b0 (14:33 +0200) made that text single-line. This places the build between 1472af1 and c5a05b0.
  - The binary's ten digits are tabular (604 units), as in the sources from c69c2fa onwards. At the tag, the ExtraLight digits were proportional (537-673 units).
  - `sources/` is identical at 1472af1, at the recorded commit 2593853 (14:46 +0200, "Add OFL.txt to generated fonts dir") and at the current HEAD f4708e8 (2026-07-11). The commits between 1472af1 and 2593853 changed only the patch script and the Makefile. The commits after 2593853 changed only `README.md` and one documentation image. No source commit landed after the build, before or after the google/fonts merge.
  - Kept the recorded commit.
- Found the gftools-builder config `sources/config.yaml` at the recorded commit. It lists `ufo/Geomini.designspace` and both master UFOs and defines the STAT table for wght 200-800.
- Built the recorded commit with that config:
  - gftools-builder 3.0.0 (builder3 e851b8b, fontc 1.0.0) failed with "feature files are non-identical: ufo/Geomini-ExtraLight.ufo/features.fea, ufo/Geomini-ExtraBold.ufo/features.fea". Each master's `features.fea` has a hard-coded `mark` feature with that master's anchor coordinates. fontc refuses masters whose feature files differ. fontmake (ufo2ft) compiles each master's features separately and merges them, so the shipped font's mark anchors vary with weight and match each master exactly. This is a fontc limitation, not a config error.
  - The Python builder (gftools 0.9.100.dev6, fontmake 3.11.1) succeeded and produced the same 16 font files as `fonts.zip`.
  - Compared the built variable font with the shipped one. All tables except `head` (timestamps, checksum) and `name` were byte-identical, including `glyf`, `gvar`, `GPOS`, `GSUB`, `STAT` and `fvar`. The built `name` table lacks IDs 13 and 14, which upstream adds after the build with `scripts/post_build_patch_fonts.py`, outside the gftools-builder config. `functional_gate.py` passed all seven checks: 322 codepoints; 846244 shaping runs, 0 different; 323 advances equal.
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- `METADATA.pb` references the upstream config. No override `config.yaml` is needed.
- With the Python builder, the config reproduces the shipped font except for name IDs 13 and 14.
- fontc-based builds (builder3, fontc_crater) fail on this config because the two masters' feature files differ.
