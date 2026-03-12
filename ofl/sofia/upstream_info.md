# Sofia — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for
the Sofia font.

## Research

Sofia was designed by Paula Nazal and Daniel Hernández for LatinoType Limitada
(info@latinotype.com). The font was released in 2011. Searches on GitHub and
the web did not reveal any repository maintained by LatinoType or the
individual designers that contained open source files in UFO, Glyphs, or
other editable formats.

A separate unrelated typeface called "Sofia Sans" exists on GitHub at
`lettersoup/Sofia-Sans`, but this is a different typeface and not related to
the LatinoType Sofia font on Google Fonts.

## Decision

No `source` block was added to `METADATA.pb`. The font's source files did not
appear to be publicly available in a format suitable for the source metadata.

## Notes

The designer listed in METADATA.pb is LatinoType. The font is described as
an upright script font with unconventional ligatures. LatinoType is a Chilean
type foundry founded by Paula Nazal Selaive and Daniel Hernández Zamora.
