# Gudea

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `84926eb57483`; diffenator3 1.1.4 reports the rendering pixel-perfect within rasterizer rounding: the flagged glyphs are point-for-point identical to the shipped outlines (FreeType-verified), with residual antialiasing coverage-rounding noise of at most 1/255 gray levels, stated in the conversion commit message.

## Initial state

Google Fonts shipped Gudea (Regular, Italic, Bold) built from FontForge SFD sources at https://github.com/librefonts/gudea. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The three canonical FontForge SFD sources were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The non-breaking space (U+00A0) advance width was corrected in each source, and the Bold source had its OS/2 usWeightClass set to 700.
- A new Unified Font Repository was created at https://github.com/googlefonts/gudea, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/gudea (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Each of the three styles matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 10 to 11 glyphs per style were renamed to their production names, which leaves the encoded coverage unchanged and is therefore accepted.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/gudea (`.sfd`), latest at commit `0eb36c75099c39430192adf41887965fdc51e819`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
