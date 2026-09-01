# Geostar Fill

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Geostar Fill (Regular) built from FontForge SFD sources at https://github.com/librefonts/geostarfill. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`GeostarFill-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/geostarfill, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/geostarfill (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GDEF classes and advance widths. Two benign differences were accepted: four glyphs were renamed to their production names (coverage unchanged), and the legacy `kern` table (3796 pairs) was modernized into a GPOS `kern` feature.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/geostarfill (`.sfd`), latest at commit `48dc43d804ebfd6743caa51e2d42d17dd34b275c`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
