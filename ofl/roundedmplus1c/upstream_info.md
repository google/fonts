# Rounded M+ 1c — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

No canonical upstream repository was found on GitHub, and this directory has no METADATA.pb file.

The font originates from two related projects:
- The [M+ Outline Fonts Project](http://mplus-fonts.sourceforge.jp/mplus-outline-fonts/) (hosted on SourceForge)
- The [Rounded M+ Project](http://jikasei.me/font/rounded-mplus/) (hosted at jikasei.me)

## What Was Done

The DESCRIPTION.en_us.html was examined to identify the upstream project. The Rounded M+ Project was hosted at `jikasei.me`, not on GitHub. Searches were conducted for "rounded-mplus font", "Rounded M+ 1c font", and "M PLUS Rounded 1c font" on GitHub. Only packaging repositories (e.g., an Arch Linux PKGBUILD) were found, not the original source repository. The `jikasei` GitHub account was checked but did not exist.

## Notes

This directory has no METADATA.pb file, so no source block could be added. The DESCRIPTION states this is "Version v1.059g, released upstream on 2015-05-29, and slightly modified by Google Fonts." The source appears to have been distributed via the SourceForge project for M+ fonts and the jikasei.me website, neither of which is a GitHub repository. Investigation concluded without adding a source block.
