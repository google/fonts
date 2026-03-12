# Sonsie One — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for
Sonsie One. The original sources were in FontLab VBF format, which is not
an open editable format suitable for the source metadata.

## Research

Sonsie One was designed by Riccardo De Franceschi and mastered by Eben Sorkin
at Sorkin Type Co. The FONTLOG.txt documented that the font was originally
completed in FontLab VBF format by De Franceschi, and then mastered to TTF
format by Eben Sorkin. No GitHub repository was found under Sorkin Type
(`SorkinType` GitHub org does not include Sonsie One), nor under Riccardo
De Franceschi's name.

## Decision

No `source` block was added to `METADATA.pb`. The original sources were in
FontLab VBF (proprietary) format, which is excluded from consideration per
the investigation policy.

## Notes

The designer listed in METADATA.pb is Riccardo De Franceschi. The font is
described as a heavy, medium contrast, large x-height script font inspired
by hand-painted signs seen in Munich. The copyright is held by Sorkin Type Co.
