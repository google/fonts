# Felipa

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Felipa (Regular) built from FontForge SFD sources at https://github.com/librefonts/felipa. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Felipa-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected to 200 to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/felipa, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/felipa (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 12 glyphs were renamed to their standard production names; the set of encoded characters is unchanged, so this is cosmetic and acceptable.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/felipa (`.sfd`), latest at commit `3489dd2445fc633f3b32485420d9c56998fad093`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
