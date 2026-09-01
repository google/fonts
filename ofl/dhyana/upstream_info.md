# Dhyana

## Summary

Dhyana is a Lao sans-serif typeface designed by Vernon Adams. The upstream repo at github.com/vernnobile/DhyanaFont contains UFO and SFD sources for both Regular and Bold weights. No config.yaml exists. Vernon Adams passed away, so the upstream repo is inactive.

## Key Findings

- **Designer**: Vernon Adams
- **Date added to Google Fonts**: 2011-12-15
- **Repository URL**: https://github.com/vernnobile/DhyanaFont
- **Commit**: `600f15faf4489ecca60dbcecad6f163e095f2af3` (latest/HEAD commit "updates")
- **Source formats available**: UFO, SFD (FontForge), FEA (feature files)
- **config_yaml**: Override in google/fonts
- **Override config.yaml**: None in google/fonts
- **Weights**: Regular (400), Bold (700)

## Repository Analysis

The vernnobile/DhyanaFont repo contains:

**Regular weight:**
- `Regular/src/Dhyana.ufo` - UFO source
- `Regular/src/Dhyana.sfd` - FontForge source
- `Regular/src/Dhyana.fea` - OpenType feature file
- `Regular/src/Dhyana.otf` - OTF binary
- `Regular/Dhyana.ttf` - TTF binary

**Bold weight:**
- `Bold/src/Dhyana-Bold.ufo` - UFO source
- `Bold/src/Dhyana-Bold.sfd` - FontForge source
- `Bold/src/Dhyana-Bold.otf` - OTF binary
- `Bold/Dhyana-Bold.ttf` - TTF binary

The repo has 4 commits total, all by Vernon Adams, spanning from initial migration from Google Code (c38a607) to the final "updates" commit (600f15f, dated 2012-07-01).

## google/fonts History

- Initial commit (90abd17b4): Font binaries added (both Regular and Bold)
- c8f729cbd (2024-01-14): Simon Cozens added the repository_url source block
- 9a14639f3 (2026-02-25): Commit hash added to source block in batch update

The font binaries have not been updated since the initial commit (only a chmod -x fix in 49fbebd3d).

## Status

- **repository_url**: Correct (https://github.com/vernnobile/DhyanaFont)
- **commit**: `600f15f` is the latest commit (HEAD), confirmed correct
- **config_yaml**: Missing - needs to be created (either in upstream or as override)
- **Overall**: missing_config (has gftools-buildable UFO sources but needs config.yaml)

## Recommendation

Status should remain `missing_config`. The UFO sources are present for both weights and could be used with gftools-builder. Since Vernon Adams has passed away and the repo is inactive, an override config.yaml in google/fonts is the only practical approach. A config would need to reference both UFO sources:

```yaml
sources:
  - Regular/src/Dhyana.ufo
  - Bold/src/Dhyana-Bold.ufo
familyName: Dhyana
buildVariable: False
```

Note: The non-standard directory structure (sources in `Regular/src/` and `Bold/src/` subdirectories) may require special handling.

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Regular/src/Dhyana.ufo
  - Bold/src/Dhyana-Bold.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.
