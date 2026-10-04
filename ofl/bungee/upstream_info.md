# Bungee

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungee/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Config YAML | Override in google/fonts (`ofl/bungee/config.yaml`) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` is documented in the METADATA.pb `source { repository_url }` field. It was also explicitly referenced in the google/fonts commit `6bc4f73e2` ("Bungee: Version 2.000 added"): "Taken from the upstream repo https://github.com/djrrb/Bungee". The repository belongs to David Jonathan Ross (djrrb), the font's designer. The METADATA.pb also includes a minisite URL at `https://djr.com/bungee`.

Note: This upstream repository is shared by all Bungee variants (Bungee, Bungee Color, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, Bungee Tint).

## How the Commit Hash Was Identified

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` is explicitly referenced in the google/fonts commit `6bc4f73e2` ("Bungee: Version 2.000 added"): "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99."

This commit exists in the upstream repo with date 2024-05-30 and message "Bump fontbakery". The METADATA.pb also references an archive URL for the v2.000 release: `https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip`, indicating the binary was taken from a release ZIP rather than being compiled from source.

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file at any commit. An override `config.yaml` was created in the google/fonts family directory (`ofl/bungee/config.yaml`) as part of commit `f6c68379a` ("Add override config.yaml for 50 font families"). The override config contains:

```yaml
sources:
  - sources/1-drawing/Bungee-Regular.ufo
familyName: Bungee
buildStatic: true
buildOTF: false
```

The source file `sources/1-drawing/Bungee-Regular.ufo` was verified to exist at the recorded commit `eb03cf69`. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-05-30 07:17:37 +0200
- Commit message: "Bump fontbakery"
- Source files at commit: `sources/1-drawing/Bungee-Regular.ufo` (verified)
- Font binary in google/fonts: `Bungee-Regular.ttf` (static)
- Binary taken from release archive: `Bungee-fonts.zip` (v2.000 release)
- Font originally added to Google Fonts: 2016-06-20
- Version 2.000 update: google/fonts commit `6bc4f73e2`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts commit message that brought in the v2.000 update. The commit exists in the upstream repo and the source files are present. The override config.yaml correctly points to the source file at the recorded commit. The binary was distributed via a release archive from the same commit.

## Open Questions

None. All data is well-documented and verified.
