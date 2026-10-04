# Prompt — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at https://github.com/cadsondemak/prompt, owned by Cadson Demak, the designer listed in METADATA.pb. The repository is not a mirror and contains source files. The METADATA.pb source block was updated accordingly.

## Designer

Cadson Demak (info@cadsondemak.com) — a Thai type foundry. The DESCRIPTION.en_us.html explicitly links to `https://github.com/cadsondemak/prompt` as the contribution URL.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry for cadsondemak/prompt.
- **GitHub search**: The repository `https://github.com/cadsondemak/prompt` was found and verified (HTTP 200).
- **Ownership**: The repository owner is `cadsondemak`, matching the designer credit. It is not a fork.
- **Description**: "Prompt is a Thai + Latin formal sans serif font family with 18 styles" (51 stars).
- **Latest commit**: `18f813a4dea16a7ecc6f944053d3ce2cd4d7e824` — "The mark has been fixed. The mark of the letters Ỗ and ỗ has been fixed."

## Source Files

The repository contains the full 18-style family (9 weights × 2 axes: upright and italic).

## Verdict

**Canonical upstream repo found.** `https://github.com/cadsondemak/prompt` is the designer-owned repository. METADATA.pb was updated with `repository_url` and `commit` fields.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/prompt/` referencing the upstream gftools-builder-compatible source at the pinned commit `18f813a` (`Source/Prompt_100_Thin.glyphs`, `Source/Prompt_100_Thin_Ita.glyphs`, `Source/Prompt_200_ExtraLight.glyphs`, `Source/Prompt_200_ExtraLight_Ita.glyphs`, `Source/Prompt_300_Light.glyphs`, `Source/Prompt_300_Light_Ita.glyphs`, `Source/Prompt_400_Regular.glyphs`, `Source/Prompt_400_Regular_Ita.glyphs`, `Source/Prompt_500_Medium.glyphs`, `Source/Prompt_500_Medium_Ita.glyphs`, `Source/Prompt_600_SemiBold.glyphs`, `Source/Prompt_600_SemiBold_Ita.glyphs`, `Source/Prompt_700_Bold.glyphs`, `Source/Prompt_700_Bold_Ita.glyphs`, `Source/Prompt_800_ExtraBold.glyphs`, `Source/Prompt_800_ExtraBold_Ita.glyphs`, `Source/Prompt_900_Black.glyphs`, `Source/Prompt_900_Black_Ita.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
