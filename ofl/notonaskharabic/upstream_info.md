# Noto Naskh Arabic — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/arabic
- **Commit**: `59f5a3fd985bf24858915c3dddfc51a537640965`
- **Status**: Source block present

## What Was Done
The existing source metadata was reviewed. The source block contained both a repository_url and a commit hash pointing to the notofonts/arabic GitHub repository, along with an archive_url to the NotoNaskhArabic v2.021 release.

## Notes
- **Designer**: Google
- **Script**: Arabic (Naskh style)
- **Category**: SERIF
- Part of the Google Noto project at github.com/notofonts/arabic. Provides Naskh-style Arabic script coverage with variable weight (wght 400–700). Supports a wide range of Arabic-script languages.

## Recent upstream/main activity (post-investigation)

- **2026-01-16** — Simon Cozens, commit [`35ddfc50b`](https://github.com/google/fonts/commit/35ddfc50b) ("Noto Naskh Arabic: Version 2.021 added"): advanced the source block from v2.020 → v2.021. METADATA.pb changes:
  - `commit`: `1b2b7e5c6ce3ab4d50681c854892325530084c35` → `59f5a3fd985bf24858915c3dddfc51a537640965`
  - `archive_url`: `.../NotoNaskhArabic-v2.020/...zip` → `.../NotoNaskhArabic-v2.021/...zip`

  Binary `NotoNaskhArabic[wght].ttf` updated.

### Earlier (2025-10-15 → 2025-10-29)

- **2025-10-15** — simoncozens, commit [`a5cb0f48a`](https://github.com/google/fonts/commit/a5cb0f48a) ("Noto Naskh Arabic: Version 2.020 added"): preceded the v2.021 update — initial v2.020 onboarding via gftools-packager. Source block fields were populated then.
- **2025-10-29** — Emma Marichal, commit [`4b76b0ca7`](https://github.com/google/fonts/commit/4b76b0ca7) ("Remove 'ms_Arab' language entry"): removed `languages: "ms_Arab"` from METADATA.pb. Outside the `source { ... }` block.
