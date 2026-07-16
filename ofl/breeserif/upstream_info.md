# Bree Serif

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from a FontForge `.sfd` source (`src/BreeSerif-Regular-TTF.sfd`) with no gftools-builder configuration. The METADATA.pb source block pointed at the librefonts repository but carried no `config_yaml`, so the family could not be rebuilt with the current pipeline.

## Actions taken

The `.sfd` source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `BreeSerif-Regular.glyphs`. During conversion the non-breaking space (U+00A0) glyph width was corrected to match the regular space. The repository was restructured on the Unified Font Repository template, a gftools-builder configuration was added, and the superseded FontForge sources and legacy build cruft were retired.

## Final state

The family now builds from `.glyphs` with gftools-builder3 and fontc. A single static instance, Bree Serif Regular, is produced.

## Verification

The fontc-built TTF was compared against the shipped `BreeSerif-Regular.ttf`. The result is a FUNCTIONAL match: glyph coverage, metrics and layout are equivalent. The only difference is benign: 21 glyphs were renamed to their production names, leaving codepoint coverage unchanged. No blocking differences were found.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/breeserif (branch `master`), latest commit `86684a17aaa88ce2d9d85d77f9e9ce1f64c06462`. This was also the onboarding commit for the family. The modernized sources now live in the googlefonts fork.
