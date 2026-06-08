# Mukta Malar — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [EkType/Mukta](https://github.com/EkType/Mukta) |
| Commit | `7db4b0fc09894ad6814346172f6f0c1cf822a722` |
| Date | 2017-05-23 |
| Confidence | High |

## Investigation

The METADATA.pb for Mukta Malar had no source block. The upstream repository is EkType/Mukta, a monorepo containing four Mukta script variants. Mukta Malar (Tamil) sources are under the `MuktaMalar-Tamil/` directory.

### Source Types Available

- **VFB** (FontLab): `MuktaMalar-Tamil/{weight}/VFB/MuktaMalar-{weight}.vfb` (7 weights)
- **TTX**: `TTX/MuktaMalar-Tamil/MuktaMalar-{weight}.ttx` (all 7 weights)
- **Feature files**: Per-weight `GPOS`, `features` files plus shared `GDEF`, `GSUB`, `GlyphOrderAndAliasDB`

### Buildability

VFB-only editable sources. The TTX files are XML representations of compiled fonts, not design sources. Not directly buildable with gftools-builder.

### Actions Taken

A source block was added to METADATA.pb pointing to commit `7db4b0f` (2017-05-23, "Update to 2.538"), which corresponds to the v2.538 update that was onboarded to google/fonts (PR #1019).

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/muktamalar/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `7db4b0fc09`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
