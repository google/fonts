# Dr Sugiyama

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Dr Sugiyama (Regular) built from FontForge SFD sources at https://github.com/librefonts/drsugiyama. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`DrSugiyama-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`). Four stray NUL bytes in the SFD were stripped during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/drsugiyama, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/drsugiyama (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only accepted difference is that 5 glyphs were renamed to their production names; character coverage is unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/drsugiyama (`.sfd`), latest at commit `11d194b70af6df309a24c9395f64280172839879`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
