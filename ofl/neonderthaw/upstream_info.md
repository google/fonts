# Neonderthaw — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/neonderthaw
- **Owner**: googlefonts (Google Fonts org mirror)
- **Default branch**: master
- **License**: OFL-1.1
- **Last pushed**: 2021-11-18
- **Pinned commit**: `67e6f60e5addb09d39d7a36f908430cc508165fb` (2021-11-18) — "Merge branch 'qaNeonderthaw'"

The repo is not cached locally at `/mnt/shared/upstream_repos/fontc_crater_cache/`.

## Source Files

The primary source is a single Glyphs file in the `sources/` directory:

- `sources/NeonDerThaw.glyphs` — main Glyphs source (static, single weight)
- `sources/config.yml` — gftools builder config (note: `.yml` extension, not `.yaml`)

Output fonts:
- `fonts/ttf/Neonderthaw-Regular.ttf` — static TTF (what Google Fonts uses)
- `fonts/otf/` — OTF versions
- `fonts/webfonts/` — web font variants

## Build System

The repo uses the **gftools builder** (`gftools builder sources/config.yml`) with a standard structure. Requirements are loosely pinned:

```
fontmake>=2.4
fontbakery>=0.8
gftools[qa]>=0.7
drawbot-skia>=0.4.8
sh>=1.14.2
```

CI is handled via GitHub Actions (`.github/` directory present).

## config.yaml Status

`sources/config.yml` exists in the upstream repo and is referenced in `METADATA.pb` as `source.config_yaml: "sources/config.yml"`. Content:

```yaml
sources:
  - NeonDerThaw.glyphs
familyName: "Neonderthaw"
buildVariable: false
# autohintTTF: false
```

**Note**: The config file uses the `.yml` extension (not `.yaml`), and METADATA.pb correctly uses `"sources/config.yml"` to match. `buildVariable: false` is set, which is correct as this is a static font only. The `config_yaml` field in `METADATA.pb` is correctly populated.

## Notes

- This is a static (non-variable) handwriting/display font with a single Regular weight.
- The designer is Robert Leuschke; the repo is hosted under the `googlefonts` organization, indicating it was migrated for QA purposes.
- The pinned commit is the HEAD of master at the time of addition to Google Fonts (2021-11-18), which matches the `date_added` field.
- Subsets: latin, latin-ext, vietnamese — appropriate for the character coverage of this handwriting face.
- Classifications in METADATA.pb: `DISPLAY` and `HANDWRITING`, which correctly reflect the font's nature.
- The repository has been inactive since November 2021 — no further development is anticipated. The source metadata appears stable and complete.
- The METADATA.pb `source.files` block maps `fonts/ttf/Neonderthaw-Regular.ttf` → `Neonderthaw-Regular.ttf`, which is correct.
