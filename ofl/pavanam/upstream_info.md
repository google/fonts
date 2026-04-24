# Pavanam — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Pavanam was identified as **https://github.com/enathu/pavanam**, maintained by the designer Tharique Azeez (GitHub username: enathu). This was confirmed by the DESCRIPTION.en_us.html in the google/fonts repository, which explicitly links to this repository. The repository is designer-owned and contains UFO source files.

## Investigation

The METADATA.pb listed the designer as Tharique Azeez with copyright referencing both Tharique Azeez and Vernon Adams (whose Pontano Sans Latin design was used as the basis for the Latin portion).

The DESCRIPTION.en_us.html explicitly linked to `https://github.com/enathu/pavanam` and noted the repository contains complete set of source files in UFO format. A web search confirmed this is the canonical designer's own repository, with the GitHub user enathu being Tharique Azeez.

The latest commit in the upstream repository was retrieved:

- **Commit**: `c4ba9335116a4ff2c124ebf918455748caedccac`
- **Message**: "Fix for #6"
- **Date**: 2016-05-25

## Upstream Repository

- **URL**: https://github.com/enathu/pavanam
- **Owner**: Tharique Azeez (enathu)
- **Type**: Designer-owned canonical upstream
- **License**: OFL 1.1
- **Latest commit**: `c4ba9335116a4ff2c124ebf918455748caedccac`

## METADATA.pb Changes

A `source` block was added to METADATA.pb with the repository URL and latest commit hash.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/pavanam/` referencing the upstream gftools-builder-compatible source at the pinned commit `c4ba9335` (`source/Pavanam-Regular.ufo`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
