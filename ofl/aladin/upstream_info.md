# Aladin

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Aladin (Regular) built from FontForge SFD sources at https://github.com/librefonts/aladin. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- U+00A0 (no-break space) was added to the converted source to reproduce the glyph that FontForge synthesised at export time.
- A new Unified Font Repository was created at https://github.com/googlefonts/aladin, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/aladin (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The new build was compared against the shipped Aladin-Regular.ttf on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Everything matched except that 5 glyphs now carry their production names; coverage by codepoint is unchanged, so the difference is cosmetic and benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/aladin (`.sfd`), latest at commit `0f5d0578e592bfa8431072ad4f1a557fb74c165b`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
