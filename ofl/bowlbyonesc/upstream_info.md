# Investigation Report: Bowlby One SC

## Source Data

| Field | Value |
|---|---|
| Family Name | Bowlby One SC |
| Designer | Vernon Adams |
| License | OFL |
| Date Added | 2011-07-06 |
| Repository URL | https://github.com/librefonts/bowlbyonesc |
| Commit Hash | `9566646d9feaafcdc1c23174931ac4599803442b` |
| Branch | master |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Found

The repository URL `https://github.com/librefonts/bowlbyonesc` was previously recorded in the tracking data. The librefonts organization hosts archival copies of many early Google Fonts projects. The repository is accessible on GitHub.

## How Commit Determined

The repository has only 12 commits total, all from 2014. The recorded commit `9566646` is the tip of master (the latest commit, from 2014-10-17: "update .travis.yml"). This is the only meaningful commit to use as a reference since the repo has not been updated since 2014.

The font binary in google/fonts was last updated in:
- `c6a838cef` (2015-04-27) - "Updating ofl/bowlbyonesc/*ttf with nbspace and fsType fixes" by Dave Crossland

Unlike Bowlby One, Bowlby One SC has not received any additional hotfix updates since 2015.

## Config YAML Status

**No config.yaml exists** in either the upstream repository or as an override in google/fonts.

The upstream repository contains a mix of source formats:
- `src/BowlbyOneSC-Regular.sfd` (FontForge format)
- `src/BowlbyOneSC-Regular-TTF.vfb` (FontLab format)
- `src/BowlbyOneSC-Regular.ufo` (UFO format - gftools-buildable)
- `src/BowlbyOneSC-TThints.vfb` (FontLab hinting file)

**Important**: The presence of a UFO source means this family could potentially be built with gftools-builder if a config.yaml were created. However, the UFO source dates from 2014 and may not produce output matching the current binary (which was modified in 2015 for nbspace/fsType fixes).

## Verification

- **Repository accessible**: Yes, `librefonts/bowlbyonesc` is accessible on GitHub
- **Commit exists**: Yes, `9566646` verified on GitHub (2014-10-17)
- **Local cache**: Repo cached at `upstream_repos/fontc_crater_cache/librefonts/bowlbyonesc/`
- **Commit matches tip**: Yes, the recorded commit is the latest commit in the repo
- **Source files**: SFD, VFB, and UFO (UFO is gftools-builder compatible in principle)

## Confidence Level

**HIGH** - The repository URL and commit hash are correct. The commit is the tip of an archival repo that has not been updated since 2014. The current tracking notes say "Has gftools-buildable sources (ufo), needs config.yaml" which is accurate.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - src/BowlbyOneSC-Regular.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The UFO source file exists but is from 2014. Would building from this UFO produce output matching the current binary in google/fonts (which had nbspace/fsType fixes applied in 2015)? Testing would be needed.
2. A config.yaml could potentially be created as an override in google/fonts to build from the UFO source, but the output would need to be verified against the current binary.
3. This family was created by Vernon Adams, who passed away in 2014. The source is unlikely to receive further updates.
