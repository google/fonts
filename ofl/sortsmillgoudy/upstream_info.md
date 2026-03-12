# Sorts Mill Goudy — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Sorts Mill Goudy was identified as
`theleagueof/sorts-mill-goudy` on GitHub, hosted by The League of Moveable
Type. The repository contained UFO source files on the `master` branch.

## Repository

- **URL**: https://github.com/theleagueof/sorts-mill-goudy
- **Branch**: `master`
- **Commit**: `06072890c7b05f274215a24f17449655ccb2c8af`
- **Commit message**: "Initial commit with readme and licenses"

## Source Format

The repository's `source/` directory contained `OFLGoudyStM.ufo` and
`OFLGoudyStM-Italic.ufo`, both valid UFO directories with `fontinfo.plist`,
`glyphs/`, `groups.plist`, `kerning.plist`, and other standard UFO files.
The repository had only a single commit. An SFD-based source also existed
in a separate repository (`chemoelectric/sortsmill`) but this was a Mercurial
mirror of Google Code and contained only SFD files.

## Decision

The `source` block was added to `METADATA.pb` pointing to
`theleagueof/sorts-mill-goudy` at commit
`06072890c7b05f274215a24f17449655ccb2c8af` on the `master` branch.

## Notes

The designer listed in METADATA.pb is Barry Schwartz. Sorts Mill Goudy is a
digital revival of Frederic Goudy's Goudy Oldstyle and Italic typefaces,
originally created by Barry Schwartz. It was published by The League of
Moveable Type, an open-source type foundry. The font includes features such
as small capitals (roman only), oldstyle and lining figures, superscripts,
subscripts, fractions, ligatures, class-based kerning, and case-sensitive
forms. The typeface is licensed under the SIL Open Font License.
