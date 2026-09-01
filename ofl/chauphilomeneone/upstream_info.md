# Chau Philomene One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Chau Philomene One (Regular and Italic) built from FontForge SFD sources at https://github.com/librefonts/chauphilomeneone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The two canonical FontForge SFD sources (`ChauPhilomeneOne-Regular-TTF.sfd` and `ChauPhilomeneOne-Italic-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/chauphilomeneone, building both fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/chauphilomeneone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

For both Regular and Italic, the rebuilt fonts matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 4 glyphs were renamed to their standard production names; glyph coverage is unchanged and the difference is cosmetic to the source, so equivalence is functional.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/chauphilomeneone (`.sfd`), latest at commit `ac51123e5c7a33cd48b4fdf686b91922ea68c422`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
