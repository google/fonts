# Armata

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary) and carried undocumented source edits. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, each documented edit (version bump, metric or naming correction) as its own commit with its justification, then the conversion to `.glyphs`. METADATA.pb references the conversion commit `8594fe9afcf0`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

The upstream repository at librefonts/armata shipped only FontForge sources (`src/Armata-Regular-TTF.sfd`) and had no config.yaml or Glyphs sources, so it could not build with the current Google Fonts pipeline. METADATA.pb recorded the repository and onboarding commit but no build configuration.

## Actions taken

The repository adopted the Unified Font Repository template. The FontForge source `src/Armata-Regular-TTF.sfd` was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), producing `sources/Armata-Regular.glyphs`, and a gftools-builder3 config was added. During conversion, the no-break space (U+00A0) was corrected to the expected advance width (683 units), and 22 glyphs were renamed to their production names. The superseded FontForge sources and legacy build cruft were then retired.

## Final state

The repository builds `Armata-Regular.ttf` from `sources/Armata-Regular.glyphs` using gftools-builder3 and fontc. The `source { }` block in METADATA.pb points at the modernized repository, branch and config.

## Verification

The freshly built `Armata-Regular.ttf` was compared against the shipped Google Fonts binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The verdict was FUNCTIONAL: the only difference was 22 glyphs renamed to their production names, with codepoint coverage unchanged. No blocking differences were found.

## Original repository (dormant)

The original upstream repository is https://github.com/librefonts/armata (default branch `master`), whose latest commit is `fbbc7c2575fe310df0450aaa721ee4e860b03a0e`. This is the same commit recorded as the Google Fonts onboarding commit; no upstream commits were made after onboarding.
