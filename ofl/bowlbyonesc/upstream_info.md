# Bowlby One SC

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Bowlby One SC (Regular) built from FontForge SFD sources at https://github.com/librefonts/bowlbyonesc. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 616 in the converted source.
- A new Unified Font Repository was created at https://github.com/googlefonts/bowlbyonesc, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/bowlbyonesc (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and the GSUB/GPOS feature sets. Accepted differences: the FontForge-only `nonmarkingreturn` glyph was dropped; 7 glyphs were renamed to production names (coverage unchanged); and three combining marks (U+030F, U+0311, U+0326) are now classified as marks in GDEF and given zero advance widths, correcting the shipped font, which had missed those GDEF classes and given the same marks spacing advances.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/bowlbyonesc (`.sfd`), latest at commit `9566646d9feaafcdc1c23174931ac4599803442b`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
