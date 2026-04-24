**Model**: Claude Opus 4.6

# Zilla Slab — Upstream Source Investigation

## Summary

The upstream source repository for Zilla Slab was identified and a source block was added to `METADATA.pb`.

## Repository

- **URL**: https://github.com/mozilla/zilla-slab
- **Owner**: Mozilla
- **Designer**: Typotheque
- **Source format**: UFO (10 masters: Light, LightItalic, Regular, Italic, Medium, MediumItalic, SemiBold, SemiBoldItalic, Bold, BoldItalic)
- **Branch**: main
- **Commit**: `6dcec520f9b23ad7f380b7ce3e8072be95fe0004`
- **Commit date**: 2021-01-04
- **Commit message**: "Merge pull request #39 from shoorick/typo — Fix typos"

## Investigation Notes

The repository was found at `mozilla/zilla-slab`. The DESCRIPTION.en_us.html in google/fonts explicitly referenced `github.com/mozilla/zilla-slab`. A second repository at `typotheque/zilla-slab` was also found, but it contained only zipped UFO files rather than proper source directories. The `mozilla/zilla-slab` repository was determined to be the canonical upstream, containing proper UFO source directories for all 10 weights in the `sources/` directory. The repository also contained source files for Zilla Slab Highlight (see `zillaslabhighlight/upstream_info.md`).

## Confidence

High — the repository URL is referenced in DESCRIPTION.en_us.html and the Mozilla copyright holder confirms this as the canonical upstream source.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/zillaslab/` referencing the upstream gftools-builder-compatible source at the pinned commit `6dcec52` (`sources/ZillaSlab-Light.ufo`, `sources/ZillaSlab-LightItalic.ufo`, `sources/ZillaSlab-Regular.ufo`, `sources/ZillaSlab-Italic.ufo`, `sources/ZillaSlab-Medium.ufo`, `sources/ZillaSlab-MediumItalic.ufo`, `sources/ZillaSlab-SemiBold.ufo`, `sources/ZillaSlab-SemiBoldItalic.ufo`, `sources/ZillaSlab-Bold.ufo`, `sources/ZillaSlab-BoldItalic.ufo`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
