# Chicle

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from FontForge `.sfd` sources with no gftools-builder configuration. METADATA.pb pointed at the librefonts mirror with an onboarding commit but no config_yaml, so the family could not be rebuilt with the current pipeline.

## Actions taken

The FontForge source `src/Chicle-Regular-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Chicle-Regular.glyphs`. During conversion 4 stray NUL bytes were stripped and a U+00A0 no-break space glyph was added, which FontForge used to synthesise at export time. A build configuration was added so the family builds with gftools-builder3 and fontc.

## Final state

The repository was adopted into the Unified Font Repository template and now builds Chicle-Regular from the `.glyphs` source. The superseded `.sfd` sources and legacy build cruft were retired.

## Verification

The Rust-built `Chicle-Regular.ttf` was compared against the shipped binary. Codepoint coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths all agreed; the verdict is FUNCTIONAL. The only difference is benign: 7 glyphs were renamed to their production names, which leaves the codepoint coverage unchanged.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/chicle (branch `master`), latest commit `4ee3e89dbbdcfc0d56f7e1e3cc3d2de009219502`. This was also the onboarding commit recorded in the previous METADATA.pb source block.
