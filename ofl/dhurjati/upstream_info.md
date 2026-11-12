# Dhurjati

## Summary

Dhurjati is a Telugu sans-serif display typeface designed by Purushoth Kumar Guttula, led by Appaji Ambarisha Darbha of Silicon Andhra. The upstream repo at github.com/appajid/dhurjati has a single commit containing both SFD and UFO sources. The UFO source is gftools-buildable but no config.yaml exists.

## Key Findings

- **Designer**: Purushoth Kumar Guttula
- **Date added to Google Fonts**: 2014-12-10
- **Repository URL**: https://github.com/appajid/dhurjati
- **Commit**: `a318ca871e126878f22e1e235ea9c3563b2344fc` (only commit in repo)
- **Source formats available**: SFD (FontForge), UFO
- **config_yaml**: Override in google/fonts
- **Override config.yaml**: None in google/fonts
- **Primary script**: Telugu (Telu)

## Repository Analysis

The appajid/dhurjati repo contains:
- `Dhurjati.sfd` - FontForge source (5.5 MB)
- `Dhurjati.ufo/` - UFO source directory
- `OFL.txt` - License file

The repo has exactly one commit (`a318ca8` - "updated copyright & version, no latin characters") by appajid (Ambarisha) dated 2014-11-26. This commit added all the files.

The UFO source is present and could potentially be used with gftools-builder if a config.yaml were created.

## google/fonts History

- Initial commit (90abd17b4): Font binary added to google/fonts
- c8f729cbd (2024-01-14): Simon Cozens added the repository_url source block
- 9a14639f3 (2026-02-25): Commit hash added to source block in batch update

The font binary has not been updated since the initial commit.

## Status

- **repository_url**: Correct (https://github.com/appajid/dhurjati)
- **commit**: `a318ca8` is the only commit in the repo, confirmed correct
- **config_yaml**: Missing - needs to be created (either in upstream or as override)
- **Overall**: missing_config (has gftools-buildable UFO sources but needs config.yaml)

## Recommendation

Status should remain `missing_config`. A config.yaml could be created as an override in the google/fonts family directory, pointing to the UFO source. The config would look something like:

```yaml
sources:
  - Dhurjati.ufo
familyName: Dhurjati
buildVariable: False
```

However, since the upstream repo owner (appajid) appears inactive (single commit from 2014), an override config.yaml in google/fonts would be the practical approach.

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Dhurjati.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.
