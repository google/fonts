# Covered By Your Grace

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Covered By Your Grace (Regular) built from FontForge SFD sources at https://github.com/librefonts/coveredbyyourgrace. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/CoveredByYourGrace-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`). A few stray NUL bytes were stripped from the SFD and the non-breaking space was normalized during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/coveredbyyourgrace, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/coveredbyyourgrace (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Regular was compared against the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. It matched functionally, with three accepted differences: the converted source's cmap adds 4 codepoints; 18 glyphs were renamed to production names with coverage unchanged; and GDEF now classifies uni0326 as a combining mark that the shipped font had missed.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/coveredbyyourgrace (`.sfd`), latest at commit `eca9fdc2d5ae964ff4838cb850b215d9ea703801`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
