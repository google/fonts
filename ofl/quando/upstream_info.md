# Quando - Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/quando](https://github.com/librefonts/quando) |
| **Commit** | `328635dcbaae8f2fc4fd84c9b872e596a82bebe5` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

## Investigation Summary

METADATA.pb for Quando had no source block. A source block was added pointing to the librefonts mirror repository.

## Source Analysis

The repository at https://github.com/librefonts/quando is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

## Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

## Notes

librefonts mirror with TTX sources.

## Binary History in google/fonts

```
2015-03-07 05:14:52 +0530 90abd17b4f97671435798b6147b698aa9087612f Initial commit
```

## Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
