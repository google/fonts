# Cherry Swash

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied vertical metrics, GDEF classes and other values out of the shipped binary). The sources were regenerated purely from the original FontForge `.sfd`, byte-identical to the repository's own history, with babelfont `c368660` (gftools-builder3 `17b215c5` + fontc `3518040e`, 0.6.0); diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style. METADATA.pb now references the rebuild commit `d676530fe731`.

## Initial state

Google Fonts shipped Cherry Swash (Regular and Bold) built from FontForge SFD sources at https://github.com/librefonts/cherryswash. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD sources (`CherrySwash-Regular-TTF.sfd` and `CherrySwash-Bold-TTF.sfd`) were converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- U+00A0 (no-break space) was added to both sources, since FontForge used to synthesise it at export time, and the Bold source had its OS/2 usWeightClass set to 700.
- A new Unified Font Repository was created at https://github.com/googlefonts/cherryswash, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binaries.

## Final state

The source now lives at https://github.com/googlefonts/cherryswash (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binaries.

## Verification

Both weights matched the shipped binaries on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that 8 glyphs were renamed to their production names; character coverage is unchanged, so the difference is cosmetic.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/cherryswash (`.sfd`), latest at commit `84e28ad7cc2937ce20bac9dd6f2689cb42c6814a`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
