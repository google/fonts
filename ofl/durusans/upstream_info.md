# Duru Sans

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `43875057a510`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Duru Sans (Regular) built from FontForge SFD sources at https://github.com/librefonts/durusans. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`DuruSans-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected to 493 units in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/durusans, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/durusans (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Compared against the shipped DuruSans-Regular.ttf, the rebuilt font matched on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The one accepted difference: 22 glyphs were renamed to production names, which leaves coverage unchanged and does not affect rendering.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/durusans (`.sfd`), latest at commit `2895eb6c9842f80c1e01bbf9fbb6231eaef66724`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
