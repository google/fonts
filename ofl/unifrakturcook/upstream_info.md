# UnifrakturCook — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: j. 'mach' wust

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `unifrakturcook/src/`.

### Source Files

- **SFD (FontForge)**: UnifrakturCook-Bold-TTF.sfd

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

## Investigation Details

UnifrakturCook was created by j. 'mach' wust as a modification of Peter Wiegel's font "Koch fette deutsche Schrift" (itself based on a 1910 typeface by Rudolf Koch). The font was originally published at http://unifraktur.sourceforge.net/cook.html.

The FONTLOG.txt confirmed that the source format is FontForge SFD:

> "The FontForge source file of Unifraktur Cook. FontForge is a free font editor. FontForge has been used to add OpenType features and to generate UnifrakturCook.ttf"

The following searches were conducted:

1. **SourceForge**: The project is hosted at https://unifraktur.sourceforge.net/ and distributes SFD (FontForge) source files. No GitHub repository is mentioned on the project page.
2. **GitHub search**: Searches for "unifrakturcook" and "unifraktur cook" on GitHub returned only `librefonts/unifrakturcook` (a downstream binary mirror, skipped per policy) and `google-fonts-bower/unifrakturcook-bower` (a CSS wrapper, not font sources).
3. **j. 'mach' wust GitHub**: No GitHub account was identified for the designer.
4. **Peter Wiegel**: Peter Wiegel (the original Koch Fraktur designer) maintains fonts at peter-wiegel.de but no GitHub presence was found.

UnifrakturCook is hosted on SourceForge and its sources exist in FontForge SFD format. SFD sources are not eligible per the source block policy (which requires UFO or Glyphs format). The font predates the adoption of modern open font source workflows.
