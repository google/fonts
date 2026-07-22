# Delius

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Delius (Regular) built from FontForge SFD sources at https://github.com/librefonts/delius. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`Delius-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 238 in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/delius, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/delius (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Delius Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 11 glyphs were renamed to their production names; character coverage is unchanged, so this is benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/delius (`.sfd`), latest at commit `5bd1633b6b5175d36e260f3f6d06686482d32212`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
