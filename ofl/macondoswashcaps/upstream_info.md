# Macondo Swash Caps

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Macondo Swash Caps (Regular) built from FontForge SFD sources at https://github.com/librefonts/macondoswashcaps. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/macondoswashcaps, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/macondoswashcaps (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 9 glyphs were renamed to their standard production names; glyph coverage is unchanged, so this is cosmetic and acceptable.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/macondoswashcaps (`.sfd`), latest at commit `2768d9b33c7d703085314fcd8c823ad1a8b02edb`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
