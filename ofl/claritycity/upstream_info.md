# Clarity City: upstream source metadata

**Model**: Claude Opus 5.5
**Date**: 2026-09-27

## Initial state

- METADATA.pb had a source block with repository_url https://github.com/googlefonts/clarity-city, branch "next", file mappings for OFL.txt and both variable fonts, and commit 0193ff048d04acd372716672b45eb88ee3a0119e.
- It had no config_yaml. The family directory had no override config.yaml and no earlier upstream_info.md.
- The family was added through PR #10848 (merged 2026-09-04). Its first commit, 5a7120639 (2026-08-27, "Clarity City: Version 1.000 added"), cited upstream 0193ff0. A comment in that PR then reported the position of the ncommaaccent comma in the Italic. 09afe44c6 (2026-08-28, "Fix ncommaaccent (ital)") replaced both binaries and did not update METADATA.pb.

## Actions taken

- The shipped binaries were compared with the upstream history. Both current files are byte-identical (same git blob) to fonts/variable/ at upstream 0931475a6dc023d191ac5de7c16e8739c16e31f3 ("build fonts", 2026-08-28, head of next). That commit directly follows db50dde ("fix n anchor in italic"), which moved the ncommaaccent comma in the Italic (wght 400) master from x=63 to x=194.
- At 0193ff0, fonts/variable/ still held the binaries committed in 0b440d9, which were the first shipped set. The sources at 0193ff0 already included the italic spacing edits made in that commit.
- 0193ff0 was built as a control with the same toolchain. At the default instance its Italic places the comma of U+0146 at x=63, as the first shipped Italic does. The current shipped Italic and a build of 0931475 place it at x=194. The upright builds of the two commits have identical glyf, gvar, hmtx and layout tables.
- commit was changed to 0931475a6dc023d191ac5de7c16e8739c16e31f3.
- At that commit, sources/config.yaml is a gftools-builder config with the two .glyphs sources and STAT definitions. It has not changed since 0b440d9. config_yaml was set to "sources/config.yaml", and no override was needed.
- The config was build-tested with gftools-builder3 (e851b8b, fontc 1.0.0), and both variable fonts built. Compared with the shipped files, the builds have:
  - the same 353 glyphs in the same order and an identical cmap (338 codepoints)
  - the same fvar (wght 100-900, default 400, 9 instances)
  - the same table set, the same STAT and the same vertical metrics
- functional_gate.py gave PASS for both fonts: 0 of about 1.26 million shaped runs differed per font, with 0 diffenator3 diffs and 0 advance differences.
- Two name records differ:
  - Name ID 5 gains ";fontc 1.0.0".
  - Name ID 25 (Variations PostScript Name Prefix) is "ClarityCity" and "ClarityCityItalic" in the shipped files and is absent from the builder3 output. A Python gftools builder build of the same commit writes both values, so the missing record comes from builder3 and not from the config.

## Final state

- source.commit: 0931475a6dc023d191ac5de7c16e8739c16e31f3 (the upstream commit whose fonts/variable/ files are the shipped binaries)
- source.config_yaml: sources/config.yaml (upstream; no override)
- repository_url, branch "next" and the file mappings are unchanged.

## Repository history

googlefonts/clarity-city continues the VMware repository https://github.com/vmware/clarity-city. That repository's master and next branches are still at f2ecc97 (2020-11-11). Its history starts on 2015-11-24 and has 131 commits: 118 authored as Chris Simpson and 1 as Chris. Tag v1.0.0 is at 7f234b1 (2019-12-10). The repository held:

- Source/ (six UFOs, ClarityCity.glyphs, ClarityCity-Italic.glyphs)
- OpenType/ (18 OTF) and TrueType/ (18 TTF)
- Webfonts/ and css/
- package.json (@cds/city 1.1.0)

The Google Fonts work began on 2026-08-26 on branch next, at f4b410c, whose parent is f2ecc97. The googlefonts repo keeps the master (f2ecc97) and rebranding (e107561) branches.
