# Mukta Mahee — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [EkType/Mukta](https://github.com/EkType/Mukta) |
| Commit | `7db4b0fc09894ad6814346172f6f0c1cf822a722` |
| Date | 2017-05-23 |
| Confidence | High |

## Investigation

The METADATA.pb for Mukta Mahee had no source block. The upstream repository is EkType/Mukta, a monorepo containing four Mukta script variants. Mukta Mahee (Gurmukhi) sources are under the `MuktaMahee-Gurmukhi/` directory.

### Source Types Available

- **VFB** (FontLab): `MuktaMahee-Gurmukhi/{weight}/VFB/MuktaMahee-{weight}.vfb` (7 weights)
- **TTX**: `MuktaMahee-Gurmukhi/MuktaMahee-{weight}.ttx` (all 7 weights)
- **Feature files**: Per-weight `GPOS`, `features` files plus shared `GDEF`, `GSUB`, `GlyphOrderAndAliasDB`

### Buildability

VFB-only editable sources. The TTX files are XML representations of compiled fonts, not design sources. Not directly buildable with gftools-builder.

### Actions Taken

A source block was added to METADATA.pb pointing to commit `7db4b0f` (2017-05-23, "Update to 2.538"), which corresponds to the v2.538 update that was onboarded to google/fonts (PR #1018).
