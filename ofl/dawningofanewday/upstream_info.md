# Dawning of a New Day

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary) and carried undocumented source edits. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, each documented edit (version bump, metric or naming correction) as its own commit with its justification, then the conversion to `.glyphs`. METADATA.pb references the conversion commit `7becafaca78e`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Dawning of a New Day (Regular) built from FontForge SFD sources at https://github.com/librefonts/dawningofanewday. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`DawningofaNewDay-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- During conversion, embedded NUL bytes were stripped from the source and the no-break space (U+00A0) advance width was corrected.
- A new Unified Font Repository was created at https://github.com/googlefonts/dawningofanewday, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/dawningofanewday (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

The rebuilt font matched the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. Two benign differences were accepted: the FontForge legacy `nonmarkingreturn` glyph was dropped (it carried no cmap coverage), and 5 glyphs were renamed to their production names with no change to coverage.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/dawningofanewday (`.sfd`), latest at commit `45ea90b8015692ee7fe07e417ea1c88392373ce3`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
