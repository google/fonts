# Bowlby One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Bowlby One (Regular) built from FontForge SFD sources at https://github.com/librefonts/bowlbyone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion, stray NUL bytes were stripped from the source and the no-break space advance width was corrected.
- A new Unified Font Repository was created at https://github.com/googlefonts/bowlbyone, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/bowlbyone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binary.

## Verification

The rebuilt Regular matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, and GSUB/GPOS feature sets. The differences are cosmetic and accepted: two FontForge legacy glyphs (`.null`, `nonmarkingreturn`) were dropped, six glyphs were renamed to production names with coverage unchanged, and three real combining marks (U+030F, U+0311, U+0326) were zeroed and correctly classified in GDEF, where the shipped font had left them with spurious spacing advances and no mark class.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/bowlbyone (`.sfd`), latest at commit `3aca9b57cf9c7b9688b635d5dcfb6d53948e26a2`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
