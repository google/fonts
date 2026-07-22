# Nabla — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/justvanrossum/nabla
- **Branch**: `main`
- **License**: OFL
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/` (no `justvanrossum` owner directory found)

## Source Files

The METADATA.pb `source` block references a GitHub release archive:

- **Archive URL**: https://github.com/justvanrossum/nabla/releases/download/v1.002/nabla-fonts.zip
- **Archive version**: v1.002
- **Files mapped**:
  - `nabla-fonts/Nabla[EDPT,EHLT].ttf` → `Nabla[EDPT,EHLT].ttf`

The font is a variable font with two custom axes:
- `EDPT` (Edge Depth): 0–200
- `EHLT` (Edge Highlight): 0–24

Subsets covered: `cyrillic-ext`, `latin`, `latin-ext`, `math`, `vietnamese`.

## Build System

A `config.yaml` is present in the google/fonts directory:

```yaml
sources:
  - sources/Nabla.glyphs
```

This indicates the upstream source is a Glyphs file (`sources/Nabla.glyphs`), built with the standard gftools/fontmake pipeline. The font is authored by Arthur Reinders Folmer and Just van Rossum (the repo owner).

## config.yaml Status

- **Present in google/fonts**: Yes (`config.yaml` exists in `/mnt/shared/google/fonts/ofl/nabla/config.yaml`)
- **METADATA.pb `config_yaml` field**: Not set — the source block does not reference a `config_yaml` field. This is consistent with pulling pre-built binaries from the release archive rather than building from source.

## Notes

- The release archive approach (v1.002) is used rather than building from source, which is why `config_yaml` is absent from the source block despite a `config.yaml` being present in the directory.
- Minisite URL is set: https://nabla.typearture.com/
- The font covers a broad range of scripts including Cyrillic extensions, Latin extensions, math symbols, and Vietnamese — unusual for a display font, suggesting strong Unicode coverage.
- No upstream repo cache is available locally; would need to clone from `https://github.com/justvanrossum/nabla` to inspect build tooling further.
- The `config.yaml` listing `sources/Nabla.glyphs` suggests the upstream repo has a Glyphs source file that could be used for building, but Google Fonts is currently consuming pre-built binaries from the release ZIP.

## Commit Added (HIGH confidence)

Commit `2a06e9f735390a7988d0ef190981ce4abf4dfd28` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2022-09-21). This is the most reliable method.
