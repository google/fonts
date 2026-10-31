# Chathura

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Chathura (Thin, Light, Regular, Bold and ExtraBold) built from FontForge SFD sources at https://github.com/appajid/Chathura. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/Chathura, building the fonts with gftools-builder3 + fontc.
- One dead, shadowed ligature substitution was removed per weight (identical input to a preceding rule; fea-rs rejects it where FontForge silently dropped it).
- The vertical metrics were set to the shipped values, the master name was set so Bold is style-linked, and the below-base form uni0C30_uni0C4D.blwf was given subCategory = Nonspacing so its GDEF class matches the shipped binary.
- An OS/2 WeightClass override was added to the four non-Regular weights (250/300/700/800).
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/Chathura (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Identical to the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths.

## Original repository (dormant)

The original FontForge sources are at https://github.com/appajid/Chathura (`.sfd`), latest at commit `f6944e361db05f2cb3a33356e54615f4cf754de8`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
