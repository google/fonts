# Ceviche One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Ceviche One (Regular) built from FontForge SFD sources at https://github.com/librefonts/cevicheone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/CevicheOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A non-breaking space (U+00A0) was added to the converted source, restoring a glyph that FontForge used to synthesise at export time.
- A new Unified Font Repository was created at https://github.com/googlefonts/cevicheone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/cevicheone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The newly built Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference was that 8 glyphs were renamed to their production names; coverage was unchanged, so the verdict is functional equivalence.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/cevicheone (`.sfd`), latest at commit `afec42c6e7445edd88c3f45b7a51b5da6b43b027`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
