# Belgrano

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The upstream repository shipped only a FontForge source (`src/Belgrano-Regular-TTF.sfd`) with no gftools-builder configuration, so the family could not be built with the current Google Fonts Rust pipeline. METADATA.pb recorded the librefonts repository and onboarding commit but no `config_yaml`.

## Actions taken

The repository adopted the Unified Font Repository template. The FontForge source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Belgrano-Regular.glyphs`; a gftools-builder configuration was added, and the superseded `.sfd` source and legacy build cruft were retired.

## Final state

The repository builds `Belgrano-Regular.ttf` from `sources/Belgrano-Regular.glyphs` via gftools-builder3 and fontc. METADATA.pb now points at the modernized repository and records the build configuration.

## Verification

The fontc-built `Belgrano-Regular.ttf` was compared against the binary currently shipped in google/fonts. The only difference was that 4 glyphs were renamed to their production names; codepoint coverage is unchanged, so the difference is cosmetic and the verdict is FUNCTIONAL parity.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/belgrano
Latest commit: 9637660aa35d5ad59241a400f78d31413475bb77 (branch `master`), which is also the onboarding commit recorded in METADATA.pb.
