# Condiment

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Condiment (Regular) built from FontForge SFD sources at https://github.com/librefonts/condiment. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`Condiment-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`). During conversion four glyphs were given their standard production names, leaving codepoint coverage unchanged.
- A new Unified Font Repository was created at https://github.com/googlefonts/condiment, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/condiment (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that four glyphs were renamed to their production names; the set of encoded codepoints is unchanged, so this is accepted as functionally equivalent.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/condiment (`.sfd`), latest at commit `0a1933e09c9008136f997c47c75ddf6b00a8d884`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
