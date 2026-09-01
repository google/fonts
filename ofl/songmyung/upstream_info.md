# Song Myung — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for
the Song Myung font.

## Research

Song Myung was created by JIKJI (JIKJISOFT), a Korean type foundry established
in 2004. The font is a contemporary take on a traditional Hangul serif design.
Searches on GitHub for JIKJI-related repositories returned a result at
`webfontworld/jikji` but this repository did not exist (returned 404). Other
searches for JIKJI's GitHub presence and for the Song Myung source files
returned only font distribution sites, not a source repository.

## Decision

No `source` block was added to `METADATA.pb`. No publicly accessible source
repository in UFO, Glyphs, or other editable format was found.

## Notes

The designer listed in METADATA.pb is JIKJI. Song Myung is a Korean and Latin
typeface that supports the Korean (Hangul) script. The Latin portion is a
version of Source Serif Pro adjusted to fit the Korean design. The font is
licensed under the SIL Open Font License.
