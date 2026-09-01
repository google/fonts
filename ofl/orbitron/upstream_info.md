# Orbitron — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The Google Fonts version of Orbitron is sourced from a variable-font fork maintained at https://github.com/googlefonts/orbitron-vf. The original typeface was published by Matt McInerney on the League of Movable Type and the original source repository exists at https://github.com/theleagueof/orbitron. The METADATA.pb source block was already present pointing to the googlefonts variable fork, with the correct commit.

## Repositories

### Upstream Source (Variable Font Fork — used by Google Fonts)
- **URL**: https://github.com/googlefonts/orbitron-vf
- **Default branch**: `master`
- **Description**: A variable font, fork of Orbitron
- **Note**: This is not a fork in the GitHub sense (fork field is `false`); it was created as a separate repository for the variable font work.

### Original Upstream
- **URL**: https://github.com/theleagueof/orbitron
- **Default branch**: `master`
- **Description**: A geometric sans-serif from the future.
- **Latest commit**: `13e6a5222aa6818d81c9acd27edd701a2d744152` (2011-05-25, "Initial commit with readme and licenses")
- **Note**: The original League of Movable Type repository appears to be effectively archived; its latest commit dates to 2011.

## Commit

- **Pinned commit**: `f16482824e0ce4d008dee59b9b632e9ce9663359`
- **Commit message**: Remove width axis
- **Commit date**: 2024-04-10
- **Status**: This is the HEAD of the `master` branch of `googlefonts/orbitron-vf` — the repository is up-to-date with the pinned commit.

## Font Details

Orbitron is a geometric sans-serif display typeface designed by Matt McInerney, originally published on the League of Movable Type. It was remastered as a variable font in 2019 and subsequently maintained under the `googlefonts` organization. The variable font exposes a `wght` axis (400–900). The family is intended for display use in futuristic and science-fiction contexts.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/googlefonts/orbitron-vf
- `commit`: `f16482824e0ce4d008dee59b9b632e9ce9663359`
- `config_yaml`: sources/config.yaml

No changes to METADATA.pb were required.
