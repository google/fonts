# Germania One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The `source { }` block pointed at the dormant librefonts repository and recorded only a repository URL and onboarding commit. The upstream sources were FontForge `.sfd` files (`src/GermaniaOne-Regular-TTF.sfd`), which the current Rust build pipeline cannot consume, and no build configuration was present.

## Actions taken

The single SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`) and a build configuration was added. During conversion the non-breaking space (U+00A0) advance width was corrected to 250 to match the space glyph. The repository was restructured to the Unified Font Repository template and the superseded FontForge sources were retired.

## Final state

The family builds from `.glyphs` sources with gftools-builder3 and fontc. METADATA.pb now points at the modernized repository, the pinned commit, and the build configuration.

## Verification

The freshly built `GermaniaOne-Regular.ttf` was compared against the shipped Google Fonts binary. The verdict is FUNCTIONAL: the codepoint coverage matched, with the only difference being that 12 glyphs were renamed to their production names (glyph coverage unchanged). No blocking differences were found.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/germaniaone
Latest commit: 73d401d495adf37b1af75a5dca9cb5cdb046b05d (branch `master`), which is also the onboarding commit recorded in the previous METADATA.pb `source { }` block.
