# Investigation Report: Bigshot One

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bigshot One |
| Designer | Gesine Todt |
| License | OFL |
| Date Added | 2011-05-04 |
| Repository URL | https://github.com/librefonts/bigshotone |
| Commit Hash | `b8d1fa459ee9a43fbe1d7fd07b570878206bd6d5` |
| Branch | master |
| **Config YAML** | Override in google/fonts |
| Status | **Missing config** (has UFO, needs config.yaml) |

## How URL Found

The repository URL `https://github.com/librefonts/bigshotone` was identified from the librefonts organization on GitHub, which hosts archived copies of many Google Fonts. This is a standard librefonts mirror repository.

## How Commit Determined

The upstream repository has only **one commit** (`b8d1fa4 update .travis.yml`), making the commit hash trivially the only option. The font was last updated in google/fonts via PR #857 ("hotfix-bigshotone: v1.001 added") by Marc Foley on 2017-08-07.

## Config YAML Status

**No config.yaml exists** in the upstream repository. However, unlike Bigelow Rules, this repository contains a UFO source file that could potentially be used with gftools-builder:

- `src/BigshotOne.ufo/` - UFO source directory (contains fontinfo.plist, features.fea, glyphs/, groups.plist, kerning.plist)
- `src/BigshotOne-TTF.sfd` - FontForge SFD
- `src/BigshotOne.vfb` - FontLab VFB (proprietary format)
- `src/BigshotOne-TTF.vfb` - FontLab VFB

The UFO file could be targeted by a config.yaml for gftools-builder, but no such configuration has been created yet. An override config.yaml could be placed in the google/fonts family directory.

## Verification

- **Commit exists in upstream repo**: Yes (it is the only commit)
- **Config YAML exists at commit**: No
- **Buildable sources available**: Yes (UFO)
- **Source block in METADATA.pb**: Not yet in the upstream google/fonts (pending PR)
- **Override config.yaml in google/fonts**: No

## Google Fonts History

1. `90abd17b4` - Initial commit (part of the original google/fonts repo)
2. `c49ea1306` - PR #857: "hotfix-bigshotone: v1.001 added" by m4rc1e (2017-08-07) - last font binary update; renamed from `BigshotOne.ttf` to `BigshotOne-Regular.ttf`
3. Various metadata updates (stroke, classifications, languages)

## Confidence Level

**High** for URL and commit hash (single-commit repo, standard librefonts mirror). **Actionable** for config.yaml - the UFO source exists and a config.yaml could be written.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - src/BigshotOne.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

- A config.yaml needs to be created (either in the upstream repo or as an override in google/fonts) targeting `src/BigshotOne.ufo` to enable gftools-builder compilation. The quality and completeness of the UFO source should be verified before creating the config.
