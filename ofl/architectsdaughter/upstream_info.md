# Architects Daughter

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The upstream repository at librefonts/architectsdaughter shipped only FontForge sources. METADATA.pb recorded the repository and onboarding commit but no config.yaml, so the family could not be rebuilt with the current Rust toolchain.

## Actions taken

The FontForge source `src/ArchitectsDaughter-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/ArchitectsDaughter-Regular.glyphs`. During conversion 109 stray NUL bytes were stripped from the source. A gftools-builder3 `config.yaml` was added, and the repository was restructured onto the Unified Font Repository template. The superseded FontForge sources and legacy build cruft were retired.

## Final state

The repository builds `ArchitectsDaughter-Regular.ttf` from `.glyphs` sources through gftools-builder3 and fontc. The `source { }` block in METADATA.pb points at the modernized googlefonts/architectsdaughter repository, together with its build commit and gftools-builder3 config.

## Verification

The freshly built `ArchitectsDaughter-Regular.ttf` was compared against the binary currently shipped in google/fonts. Glyph coverage, metrics and layout matched. The verdict was FUNCTIONAL: 18 glyphs were renamed to production names with no change in coverage, and the rebuilt GDEF correctly classifies one combining mark (uni0326) that the shipped font had failed to mark. Both differences are improvements or naming-only and are accepted.

## Original repository (dormant)

The original upstream lived at https://github.com/librefonts/architectsdaughter (branch `master`), latest commit `1a94ca0aea18288ee7685ed6aee918b58399a307`, which was also the onboarding commit. It carried only the FontForge `.sfd` sources and is now superseded by the modernized repository.
