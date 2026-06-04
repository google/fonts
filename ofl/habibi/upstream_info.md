# Investigation Report: Habibi

## Summary

Habibi is a high-contrast serif typeface designed by Magnus Gaarde and mastered by Eben Sorkin (Sorkin Type Co). It was added to Google Fonts on 2011-12-19 as part of the initial commit of the google/fonts repository. The upstream repository at `librefonts/habibi` is a legacy mirror (originally from Google Code) containing only VFB and SFD source files -- no gftools-builder compatible sources exist.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Habibi |
| **Designer**      | Magnus Gaarde |
| **Repository URL**| https://github.com/librefonts/habibi |
| **Commit Hash**   | `1c3eb606631e9da373f1017f7972765a7ab32bd5` (only commit) |
| **Config YAML**   | None (SFD/VFB-only sources) |
| **Status**        | no_config_possible |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb in `ofl/habibi/` has no `source { }` block. Key fields:
- Name: "Habibi"
- Designer: "Magnus Gaarde"
- License: OFL
- Date added: 2011-12-19
- Copyright: "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com)"

### Google Fonts Repository History

The font file history in google/fonts shows only metadata-related changes after the initial commit:

| Commit | Date | Description |
|--------|------|-------------|
| `90abd17b4` | 2015-03-07 | Initial commit (contains Habibi-Regular.ttf) |
| `480630de3` | -- | Tentative update to METADATA.pb textprotos |
| `27f377ab0` | -- | Update copyright field in METADATA.pb |
| `633ebadbf` | -- | Add language support metadata |
| `701bd391b` | -- | Undo rollback, remove languages from METADATA |

The font binary (`Habibi-Regular.ttf`) has not been updated since the initial commit. This is a legacy font from 2011 that predates the modern gftools-packager workflow.

### Upstream Repository Analysis

The repository at `https://github.com/librefonts/habibi` is a `librefonts` mirror, likely auto-generated from the old Google Code font directory. It contains a single commit:

- **Commit**: `1c3eb606631e9da373f1017f7972765a7ab32bd5` (2014-10-17)
- **Author**: hash3g
- **Message**: "update .travis.yml"

The repository contains TTX decompositions of the font alongside source files:

**Source files found:**
- `src/Habibi-Regular.vfb` -- FontLab VFB format (proprietary binary)
- `src/Habibi-Regular-TTF.sfd` -- FontForge SFD format

**No gftools-builder compatible sources found** -- no `.glyphs`, `.ufo`, or `.designspace` files. The VFB format requires FontLab (proprietary) and the SFD format is a FontForge format not supported by gftools-builder/fontmake.

The repository also includes a `.travis.yml` for fontbakery CI and a `FONTLOG.txt` documenting the design history.

### Build Configuration

No `config.yaml` exists in the upstream repository, and none can be created because the source files (VFB/SFD) are not compatible with gftools-builder. The font was mastered manually from FontLab VFB to TTF in December 2011.

## Conclusion

Habibi is a legacy font from 2011 with only VFB/SFD source files in the `librefonts/habibi` mirror repository. No gftools-builder configuration is possible because the source formats are incompatible. The font has never been updated since its initial inclusion.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/habibi"
  commit: "1c3eb606631e9da373f1017f7972765a7ab32bd5"
}
```

Note: No `config_yaml` field is possible because the repository only contains VFB and SFD source files, which are not compatible with gftools-builder.

### Status: `no_config_possible`
### Confidence: HIGH
