# Fresca

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Fresca (Regular) built from FontForge SFD sources at https://github.com/librefonts/fresca. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Fresca-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted source was corrected: the non-breaking space (U+00A0) advance width was fixed to match the space glyph (253).
- A new Unified Font Repository was created at https://github.com/googlefonts/fresca, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/fresca (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Fresca-Regular was compared against the shipped binary and matched on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and the GSUB/GPOS feature sets. The verdict is FUNCTIONAL, with these accepted differences: the FontForge legacy glyph `nonmarkingreturn` was dropped; 14 glyphs were renamed to production names with coverage unchanged; the new GDEF correctly classifies two combining marks (U+0307, U+0326) that the shipped font failed to mark; and one combining mark (U+0307) had its advance zeroed, where the shipped font had given it a spacing advance.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/fresca (`.sfd`), latest at commit `ca8ad60bad380c425ebe357ee8a3a71770a849b4`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
