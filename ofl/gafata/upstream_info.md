# Gafata

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from FontForge `.sfd` sources with no gftools-builder configuration. METADATA.pb pointed at the librefonts repository but recorded no config_yaml, so the family could not be rebuilt by the current pipeline.

## Actions taken

The `src/Gafata-Regular-TTF.sfd` source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Gafata-Regular.glyphs`. During conversion the `aalt` feature was repaired and the no-break space (U+00A0) advance width was corrected to 228. The repository adopted the Unified Font Repository template and a gftools-builder configuration was added; the superseded FontForge sources and legacy build cruft were retired.

## Final state

The repository builds Gafata-Regular.ttf from the `.glyphs` source via gftools-builder3 and fontc.

## Verification

The freshly built Gafata-Regular.ttf was compared against the shipped binary. The verdict was FUNCTIONAL: glyph coverage, metrics and layout matched, with the only difference being 5 glyphs renamed to their production names (coverage unchanged), which is an expected consequence of the Glyphs conversion.

## Original repository (dormant)

Original repository: https://github.com/librefonts/gafata
Latest commit: dcd42b72333486b9704c2d3736e3c26b0346cb67 (branch master)
