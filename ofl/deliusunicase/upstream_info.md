# Delius Unicase

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Delius Unicase (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/deliusunicase. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources (`DeliusUnicase-Regular-TTF.sfd` and `DeliusUnicase-Bold-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected, and the Bold master had its OS/2 usWeightClass set to 700.
- A new Unified Font Repository was created at https://github.com/googlefonts/deliusunicase, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/deliusunicase (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, and GSUB/GPOS feature sets. The accepted differences are benign: the FontForge legacy glyph `nonmarkingreturn` was dropped; 11 glyphs were renamed to production names with coverage unchanged; GDEF now classifies the real combining mark uni0326 that the shipped font had missed; and the combining mark U+F6C3, which the shipped font gave a spacing advance, was zeroed.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/deliusunicase (`.sfd`), latest at commit `cf094caecc96589701f341db1994fd10642e3c88`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
