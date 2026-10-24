# Scope One — Upstream Source Investigation

**Designer**: Dalton Maag
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Scope One was found at `daltonmaag/scope-one` on GitHub. The repository contained UFO source files and was maintained by Dalton Maag Ltd, the credited designer.

## Repository

- **URL**: https://github.com/daltonmaag/scope-one
- **Commit**: `7a5c5df7367bdba124c4dcf8f59b15912811c3c4`
- **Commit date**: 2017-02-01
- **Default branch**: master

## Sources Found

The `source/` directory contained:
- `ScopeOne_Rg.ufo` (UFO3 format)
- `GlyphOrderAndAliasDB.txt`
- `ttfautohint.ctrl`

## Confidence

High. The repository was hosted under the daltonmaag organization (the credited designer) and contained UFO sources directly corresponding to the released font binary.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/scopeone/` referencing the upstream gftools-builder-compatible source at the pinned commit `7a5c5df` (`source/ScopeOne_Rg.ufo`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
