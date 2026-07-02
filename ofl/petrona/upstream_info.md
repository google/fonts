# Petrona — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Petrona was identified at https://github.com/RingoSeeber/Petrona, maintained by Ringo R. Seeber under his personal GitHub account. The METADATA.pb file referenced commit `03d4b6dd8af6ecf3a51d3b126bd64e491cb01d18`. No config_yaml or explicit file mappings were specified in the source block.

## Font Description

Petrona is a serif variable font with a weight range from Thin (100) to Black (900), available in both upright and italic styles. It was designed by Ringo R. Seeber and added to Google Fonts on 2020-07-15. The font covers Latin and Latin Extended scripts, as well as Vietnamese. The copyright dates to 2019.

## Designer

Ringo R. Seeber is the sole designer and maintainer of the Petrona typeface. The repository is hosted under his personal GitHub account.

## Repository

- **URL**: https://github.com/RingoSeeber/Petrona
- **Commit**: `03d4b6dd8af6ecf3a51d3b126bd64e491cb01d18`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | SERIF |
| Style | Regular + Italic |
| Weight Axis | 100–900 |
| Subsets | latin, latin-ext, vietnamese |
| Variable | Yes (wght) |

## Notes

The source block contained no `config_yaml`, no explicit `files` mappings, and no branch specification. This is a minimal source entry; the build pipeline relies on default conventions.

## Confidence

**High** — The repository is referenced directly in both the METADATA.pb `repository_url` and the copyright notice. The commit is explicitly specified.
