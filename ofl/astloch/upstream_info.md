# Astloch

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Astloch (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/astloch. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources (`src/Astloch-Regular-TTF.sfd` and `src/Astloch-Bold-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The no-break space (U+00A0) advance width was corrected to 500, and the Bold usWeightClass was set to 700.
- A new Unified Font Repository was created at https://github.com/googlefonts/astloch, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/astloch (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at strict functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only differences were benign: the converted source drops two FontForge legacy glyphs (`.null` and `nonmarkingreturn`) that carry no Unicode coverage, and 5 glyphs were renamed to production names with cmap coverage unchanged.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/astloch (`.sfd`), latest at commit `d15f7a51db3956d34a87ac47c532eae74237f07f`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
