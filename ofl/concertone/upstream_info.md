# Concert One

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

Sources rebuilt 2026-09: the 2026-07 conversion was back-fitted (post-conversion scripts copied values out of the shipped binary) and carried undocumented source edits. The upstream repository now carries an explicit commit series: the `.sfd` restored byte-identical from the repository's own history, each documented edit (version bump, metric or naming correction) as its own commit with its justification, then the conversion to `.glyphs`. METADATA.pb references the conversion commit `d68fc365f489`; diffenator3 1.1.4 reports zero glyph, word and pixel differences against the shipped binaries on every style.

## Initial state

Google Fonts shipped Concert One (Regular) built from FontForge SFD sources at https://github.com/librefonts/concertone. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source (`ConcertOne-Regular-TTF.sfd`) was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- Seven glyphs were renamed to their production names during conversion; character coverage was unchanged.
- A new Unified Font Repository was created at https://github.com/googlefonts/concertone, building the font with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/concertone (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary.

## Verification

Identical to the shipped ConcertOne-Regular.ttf on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths. The only difference is that seven glyphs were renamed to production names, which leaves character coverage unchanged; the result is accepted as functionally equivalent.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/concertone (`.sfd`), latest at commit `c2160f498dbb0ebf8394fbd117c21d2160cdef01`. Preserved for provenance; the new `.glyphs` source supersedes it for building.
