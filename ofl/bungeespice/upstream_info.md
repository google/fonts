# Investigation Report: Bungee Spice

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bungee Spice |
| Designer | David Jonathan Ross |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Branch | master |
| Config YAML | N/A (override in google/fonts) |
| Date Added | 2022-04-05 |
| License | OFL |
| Status | complete |

## How URL Found

The repository URL `https://github.com/djrrb/Bungee` is recorded in METADATA.pb. It was added by Viviana Monsalve on 2024-05-30 (`a7a9198fd` "Bungee Spice github repo url added") during the v2.000 update cycle. All Bungee variants share this upstream repository.

## How Commit Determined

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` is explicitly stated in the google/fonts commit message:

```
17bae36eb Bungee Spice: Version 2.000 added
Taken from the upstream repo https://github.com/djrrb/Bungee at commit
https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99.
```

This commit was authored by Viviana Monsalve on 2024-05-30.

**Cross-verification**: The commit `eb03cf69` corresponds exactly to the upstream `v2.000` release tag. The METADATA.pb also references `archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip"`. This is the same commit hash used for Bungee Inline, Bungee Outline, and Bungee Shade.

### History

Bungee Spice has a more complex history than the other "basic" Bungee variants:

- **Initial add** (2021-12-07): Added by Rod Sheeter (`e15b29728`, PR #4154) as a COLRv1 color font
- **Color table processing** (2022): Multiple rounds of color table manipulation using `maximum_color` from nanoemoji, including:
  - `e6fe96669` - Exploratory generation of additional color tables
  - `9f92199e0` - Test builds passed through nanoemoji's maximum_color
  - `12ed8f97f` - Removed CBDT, ran maximum_color (PR #4993)
  - `87ecc71a0` - Re-run maximum_color to fix colored .notdef glyph issue (PR #5171)
- **v2.000** (2024-05-30): Updated by Viviana Monsalve (`17bae36eb`) from upstream commit `eb03cf69`

## Config YAML Status

**No config.yaml in upstream repo** at any commit. The Bungee project uses a custom build pipeline. For the color fonts (Bungee Spice), the build process is particularly complex: assembly scripts create a COLRv1 font, then `maximum_color` adds SVG tables.

**Override config.yaml** exists in google/fonts at `ofl/bungeespice/config.yaml`:
```yaml
sources:
  - sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo
familyName: Bungee Spice
buildStatic: true
buildOTF: false
```

This override points to `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` which exists at the recorded commit `eb03cf69`. Note that the `sources/2-build/` directory was removed from the upstream repo 3 commits later (in `7ffc5a64`), so this override config only works with the recorded commit hash.

**Important caveat**: The override config may not fully reproduce the original binary, because Bungee Spice is a COLRv1 color font that requires additional post-processing with `maximum_color` to add SVG tables. A standard gftools-builder invocation from the UFO source alone would not produce an equivalent font.

## Verification

- **Repository URL**: Valid, accessible GitHub repository
- **Commit hash exists**: Confirmed `eb03cf69` exists in the upstream repo
- **Tag alignment**: Commit `eb03cf69` is exactly the `v2.000` release tag
- **Source files at commit**: `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` exists at this commit (along with a pre-built `Bungee_Color-Regular.ttf`)
- **Override config**: References existing source path at the recorded commit
- **Binary source**: METADATA.pb uses `archive_url` pointing to v2.000 release zip; the binary was taken from `Bungee_Color/BungeeSpice-Regular.ttf` within the archive

## Confidence Level

**HIGH** - The commit hash is explicitly stated in the google/fonts commit message and aligns exactly with the upstream v2.000 release tag. The override config.yaml points to valid sources, though full reproduction of the color font binary may require additional tooling beyond gftools-builder.

## Open Questions

1. **Color font reproduction**: Can gftools-builder produce a fully equivalent Bungee Spice binary from the UFO source alone, or does it require the `maximum_color` post-processing step? The override config may produce a font without the SVG table that the current binary includes.
