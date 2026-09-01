# Bilbo Swash Caps

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped from a FontForge `.sfd` source (`src/BilboSwashCaps-Regular-TTF.sfd`) with no config.yaml and no build pipeline compatible with the current Google Fonts tooling. METADATA.pb recorded only the repository URL and onboarding commit.

## Actions taken

The repository was migrated onto the Unified Font Repository template. The `.sfd` source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`); a stray NUL byte carried over from the FontForge export was stripped during conversion. A `config.yaml` was added under `sources/` so the family builds with gftools-builder3 and fontc, and the superseded FontForge sources and legacy build cruft were retired.

## Final state

The repository builds `BilboSwashCaps-Regular.ttf` from `sources/BilboSwashCaps-Regular.glyphs` through the Rust pipeline. METADATA.pb points at the modernized repository, branch and config.

## Verification

The freshly built TTF was compared against the binary currently shipped in Google Fonts. Glyph coverage and outlines matched. The verdict was FUNCTIONAL: the only differences were benign. The rebuild drops two FontForge legacy glyphs (`.null` and `nonmarkingreturn`) that carry no encoded codepoints, and 7 glyphs were renamed to standard production names with no change to coverage. There were no blocking differences.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/bilboswashcaps (branch `master`), latest commit `7fb5653f339a4a574c26a8df75b6e7fac7db9280`, which is the same commit used to onboard the family into Google Fonts.
