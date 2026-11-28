# Valley Sans: upstream source metadata

## Initial state

- `METADATA.pb` had a source block with `repository_url` https://github.com/HelsinkiTypeStudio/valley-sans, `commit` f5c2dec81e78da325c6934da87b6a6ad4c236e6a, `branch` main and file mappings for `OFL.txt` and the two variable fonts, but no `config_yaml`.
- The family directory had no override `config.yaml` and no earlier `upstream_info.md`.
- The family was onboarded at version 1.001 by google/fonts PR #10755 (gftools-packager commit f5c1887; the PR was merged on 2026-07-31). The packager commit recorded upstream commit f5c2dec.

## Actions taken

- Verified the recorded commit against the upstream repository:
  - f5c2dec (2026-07-28, "typo in readme") was the upstream HEAD when PR #10755 was opened (2026-07-29) and merged (2026-07-31). The next upstream commit is dated 2026-09-07.
  - The shipped `ValleySans[wght].ttf`, `ValleySans-Italic[wght].ttf` and `OFL.txt` are byte-identical to `fonts/variable/` and `OFL.txt` at f5c2dec (same git blobs).
  - The binaries were last rebuilt in ecf64a5 (2026-07-27). The commits from ecf64a5 to f5c2dec touched only the CI workflow (net unchanged), `requirements.in`, the README, the article and documentation images. `sources/` is identical from ecf64a5 through the current upstream HEAD 010d315.
- Found a gftools-builder configuration at `sources/config.yaml` at f5c2dec. It lists `ValleySans.glyphspackage` and `ValleySans-Italic.glyphspackage` and is the file the upstream Makefile and CI build from. `sources/ValleySans.glyphs`, a combined four-master file, is not used by the config.
- Build-tested `sources/config.yaml` at f5c2dec:
  - gftools-builder3 (fontc 1.0.0) failed with `missing master` on every glyph of both packages. Each `.glyph` file in both packages carries a layer for each of the four masters of the combined file, so two layers per glyph belong to masters that exist only in the other package. glyphsLib skips such dangling layers; fontc treats them as master layers and stops. The failure comes from fontc, not from the config.
  - The Python gftools builder (fontmake 3.11.1, glyphsLib 6.12.7) built both variable fonts. Glyph set (545), cmap (467 codepoints), `glyf`, `gvar`, `GPOS`, `name` and metrics matched the shipped fonts exactly; `GSUB` differed only in the encoding of one chained-context subtable and `head` only in its timestamp and checksum. The functional gate returned PASS for both styles.
  - A scratch copy with only those two foreign master layers per glyph removed built with gftools-builder3 and also returned PASS, so those layers are the only fontc blocker.
- Added `config_yaml: "sources/config.yaml"` to the source block of `METADATA.pb`.

## Final state

- `METADATA.pb` points to `sources/config.yaml` at commit f5c2dec81e78da325c6934da87b6a6ad4c236e6a. No other field changed.
- The config reproduces the shipped fonts functionally with the Python gftools builder. A fontc build needs either a fontc fix for dangling layers or removal of those layers upstream.
