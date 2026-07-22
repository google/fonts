# Copse

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Copse (Regular) built from FontForge SFD sources at https://github.com/librefonts/copse. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Copse-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to match the space glyph (440).
- A new Unified Font Repository was created at https://github.com/googlefonts/copse, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/copse (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The built Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. One glyph was renamed to its production name; cmap coverage is unchanged, so this difference is benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/copse (`.sfd`), latest at commit `cb3ef9c1cce0dcea7f5743e84e9ed7da7e259fd4`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
