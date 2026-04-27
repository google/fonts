# Noto Sans Kannada — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/kannada
- **Commit**: `6387faa16123c9becca4f0f3ca095189de5c61da`
- **Status**: present

## What Was Done
The existing source metadata was reviewed. A complete `source` block was present, pointing to the notofonts/kannada repository with an archive release at NotoSansKannada-v2.005. The font is variable with `wdth` (62.5–100) and `wght` (100–900) axes.

## Notes
- Designer: Google
- Script: Kannada (Knda)
- Category: SANS_SERIF
- Covers Kannada and Tulu.

## Recent upstream/main activity (post-investigation)

- **2026-02-25** — Aaron Bell, commit [`9d71243b7`](https://github.com/google/fonts/commit/9d71243b7) ("Updating Noto Sans Kannada"): bumped the shipping `NotoSansKannada[wdth,wght].ttf` from v2.005 to v2.006 (binary-only commit; size 654460 → 641372). Aaron's commit body explained: "It seems the 2.006 release was never pushed out." — meaning the v2.006 release archive existed upstream but the corresponding binary had not been merged to google/fonts.

  Aaron's commit did NOT update the source block in METADATA.pb. This left the recorded `commit` and `archive_url` referencing v2.005 while the shipping binary was v2.006, an out-of-sync state.

  ### Source-block corrections (this commit)

  Updated `commit` and `archive_url` to point to the v2.006 release:
  - `commit`: `6387faa16123c9becca4f0f3ca095189de5c61da` (Simon Cozens 2023-09-27 "Fix website template", which was pre-v2.006) → `7eeac8993f890e3d8568ba909ae67f554113ea92` (Simon Cozens 2024-09-19 "Bump sans version to 2.006", the commit that the `NotoSansKannada-v2.006` tag points to).
  - `archive_url`: `.../NotoSansKannada-v2.005/NotoSansKannada-v2.005.zip` → `.../NotoSansKannada-v2.006/NotoSansKannada-v2.006.zip`.

  After the fix, METADATA.pb reads:

  ```
  source {
    repository_url: "https://github.com/notofonts/kannada"
    commit: "7eeac8993f890e3d8568ba909ae67f554113ea92"
    config_yaml: "sources/config-sans-kannada.yaml"
    archive_url: "https://github.com/notofonts/kannada/releases/download/NotoSansKannada-v2.006/NotoSansKannada-v2.006.zip"
    ...
    branch: "main"
  }
  ```

### Updated source-of-truth fields

- **Repository URL**: https://github.com/notofonts/kannada (unchanged)
- **Commit**: `7eeac8993f890e3d8568ba909ae67f554113ea92` (v2.006 tag)
- **Archive URL**: v2.006 release zip
- **Branch**: `main` (unchanged)
- **Config YAML**: `sources/config-sans-kannada.yaml` (unchanged)
- **Status**: present
- **Confidence**: HIGH — the v2.006 tag commit is unambiguous and corresponds to the shipping `Version 2.006` binary (`head.fontRevision = 2.0060`).
