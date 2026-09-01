# Fjord One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from the dormant librefonts repository, whose only sources were FontForge `.sfd` files under `src/`. METADATA.pb recorded that repository and commit but carried no `config_yaml`, and the sources could not be built by the current Rust pipeline.

## Actions taken

The repository was forked to the Google Fonts org and rebuilt on the Unified Font Repository template. The single FontForge source `src/FjordOne-Regular-TTD.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), and a build configuration was added. During conversion the non-breaking space (U+00A0) advance width was corrected to 537 to match the space glyph. The superseded `.sfd` sources and legacy build cruft were then retired.

## Final state

The repository builds `FjordOne-Regular.ttf` from the `.glyphs` source with gftools-builder3 and fontc. METADATA.pb points at the modernized repository, the post-conversion commit and the build configuration.

## Verification

The freshly built TTF was compared against the shipped `FjordOne-Regular.ttf`: glyph coverage, outlines, metrics and layout matched. The verdict is FUNCTIONAL. Two benign differences were accepted: 9 glyphs were renamed to their production names (coverage unchanged), and GDEF now classifies one real combining mark (uni0326) that the shipped font had failed to mark.

## Original repository (dormant)

The original upstream lived at https://github.com/librefonts/fjordone, latest commit `90b0be2c47a5acd683621f38ce4f046f741abafb` on branch `master`. It contained only FontForge `.sfd` sources and had received no commits after the Google Fonts onboarding.
