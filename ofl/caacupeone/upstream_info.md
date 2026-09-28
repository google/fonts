# Caacupe One: upstream source information

**Date investigated**: 2026-09-27
**Model**: Claude Opus 5.5

- **Repository**: https://github.com/googlefonts/caacupe
- **Commit**: 9c4e9828f887cbf1bafdae5232d86c644777576e
- **Branch**: main
- **Config**: sources/config.yaml (upstream)
- **Status**: complete
- **Confidence**: HIGH

## Initial state

- METADATA.pb had a source block with repository_url, branch, file mappings and commit 07166dbe0310593a587ac99055a97b32f70b1630, but no config_yaml. The family directory had no override config.yaml and no upstream_info.md.
- That commit came from the gftools-packager commit 59b8ba3 of PR #10666 (2026-07-01 16:18 +0200), whose TTF was identical to the upstream TTF at 07166dbe.
- Later in the same PR, commit b0ea14e ("small fix in copyright", 2026-07-01 17:55:04 +0200) replaced the TTF, and the commit field was not updated. The shipped TTF is byte-identical (git blob cfcf8b9b) to fonts/ttf/CaacupeOne-Regular.ttf at upstream commit 9c4e982 ("small fix in copyright and name", 17:54:35 +0200), and no other upstream commit contains that file. 9c4e982 changed the copyright and the localized family names in sources/Caacupe.glyphs and updated the TTF and WOFF2 binaries.
- sources/config.yaml existed upstream, unchanged, at both commits. 9c4e982 predates the merge of PR #10666 (2026-07-03) and was still the head of upstream main on 2026-09-27.

## Actions taken

- Changed commit to 9c4e9828f887cbf1bafdae5232d86c644777576e, the upstream commit whose TTF google/fonts ships.
- Set config_yaml to sources/config.yaml.
- Built 9c4e982 with sources/config.yaml:
  - gftools builder (Python; gftools 0.9.100.dev6+g2db1fe32f.d20260315, fontmake 3.11.1, glyphsLib 6.12.7) produced CaacupeOne-Regular.ttf, identical to the shipped file in every table except head (modified, checkSumAdjustment).
  - gftools-builder 3.0.0 (builder3 e851b8b, fontc 1.0.0) produced a font that passed the functional gate against the shipped file (cmap, shaping, rendering, names, line spacing, advances, GDEF). It was unhinted, because builder3 e851b8b adds no autohint step for a single-master static. It was named Unknown-Regular.ttf, because the .glyphs file carries familyNames only under the ENG and ESP language tags and builder3 names static files from the default-language (dflt) entry.

## Final state

- METADATA.pb points at commit 9c4e982 and at the upstream sources/config.yaml. No override config.yaml was needed.
- The shipped OFL.txt differs from upstream: google/fonts commit c08e603 changed its first line to "The Caacupe One Project Authors", while upstream OFL.txt at 9c4e982 still reads "The Caacupe Project Authors". A packager run from upstream would revert that line unless upstream OFL.txt is updated.
