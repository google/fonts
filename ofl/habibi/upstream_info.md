# Habibi

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Habibi (Regular) built from FontForge SFD sources at https://github.com/librefonts/habibi. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`Habibi-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected to match the space glyph (686 units).
- A new Unified Font Repository was created at https://github.com/googlefonts/habibi, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/habibi (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Two benign differences were accepted: 22 glyphs were renamed to their production names (coverage unchanged), and the GDEF table now classifies two real combining marks (uni0326 and uni0326.cap) that the shipped font had left unclassified.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/habibi (`.sfd`), latest at commit `1c3eb606631e9da373f1017f7972765a7ab32bd5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
