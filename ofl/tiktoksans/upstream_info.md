# TikTok Sans — Source Metadata Investigation
**Model**: Claude Opus 5.5
**Date**: 2026-10-13 (first investigation 2026-03-12, Claude Opus 4.6)

## Source Repository
- **URL**: https://github.com/TikTok/TikTokSans
- **Commit**: `1cfe2b707a0348b18fecf94532a5c7636d0acc43` (2025-06-13, "Remove RFN & update Makefile help")
- **Config**: `sources/config.yaml`

## What Was Done
- 2026-03-12: the source block had no commit, and the latest commit on main, `baa2f381f9102da9fbc3c83843ad224774240516` (2025-08-11, "Update requirements"), was added.
- 2026-10-13: that commit post-dates the onboarding (the font was added on 2025-07-09) and was replaced by `1cfe2b7`, the commit whose CI build the shipped font is. The font's head.modified, 2025-06-13T04:50:14Z, falls between that commit (04:41:44Z) and the deploy its CI run made to the repository's gh-pages branch (05:04:16Z, "deploy: 1cfe2b7..."); the next deploy is from 2025-07-08. Between `1cfe2b7` and `baa2f38`, sources/, scripts/ and the Makefile are identical; `baa2f38` only changes requirements.txt (fontmake 3.10.0 to 3.10.1, ufo2ft 3.4.3 to 3.6.0, glyphsLib 6.10.1 to 6.11.4, fontParts, fontTools).

## Notes
- Variable font with four axes: opsz, slnt, wdth, wght.
- `gftools builder sources/config.yaml` alone does not build it: sources/TikTokSans.designspace (format 5.0) names UFOs in sources/build/, which `make build` first generates from sources/TikTokSans.glyphspackage with scripts/build/glyphsToUFO.py (conversion, decomposition, wider sidebearings on the Text masters, and the slanted masters of the slnt axis).
