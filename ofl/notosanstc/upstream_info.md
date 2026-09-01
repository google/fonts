# Noto Sans TC — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/notofonts/noto-cjk |
| Commit | `523d033d6cb47f4a80c58a35753646f5c3608a78` |
| Version | 2.004 |
| Onboarding PR | [google/fonts#5534](https://github.com/google/fonts/pull/5534) |
| Date | 2022-12-09 |

## Investigation Summary

Noto Sans TC is a regional subset of the Noto CJK mega-font family, targeting Traditional Chinese. The binary was taken from the `Sans2.004` tag at commit `523d033d`, specifically from `Sans/Variable/TTF/Subset/NotoSansTC-VF.ttf`. An 832-byte post-processing difference exists between the upstream binary and the shipped version, consistent with table rewriting during onboarding.

## Build Pipeline

The Noto CJK fonts use a **custom build pipeline** that is fundamentally different from gftools-builder:

1. **Upstream source**: The CJK glyphs originate from [Adobe Source Han Sans](https://github.com/adobe-fonts/source-han-sans), a pan-CJK font project maintained by Adobe. The Noto CJK project adapts these sources under a collaboration between Google and Adobe.

2. **Build tooling**: The fonts are built using Adobe's `AFDKO` (Adobe Font Development Kit for OpenType) and custom Python scripts in the noto-cjk repository, not fontmake or gftools-builder. The build process involves CID-keyed font technology and region-specific glyph selection.

3. **Regional subsetting**: The unified CJK source contains glyphs for all regions (SC, TC, HK, JP, KR). Each regional variant is produced by selecting the appropriate glyph forms for that locale — Traditional Chinese uses locale-standard character forms that may differ from other regions for the same Unicode codepoints.

4. **Pre-built binaries**: The notofonts/noto-cjk repository distributes pre-built variable TTF files under `Sans/Variable/TTF/`. The `Subset/` subdirectory contains smaller regional subsets (e.g., `NotoSansTC-VF.ttf`) that are what Google Fonts ships.

5. **No config.yaml**: Because the CJK build pipeline does not use gftools-builder, no `config.yaml` is applicable. Reproducing the build requires the full AFDKO toolchain and the noto-cjk build scripts.

## Commit Verification

This commit corresponds to the `Sans2.004` tag in the notofonts/noto-cjk repository. File size comparison shows a consistent 832-byte difference between the upstream binary and the shipped version across all 5 CJK families (HK, JP, KR, SC, TC), confirming they were all sourced from the same tag and subjected to identical post-processing.

**Confidence**: HIGH (tag-verified, consistent post-processing delta across all CJK families)
