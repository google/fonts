# Noto Sans Bengali — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/bengali
- **Commit**: `85d80394cbbbb798ca0a41c983902e6cf77be3a3`
- **Status**: Source block present

## What Was Done
The existing source metadata was reviewed. The source block contained both a repository_url and a commit hash pointing to the notofonts/bengali GitHub repository, along with an archive_url to the NotoSansBengali v3.011 release.

## Notes
- **Designer**: Google
- **Script**: Bengali/Bangla (Beng)
- **Category**: SANS_SERIF
- Part of the Google Noto project at github.com/notofonts/bengali. Variable axes wdth (62.5–100) and wght (100–900). Covers Bengali/Bangla, Assamese, Manipuri, and many other languages using the Bengali script.

## Recent upstream/main activity (post-investigation)

- **2026-01-09** — Simon Cozens, commit [`73b393782`](https://github.com/google/fonts/commit/73b393782) ("Noto Sans Bengali: Version 3.011 added"): advanced the source block from v3.000 → v3.011. METADATA.pb changes:
  - `commit`: `7ab89a047313e4a2c7ca5d670b28ced031c86542` → `85d80394cbbbb798ca0a41c983902e6cf77be3a3`
  - `archive_url`: `.../NotoSansBengali-v3.000/...zip` → `.../NotoSansBengali-v3.011/...zip`

  Binary `NotoSansBengali[wdth,wght].ttf` updated.
