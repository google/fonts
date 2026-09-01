# New Tegomin — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/nagamaki008/NewTegomin
- **Branch**: master
- **Pinned commit**: `955803d27527edbfb9a416f765b6144215c250df`
- **Designer**: Kousuke Nagai
- **License**: OFL

The repository URL resolves correctly (HTTP 200). The copyright notice uses the same HTTPS URL as `repository_url`, which is consistent. No local cache exists at `/mnt/shared/upstream_repos/fontc_crater_cache/nagamaki008/`.

## Source Files

The METADATA.pb maps:
- `fonts/ttf/NewTegomin-Regular.ttf` → `NewTegomin-Regular.ttf`
- `OFL.txt` → `OFL.txt`
- `DESCRIPTION.en_us.html` → `DESCRIPTION.en_us.html`

This is a single-weight static Japanese (Mincho/Serif style) font. No variable font is present. The family covers Japanese (Jpan primary script), Latin, Latin-ext, and menu subsets.

## Build System

A `config.yaml` is present in the `ofl/newtegomin/` directory in google/fonts. It specifies a non-variable (static-only) build from a Glyphs source file:

```yaml
buildVariable: false
sources:
  - sources/NewTegomin.glyphs
```

The build uses fontmake with a `.glyphs` source file (Glyphs.app format). Variable font production is explicitly disabled (`buildVariable: false`), consistent with the single-weight nature of the family.

Sources info was introduced via PR #2878 (`994ab2abf`).

## config.yaml Status

**Present** in `ofl/newtegomin/config.yaml`. The build configuration is complete, referencing the upstream `.glyphs` source. The `buildVariable: false` flag is appropriate for a single-weight font.

## Notes

- New Tegomin is a Japanese Mincho-style font designed on a square grid, blending clean Mincho structure with handwritten organic characteristics (per DESCRIPTION.en_us.html).
- `primary_script: "Jpan"` is set correctly in METADATA.pb, reflecting the Japanese character coverage.
- The font is single-weight (Regular 400) with no italic or variable counterpart.
- The `.glyphs` source format requires Glyphs.app or the `glyphsLib` Python package to build; fontmake handles this via `glyphsLib`.
- No upstream repo cache is available locally; investigation is based on METADATA.pb, directory contents, and config.yaml.
- DESCRIPTION.en_us.html is present and links correctly to the upstream GitHub repository.
