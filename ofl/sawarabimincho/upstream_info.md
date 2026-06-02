# Sawarabi Mincho — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/sawarabi-mincho
- **Commit**: `8bd1525717e74e24943d30e07b0ae56ee60c0915`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
A Japanese serif (mincho) typeface designed by mshio, with primary script `Jpan`. The source block references an archive URL pointing to release v1.082 on GitHub. Both a repository commit and an archive_url are specified. The repository is hosted under the googlefonts organization. The source block uses the `main` branch and references a config.yaml.


## Source-metadata review (2026-06-02) — build-time-generated `.glyphs` from `.sfdir` (no `.ufoz`; PENDING upstream fix)

**Model**: Claude Opus 4.8

fontc_crater reports `missing source 'SawarabiMincho.glyphs'`. Unlike the `.ufoz` families in this batch, **there is no committed `.ufoz` (or any gftools-buildable source) to declare**: `SawarabiMincho.glyphs` is generated at build time by a `babelfont` `exec` step in `sources/config.yaml`'s recipe, which converts the committed FontForge source (`fonts/mincho/sawarabi-mincho-medium.sfdir`) to `.glyphs`. gftools-builder / fontc cannot read a `.sfdir` directly, so there is nothing to point an override config at.

**PENDING (work on later):** an upstream PR to `googlefonts/sawarabi-mincho` that commits the generated `SawarabiMincho.glyphs` (conventionally under `sources/generated/`) and points the config at it — or, alternatively, tooling support for running the `babelfont` conversion. No override config is added here.
