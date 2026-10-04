# Nata Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/dnlzqn/nata-sans
- **Branch**: `main`
- **License**: OFL
- **Designer**: Daniel Uzquiano
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/` (no `dnlzqn` owner directory found)

## Source Files

The METADATA.pb `source` block references a GitHub release archive:

- **Archive URL**: https://github.com/dnlzqn/nata-sans/releases/download/v2.2/Nata.Sans.zip
- **Archive version**: v2.2
- **Files mapped from archive** (`Nata.Sans/` prefix):
  - `OFL.txt`
  - `build/variable/NataSans[wght].ttf` → `NataSans[wght].ttf`

The font is a variable font with a weight axis:
- `wght`: 100–900

Subsets covered: `cyrillic`, `cyrillic-ext`, `latin`, `latin-ext`, `vietnamese`.

The family directory also contains an `article/` subdirectory with `ARTICLE.en_us.html` and `Nata.svg`.

## Build System

The METADATA.pb source block explicitly references `config_yaml: "config.yaml"`, indicating a `config.yaml` is expected at the root of the upstream repository. The archive path `build/variable/NataSans[wght].ttf` suggests the upstream repo uses a standard `build/` output structure, consistent with a fontmake/gftools build pipeline.

The font's variable nature (wght axis 100–900) and the `build/variable/` path strongly suggest the upstream uses either a `.designspace` file or a Glyphs/UFO source with fontmake to produce the variable TTF.

## config.yaml Status

- **Present in google/fonts**: No — no `config.yaml` found in `/mnt/shared/google/fonts/ofl/natasans/` (directory contains only `METADATA.pb`, `NataSans[wght].ttf`, `OFL.txt`, and `article/`)
- **METADATA.pb `config_yaml` field**: **Set** — `config_yaml: "config.yaml"` is referenced in the source block, pointing to a `config.yaml` in the upstream repository root
- The absence of a local `config.yaml` in the google/fonts directory means the GF pipeline currently pulls from the release archive without building from source. The `config_yaml` field indicates intent to build from source once the config is confirmed.

## Notes

- Minisite URL is set: https://dnlzqn.xyz/nata/
- Stroke classification: `SANS_SERIF`.
- This is a relatively new addition to Google Fonts (date_added: 2025-06-26).
- The font covers Latin, Cyrillic, and Vietnamese — a broad coverage for a sans-serif variable font.
- The `config_yaml` field in METADATA.pb references a `config.yaml` in the upstream repo, but this file has not been pulled into the google/fonts directory. A follow-up action would be to fetch and include the upstream `config.yaml` in the google/fonts directory.
- To fully inspect build tooling, the upstream repo at https://github.com/dnlzqn/nata-sans would need to be cloned.

## Commit Added (HIGH confidence)

Commit `dd4741f58266ea26270ff1e487856b1ea73eb5b8` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2025-06-21). This is the most reliable method.
