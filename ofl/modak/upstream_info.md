# Modak — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [EkType/Modak](https://github.com/EkType/Modak) |
| Commit | `143b2db4fd5c8db6cdab20fad82b26ded9ce9eb7` |
| Date | 2015-02-25 |
| Confidence | High |

## Investigation

The METADATA.pb for Modak had no source block. The upstream repository was identified as EkType/Modak, by the Ek Type foundry.

### Source Types Available

- **VFB** (FontLab): `SourceFiles/Modak.vfb`
- **TTX**: `TTX/Modak.ttx`
- **Feature files**: `SourceFiles/fea.Classes`, `fea.GDEF`, `fea.GPOS`, `fea.GSUB`, `features`
- **Supporting files**: `SourceFiles/FontMenuNameDB`, `GlyphOrderAndAliasDB`, `current.fpr`

### Buildability

VFB-only editable source. The TTX file is an XML representation of the compiled font, not a design source. No `.glyphs`, `.ufo`, or `.designspace` files are present. Not directly buildable with gftools-builder.

### Actions Taken

A source block was added to METADATA.pb pointing to commit `143b2db` (2015-02-25), which is the latest commit in the repository and was present at the time of the initial google/fonts commit.

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/modak/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `143b2db4fd`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
