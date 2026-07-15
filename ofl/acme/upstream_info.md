# Acme

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The upstream repository shipped only a FontForge source (`src/Acme-Regular-TTF.sfd`) and legacy build cruft. There was no Glyphs source and no gftools-builder configuration, so the family could not be built with the current Google Fonts Rust pipeline.

## Actions taken

The repository adopted the Unified Font Repository template. The FontForge source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Acme-Regular.glyphs`, and a gftools-builder configuration was added. During conversion the non-breaking space (U+00A0) advance width was corrected. The superseded FontForge source and legacy build files were retired.

## Final state

The repository builds `Acme-Regular.ttf` from `sources/Acme-Regular.glyphs` using gftools-builder3 and fontc.

## Verification

The freshly built `Acme-Regular.ttf` was compared against the binary currently shipped in Google Fonts. The comparison reached FUNCTIONAL parity: character coverage and rendering match. The only difference is that 8 glyphs were renamed to their production names, which leaves coverage unchanged and is therefore acceptable.

## Original repository (dormant)

The original upstream source lived at https://github.com/librefonts/acme (default branch `master`). Its latest commit was `fa0a4445feb570b5cfc7ce4b8f6dbacc6ae5ad73`, which is also the commit that was onboarded into Google Fonts.
