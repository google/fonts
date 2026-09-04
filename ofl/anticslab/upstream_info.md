# Antic Slab

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources reconstructed 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary), and this family's committed `.sfd` did not exactly reproduce the shipped outlines. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, every deviation from the shipped binaries applied as its own documented commit, then the conversion to `.glyphs`. METADATA.pb references the binary-correspondence conversion commit `53727d3f8f4e`; diffenator3 1.1.4 reports the rendering pixel-perfect within rasterizer rounding: the flagged glyphs are point-for-point identical to the shipped outlines (FreeType-verified), with residual antialiasing coverage-rounding noise of at most 0/255 gray levels, stated in the conversion commit message.

## Initial state

Google Fonts shipped Antic Slab (Regular) built from FontForge SFD sources at https://github.com/librefonts/anticslab. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`AnticSlab-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/anticslab, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/anticslab (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 4 glyphs were renamed to their production names; coverage is unchanged, so this is accepted as benign.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/anticslab (`.sfd`), latest at commit `64168753771367673ec5efa56c747427648d9f29`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
