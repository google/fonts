# Delius Swash Caps

Source modernized 2026-07: the FontForge `.sfd` sources were converted to Glyphs (`.glyphs`) and now build with the Google Fonts Rust pipeline (gftools-builder3 + fontc). The repository, commit and config are recorded in the `source { }` block of METADATA.pb and are not duplicated here.

## Initial state

The family shipped a single static TTF (Delius Swash Caps Regular) whose only upstream source was a FontForge `.sfd` file (`src/DeliusSwashCaps-Regular-TTF.sfd`). METADATA.pb pointed at the dormant librefonts repository and carried no `config_yaml`, so the family could not be rebuilt with the current Google Fonts tooling.

## Actions taken

The repository was re-based on the Unified Font Repository template. The FontForge source was converted to Glyphs (`DeliusSwashCaps-Regular.glyphs`) with babelfont-rs (upstream commit `219c0bb`), a `config.yaml` was added for gftools-builder3, and the superseded `.sfd` sources and legacy build cruft were retired. During conversion the no-break space (U+00A0) advance width was corrected to match the space glyph (238 units).

## Final state

The repository builds Delius Swash Caps Regular from the `.glyphs` source through gftools-builder3 + fontc. The `source { }` block in METADATA.pb now points at the modernized googlefonts repository, branch and build config.

## Verification

The freshly built Regular was compared against the shipped `DeliusSwashCaps-Regular.ttf`. Character-map coverage matched. The verdict is FUNCTIONAL, with only benign differences: the FontForge legacy helper glyphs (`.null`, `nonmarkingreturn`) were dropped; 11 glyphs were renamed to production names with no change in coverage; GDEF now correctly classifies one combining mark (U+0326) that the shipped font left unclassified; and the private-use combining glyph U+F6C3 was zeroed to a true mark advance (the shipped font gave it a spacing advance). No blocking differences were found.

## Original repository (dormant)

The original upstream lived at https://github.com/librefonts/deliusswashcaps (branch `master`), latest commit `a18d931eb4b66533df5df07d91e0851938a96121`, which is the same commit recorded for the original onboarding.
