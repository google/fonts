**Model**: Claude Opus 4.6

## Unna

**Designer**: Omnibus-Type
**License**: OFL
**Category**: SERIF

### Upstream Repository

The canonical upstream repository for Unna was identified at **https://github.com/Omnibus-Type/Unna**, maintained by the Omnibus-Type foundry. The repository contained Glyphs source files (`Unna.glyphs` and `Unna Italic.glyphs`) in the `sources/` directory, confirming it as the primary source of truth for the font.

### Source Files

The repository contained:
- `sources/Unna.glyphs` — Glyphs source for regular and bold upright styles
- `sources/Unna Italic.glyphs` — Glyphs source for italic styles
- `fonts/` — compiled TTF output files
- `docs/` — specimen documentation

### Investigation Notes

The repository was located by searching for the Omnibus-Type organization on GitHub, which manages many of its Google Fonts contributions under the [Omnibus-Type](https://github.com/Omnibus-Type) organization. The email address `omnibus.type@gmail.com` in the copyright string matched the organization's known contact. The repository was last updated in July 2019.

**Repo**: https://github.com/Omnibus-Type/Unna
**Commit**: 826be2abebda53d63bcd99b7ca30a7061b89bcfd
**Status**: Glyphs sources present
**Confidence**: High

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/unna/` referencing the upstream gftools-builder-compatible source at the pinned commit `826be2a` (`sources/Unna.glyphs`, `sources/Unna Italic.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
