# Cambo

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Cambo (Regular) built from FontForge SFD sources at https://github.com/librefonts/cambo. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Cambo-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/cambo, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/cambo (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference was 10 glyphs renamed to their production names, which leaves cmap coverage unchanged; the fonts are therefore functionally equivalent.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/cambo (`.sfd`), latest at commit `3b97d12b34a587e8868700ffa711df7dc6aa0d04`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
