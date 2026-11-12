# Inder

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `0021128e5c59`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Inder (Regular) built from FontForge SFD sources at https://github.com/librefonts/inder. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/inder, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/inder (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Inder Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets and advance widths. The remaining differences are benign: 22 glyphs were renamed to production names with coverage unchanged, and GDEF now classifies two real combining marks the shipped font missed (uni0326, uni0326.cap).

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/inder (`.sfd`), latest at commit `5620f4744158d400ba1286612d14d49c43597033`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
