# Ruslan Display — Upstream Source Investigation

**Designer**: Oleg Snarsky, Denis Masharov, Vladimir Rabdu
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for Ruslan Display. The METADATA.pb already contained an empty `source {}` block, which was left unchanged.

## Investigation

Ruslan Display is a digitization of a 1970s typeface by Ukrainian designer Oleg Snarsky, extended with a Latin complement by Denis Masharov in collaboration with Vladimir Rabdu in 2011.

Searches were conducted for:
- `RuslanDisplay` by name on GitHub
- `Ruslan Display font Cyrillic`
- `masharov font`
- `masharov cyrillic font`
- GitHub users `masharov`, `denis-masharov`, `DenisMasharov`

Denis Masharov's work was found to be associated with the GitHub user `alexeiva` (who maintains the Google Fonts upstream for several Masharov fonts like Poiret One and Tenor Sans), but no Ruslan Display source repository was found under `alexeiva` or any other account.

The only repositories matching `RuslanDisplay` were:
- `librefonts/ruslandisplay` — a librefonts mirror (skipped per policy)
- `google-fonts-bower/ruslandisplay-bower` — a bower packaging repo (skipped)

## Conclusion

No canonical upstream repository with editable UFO or Glyphs sources was found for Ruslan Display. The existing empty `source {}` block in METADATA.pb was left unchanged.
