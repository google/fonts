# Amarante

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Amarante (Regular) built from FontForge SFD sources at https://github.com/librefonts/amarante. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Amarante-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/amarante, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/amarante (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 22 glyphs were renamed to their production names; this leaves coverage and rendering unchanged, so the verdict is functional equivalence.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/amarante (`.sfd`), latest at commit `e5bd4a952443385746182ed5f729787c33ed04d3`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
