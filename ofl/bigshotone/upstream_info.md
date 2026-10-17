# Bigshot One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `f29b15c2cb86`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Bigshot One (Regular) built from FontForge SFD sources at https://github.com/librefonts/bigshotone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The advance width of the non-breaking space (U+00A0) was corrected to 160 during conversion so the built binary matches the shipped one.
- A new Unified Font Repository was created at https://github.com/googlefonts/bigshotone, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/bigshotone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at full equivalence with the shipped binaries.

## Verification

Full parity with the shipped binary: identical on every dimension checked, including cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/bigshotone (`.sfd`), latest at commit `b8d1fa459ee9a43fbe1d7fd07b570878206bd6d5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
