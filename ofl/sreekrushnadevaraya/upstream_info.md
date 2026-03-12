# Sree Krushnadevaraya — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Sree Krushnadevaraya was identified as
`appajid/sreekrushnadevaraya` on GitHub. The link to this repository was found
in the font's `DESCRIPTION.en_us.html` file. The repository contained a UFO
source file on the `master` branch.

## Repository

- **URL**: https://github.com/appajid/sreekrushnadevaraya
- **Branch**: `master`
- **Commit**: `1d8aea8611ff50608f113c079890bd4c996d12be`
- **Commit message**: "updated copyright & version, no latin characters"

## Source Format

The repository contained `SreeKrushnadevaraya.ufo` (a valid UFO directory with
`fontinfo.plist`, `glyphs/`, `kerning.plist`, `lib.plist`, and `metainfo.plist`)
alongside `SreeKrushnadevaraya.sfd` and `OFL.txt`. The UFO was the primary
source format used.

## Decision

The `source` block was added to `METADATA.pb` pointing to
`appajid/sreekrushnadevaraya` at commit
`1d8aea8611ff50608f113c079890bd4c996d12be` on the `master` branch.

## Notes

The designer listed in METADATA.pb is Purushoth Kumar Guttula. Sree
Krushnadevaraya is a Telugu display font developed by Silicon Andhra, named
after the Telugu king Krishnadevaraya. The project was led by Appaji Ambarisha
Darbha. The Latin portion of the font was derived from Cantata One, designed
by Joana Correia da Silva for Sorkin Type Co. The repository was maintained by
`appajid` (Appaji Ambarisha Darbha) on GitHub.
