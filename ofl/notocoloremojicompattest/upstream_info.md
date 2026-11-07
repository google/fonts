# Noto Color Emoji Compat Test — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | None (no upstream) |
| Commit | N/A |
| Version | 0.000 |
| Date Added | 2022-01-20 |
| Last Modified | 2022-02-22 (commit `186b5bc0`) |

## Investigation Summary

Noto Color Emoji Compat Test is a **test font** created and modified entirely within the google/fonts repository. No upstream repository exists. No source block was added to METADATA.pb because there is no external source to reference.

## Build Pipeline

This font was built using [nanoemoji](https://github.com/googlefonts/nanoemoji), a tool for compiling color fonts from SVG/bitmap sources into COLRv1 format. The build process:

1. **Source format**: SVG emoji artwork, compiled into a COLRv1 (Color OpenType) font
2. **Build tool**: `nanoemoji` — a Google-developed tool for building color vector fonts, distinct from the standard gftools-builder/fontmake pipeline
3. **Iterative development**: The font was created as an "Exploratory nanoemoji font" (commit `9ac25b635`) and iteratively modified in-place within google/fonts through several commits
4. **Purpose**: This is a compatibility test font for the COLRv1 emoji format, not a production font for end users. It tests whether platforms can render the newer color font format correctly
5. **No config.yaml**: The font was hand-built with nanoemoji, not through gftools-builder, so no config.yaml is applicable
6. **No upstream**: Unlike other Noto emoji fonts (which live in `googlefonts/noto-emoji`), this test font has no corresponding entry in any upstream repository. The files `Noto-COLRv1-emojicompat.ttf` and `NotoColorEmoji-emojicompat.ttf` in the noto-emoji repo are different fonts from `NotoColorEmojiCompatTest-Regular.ttf`

## Git History in google/fonts

The font was modified through several commits, the last being `186b5bc050d1` (2022-02-22, "Restore the red pen, it's helpful to have a marker").

**Confidence**: HIGH (no upstream exists — verified by full git history analysis and cross-reference against googlefonts/noto-emoji)
