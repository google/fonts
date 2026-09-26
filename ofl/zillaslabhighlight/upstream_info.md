**Model**: Claude Opus 4.6

# Zilla Slab Highlight — Upstream Source Investigation

## Summary

The upstream source repository for Zilla Slab Highlight was identified and a source block was added to `METADATA.pb`.

## Repository

- **URL**: https://github.com/mozilla/zilla-slab
- **Owner**: Mozilla
- **Designer**: Typotheque
- **Source format**: UFO (`ZillaSlabHighlight-Regular.ufo`, `ZillaSlabHighlight-Bold.ufo`)
- **Branch**: main
- **Commit**: `6dcec520f9b23ad7f380b7ce3e8072be95fe0004`
- **Commit date**: 2021-01-04
- **Commit message**: "Merge pull request #39 from shoorick/typo — Fix typos"

## Investigation Notes

Zilla Slab Highlight shared the same upstream repository as Zilla Slab (`mozilla/zilla-slab`). The `sources/` directory of that repository contained `ZillaSlabHighlight-Regular.ufo` and `ZillaSlabHighlight-Bold.ufo` alongside the main Zilla Slab UFO files. This is a separate decorative variant of the Zilla Slab typeface with a highlighted/outlined effect, built from the same source repository.

## Confidence

High — the Highlight UFO sources were directly confirmed in the `mozilla/zilla-slab` repository, and the copyright string matches The Mozilla Foundation.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/zillaslabhighlight/` referencing the upstream gftools-builder-compatible source at the pinned commit `6dcec52` (`sources/ZillaSlabHighlight-Regular.ufo`, `sources/ZillaSlabHighlight-Bold.ufo`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
