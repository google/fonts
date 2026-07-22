# Chela One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Chela One (Regular) built from FontForge SFD sources at https://github.com/librefonts/chelaone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`ChelaOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A no-break space (U+00A0) was added to the source, matching the glyph FontForge used to synthesise at export time.
- A new Unified Font Repository was created at https://github.com/googlefonts/chelaone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/chelaone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 8 glyphs were renamed to their production names, which leaves character coverage unchanged; this is why the verdict is functional rather than byte-identical.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/chelaone (`.sfd`), latest at commit `cb9b95fc0510c91bc45664e5a62ed3893c09bfba`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
