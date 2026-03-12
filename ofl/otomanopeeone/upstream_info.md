# Otomanopee One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/Gutenberg-Labo/Otomanopee, maintained by the Gutenberg-Labo GitHub organization. The METADATA.pb source block was already present with a pinned commit. A newer commit was found on the `master` branch after the pinned commit; however, that newer commit (`726daba0dc4e5c7f600fa47f936ff9c1a2423c89`, dated 2023-12-13) only updates a Markdown documentation file and does not affect the font binaries.

## Repository

- **URL**: https://github.com/Gutenberg-Labo/Otomanopee
- **Default branch**: `master`
- **Description**: オとマのペ / Otomanopee (original designed Japanese font) for Google Fonts

## Commit

- **Pinned commit**: `21c3571eebc24b2723f94ef25dbf478c3a996047`
- **Commit message**: Merge pull request #7 from aaronbell/master — Flattening components
- **Commit date**: 2020-12-09
- **Latest HEAD commit**: `726daba0dc4e5c7f600fa47f936ff9c1a2423c89` — Update Otomanopee-Features.md (2023-12-13)
- **Status**: The pinned commit is not the HEAD of `master`. The newer HEAD commit only updates documentation, not font files.

## Font Details

Otomanopee is a Japanese display typeface designed by a creator working under the Gutenberg-Labo organization. The design was inspired by the graphical lettering style used for onomatopoeia in manga. The author had been drawing in this style since her teenage years and later formalized it into a font distributed under an open source license starting in 2007. The name derives from a childhood misspelling of "onomatopoeia" as "otomanopoeia."

The Google Fonts version ships a single static TTF: `OtomanopeeOne-Regular.ttf`, sourced from `fonts/ttf/` in the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/Gutenberg-Labo/Otomanopee
- `commit`: `21c3571eebc24b2723f94ef25dbf478c3a996047`
- `branch`: master
- File mappings for OtomanopeeOne-Regular.ttf, OFL.txt, and DESCRIPTION.en_us.html are present.

No changes to METADATA.pb were required.
