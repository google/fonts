# Underdog — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Sergey Steblina, Jovanny Lemonad

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `underdog/src/`.

### Source Files

- **VFB (FontLab)**: Underdog-Regular-OTF.vfb, Underdog-Regular-TTF.vfb
- **OTF (compiled)**: Underdog-Regular.otf
- **Adobe Illustrator**: ai_files/underdog_f.ai, ai_files/underdog_f2_extra.ai, ai_files/underdog_letters_correction.ai
- **Other**: test_files/cyr.jpg, test_files/cyr_caps.jpg, test_files/latin.jpg, test_files/latin_caps.jpg

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

## Investigation Details

Underdog was designed by Sergey Steblina and technically engineered and published by Jovanny Lemonad (lemonad@jovanny.ru). It is an informal display typeface with Cyrillic and Latin support.

The following searches were conducted:

1. **steblina GitHub**: A GitHub account `steblina` was found but contained only two personal/unrelated repositories (miniature-tribble, theme-binary).
2. **lemonad GitHub**: The GitHub account `lemonad` (Jovanny Lemonad) was found but its repositories were all unrelated to font design (coding exercises, course projects, moodle plugins, web apps, etc.).
3. **jovanny GitHub**: A GitHub user `jovanny` was found but had only one repository (`repositorio`) unrelated to fonts.
4. **alexeiva GitHub**: Examined as a related Russian type designer with Cyrillic fonts on Google Fonts, but no Underdog repository was found.
5. **Repository name search**: Searches for "underdog font", "underdog cyrillic", and related terms returned no font source repositories.

Underdog was published to Google Fonts in 2012 but the source files have not been made publicly available on GitHub or any other discoverable platform. Neither of the two credited designers has published font source repositories under their GitHub accounts.
