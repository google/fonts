# Gochi Hand

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Gochi Hand (Regular) built from FontForge SFD sources at https://github.com/librefonts/gochihand. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`GochiHand-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected during conversion.
- A new Unified Font Repository was created at https://github.com/googlefonts/gochihand, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/gochihand (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets. The accepted differences are cosmetic and correct: 10 glyphs were renamed to production names (coverage unchanged); the GDEF table now classifies the combining mark U+0326 that the shipped font had missed; and that same mark's advance width was zeroed (the shipped font gave the combining mark a spacing advance).

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/gochihand (`.sfd`), latest at commit `e202a9f4b7cd6f9c84440e684f0a3d0b5dd234e0`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
