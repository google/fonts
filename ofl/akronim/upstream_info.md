# Akronim - Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/akronim](https://github.com/librefonts/akronim) |
| **Commit** | `9288ae0636d38a5b42002d6df8b5906c49fe9b1a` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

## Investigation Summary

METADATA.pb for Akronim had no source block. A source block was added pointing to the librefonts mirror repository.

## Source Analysis

The repository at https://github.com/librefonts/akronim is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

## Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

## Notes

librefonts mirror with TTX sources. src/ has only METADATA_comments.txt and VERSIONS.txt.

## Binary History in google/fonts

```
2017-05-01 13:20:28 -0400 347b8a4d15b618e787fc726898c66bb1dd6c0b02 hotfix-akronim: v1.002 added (#746)
```

## Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
