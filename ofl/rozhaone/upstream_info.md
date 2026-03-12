# Rozha One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **URL**: https://github.com/itfoundry/rozhaone
- **Owner**: itfoundry (Indian Type Foundry)
- **Branch**: master
- **Latest commit**: `8225a64e986c03b78fb1bb08d55705c52c9eeab8` (2014-11-21)
- **Source format**: UFO (`masters/RozhaOne_0.ufo`)

## What Was Done

The canonical upstream repository at `itfoundry/rozhaone` was located by searching GitHub for the Indian Type Foundry organization and the font name. The repository contains UFO sources for the Devanagari + Latin family. The masters directory holds `RozhaOne_0.ufo` along with legacy VFB files. The latest commit hash was verified via the GitHub API. A `source` block was added to `METADATA.pb`.

## Notes

The designer is the Indian Type Foundry (`info@indiantypefoundry.com`), consistent with the copyright statement in METADATA.pb. A secondary fork exists at `web1o1/rozhaone`, but the `itfoundry` repository is the canonical upstream. The repository has not been updated since 2014. The build system uses custom Python scripts (`build.py`, `reference.py`) rather than a standard `config.yaml`.
