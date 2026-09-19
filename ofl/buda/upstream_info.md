# Buda

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Buda (Light) built from FontForge SFD sources at https://github.com/librefonts/buda. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/buda, building the fonts with gftools-builder3 + fontc.
- An explicit OS/2 WeightClass override (300) was added (usWeightClass Light).
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/buda (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/buda (`.sfd`), latest at commit `c632d6ba92f1c89f40f704c2cd873d5a9ede22a6`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
