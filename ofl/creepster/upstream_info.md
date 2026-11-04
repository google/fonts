# Creepster

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Creepster (Regular) built from FontForge SFD sources at https://github.com/librefonts/creepster. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/creepster, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/creepster (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional parity with the shipped binaries.

## Verification

cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and advance widths are identical to the shipped binary. The 1488 kerning pairs are preserved but modernized from the shipped legacy `kern` table to a GPOS `kern` feature (the current Google Fonts mechanism); neither version has any other OpenType layout tables.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/creepster (`.sfd`), latest at commit `f6eec0d741fd8ecba905f403d77c073f2e8be7f6`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
