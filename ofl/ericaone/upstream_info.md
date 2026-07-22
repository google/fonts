# Erica One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Erica One (Regular) built from FontForge SFD sources at https://github.com/librefonts/ericaone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`EricaOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- Seven glyphs were renamed to their standard production names during conversion; codepoint coverage was unchanged.
- A new Unified Font Repository was created at https://github.com/googlefonts/ericaone, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/ericaone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference was seven glyphs renamed to their standard production names, which leaves codepoint coverage unchanged and is therefore accepted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/ericaone (`.sfd`), latest at commit `bde7cb1ee528f936a9bae89a746742983531d9f8`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
