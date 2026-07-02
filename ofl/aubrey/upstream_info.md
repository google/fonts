# Aubrey

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cyreal
**METADATA.pb path**: `ofl/aubrey/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cyrealtype/Aubrey |
| Commit | `1946b0d99c0fec87702a59afc8b5b941a32e0171` |
| Config YAML | `sources/builder.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL is present in the METADATA.pb source block on the main branch. It was added as part of PR #4229 (`4678b39e`, "Aubrey: Version 1.102; ttfautohint (v1.8.3) added", 2022-01-28) which used gftools-packager to update the font from the upstream repository.

The copyright string also references `https://github.com/cyrealtype/Aubrey`.

## How the Commit Hash Was Identified

The commit hash is explicitly documented in both the METADATA.pb source block and the PR #4229 body. The PR body states:

> "Aubrey Version 1.102; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/cyrealtype/Aubrey at commit https://github.com/cyrealtype/Aubrey/commit/1946b0d99c0fec87702a59afc8b5b941a32e0171."

This commit is also the only commit in the upstream repository (and thus also HEAD).

## How Config YAML Was Resolved

The config file `sources/builder.yaml` exists in the upstream repository at the referenced commit. It was created as part of the gftools-packager workflow. The file contains:

```yaml
sources:
  - Aubrey.glyphs
outputDir: "../fonts"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a standard gftools-builder configuration for a static-only font build from a .glyphs source. No override config.yaml exists in `google/fonts/ofl/aubrey/`.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-01-21 12:55:26 +0300
- Commit message: "Update CONTRIBUTORS.txt"
- Source files at commit:
  - `sources/Aubrey.glyphs` (Glyphs source file)
  - `sources/builder.yaml` (gftools-builder config)

## Confidence

**High**: All source data fields are complete and verified. The repository URL, commit hash, and config_yaml path are all explicitly documented in METADATA.pb and confirmed by the PR history. The gftools-packager workflow provides strong provenance. The upstream repo has a proper builder.yaml and .glyphs source file.

## Open Questions

None
