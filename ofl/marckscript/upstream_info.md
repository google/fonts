# Marck Script

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Marck Script (Regular) built from FontForge SFD sources at https://github.com/librefonts/marckscript. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`MarckScript-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/marckscript, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/marckscript (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Two differences were reviewed and accepted: the non-printing FontForge helper glyphs `.null` and `nonmarkingreturn` are no longer emitted (they carry no encoded codepoints), and one glyph was renamed to its production name with no change to codepoint coverage.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/marckscript (`.sfd`), latest at commit `699f31478702f9901c943b7be7caa6e38b6535b7`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
