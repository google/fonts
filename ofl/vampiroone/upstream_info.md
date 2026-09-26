**Model**: Claude Opus 4.6

## Vampiro One

**Designer**: Riccardo De Franceschi
**License**: OFL
**Category**: DISPLAY

### Upstream Repository

The canonical upstream repository for Vampiro One was identified at **https://github.com/SorkinType/Vampiro**, maintained by Sorkin Type. The repository contained a UFO source directory (`Vampiro.ufo`) at the root level, confirming it as a valid open-source font source.

### Source Files

The repository contained:
- `Vampiro.ufo/` — UFO source directory (primary source)
- `Vampiro.vfb` — legacy FontLab source (not used)
- `src/` — additional legacy sources (VFB and SFD, not used)
- `Vampiro.ttf` — compiled TTF output

The UFO source was identified as the canonical source, as it is the modern, open-format version of the font. The VFB and SFD files in `src/` were legacy format files and were not considered as primary sources per policy.

### Investigation Notes

The copyright string `"Copyright (c) 2012, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Vampiro'."` confirmed the SorkinType organization as the upstream maintainer. The repository was found under the [SorkinType](https://github.com/SorkinType) GitHub organization.

**Repo**: https://github.com/SorkinType/Vampiro
**Commit**: ec42cf12230a8663c3ccb7a0c2da590ba98d2cd9
**Status**: UFO source present
**Confidence**: High

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `ec42cf1` (upstream legacy: .vfb in repo root and .sfd/.vfb archives in src/). Added an override `config.yaml` in `ofl/vampiroone/` that references the compatible sources only (`Vampiro.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
