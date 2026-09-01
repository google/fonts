# National Park — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/benhoepner/National-Park
- **Owner**: benhoepner (Ben Hoepner)
- **Default branch**: master
- **License**: OFL-1.1
- **Last pushed**: 2025-03-07
- **Pinned commit**: `ef0531a85a833b90713743639e3c5ffb8e345833` (2025-03-07) — "Merge pull request #27 from emmamarichal/master — build fonts"

The repo is not cached locally at `/mnt/shared/upstream_repos/fontc_crater_cache/`.

## Source Files

The primary source is a single Glyphs file located at the root of the `sources/` directory:

- `sources/NationalPark.glyphs` — main Glyphs 3 source file (variable font with `wght` axis, range 200–800)
- `sources/config.yaml` — gftools builder config (see below)
- `sources/Legacy-Sources/` — older working Glyphs files (`NationalPark_4msters.glyphs`, `NationalPark_d.glyphs`, `NationalPark_diacrtitics.glyphs`, `NationalPark_kerntest.glyphs`, `NationalParkx.glyphs`); these are archival only

Output fonts:
- `fonts/variable/NationalPark[wght].ttf` — variable font (what Google Fonts uses)
- `fonts/ttf/` — static instances

## Build System

The repo uses the **gftools builder** (`gftools builder sources/config.yaml`) driven by a standard Google Fonts project Makefile:

```
make build   # runs gftools builder for all config*.yaml in sources/
make test    # runs fontbakery check-googlefonts on fonts/ttf/
```

Requirements are pinned in `requirements.txt` (full lock file included). Key tools:
- `gftools` 0.9.33
- `fontmake` 3.7.1
- `fonttools` 4.42.0

CI is handled via GitHub Actions (`.github/` directory present).

## config.yaml Status

`sources/config.yaml` exists in the upstream repo and is correctly referenced in `METADATA.pb` as `source.config_yaml: "sources/config.yaml"`. Content:

```yaml
sources:
    - NationalPark.glyphs
familyName: "National Park"
buildOTF: False
```

The config is minimal and functional. The `buildOTF: False` flag suppresses OTF generation (only TTF/VF outputs are produced). The `config_yaml` field in `METADATA.pb` is correctly populated.

## Notes

- The family is a variable font with a single `wght` axis (200–800); the static TTFs are instances derived from it.
- The METADATA.pb `source.files` block correctly maps `fonts/variable/NationalPark[wght].ttf` → `NationalPark[wght].ttf`.
- Subsets: latin, latin-ext, vietnamese — appropriate for a broad Latin typeface.
- The repository is well-structured and follows the standard Google Fonts project template.
- Designers listed: Andrea Herstowski, Ben Hoepner, Jeremy Shellhorn. Emma Marichal contributed build fixes via PR #27 (not listed as designer, which is correct).
- No issues found with the source metadata; the `config_yaml` reference is valid and the commit is the HEAD of master as of the date_added value.
