# Investigation Report: Caladea

## Source Data

| Field | Value |
|---|---|
| Family Name | Caladea |
| Designer | Andres Torresi, Carolina Giovagnoli |
| License | OFL |
| Repository URL | https://github.com/googlefonts/caladea |
| Commit Hash | `336a529cfad3d103d6527752686f8331d13e820a` |
| Branch | (not set) |
| Config YAML | (none) |
| **Status** | complete |

## How URL Found

The repository URL was originally `https://github.com/huertatipografica/Caladea` (matching the copyright notice in the font binaries). It was changed to `https://github.com/googlefonts/caladea` in commit `cfd52504e` ("Caladea repo fix"). The `huertatipografica/Caladea` repo was likely transferred or forked to `googlefonts/caladea`. The upstream repo is cached and verified.

## How Commit Determined

The commit `336a529cfad3d103d6527752686f8331d13e820a` is the HEAD commit of the upstream repository (dated 2020-02-11). This is a "Merge pull request #2 from vv-monsalve/master" which fixed copyright strings. The font was onboarded on the same date (2020-02-11). The binary TTF files in the upstream repo's `fonts/ttf/` directory are byte-identical to those in `google/fonts`, confirming this is the correct commit.

The font was initially added via commit `ae5de9569` ("[Font Bakery Dashboard] create family: Caladea (#2339)") and the TTF files have never been updated since.

## Config YAML Status

**No config.yaml exists** in the upstream repository. No override config.yaml exists in the google/fonts family directory either.

The upstream repo contains source files:
- `sources/glyphs/Caladea_Italics.glyphs`
- `sources/glyphs/Caladea_Roman.glyphs`
- `sources/ufo/` (4 UFO directories for each style)

The font was onboarded using pre-built TTF files from the upstream repo's `fonts/ttf/` directory, not compiled from source via gftools-builder. A config.yaml would need to be created to enable rebuilding from source.

## Verification

- **Commit exists in upstream repo**: Yes, verified (HEAD of master)
- **Binary files match**: Yes, byte-identical md5sums between google/fonts and upstream `fonts/ttf/`
- **Config YAML exists at commit**: No - no config.yaml in upstream
- **Override config.yaml in google/fonts**: No
- **Repository URL verified**: Confirmed accessible at `https://github.com/googlefonts/caladea`

## Confidence Level

**High** for URL and commit hash. The commit is verified by binary comparison. The status is correctly identified as `missing_config` since there is no config.yaml in the upstream repo nor an override in google/fonts.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/glyphs/Caladea_Roman.glyphs
  - sources/glyphs/Caladea_Italics.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Should an override `config.yaml` be created in google/fonts to enable building from the Glyphs sources? The repo has `Caladea_Italics.glyphs` and `Caladea_Roman.glyphs` which could potentially be used with gftools-builder, but it is a static family (4 separate masters: Regular, Bold, Italic, BoldItalic) not a variable font.
