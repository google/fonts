# Hibur Mono: upstream source information

**Model**: Claude Opus 5.5

## Initial state

- `ofl/hiburmono/METADATA.pb` had a source block with `repository_url` https://github.com/typehabesha/HiburMono, `commit` ff7211ea4674598efa977f266bd61f1ee6b9e5d2, `archive_url` https://github.com/typehabesha/HiburMono/releases/download/v1.0.1/HiburMono-v1.0.1.zip, `branch` main and file mappings for OFL.txt and fonts/ttf/HiburMono-Regular.ttf. It had no `config_yaml`.
- The family directory had no override config.yaml and no earlier upstream_info.md.
- The shipped HiburMono-Regular.ttf (Version 1.001) came from PR #10795, merged 2026-08-14.

## Actions taken

- We verified the recorded commit. ff7211e (2026-07-30 21:54 -0400) is the target of tag v1.0.1 and is still the tip of upstream main. No upstream commit followed it before the merge. The gftools-packager commit message and the PR #10795 body both name it.
- We compared the binaries. The shipped TTF is byte-identical to the one in the v1.0.1 release zip. The upstream CI release job, which runs only for tags, built that zip: its entries and the TTF's head.modified are dated 2026-07-31 02:10 UTC, 15 minutes after ff7211e. The TTF committed at ff7211e differs from the shipped one only in the head table (modified date and checksum).
- We checked when the sources last changed: at 373ffad (2026-07-21, the U+1374 glyph fix). Later commits up to ff7211e touched only binaries, documentation, the CHANGELOG, METADATA.pb, Nerd Fonts files and scripts.
- We found the gftools-builder config sources/config.yaml at ff7211e. It builds sources/HiburMono-Regular.ufo, and the upstream Makefile and CI build the fonts with it.
- We built ff7211e with that config using gftools-builder3 (fontc) and the Python gftools builder. Both builds succeeded.
- The functional gate compared each build with the shipped font and gave PASS on cmap, shaping, rendering, names, line spacing, advances and GDEF. Both builds have the same 991 glyphs and 989 codepoints as the shipped font.
- The Python build matches the shipped TTF byte for byte in every table except head (modified date and checksum) and GSUB. In GSUB, two contextual lookups (ordn and the ccmp dotless i/j lookup) keep their two rules in two subtables, where the shipped font merges each pair into one. The coverage, context and substitutions are the same.
- The builder3 build is unhinted, and builder3 produced no OTF: the builder3 revision tested (main-e851b8b) has no autohint step and no OTF target for single-master statics.
- We added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The source block records repository_url, the verified commit ff7211e, archive_url, the file mappings, branch main and config_yaml sources/config.yaml.
- The upstream config builds the family. No override config.yaml was needed.
