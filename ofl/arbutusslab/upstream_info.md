# Arbutus Slab

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary) and carried undocumented source edits. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, each documented edit (version bump, metric or naming correction) as its own commit with its justification, then the conversion to `.glyphs`. METADATA.pb references the conversion commit `17c26d3b3abd`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

The upstream repository shipped only FontForge `.sfd` sources (`src/ArbutusSlab-Regular.ttf.sfd`) with no gftools-builder configuration. METADATA.pb recorded the repository and onboarding commit but no `config_yaml`, so the family could not be rebuilt with the current Rust pipeline.

## Actions taken

The repository adopted the Unified Font Repository template. The `.sfd` source for the Regular weight was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`), and a gftools-builder configuration was added. During conversion the no-break space (U+00A0) advance width was corrected to match the space glyph (838). The superseded FontForge sources and legacy build cruft were retired.

## Final state

The family now builds from `sources/ArbutusSlab-Regular.glyphs` using gftools-builder3 and fontc, producing `fonts/ttf/ArbutusSlab-Regular.ttf`.

## Verification

The freshly built Regular was compared against the binary currently shipped in google/fonts. Glyph coverage, metrics and outlines matched. The only difference is that 24 glyphs were renamed to their production names; codepoint coverage is unchanged, so the verdict is functional parity.

## Original repository (dormant)

Original upstream: https://github.com/librefonts/arbutusslab (branch `master`), latest commit `2988f79c4d6965ef9fa35768ca00f02cddd5a50a`, which is also the onboarding commit recorded in METADATA.pb.
