# Spinnaker — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for
Spinnaker.

## Research

Spinnaker was designed by Elena Albertoni for Sorkin Type Co. (Eben Sorkin),
released in 2011. The font's `DESCRIPTION.en_us.html` referenced source files
as being available from Google Code (`code.google.com/p/googlefontdirectory/`),
which has since been archived and shut down.

No GitHub repository was found for Spinnaker under SorkinType, Elena Albertoni,
or related names. The SorkinType GitHub organization did not include a
Spinnaker repository among its public repos.

## Decision

No `source` block was added to `METADATA.pb`. The referenced source location
(Google Code) was no longer accessible, and no alternative repository with
open editable source files was found.

## Notes

The designer listed in METADATA.pb is Elena Albertoni. Spinnaker is described
as inspired by French and UK lettering found on travel posters for ships. It
is a low-contrast, slightly wide sans-serif design licensed under the SIL Open
Font License, with copyright held by Sorkin Type Co.
