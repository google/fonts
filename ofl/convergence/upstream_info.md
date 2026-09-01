# Convergence

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Convergence (Regular) built from FontForge SFD sources at https://github.com/librefonts/convergence. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Convergence-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- A new Unified Font Repository was created at https://github.com/googlefonts/convergence, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/convergence (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Convergence-Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets. The accepted differences are all benign: 9 glyphs were renamed to their production names (coverage unchanged), the FontForge legacy glyph `nonmarkingreturn` was dropped, GDEF now classifies three real combining marks that the shipped font had missed (uni0307, uni0307.cap, uni0326), and one combining mark (U+0307) was zeroed to remove the spurious spacing advance FontForge had given it.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/convergence (`.sfd`), latest at commit `475145997c07041d94fabe462233b89f15450a41`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
