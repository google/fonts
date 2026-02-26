# Donegal One

## Summary

Donegal One is a serif font designed by Gary Lonergan, distributed by Sorkin Type Co. The upstream repository contains only SFD (FontForge) sources, which are not compatible with gftools-builder.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Donegal One |
| **Designer** | Gary Lonergan |
| **License** | OFL |
| **Date Added** | 2012-11-26 |
| **Repository URL** | https://github.com/librefonts/donegalone |
| **Commit Hash** | `b0af18fd94255bfdfe07e90db984167564abd565` |
| **Config YAML** | None (SFD-only sources) |
| **Status** | missing_config |

## Investigation Details

### Onboarding History

Donegal One was added to Google Fonts in the initial commit (`90abd17b4`) by Dave Crossland on 2015-03-07. The font binary has only been modified once since, in a deploy commit (`76adaf1d2`).

A source block with repository_url and commit hash is being added via a pending PR on the `sources_info_2026-02-25` branch (commit `9a14639f3`).

### Upstream Repository

The upstream repo at https://github.com/librefonts/donegalone contains:
- `src/DonegalOne-Regular-TTF.sfd` - FontForge SFD source (TrueType)
- `src/DonegalOne-Regular-OTF.sfd` - FontForge SFD source (OpenType)
- `src/DonegalOne-Regular.vfb` - FontLab VFB source (proprietary format)
- TTX dumps of the compiled font
- No `.glyphs`, `.ufo`, or `.designspace` files

The repo has a single commit (`b0af18f`, "update .travis.yml") visible in the shallow clone. The remote URL is https://github.com/librefonts/donegalone.

### Config YAML

No config.yaml exists in either the upstream repository or as an override in the google/fonts family directory. The SFD source format is not supported by gftools-builder, so a config.yaml cannot be created without source format conversion.

## Conclusion

Donegal One has a known upstream repository with correct commit hash, but the sources are in SFD (FontForge) format only. A config.yaml cannot be created without first converting the sources to a gftools-builder compatible format (UFO, .glyphs, or .designspace). The status remains `missing_config` with the note that this is an SFD-only repository.
