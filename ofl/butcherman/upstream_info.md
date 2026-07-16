# Butcherman

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

Google Fonts shipped Butcherman (Regular) built from FontForge SFD sources at https://github.com/librefonts/butcherman. The shipped binary is pre-OpenType: it has no GSUB, no GPOS and no legacy kern table. There was no Glyphs (`.glyphs`) source, and no source that builds with fontc.

## Actions taken

- The canonical FontForge SFD source was converted to Glyphs with babelfont-rs (upstream commit `219c0bb`).
- The upstream SFD defines a Standard Ligatures (`liga`) lookup (`n n -> n_n`, `o o -> o_o`) that FontForge's TTF export had dropped, so the shipped binary never applied it. To keep this modernization a strict equivalence, that feature was removed from the converted source so the rebuild matches the shipped binary. Restoring it is proposed separately (see below).
- A new Unified Font Repository was created at https://github.com/googlefonts/butcherman, building the fonts with gftools-builder3 + fontc.
- The build was verified against the shipped binary.

## Final state

The source now lives at https://github.com/googlefonts/butcherman (see METADATA.pb) and builds reproducibly with gftools-builder3 + fontc at functional equivalence with the shipped binary. The rebuilt font has no GSUB, matching the shipped binary.

## Verification

The rebuilt Butcherman-Regular was compared against the shipped binary on cmap coverage, vertical metrics, usWeightClass, fsSelection/macStyle, GSUB/GPOS feature sets, GDEF classes and advance widths, and had no blocking differences. Accepted differences: two FontForge legacy glyphs (`.null`, `nonmarkingreturn`) were dropped; 17 glyphs were renamed to their production names, with codepoint coverage unchanged; GDEF now classifies five real combining marks that the shipped font missed; and those five marks were given zero advance where the shipped font had assigned them spacing advances.

## Original repository (dormant)

The original FontForge sources are at https://github.com/librefonts/butcherman (`.sfd`), latest at commit `92a34525b5032c76484c49e652f649e52d1465e5`. Preserved for provenance; the new `.glyphs` source supersedes it for building.

## Pending improvement (separate review)

The `liga` lookup the shipped font lacks was recovered during conversion and is preserved on a separate branch. Restoring it changes rendering (the `nn` and `oo` doubles), so it is proposed as a follow-up that a Google Fonts onboarder must review and QA before it ships. It is not part of this equivalence modernization.
