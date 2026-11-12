**Model**: Claude Opus 4.6

# Sulphur Point — Upstream Source Investigation

## Summary

The canonical upstream repository for Sulphur Point was identified at `https://github.com/noponies/sulphur-point`, maintained by Dale Sattler. The repository contained a Glyphs source file (`sources/sulphur-point.glyphs`) along with documentation, fonts, and assets directories.

## Repository Details

- **Repository**: https://github.com/noponies/sulphur-point
- **Owner**: noponies (Dale Sattler)
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `2c1a600846ca8b7890a89076aeeb2d43cdaeac23`
- **Commit message**: "S character adjustments — Minor fixes to the lower case s"
- **Commit date**: 2019-11-17

## Source Files

The `sources/` directory contained:
- `sulphur-point.glyphs`

## Confidence

**High** — The repository URL matched the copyright notice in the font files (`Copyright 2019 The Sulphur Point Project Authors (https://github.com/noponies)`). The designer name (Dale Sattler) matched the METADATA.pb. The Glyphs source file was present and the repository was not a librefonts mirror.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/noponies/sulphur-point` at commit `2c1a600846ca8b7890a89076aeeb2d43cdaeac23`.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sulphurpoint/` referencing the upstream gftools-builder-compatible source at the pinned commit `2c1a600` (`sources/sulphur-point.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`2c1a6008`](https://github.com/noponies/sulphur-point/commit/2c1a6008) ("S character adjustments", 2019-11-18) to [`0212c26a`](https://github.com/noponies/sulphur-point/commit/0212c26a) ("Webont update", 2019-09-03, on `master`), the commit named by [google/fonts `b39281ee`](https://github.com/google/fonts/commit/b39281ee) (2019-09-25). `2c1a6008` reworked `s` in the Glyphs source after onboarding without re-exporting, so it still carries the older TTFs.

The three shipped TTFs are byte-identical to `fonts/ttf/SulphurPoint-*.ttf` at `0212c26a`: Light md5 `aa6c6c31728442ad5dd4d080f0dc1e93`, Regular `1affad35ce6cab9c36b06b4172000bad`, Bold `166a7670769880239a7aedd4d53dba03`. They were exported with the source in [`83eff11b`](https://github.com/noponies/sulphur-point/commit/83eff11b) ("Accent component fixes"); the two commits after it touch only FONTLOG.txt and the webfonts.

The override `config.yaml` (`sources/sulphur-point.glyphs`) resolves at `0212c26a`.
