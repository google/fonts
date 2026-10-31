# Pragati Narrow — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [Omnibus-Type/PragatiNarrow](https://github.com/Omnibus-Type/PragatiNarrow) |
| Commit | `829be323c427aab3669e2eb55e253573aeefb1e3` |
| Date | 2015-05-25 |
| Confidence | High |

## Investigation

The METADATA.pb for Pragati Narrow had no source block. The upstream repository was identified as Omnibus-Type/PragatiNarrow.

### Source Types Available

- **Glyphs**: `SRC/PragatiNarrow.glyphs`
- **UFO**: `SRC/Pragati Narrow-Regular.ufo`, `SRC/Pragati Narrow-Bold.ufo`
- **Binary fonts**: `Fonts/PragatiNarrow-Regular.ttf`, `Fonts/PragatiNarrow-Bold.ttf` (plus OTF, WOFF, WOFF2, EOT)
- **Supporting**: `SRC/GlyphData.xml`

### Buildability

The repository contains both Glyphs and UFO sources, which are gftools-builder compatible formats. A `config.yaml` could potentially be created for this family. However, the sources date from 2015 and may require testing to verify compatibility with current gftools-builder.

### Notes

- The `SRC/` directory also contains process documentation and test pages
- The Glyphs source is the most likely canonical source format
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `829be32` (2015-05-25, "New anchors, support for half rakar with nutka and more"), which is the latest commit in the repository and predates the google/fonts onboarding (2015-06-04).

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing the Glyphs source from `Omnibus-Type/PragatiNarrow`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: [PragatiNarrow.glyphs]` — a repository-root path. fontc_crater failed with `missing source 'PragatiNarrow.glyphs'`.

### Investigation
At the recorded commit `829be32` the Glyphs source is `SRC/PragatiNarrow.glyphs`; the repository root contains only `Fonts/`, `LICENSE.md`, `README.md` and `SRC/`. The override config path was missing the `SRC/` directory prefix. The recorded commit is correct and required no change.

### Actions taken
The override `config.yaml` source path was corrected from `PragatiNarrow.glyphs` to `SRC/PragatiNarrow.glyphs`.

### Final state
The override `config.yaml` references `SRC/PragatiNarrow.glyphs`, which exists at the recorded commit `829be32`.
