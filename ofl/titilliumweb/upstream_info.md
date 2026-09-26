# Titillium Web — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Accademia di Belle Arti di Urbino

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `titilliumweb/src/`.

### Source Files

- **SFD (FontForge)**: TitilliumWeb-Black-TTF.sfd, TitilliumWeb-Bold-TTF.sfd, TitilliumWeb-BoldItalic-TTF.sfd, TitilliumWeb-Italic-TTF.sfd, TitilliumWeb-Light-TTF.sfd, TitilliumWeb-LightItalic-TTF.sfd, TitilliumWeb-Regular-TTF.sfd, TitilliumWeb-SemiBold-TTF.sfd, TitilliumWeb-SemiBoldItalic-TTF.sfd, TitilliumWeb-Thin-TTF.sfd, TitilliumWeb-ThinItalic-TTF.sfd
- **OTF (compiled)**: TitilliumWeb-Black.otf, TitilliumWeb-Bold.otf, TitilliumWeb-BoldItalic.otf, TitilliumWeb-Italic.otf, TitilliumWeb-Light.otf, TitilliumWeb-LightItalic.otf, TitilliumWeb-Regular.otf, TitilliumWeb-SemiBold.otf, TitilliumWeb-SemiBoldItalic.otf, TitilliumWeb-Thin.otf, TitilliumWeb-ThinItalic.otf

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

## Investigation Details

Titillium Web was created as a collective academic project at the Accademia di Belle Arti di Urbino (Italy) within its Visual Design Master program (Campi Visivi course). The font was iteratively developed by successive student cohorts.

The following searches were conducted:

1. **GitHub organization search**: No GitHub organization or user account was found for the Accademia di Belle Arti di Urbino (`accademiadiurbino`).
2. **SFD sources**: A repository at `ecm4u/Titillium` was found containing SFD (FontForge) source files and compiled fonts, attributed to the Accademia. However, SFD sources are FontForge-specific format and do not meet the requirement for UFO or Glyphs sources.
3. **Derived works**: A repository `eliheuer/titillium-web-vf` was found containing Glyphs files for a variable font version, but this is a fork/derivative (based on Cairo by Mohamed Gaber), not the canonical upstream.
4. **Pro version**: `chialab/titillium_pro` was found with UFO sources, but this is a commercial extended variant ("Titillium Pro") — not the original Titillium Web distributed on Google Fonts.
5. **Mirror repositories**: `FontFaceKit/titilliumweb`, `librefonts/titilliumweb` were found but are downstream binary mirrors.

The original Titillium Web sources exist only in FontForge SFD format. The font predates the widespread adoption of UFO as a standard open font source format. No eligible upstream source repository was identified.
