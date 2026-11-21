# Mukta — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [EkType/Mukta](https://github.com/EkType/Mukta) |
| Commit | `418021bbb8f5e7bf0bfd96296f9e015bf953efed` |
| Date | 2017-09-07 |
| Confidence | High |

## Investigation

The METADATA.pb for Mukta had no source block. The upstream repository was identified as EkType/Mukta, a monorepo by Ek Type containing four Mukta script variants: Mukta-Devanagari, MuktaMahee-Gurmukhi, MuktaMalar-Tamil, and MuktaVaani-Gujarati.

### Source Types Available

- **VFB** (FontLab): `Mukta-Devanagari/{weight}/VFB/Mukta-{weight}.vfb` (7 weights: ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold)
- **TTX**: `TTX/Mukta-Devanagari/Mukta-{weight}.ttx` (all 7 weights)
- **Feature files**: Per-weight `GPOS`, `features` files plus shared `GDEF`, `GSUB`, `GlyphOrderAndAliasDB`

### Buildability

VFB-only editable sources. The TTX files are XML representations of compiled fonts, not design sources. No `.glyphs`, `.ufo`, or `.designspace` files are present. Not directly buildable with gftools-builder.

### Actions Taken

A source block was added to METADATA.pb pointing to commit `418021b` (2017-09-07, "Directory Cleanup"), which is the latest commit in the repository and represents the final state after the v2.538 update that was onboarded to google/fonts.
