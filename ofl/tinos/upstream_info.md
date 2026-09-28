# Tinos: source metadata

**Model**: Claude Opus 5.5

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/tinos |
| Commit | `3b4482a99b80ea5fc75f187b1be3120a3f5905b3` |
| Config | `sources/config.yaml` (upstream) |
| Status | complete |
| Confidence | HIGH |

## Initial state

- `METADATA.pb` had a source block with `repository_url` and `commit` (`3b4482a`) but no `config_yaml`. `ofl/tinos/` had no override `config.yaml` and no `upstream_info.md`.
- PR #10477 (commit `ba95515f13`, merged 2026-04-29) moved the family from `apache/tinos/` to `ofl/tinos/`, shipped version 1.340 and set the commit to `3b4482a`. It deleted `apache/tinos/config.yaml` and `apache/tinos/upstream_info.md`, which commit `d4dc6ad9d1` had added on 2026-03-26 for the older upstream commit `aaf68d5`.
- At `3b4482a` the upstream repo has `sources/config.yaml`:

```yaml
removeOutlineOverlaps: false
buildVariable: false
sources:
- Tinos-Bold.glyphs
- Tinos-BoldItalic.glyphs
- Tinos-Italic.glyphs
- Tinos-Regular.glyphs
```

## Actions taken

- The recorded commit was verified. `3b4482a` ("Update built fonts", Simon Cozens, 2026-04-27 13:16 +0100) is the last of four upstream commits made that day:
  - `9fd1731`: moved each style's `.glyphs` file out of its per-style directory and folded the GDEF/GPOS/GSUB feature files into it.
  - `5df0233`: applied the project template and added `sources/config.yaml`.
  - `6a938e5`: set the version to 1.340.
  - `3b4482a`: committed the built fonts.

  The google/fonts commit followed at 14:37 +0100 the same day. The four shipped TTFs have the same git blob IDs as `fonts/ttf/Tinos-*.ttf` at `3b4482a`, so the files are byte-identical. On 2026-09-27, `3b4482a` was still the HEAD of `main`. Later upstream commits exist only on unmerged dependabot branches.
- `sources/config.yaml` at `3b4482a` was built with gftools-builder3 (rev `e851b8b`, fontc 1.0.0). The build succeeded.
  - Compared with the shipped fonts: the cmap (3011 codepoints) was exact and the glyph sets and order were equal (3285 glyphs upright, 3290 italic). There were no shaping, rendering or advance-width differences.
  - `functional_gate.py`: Regular and Italic PASS. Bold and Bold Italic FAIL on one item, `OS/2.usWeightClass` (shipped 700, built 400).
  - The sources are single-master Glyphs 2 files, and some values sit on the export instance. The bold instances set `weightClass = Bold`. The Italic, Bold and Bold Italic instances carry the custom parameters `panose` and `uniqueID`. fontc 1.0.0 does not apply these instance values to a single-master font. This is a fontc gap, not a config error.
  - The same gap causes differences that `functional_gate.py` does not check: `OS/2.panose` is all zeros in the built Italic, Bold and Bold Italic (non-zero in the shipped fonts), and name ID 3 is `1.340;GOOG;Tinos-<Style>` instead of `Monotype Imaging - Tinos <Style>` in the same three styles.
  - Name IDs 13 and 14 keep the source's older OFL text and `http://scripts.sil.org/OFL`. The shipped fonts and the Python build below carry the current OFL text and `https://openfontlicense.org`, which `gftools-fix-font` writes in place of the source strings.
  - The output is not hinted. builder3 `e851b8b` has no autohint step for single-master sources, so `fpgm` and `cvt ` are missing, name ID 5 reads `Version 1.340;fontc 1.0.0` and `head.flags` is 11 instead of 15.
- The same config was built with the Python gftools builder (gftools 0.9.100.dev6+g2db1fe32f, fontmake 3.11.1, glyphsLib 6.12.7, ufo2ft 3.7.0, fontTools 4.61.1, ttfautohint-py 0.6.0).
  - The four TTFs matched the shipped fonts in every table except `head` (`modified`, `checkSumAdjustment`).
  - The shipped fonts also carry a `Debg` table. fontTools feaLib writes this lookup debug table when `FONTTOOLS_LOOKUP_DEBUGGING` is set, and it accounts exactly for the size difference (2092 to 3868 bytes per font).
  - `functional_gate.py` on Bold: PASS.
- `config_yaml: "sources/config.yaml"` was added to the source block. No override `config.yaml` was created.

## Final state

```
source {
  repository_url: "https://github.com/googlefonts/tinos"
  commit: "3b4482a99b80ea5fc75f187b1be3120a3f5905b3"
  config_yaml: "sources/config.yaml"
}
```

The upstream config at the recorded commit rebuilds the shipped v1.340 fonts. The Python builder reproduces them in every table except `head` and `Debg`. The builder3 fonts have the same cmap, shaping, rendering and advances. They differ in three ways:
- fontc does not apply the single-master instance values (`usWeightClass` in the two bold styles, `panose` and name ID 3).
- The license strings in name IDs 13 and 14 are not updated.
- The fonts are not hinted.

## Earlier upstream_info.md (apache/tinos, removed by PR #10477)

`apache/tinos/upstream_info.md` held the text below from 2026-03-26 until PR #10477. Its headings were demoted two levels and one em dash was replaced with a hyphen. Otherwise the text is unchanged.

It described upstream commit `aaf68d53c2d49dbd443631c333c804bf4c664e60` (Marek Jeziorek, 2020-07-05, "created notofonts/Tinos repository"). That commit was a provenance pointer, not the onboarding commit, because it postdates the v1.231 binaries shipped in 2017 (PR #799). At `aaf68d5` the sources were in per-style directories: each held `sources/Tinos-<Style>/Tinos-<Style>.glyphs` plus `Tinos <Style> GDEF.txt`, `GPOS.txt`, `GSUB.txt` and `Tinos-<Style>.plist`.

The override `apache/tinos/config.yaml` added with the text below listed `sources/Tinos-<Style>.glyphs` paths, and those paths did not exist at `aaf68d5`. Its content was:

```yaml
# Override config.yaml for apache/tinos
# NOTE: This is a best-effort starting point for reproducible builds.
# The shipped binary may have been built with different tools/versions.
#
sources:
  - sources/Tinos-Regular.glyphs
  - sources/Tinos-Bold.glyphs
  - sources/Tinos-Italic.glyphs
  - sources/Tinos-BoldItalic.glyphs
```

### Tinos - Source Repository Investigation

**Model**: Claude Opus 4.6

#### Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/tinos |
| Commit | `aaf68d53c2d49dbd443631c333c804bf4c664e60` |
| Confidence | High |

#### Source Types

The repository contains Glyphs sources:
- `sources/Tinos-Regular.glyphs`
- `sources/Tinos-Bold.glyphs`
- `sources/Tinos-Italic.glyphs`
- `sources/Tinos-BoldItalic.glyphs`

All four styles have individual Glyphs source files.

#### Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs sources could potentially be built with gftools-builder given an override config.

#### Investigation Notes

Tinos is one of the Chrome OS core fonts (metrically compatible with Times New Roman), hosted under the googlefonts organization. The binary in google/fonts was last updated on 2017-08-07 (v1.231 hotfix). The repository is the canonical upstream maintained by the Google Fonts team.

A source block was added to METADATA.pb pointing to this repository and commit.

#### Confidence: High

Official googlefonts organization repository.
