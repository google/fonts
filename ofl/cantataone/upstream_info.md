# Cantata One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from the librefonts `cantataone` repository, whose only editable sources were FontForge `.sfd` files (`src/CantataOne-Regular-TTF.sfd`). METADATA.pb carried a bare `source { }` block with the repository URL and onboarding commit but no build configuration, and the sources could not be built by the current Rust toolchain.

## Actions taken

The single master `src/CantataOne-Regular-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/CantataOne-Regular.glyphs`. During conversion the non-breaking space (U+00A0) advance width was corrected to 682 units to match the space glyph. A `config.yaml` for gftools-builder3 was added, and the repository was restructured to the Unified Font Repository template. The superseded `.sfd` sources and legacy build cruft were retired.

## Final state

The repository builds `CantataOne-Regular.ttf` from `.glyphs` sources with gftools-builder3 and fontc. METADATA.pb now points at the modernized repository and records the build configuration.

## Verification

The freshly built `CantataOne-Regular.ttf` was compared against the binary currently shipped in google/fonts. The result is FUNCTIONAL parity: character-map coverage and per-weight metrics match. The only difference is that 23 glyphs were renamed to their production names, which leaves the encoded coverage unchanged. No blocking differences were found.

## Original repository (dormant)

The original upstream lives at https://github.com/librefonts/cantataone (branch `master`). Its latest commit is `947c3dd6e969867a02166335a27c48c0a7f9123d`, which is also the commit from which the shipped binary was onboarded. That repository is now dormant; ongoing maintenance moves to the modernized fork.
