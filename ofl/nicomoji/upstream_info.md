# NicoMoji — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

No public Git/GitHub source repository was found for the NicoMoji font.

The font is distributed from the author's personal website:
- **Distribution site**: https://nicofont.pupu.jp/nicomoji-plus.html
- **Author**: Ku-Ku (site: nicofont.pupu.jp)
- **Download URL (latest)**: https://nicofont.pupu.jp/nicomoji_u_2525/nicomoji-plus_v2.5.zip (Ver. 2.5, updated 2024-09-18)

Searches performed:
- GitHub search for "nicomoji", "NicoMoji" — no official source repo found; only downstream packaging repos
- GitHub user search for "nicofont" — profile exists but contains only an unrelated repo (`leviosa-catalogo-img`)
- GitHub user search for "ku-ku" — profile with 13 repos, none font-related based on visible content
- AUR archive package (`aur-archive/ttf-nicomoji-plus`) references source ZIP from nicofont.pupu.jp

## Latest Relevant Version

- **Version**: 2.5
- **Release date**: 2024-09-18
- **Download**: https://nicofont.pupu.jp/nicomoji_u_2525/nicomoji-plus_v2.5.zip

Note: The version in the Google Fonts binary is 1.02, which is significantly older than the current 2.5 release. The latest version also incorporates open-source typefaces "M PLUS 1" and "Rounded Mplus 1c".

## Source Files

No source files (UFO, SFD, etc.) found publicly. The font is distributed as a compiled TTF/OTF ZIP archive only.

Font metadata from the binary:
- Font name: Nico Moji
- Version: 1.02 (as shipped in Google Fonts)
- No copyright string extractable via `strings`

## Build System

Unknown — no source repository or build scripts found. The font appears to be distributed as a binary-only release.

## config.yaml Status

No `config.yaml` is present in the google/fonts directory for this family. The family directory also has no `METADATA.pb` — only `DESCRIPTION.en_us.html`, `NicoMoji-Regular.ttf`, and `OFL.txt`.

## Notes

- NicoMoji is a cute and playful Japanese font covering Katakana and Hiragana (744 glyphs), released under the SIL Open Font License.
- The font has been actively updated by the author (latest version 2.5 from September 2024), but the Google Fonts copy appears to be an older version (1.02).
- No METADATA.pb exists for this family in the google/fonts repo.
- The original website uses HTTP (http://nicofont.pupu.jp/), which redirects to HTTPS (https://nicofont.pupu.jp/). The HTTPS URL is functional.
- No cached clone found in `/mnt/shared/upstream_repos/fontc_crater_cache/`.
- **Confidence**: Medium — distribution site identified with newer version available, but no source repo.
