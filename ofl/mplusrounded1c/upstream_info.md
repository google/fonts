# M PLUS Rounded 1c — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/coz-m/MPLUS_FONTS |
| Commit | `eb604901d6f04b6f7f2a84b0378c58df84a9dba6` |
| Confidence | Low |

## Source Types

The repository contains Glyphs and Designspace sources:
- `.glyphs` files — Glyphs source format
- `.designspace` files — designspace/UFO format

## Build Compatibility

No `config.yaml` is present in the upstream repository. The sources use modern formats, but it is unclear whether the Rounded variant is included in this repository.

## Investigation Notes

The coz-m/MPLUS_FONTS repository is the new M PLUS project by Coji Morishita. M PLUS Rounded 1c is an older variant of the M PLUS family with rounded terminals. The confidence is low because the new MPLUS_FONTS repository focuses on the redesigned M PLUS 1 and M PLUS 2 families, and it is unclear whether it covers the legacy Rounded 1c variant. Further investigation is needed to determine if the Rounded variant sources exist at this commit.

The binary in google/fonts was recently re-added (2025-04-10, "Missing in GH" fix).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Low

The repository may not cover the Rounded variant; needs further investigation to confirm.
