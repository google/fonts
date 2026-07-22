# Doppio One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Doppio One (Regular) built from FontForge SFD sources at https://github.com/librefonts/doppioone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 410 to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/doppioone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/doppioone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. Two benign differences were accepted: 22 glyphs were renamed to their production names (coverage unchanged), and the GDEF table now classifies the combining mark uni0326 that the shipped font had left unclassified.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/doppioone (`.sfd`), latest at commit `14bdd2e78b5b8e4f5bc5a39e5f1b02d398883a99`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
