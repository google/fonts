# Cagliostro

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Cagliostro (Regular) built from FontForge SFD sources at https://github.com/librefonts/cagliostro. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`src/Cagliostro-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The converted source was cleaned up: stray NUL bytes were stripped and the no-break space (U+00A0) advance was corrected to 250.
- A new Unified Font Repository was created at https://github.com/googlefonts/cagliostro, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/cagliostro (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt Cagliostro Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle and the GSUB/GPOS feature sets. The remaining differences are cosmetic and expected from the conversion: two synthetic FontForge legacy glyphs (`.null`, `nonmarkingreturn`) were dropped, 9 glyphs were renamed to production names with no change in coverage, GDEF now correctly classifies two combining marks the shipped font missed (uni0307, uni0326), and two combining marks (U+0307, U+F6C3) had their spacing advances zeroed to match their combining-mark role.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/cagliostro (`.sfd`), latest at commit `5c0de59bedd45c878edfeeeb31e2105f987e7270`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
