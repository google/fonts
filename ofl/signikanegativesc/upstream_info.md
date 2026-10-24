**Model**: Claude Opus 4.6

# Signika Negative SC — Upstream Source Investigation

## Summary

Signika Negative SC is a small-caps variant of the Signika Negative typeface, designed by Anna Giedryś (ancymonic.com) and released in 2011. The font was added to Google Fonts on 2011-11-23.

## Designer

Anna Giedryś (info@ancymonic.com / ancymonic.com)

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. The following repositories were found:

- **googlefonts/Signika** (https://github.com/googlefonts/Signika) — archived repository containing Glyphs source files for Signika (variable) and SignikaNegative (via `SignikaNegative.designspace` and master UFO files). This is the most relevant repository for the Signika Negative family. The repository is archived as of 2025.
- **librefonts/signikanegative** — a librefonts mirror containing only VFB/SFD sources (not canonical).
- No dedicated `SignikaNegativeSC` repository was found.

## Source Files

The `googlefonts/Signika` repository contained:
- `sources/Signika.glyphs` — Glyphs source for Signika
- `sources/SignikaNegative.designspace` — designspace for Signika Negative variable family
- `sources/master_ufo/Signika-NegativeLight.ufo` and `Signika-NegativeBold.ufo` — UFO sources
- `sources/configNegative.yaml` — build configuration for the Negative family

The repository did not contain dedicated small-caps (SC) sources. The SC variant was derived from the original 2011 VFB-based sources. The `googlefonts/Signika` repo represents the best available canonical upstream for the Signika Negative family.

## Status

Source block was added pointing to `googlefonts/Signika` (archived) at commit `7361a224d1d77274af1ea11dd06448c54c16f598` on the `master` branch. The repository does not contain SC-specific sources, but is the canonical upstream for the broader Signika Negative family.

## Confidence

Medium — The `googlefonts/Signika` repo is canonical for the Signika/SignikaNegative family overall, but the SC variant has no dedicated modern source. The VFB sources exist only in the librefonts mirror which was excluded per policy.
