# Candal

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Candal (Regular) built from FontForge SFD sources at https://github.com/librefonts/candal. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Candal-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 713 units to match the space glyph, replacing the value FontForge previously synthesised at export.
- A new Unified Font Repository was created at https://github.com/googlefonts/candal, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/candal (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Candal Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets. The accepted differences are all benign: 15 glyphs were renamed to production names with unchanged coverage; GDEF now classifies 5 real combining marks (uni0307, uni030F, uni0311, uni0326, uni0326.1) that the shipped font failed to mark; and 4 combining marks (U+0307, U+030F, U+0311, U+0326) were given zero advance widths, correcting the spacing advances the shipped font wrongly assigned them.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/candal (`.sfd`), latest at commit `64c937069fed67f562829846315a0e2e7789e6a6`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
