# Raleway Dots - Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/ralewaydots](https://github.com/librefonts/ralewaydots) |
| **Commit** | `c845d1a8e75014ad17dbbf2633119226bed462d8` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

## Investigation Summary

METADATA.pb for Raleway Dots had no source block. A source block was added pointing to the librefonts mirror repository.

## Source Analysis

The repository at https://github.com/librefonts/ralewaydots is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

## Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

## Notes

librefonts mirror with TTX sources. Note: impallari/Raleway exists but covers main Raleway, not Dots variant.

## Binary History in google/fonts

```
2019-07-10 10:45:16 +0100 023aa4b2855c95413d1b1c510ad812beb345df75 Remove trailing whitespace from font family names
```

## Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/ralewaydots/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `c845d1a8e7`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
