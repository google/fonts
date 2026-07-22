# Balthazar

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Balthazar (Regular) built from FontForge SFD sources at https://github.com/librefonts/balthazar. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Balthazar-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion, stray NUL bytes were stripped and a non-breaking space (U+00A0) was added to match the glyph FontForge used to synthesise at export time.
- A new Unified Font Repository was created at https://github.com/googlefonts/balthazar, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/balthazar (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Two benign differences were accepted: the rebuild drops two FontForge legacy glyphs (`.null` and `nonmarkingreturn`) that carry no Unicode coverage, and 8 glyphs were renamed to their production names with no change to coverage.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/balthazar (`.sfd`), latest at commit `baa08c6f633b0fda1a83141ce7515441c56e9868`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
