# Trochut — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Andreu Balius

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `trochut/src/`.

### Source Files

- **VFB (FontLab)**: Trochut-Bold-OTF.vfb, Trochut-Italic-OTF.vfb, Trochut-Regular-OTF.vfb
- **SFD (FontForge)**: Trochut-Bold-TTF.sfd, Trochut-Italic-TTF.sfd, Trochut-Regular-TTF.sfd
- **OTF (compiled)**: Trochut-Bold.otf, Trochut-Italic.otf, Trochut-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

Trochut was designed by Andreu Balius as an homage to Joan Trochut Blanchart (1920–1980), and is distributed commercially through TypeRepublic (typerepublic.com). A subset was released on Google Fonts under the OFL.

The following searches were conducted:

1. **GitHub user search**: No GitHub account was found for Andreu Balius (`andreubalius`).
2. **GitHub repository search**: Searches for "trochut font", "TypeRepublic font", and related terms returned no canonical upstream repositories. A repository `RichardBu/Trochut` was found but contained only a portfolio website (HTML/CSS), not font sources.
3. **librefonts mirror**: `librefonts/trochut` was found but is a downstream binary mirror (skipped per policy).
4. **Designer website**: andreubalius.com was checked but contained only portfolio information with no links to font source repositories.

Trochut is primarily a commercial typeface distributed through TypeRepublic. The Google Fonts subset was released under OFL, but the font sources have not been made publicly available in an editable format.
