# Condiment

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied vertical metrics, GDEF classes and other values out of the shipped binary). The sources were regenerated purely from the original FontForge `.sfd`, byte-identical to the repository's own history, with babelfont `c368660` (gftools-builder3 `17b215c5` + fontc `3518040e`, 0.6.0); diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style. METADATA.pb now references the rebuild commit `e9c65b8fd138`.

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
