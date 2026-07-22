# Asul

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Asul (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/asul. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The Bold source's OS/2 usWeightClass was set to 700, which the SFD had not recorded.
- A new Unified Font Repository was created at https://github.com/googlefonts/asul, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/asul (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

For both Regular and Bold, the rebuilt fonts matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 9 glyphs were renamed to their production names; glyph coverage is unchanged, so this is accepted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/asul (`.sfd`), latest at commit `687362de82c870100b6003ad71a82c3327e05d90`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
