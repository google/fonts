# Bubbler One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Bubbler One (Regular) built from FontForge SFD sources at https://github.com/librefonts/bubblerone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`BubblerOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted source was corrected: a NO-BREAK SPACE (U+00A0) glyph was added, since FontForge used to synthesise it at export time, and "Use Typo Metrics" (fsSelection bit 7) was set.
- A new Unified Font Repository was created at https://github.com/googlefonts/bubblerone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/bubblerone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The accepted differences are benign: two unencoded FontForge legacy glyphs (`.null`, `nonmarkingreturn`) were dropped, four glyphs were renamed to production names with coverage unchanged, and the `.notdef` advance width differs (203 vs 510).

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/bubblerone (`.sfd`), latest at commit `be2343608e5751bca73956b02860a1758e1e29a7`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
