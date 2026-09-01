# Investigation Report: Bigelow Rules

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bigelow Rules |
| Designer | Astigmatic (Brian J. Bonislawsky) |
| License | OFL |
| Date Added | 2012-11-02 |
| Repository URL | https://github.com/librefonts/bigelowrules |
| Commit Hash | `f3ba7414e96d1a940b935d4fa4d2bab47150c7fc` |
| Branch | master |
| Config YAML | N/A (no buildable sources) |
| Status | **Missing config** (unbuildable - VFB only) |

## How URL Found

The repository URL `https://github.com/librefonts/bigelowrules` was identified from the librefonts organization on GitHub, which hosts archived copies of many Google Fonts. This is a standard librefonts mirror repository.

## How Commit Determined

The upstream repository has only **one commit** (`f3ba741 update .travis.yml`), making the commit hash trivially the only option. Since the font was last updated in google/fonts via PR #856 ("hotfix-bigelowrules: v1.001 added") by Marc Foley on 2017-08-07, and the librefonts repo contains the corresponding TTX decomposition of the font files, the single commit represents the full state of the repository.

## Config YAML Status

**No config.yaml exists**, and none can be created because the upstream repository contains no gftools-buildable source files. The available source files are:

- `src/BigelowRules-Regular.vfb` - FontLab VFB (proprietary format)
- `src/BigelowRules-Regular-OTF.vfb` - FontLab VFB
- `src/BigelowRules-Regular-TTF.vfb` - FontLab VFB
- `*.ttx` files - TTX decompositions of the binary font

VFB files cannot be processed by gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` source files.

## Verification

- **Commit exists in upstream repo**: Yes (it is the only commit)
- **Config YAML exists at commit**: No
- **Buildable sources available**: No (VFB only)
- **Source block in METADATA.pb**: Not yet in the upstream google/fonts (pending PR)
- **Override config.yaml in google/fonts**: No

## Google Fonts History

1. `90abd17b4` - Initial commit (part of the original google/fonts repo)
2. `4a101fcb7` - PR #856: "hotfix-bigelowrules: v1.001 added" by m4rc1e (2017-08-07) - last font binary update
3. Various metadata updates (stroke, classifications, languages)

## Confidence Level

**High** for URL and commit hash (single-commit repo, standard librefonts mirror). **N/A** for config.yaml since the font has no buildable sources.

## Open Questions

- This font cannot be rebuilt from source using gftools-builder due to VFB-only sources. The original designer (Astigmatic/Brian Bonislawsky) would need to provide sources in a buildable format (.glyphs, .ufo, or .designspace) for this to change.
