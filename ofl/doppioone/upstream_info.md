# Doppio One

## Summary

Doppio One is a sans-serif font by Szymon Celej, distributed by Sorkin Type Co. The upstream repository contains only SFD (FontForge) sources, which are not compatible with gftools-builder.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Doppio One |
| **Designer** | Szymon Celej |
| **License** | OFL |
| **Date Added** | 2012-02-22 |
| **Repository URL** | https://github.com/librefonts/doppioone |
| **Commit Hash** | `14bdd2e78b5b8e4f5bc5a39e5f1b02d398883a99` |
| **Config YAML** | None (SFD-only sources) |
| **Status** | missing_config |

## Investigation Details

### Onboarding History

Doppio One was added to Google Fonts in the initial commit (`90abd17b4`) by Dave Crossland on 2015-03-07. The font binary has only been modified once since, in a deploy commit (`76adaf1d2`).

A source block with repository_url and commit hash is being added via a pending PR on the `sources_info_2026-02-25` branch (commit `9a14639f3`).

### Upstream Repository

The upstream repo at https://github.com/librefonts/doppioone contains:
- `src/DoppioOne-Regular-TTF.sfd` - FontForge SFD source (TrueType)
- `src/DoppioOne-Regular-OTF.sfd` - FontForge SFD source (OpenType)
- `src/DoppioOne-Regular.vfb` - FontLab VFB source (proprietary format)
- TTX dumps of the compiled font
- No `.glyphs`, `.ufo`, or `.designspace` files

The repo has a single commit (`14bdd2e`, "update .travis.yml") visible in the shallow clone. The remote URL is https://github.com/librefonts/doppioone.

### Config YAML

No config.yaml exists in either the upstream repository or as an override in the google/fonts family directory. The SFD source format is not supported by gftools-builder, so a config.yaml cannot be created without source format conversion.

## Conclusion

Doppio One has a known upstream repository with correct commit hash, but the sources are in SFD (FontForge) format only. A config.yaml cannot be created without first converting the sources to a gftools-builder compatible format (UFO, .glyphs, or .designspace). The status remains `missing_config` with the note that this is an SFD-only repository.
