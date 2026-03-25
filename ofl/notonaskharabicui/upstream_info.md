# Noto Naskh Arabic UI — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/notofonts/arabic |
| Commit | `133ccaebf922ca080a7eef22998611ac3c242df9` |
| Version | 2.015 (shipped) / 2.014 (base commit) |
| Onboarding PR | [google/fonts#5025](https://github.com/google/fonts/pull/5025) |
| Date | 2022-08-04 |

## Investigation Summary

Noto Naskh Arabic UI was onboarded via PR #5025 from the notofonts/arabic repository. The base font binary corresponds to v2.014 from commit `133ccaebf922ca080a7eef22998611ac3c242df9`.

The version shipped in google/fonts is v2.015, which is a hand-modified binary created to fix Persian/Urdu figure localization. This manual binary edit was applied on top of the v2.014 base, meaning no exact upstream match for v2.015 exists in any repository. The commit recorded here represents the closest upstream source (the v2.014 base from which v2.015 was derived).

This commit corresponds to the NotoNaskhArabicUI-v2.014 tag. The shipped v2.015 binary was created by a direct binary edit on top of v2.014 to fix Persian/Urdu figure localization (notofonts/arabic#27). No exact upstream commit for v2.015 exists; this commit identifies the v2.014 base from which the edit was derived.

**Note**: Shipped v2.015 is a hand-modified binary (Persian/Urdu figure localization fix). Base is v2.014 from this commit. No exact upstream match for v2.015 exists.

**Confidence**: MEDIUM (base commit identified, shipped binary is hand-modified)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-naskh-arabic-ui.yaml` in the `notofonts/arabic` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.
