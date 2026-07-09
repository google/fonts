# Allan

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Allan (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/allan. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/allan, building the fonts with gftools-builder3 + fontc.
- An explicit OS/2 WeightClass override (700) was added to Bold, because fontc does not yet derive usWeightClass for a static single-master source.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/allan (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Identical to the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/allan (`.sfd`), latest at commit `91202d58a376d6f9bca1234b360e977411222085`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
