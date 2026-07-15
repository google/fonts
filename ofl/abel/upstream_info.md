# Abel

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Abel (Regular) built from FontForge SFD sources at https://github.com/librefonts/abel. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to match the space glyph.
- A new Unified Font Repository was created at https://github.com/googlefonts/abel, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/abel (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Abel Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and GSUB/GPOS feature sets. The remaining differences are benign: 10 glyphs were renamed to production names with coverage unchanged; the legacy `kern` table (748 pairs) was modernized into a GPOS `kern` feature; GDEF now classifies two real combining marks the shipped font missed (uni0307, uni0326); and two combining marks (U+0307, U+F6C3) were zeroed after the shipped font left them with spacing advances.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/abel (`.sfd`), latest at commit `adf2c7e74ecde8ca41959c0d974f039789fe7b9d`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
