# Geostar

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Geostar (Regular) built from FontForge SFD sources at https://github.com/librefonts/geostar (`src/Geostar-Regular-TTF.sfd`). METADATA.pb carried a bare source block with the upstream repository URL and onboarding commit but no config, and there was no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/geostar, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/geostar (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Geostar Regular was compared against the shipped Google Fonts binary. Glyph coverage, outlines and metrics matched. Two benign differences were accepted: four glyphs were renamed to their production names, leaving glyph coverage unchanged; and the legacy `kern` table (3753 pairs) was modernized into a GPOS `kern` feature. No blocking differences remained.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/geostar (branch `master`, `.sfd`), latest at commit `ca481fdb49204442916697e3d7b1cf6fda792b77`, which is also the onboarding commit. Preserved for provenance; the new `.glyphs` source supersedes it for building.
