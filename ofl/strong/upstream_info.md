# Strong -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `strong/src/`

## Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Strong-Regular-TTF.vfb` (VFB, proprietary)
- `Strong_Regular-OTF.vfb` (VFB, proprietary)
- `Strong_Regular.vfb` (VFB, proprietary)
- `Strong_Regular.otf` (compiled binary)

## Designer

Gaslight (copyright held by Cyreal, www.cyreal.org)

## Search Results

- **librefonts/strong**: Mirror repository only. The `src/` directory contained `Strong-Regular-TTF.vfb`, `Strong_Regular-OTF.vfb`, and `Strong_Regular.vfb` — VFB only, no UFO or Glyphs sources.
- **cyrealtype GitHub**: The cyrealtype organization hosted many Cyreal fonts but did not include Strong.
- No direct GitHub repository for Strong from Cyreal was found.
- The font was created in 2011 under the Cyreal brand, predating common use of UFO/Glyphs workflows.
