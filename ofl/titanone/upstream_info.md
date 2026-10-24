# Titan One — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Rodrigo Fuenzalida

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `titanone/src/`.

### Source Files

- **VFB (FontLab)**: TitanOne-Regular-OTF.vfb
- **SFD (FontForge)**: TitanOne-Regular-TTF.sfd
- **OTF (compiled)**: TitanOne-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

## Investigation Details

Rodrigo Fuenzalida's GitHub account (https://github.com/rfuenzalida) was found and examined. It contained repositories for other fonts he designed: AntonFont, Freeman, Instrument_Serif, MondaFont, and Outfit-Fonts — but no repository for Titan One.

Additional searches were conducted on GitHub using queries for "TitanOne font Rodrigo Fuenzalida" and related terms. No canonical upstream repository was found.

The designer's portfolio website (rfuenzalida.com) was found to be a parked domain at the time of investigation, returning no relevant content.

Titan One's sources do not appear to be publicly hosted on GitHub or any other discoverable platform. The font may have been produced with proprietary tooling and the sources retained privately.
