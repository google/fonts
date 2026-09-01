# Uncial Antiqua — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Astigmatic (Brian J. Bonislawsky)

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `uncialantiqua/src/`.

### Source Files

- **VFB (FontLab)**: UncialAntiqua-Regular-OTF.vfb, UncialAntiqua-Regular-TTF.vfb, UncialAntiqua-Regular.vfb
- **OTF (compiled)**: UncialAntiqua-Regular.otf

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

## Investigation Details

Uncial Antiqua was designed by Brian J. Bonislawsky under the studio name Astigmatic (AOETI). It combines Uncial and Half Uncial letterforms.

The following searches were conducted:

1. **GitHub user/org search**: The GitHub account `astigmatic` was found but contained only two repositories unrelated to fonts (`pro` — an Android app project, and `project1`). No font repositories were present.
2. **Repository name search**: Searches for "uncial antiqua", "uncialantiqua", and "astigmatic font" returned no canonical font source repositories on GitHub.
3. **Astigmatic website**: astigmatic.com was not investigated further as Astigmatic is a commercial foundry that releases fonts for free distribution but typically does not publish editable source files.

Uncial Antiqua was contributed to Google Fonts by Astigmatic, a commercial type foundry. While the font is released under OFL, the source files have not been made publicly available. This is consistent with Astigmatic's other Google Fonts contributions.
