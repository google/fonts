# Palanquin — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Palanquin was identified as **https://github.com/VanillaandCream/Palanquin**, maintained by the designer Pria Ravichandran under the GitHub organization VanillaandCream. This was confirmed by the DESCRIPTION.en_us.html file in the google/fonts repository, which explicitly links to this repository. The upstream repo also contains the PalanquinDark sources, confirming it is shared with the Palanquin Dark family.

## Investigation

The METADATA.pb file listed the designer as Pria Ravichandran with copyright dated 2014. The DESCRIPTION.en_us.html confirmed the upstream URL as `https://github.com/VanillaandCream/Palanquin`. A web search confirmed this is a designer-owned repository (not a librefonts mirror), hosted under the VanillaandCream GitHub organization belonging to Pria Ravichandran.

The repository contained a `PalanquinDark/` subdirectory alongside the `Palanquin/` directory, confirming both font families originate from the same upstream repository.

The latest commit in the upstream repository was retrieved:

- **Commit**: `f912925eccf9b020425a6f0ddc2ce32fc1640695`
- **Message**: "Test docs added"
- **Date**: 2015-07-03

## Upstream Repository

- **URL**: https://github.com/VanillaandCream/Palanquin
- **Owner**: Pria Ravichandran (VanillaandCream)
- **Type**: Designer-owned canonical upstream
- **License**: OFL 1.1
- **Latest commit**: `f912925eccf9b020425a6f0ddc2ce32fc1640695`

## METADATA.pb Changes

A `source` block was added to METADATA.pb with the repository URL and latest commit hash.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `f912925` (upstream legacy: .vfb in Palanquin/SourceFiles/VFBs/). Added an override `config.yaml` in `ofl/palanquin/` that references the compatible sources only (`Palanquin/SourceFiles/UFOs/Palanquin_Th.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin_ExLt.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin Light.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin Regular.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin Medium.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin SemiBold.ufo`, `Palanquin/SourceFiles/UFOs/Palanquin Bold.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
