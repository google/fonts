# Zalando Sans — Upstream Source Information

**Repo:** https://github.com/zalando/sans
**Commit:** `4e44d0864c4e37ab67fa549cd188aec8776dc948` (updated 2026-03-11; was `2fe06d0700b5b9ccd18a52c240e8927f48e92629`)
**Branch:** main
**Config:** `sources/config.yaml`

**Model**: Claude Opus 4.6 / Claude Opus 4.7 (1M context) [appendix]

## Summary

Zalando Sans was designed by Jakob Ekelund, KH Type, and Zalando as a variable sans-serif typeface with both width and weight axes, supporting Latin and Latin Extended subsets. The font was sourced from the `zalando/sans` repository at the commit listed above (shared with Zalando Sans Expanded and Zalando Sans SemiExpanded). Two variable font files were copied from `fonts/variable/` to the Google Fonts distribution: `ZalandoSans[wdth,wght].ttf` and `ZalandoSans-Italic[wdth,wght].ttf`. The width axis spans from 75 (Condensed) to 125 (Expanded) and the weight axis spans from 200 to 900.

## Recent upstream/main activity (post-investigation)

- **2026-03-11** — Emma Marichal, commit [`7644e9a8c`](https://github.com/google/fonts/commit/7644e9a8c) ("Zalando Sans: Version 1.800 added"): advanced the recorded commit from `2fe06d0700b5b9ccd18a52c240e8927f48e92629` to `4e44d0864c4e37ab67fa549cd188aec8776dc948` and updated the binaries to v1.800. The same upstream commit also produced v1.800 binaries for Zalando Sans Expanded and Zalando Sans SemiExpanded (sibling families); see their respective `upstream_info.md`.

The shipping `ZalandoSans[wdth,wght].ttf` (281728 bytes, md5 `5f48eb1963e54fe8ca1a6334d31bbb08`) is byte-identical to upstream `fonts/variable/ZalandoSans[wdth,wght].ttf` at commit `4e44d0864`. `head.fontRevision = 1.8000`, `name` ID 5 = "Version 1.800".
