# Denk One

## Summary

Denk One is a sans-serif display typeface by Sorkin Type. It was updated via gftools-packager in February 2023 using upstream commit `95da30b`. The current METADATA.pb references commit `eadc321b` (from a fontc_crater batch update), which is the repo HEAD but is just a dependabot pip requirements update, not a font content change.

## Key Findings

- **Designer**: Sorkin Type
- **Date added to Google Fonts**: 2012-11-26
- **Repository URL**: https://github.com/SorkinType/Denk-One
- **Onboarding commit**: `95da30b8aa7bd5fb3045afb2fe054bf1b2e4e029` (Merge PR #11 from emmamarichal/master)
- **Current METADATA.pb commit**: `eadc321b9f89db0d7090550e1d7bf6dcd75b6996` (latest HEAD, dependabot update)
- **config_yaml**: `sources/config.yaml`
- **Source format**: Glyphs (.glyphs)
- **Branch**: master

## Repository Analysis

The SorkinType/Denk-One repo contains:
- `sources/DenkOne.glyphs` - Main source file
- `sources/config.yaml` - gftools-builder configuration
- `fonts/ttf/DenkOne-Regular.ttf` - Compiled font

The config.yaml contains:
```yaml
sources:
  - DenkOne.glyphs
familyName: Denk One
buildVariable: False
```

## Commit History Analysis

The gftools-packager PR (#5944) by emmamarichal was merged on 2023-03-01 and explicitly references upstream commit `95da30b8aa7bd5fb3045afb2fe054bf1b2e4e029`. This commit (Merge PR #11) updated the font files and sources.

The current METADATA.pb commit `eadc321b` was set in the fontc_crater batch (commit 19cdcec59 by Felipe Sanches, 2025-03-31). This points to the latest HEAD of the repo, which is a dependabot merge (PR #10) that only updated `requirements.txt` (pip certifi bump). No font content changed between `95da30b` and `eadc321b`.

Between the two commits:
- `95da30b` -> Merge PR #11: Font files exported (actual font content)
- `f78fac8` -> Merge PR #12: Dependabot fonttools bump
- `e02ab90` -> Bump fonttools
- `eadc321` -> Merge PR #10: Dependabot certifi bump

## google/fonts History

- Initial commit (90abd17b4): Original font added
- 8b7e1a666 (2023-02-28): gftools-packager update from commit 95da30b
- 66f91f10f (2024-04-03): Merge upstream.yaml into METADATA.pb (added file mappings and branch)
- 19cdcec59 (2025-03-31): fontc_crater batch update (changed commit to eadc321, added config_yaml)

## Status

- **repository_url**: Correct (https://github.com/SorkinType/Denk-One)
- **commit**: `eadc321b` is technically the repo HEAD. The actual font onboarding commit was `95da30b`. Since `eadc321b` only has dependency bumps (no font changes), both commits would produce the same font binary. The current value is acceptable for fontc_crater purposes.
- **config_yaml**: Correct (sources/config.yaml)
- **Overall**: complete

## Recommendation

Status is `complete`. The commit hash discrepancy (eadc321 vs 95da30b) is noted but not problematic since no font content changed between them. The fontc_crater targets list intentionally uses the latest HEAD.
