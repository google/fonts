# Devonshire

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Devonshire (Regular) built from FontForge SFD sources at https://github.com/librefonts/devonshire. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`Devonshire-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion the `aalt` feature was repaired and the no-break space (U+00A0) advance width was corrected to 202.
- A new Unified Font Repository was created at https://github.com/googlefonts/devonshire, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/devonshire (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Devonshire-Regular was compared against the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. It was functionally equivalent, with no blocking differences, and with the following accepted differences:

- Two FontForge legacy glyphs (`.null`, `nonmarkingreturn`) were dropped; they carry no cmap coverage.
- 20 glyphs were renamed to their production names; codepoint coverage is unchanged.
- GDEF now classifies three real combining marks (U+0312, U+0315, U+0326) as marks, which the shipped font missed, and those marks were given zero advance; the shipped font had incorrectly assigned them spacing advances.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/devonshire (`.sfd`), latest at commit `7d88bb81c76ccd1b7d48a15ae97a00c45f9ffb01`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
