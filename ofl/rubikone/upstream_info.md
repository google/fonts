# Rubik One — Upstream Source Investigation

**Designer**: Hubert and Fischer (Philipp Hubert, Sebastian Fischer)
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for Rubik One.

## Investigation

The DESCRIPTION.en_us.html describes Rubik One as "the initial version of the Black roman style in the Rubik family." The font was designed by Philipp Hubert and Sebastian Fischer at Hubert & Fischer as part of the Chrome Cube Lab project.

Searches were conducted for:
- `RubikOne` by name on GitHub
- `Rubik One font sources`
- `hubertfischer font`
- `sebfischer font`
- Philipp Hubert's and Sebastian Fischer's GitHub accounts

The main Rubik family is hosted at `googlefonts/rubik` with active Glyphs sources, but Rubik One is a separate family that appears to predate the main Rubik repository and represents the original single-weight release. The `googlefonts/rubik` repo's `old/version-1` directory contains UFO sources for the full multi-weight Rubik family but not specifically the Rubik One product.

The only repositories found matching `rubikone` were:
- `librefonts/rubikone` — a librefonts mirror (skipped per policy)
- `monkeyspk/rubikone` — unrelated
- `google-fonts-bower/rubikone-bower` — a bower packaging repo (skipped)

## Conclusion

No canonical upstream repository with editable UFO or Glyphs sources was found specifically for Rubik One. No source block was added to METADATA.pb.
