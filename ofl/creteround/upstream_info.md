# Crete Round

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Crete Round (Regular and Italic) built from FontForge SFD sources at https://github.com/librefonts/creteround. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources for both styles were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/creteround, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/creteround (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Both styles matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only accepted difference is that 23 glyphs were renamed to their production names; codepoint coverage is unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/creteround (`.sfd`), latest at commit `056740e1fea281c2e72adeae3d3753083b87d22c`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
