# Dawning of a New Day

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Dawning of a New Day (Regular) built from FontForge SFD sources at https://github.com/librefonts/dawningofanewday. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`DawningofaNewDay-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion, embedded NUL bytes were stripped from the source and the no-break space (U+00A0) advance width was corrected.
- A new Unified Font Repository was created at https://github.com/googlefonts/dawningofanewday, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/dawningofanewday (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Two benign differences were accepted: the FontForge legacy `nonmarkingreturn` glyph was dropped (it carried no cmap coverage), and 5 glyphs were renamed to their production names with no change to coverage.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/dawningofanewday (`.sfd`), latest at commit `45ea90b8015692ee7fe07e417ea1c88392373ce3`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
