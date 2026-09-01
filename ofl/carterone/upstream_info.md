# Carter One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Carter One (Regular) built from FontForge SFD sources at https://github.com/librefonts/carterone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`CarterOne-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the outlines were mapped to standard production glyph names and the FontForge legacy `.null` glyph was dropped.
- A new Unified Font Repository was created at https://github.com/googlefonts/carterone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/carterone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

Identical to the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only differences are benign: the FontForge legacy `.null` glyph was dropped, and 6 glyphs were renamed to standard production names with Unicode coverage unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/carterone (`.sfd`), latest at commit `9943144e585a736a95509a85b92fbf2bb29060c2`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
