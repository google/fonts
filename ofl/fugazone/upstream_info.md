# Fugaz One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Fugaz One (Regular) built from FontForge SFD sources at https://github.com/librefonts/fugazone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`FugazOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`). Four glyphs were renamed to their production names during conversion; glyph coverage was unchanged.
- A new Unified Font Repository was created at https://github.com/googlefonts/fugazone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/fugazone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 4 glyphs were renamed to their production names, which leaves coverage and rendering unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/fugazone (`.sfd`), latest at commit `d6fef0584e47767dc53d0144d0d41de77088184b`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
