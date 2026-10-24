# Quando

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `097ef0d66cfa`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Quando (Regular) built from FontForge SFD sources at https://github.com/librefonts/quando. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- In the converted source the non-breaking space (U+00A0) advance was set to 680 to match the space glyph, correcting a width FontForge had left inconsistent.
- A new Unified Font Repository was created at https://github.com/googlefonts/quando, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/quando (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Identical to the shipped Quando-Regular binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 23 glyphs were renamed to their production names; glyph coverage is unchanged, so this is a naming-only change with no visible effect.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/quando (`.sfd`), latest at commit `328635dcbaae8f2fc4fd84c9b872e596a82bebe5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
