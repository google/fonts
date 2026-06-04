**Model**: Claude Opus 4.6

## Vidaloka

**Designer**: Cyreal
**License**: OFL
**Category**: SERIF

### Upstream Repository

The canonical upstream repository for Vidaloka was identified at **https://github.com/cyrealtype/Vidaloka**, maintained by Cyreal (cyrealtype). The repository contained both a Glyphs source file (`Vidaloka.glyphs`) and a UFO source directory (`Vidaloka.ufo`) in the `source/` directory, confirming it as the primary source of truth for the font.

### Source Files

The repository contained:
- `source/Vidaloka.glyphs` — Glyphs source file (primary source)
- `source/Vidaloka.ufo/` — UFO source directory
- `source/config.yaml` — build configuration
- `fonts/` — compiled TTF output files
- `Vidaloka-Regular.ttf` — compiled TTF at root

### Investigation Notes

The copyright string `"Copyright (c) 2011, Cyreal (www.cyreal.org a@cyreal.org) with Reserved Font Name 'Vidaloka'."` identified Cyreal as the designer. The website at `www.cyreal.org` linked to the [cyrealtype](https://github.com/cyrealtype) GitHub organization, where the dedicated Vidaloka repository was found. An older archive (`cyrealtype/Cyrealfonts`) also contained Vidaloka but only with VFB legacy sources; the newer dedicated repository with Glyphs/UFO sources was used instead. The repository was last updated in December 2023.

**Repo**: https://github.com/cyrealtype/Vidaloka
**Commit**: cc4205a19aca98f15ba551e3f8050630e54df28a
**Status**: Glyphs + UFO sources present
**Confidence**: High


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "source/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `cc4205a1` (via the bare mirror in `upstream_repos/repo_archive/cyrealtype/Vidaloka.git`) confirms that `source/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.
