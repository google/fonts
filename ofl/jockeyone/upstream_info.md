# Jockey One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Jockey One (Regular) built from FontForge SFD sources at https://github.com/librefonts/jockeyone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/JockeyOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 160 in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/jockeyone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/jockeyone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets. Three benign differences were accepted: the FontForge-only helper glyph `nonmarkingreturn` was dropped; 13 glyphs were renamed to their production names with no change in coverage; and GDEF now classifies two real combining marks (uni0326 and uni0326.cap) that the shipped font had left unclassified.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/jockeyone (`.sfd`), latest at commit `71261c6f0c80fb7269df32e4aa396669a038030f`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
