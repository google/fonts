# Euphoria Script

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Euphoria Script (Regular) built from FontForge SFD sources at https://github.com/librefonts/euphoriascript. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`EuphoriaScript-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/euphoriascript, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/euphoriascript (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The build matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 4 glyphs were renamed to their standard production names during conversion; glyph coverage is unchanged, so this is accepted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/euphoriascript (`.sfd`), latest at commit `c7606fae5a17e051d983269f008dba6e8f4c0c77`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
