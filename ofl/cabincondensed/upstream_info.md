# Investigation: Cabin Condensed

**Model**: Claude Opus 5.5
**Date**: 2026-10-15

## Initial state

METADATA.pb records https://github.com/impallari/Cabin at `9476ee6f5459ee37cf8462452f3e4640c3a48519` (2017-02-23, the merge of impallari/Cabin#12), while Cabin's METADATA.pb records the same repository at `70efa8c3179359cc50b01ca184fec8a694156140` (2020-07-22, v3.001). fontc_crater triage flagged the Cabin Condensed pin as stale.

## Actions taken

The four shipped binaries (CabinCondensed-Regular, -Medium, -SemiBold and -Bold, v2.200, added to google/fonts by PR #680 on 2017-05-01, unchanged since) were looked up in the repository by blob hash. They are byte-identical to the files committed in `f0f6a1a` ("sources | fonts: v2.200 update.", 2017-02-17), which `9476ee6` merged. Cabin v3 (2020) ships as Cabin's two variable fonts, with a width axis; google/fonts never rebuilt Cabin Condensed from it.

## Final state

No change to the source block: `9476ee6` is the commit whose fonts google/fonts ships. Recording v3 would name a source that did not build them; moving Cabin Condensed to v3 would be an update of the family, with new binaries.

fontc_crater fails to build this entry in both compilers: fontc stops on the 2017 `sources/Cabin.glyphs` with "Missing mapping on Weight for default at DesignSpace(95.0)" (its axis mappings place 400 at 94, not at the default master's 95). That is a property of the source, not of the pin.
