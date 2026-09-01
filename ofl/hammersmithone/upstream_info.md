# Hammersmith One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from FontForge `.sfd` sources with no gftools-builder configuration. The METADATA.pb source block pointed at the librefonts repository and a commit hash, but carried no config_yaml and no modern build recipe.

## Actions taken

The repository adopted the Unified Font Repository template. The `src/HammersmithOne-Regular-TTF.sfd` source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/HammersmithOne-Regular.glyphs`, and a gftools-builder3 build configuration was added so the family builds with gftools-builder3 and fontc. During conversion four stray NUL bytes were stripped from the source and the no-break space (U+00A0) advance width was corrected to 440. The superseded FontForge sources and legacy build cruft were then retired.

## Final state

The repository builds `HammersmithOne-Regular.ttf` from `.glyphs` through the Rust pipeline. The source block in METADATA.pb references the modernized repository, its config.yaml and the shipped TTF.

## Verification

The TTF built from the converted `.glyphs` source was compared against the binary currently shipped in google/fonts. The result is FUNCTIONAL parity: outlines and character coverage matched. The only difference is that 22 glyphs were renamed to their standard production names, which leaves coverage unchanged and does not affect rendering.

## Original repository (dormant)

The original upstream repository was https://github.com/librefonts/hammersmithone, whose latest commit on the `master` branch is a5fae41a3eabe8ec4e1d8ff7b3fa6dfde5c4fa87 (the same commit recorded at onboarding). No upstream commits were made after onboarding.
