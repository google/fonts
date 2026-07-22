# Economica

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Economica (Regular, Italic, Bold, Bold Italic) built from FontForge SFD sources at https://github.com/librefonts/economica. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The four canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to match the space glyph, and an explicit OS/2 usWeightClass of 700 was set on the Bold and Bold Italic sources.
- A new Unified Font Repository was created at https://github.com/googlefonts/economica, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/economica (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Each style matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 6 glyphs were renamed to their production names in each style; character coverage is unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/economica (`.sfd`), latest at commit `6bf48e6858755227cdd104ee4b44e9e2e4bb197b`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
