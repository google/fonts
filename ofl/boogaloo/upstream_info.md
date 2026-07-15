# Boogaloo

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Boogaloo (Regular) built from FontForge SFD sources at https://github.com/librefonts/boogaloo. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`Boogaloo-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected to match the space glyph (484 units).
- A new Unified Font Repository was created at https://github.com/googlefonts/boogaloo, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/boogaloo (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 15 glyphs were renamed to their production names; character coverage is unchanged, so this is accepted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/boogaloo (`.sfd`), latest at commit `9837380f883a9af75b9d4a9767020c1b1abc771a`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
